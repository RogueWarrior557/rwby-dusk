#!/usr/bin/env python3
"""pixelforge — compile hand-authored text-grid sprites into game-ready PNGs.

Why this exists
---------------
This project has no human pixel artist and no image model. Every sprite is
authored pixel by pixel as a text grid, the way an artist places pixels in
Aseprite, then compiled here. The tool does not invent pixels. It only:

  * maps palette keys to colours (one key = one colour, so palettes stay
    controlled and swappable),
  * optionally adds an automatic 1px outline (plain or selective),
  * derives frames from other frames with explicit, deterministic operations
    (shift a region, repaint pixels, swap palette keys, mirror),
  * packs frames into per-animation strip sheets with JSON metadata,
  * renders integer-scaled preview contact sheets for visual QA.

Sprite file format (.pxs)
-------------------------
    @sprite  knight
    @size    32 32
    @palette ../palettes/dusk.pal      # path relative to this .pxs file
    @anchor  16 31                     # pivot (usually between the feet)
    @outline selout o                  # none | plain <key> | selout <key>

    @frame idle 0 220                  # animation, index, duration (ms)
    ....rows of exactly <width> chars, <height> rows....

    @derive idle 1 220 from idle 0     # copy a frame, then apply ops:
    shift 8 4 23 15 0 1                # move rect x0 y0 x1 y1 by dx dy
    paint 12 9 w                       # set one pixel
    swap r R                           # replace every key r with R
    flipx                              # mirror horizontally
    @end

'.' and ' ' are always transparent. Lines starting with '#' outside frame
bodies are comments.

Palette file format (.pal): one colour per line, "<key> #RRGGBB <name>".
Lines starting with "//" and text after ";" are comments. Keys '.', ' ',
'#' and '@' are reserved.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image, ImageDraw

TRANSPARENT_KEYS = {".", " "}
RGBA = tuple[int, int, int, int]


# --------------------------------------------------------------------------
# Palette
# --------------------------------------------------------------------------
@dataclass
class Palette:
    colours: dict[str, RGBA] = field(default_factory=dict)
    names: dict[str, str] = field(default_factory=dict)
    order: list[str] = field(default_factory=list)

    @classmethod
    def load(cls, path: Path) -> "Palette":
        pal = cls()
        for lineno, raw in enumerate(path.read_text().splitlines(), 1):
            line = raw.split(";", 1)[0].strip()
            if not line or line.startswith("//"):
                continue
            parts = line.split()
            if len(parts) < 2 or len(parts[0]) != 1 or not parts[1].startswith("#"):
                raise ValueError(f"{path}:{lineno}: expected '<key> #RRGGBB [name]'")
            key, hexcol = parts[0], parts[1]
            if key in TRANSPARENT_KEYS or key in "#@":
                raise ValueError(f"{path}:{lineno}: key '{key}' is reserved")
            if key in pal.colours:
                raise ValueError(f"{path}:{lineno}: duplicate key '{key}'")
            pal.colours[key] = hex_to_rgba(hexcol)
            pal.names[key] = " ".join(parts[2:]) if len(parts) > 2 else key
            pal.order.append(key)
        return pal

    def rgba(self, key: str) -> RGBA:
        if key in TRANSPARENT_KEYS:
            return (0, 0, 0, 0)
        try:
            return self.colours[key]
        except KeyError:
            raise KeyError(f"palette has no key '{key}'") from None


def hex_to_rgba(h: str) -> RGBA:
    h = h.lstrip("#")
    if len(h) == 6:
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 255)
    if len(h) == 8:
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), int(h[6:8], 16))
    raise ValueError(f"bad colour '{h}'")


# --------------------------------------------------------------------------
# Sprite model
# --------------------------------------------------------------------------
Grid = list[list[str]]


@dataclass
class Frame:
    anim: str
    index: int
    duration_ms: int
    grid: Grid


@dataclass
class Sprite:
    name: str
    width: int
    height: int
    palette: Palette
    anchor: tuple[int, int]
    outline_mode: str = "none"
    outline_key: str | None = None
    frames: list[Frame] = field(default_factory=list)

    def frame(self, anim: str, index: int) -> Frame:
        for f in self.frames:
            if f.anim == anim and f.index == index:
                return f
        raise KeyError(f"{self.name}: no frame {anim}[{index}]")

    def animations(self) -> dict[str, list[Frame]]:
        out: dict[str, list[Frame]] = {}
        for f in self.frames:
            out.setdefault(f.anim, []).append(f)
        for frames in out.values():
            frames.sort(key=lambda fr: fr.index)
        return out


class ParseError(Exception):
    pass


def parse_sprite(path: Path) -> Sprite:
    lines = path.read_text().splitlines()
    header: dict[str, list[str]] = {}
    frames: list[Frame] = []
    i = 0
    sprite: Sprite | None = None

    def need_sprite() -> Sprite:
        nonlocal sprite
        if sprite is None:
            for k in ("sprite", "size", "palette"):
                if k not in header:
                    raise ParseError(f"{path}: missing @{k} before first frame")
            w, h = int(header["size"][0]), int(header["size"][1])
            pal = Palette.load((path.parent / header["palette"][0]).resolve())
            anchor = tuple(int(v) for v in header.get("anchor", [str(w // 2), str(h - 1)]))
            mode, key = "none", None
            if "outline" in header:
                mode = header["outline"][0]
                key = header["outline"][1] if len(header["outline"]) > 1 else None
                if mode not in ("none", "plain", "selout"):
                    raise ParseError(f"{path}: bad outline mode '{mode}'")
            sprite = Sprite(header["sprite"][0], w, h, pal, anchor, mode, key)  # type: ignore[arg-type]
        return sprite

    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()
        if not stripped:
            i += 1
            continue
        if stripped.startswith("@frame"):
            sp = need_sprite()
            parts = stripped.split()
            if len(parts) != 4:
                raise ParseError(f"{path}:{i+1}: '@frame <anim> <index> <ms>'")
            anim, idx, dur = parts[1], int(parts[2]), int(parts[3])
            rows = lines[i + 1 : i + 1 + sp.height]
            if len(rows) != sp.height:
                raise ParseError(f"{path}:{i+1}: frame {anim}[{idx}] needs {sp.height} rows")
            grid: Grid = []
            for r, row in enumerate(rows):
                row = row.rstrip("\n")
                if len(row) != sp.width:
                    raise ParseError(
                        f"{path}:{i+2+r}: frame {anim}[{idx}] row {r} has {len(row)} chars, expected {sp.width}"
                    )
                for c in row:
                    if c not in TRANSPARENT_KEYS and c not in sp.palette.colours:
                        raise ParseError(f"{path}:{i+2+r}: unknown palette key '{c}'")
                grid.append(list(row))
            frames.append(Frame(anim, idx, dur, grid))
            i += 1 + sp.height
            continue
        if stripped.startswith("@derive"):
            sp = need_sprite()
            parts = stripped.split()
            # @derive <anim> <idx> <ms> from <anim> <idx>
            if len(parts) != 7 or parts[4] != "from":
                raise ParseError(f"{path}:{i+1}: '@derive <anim> <idx> <ms> from <anim> <idx>'")
            anim, idx, dur = parts[1], int(parts[2]), int(parts[3])
            src_anim, src_idx = parts[5], int(parts[6])
            src = next((f for f in frames if f.anim == src_anim and f.index == src_idx), None)
            if src is None:
                raise ParseError(f"{path}:{i+1}: source frame {src_anim}[{src_idx}] not defined yet")
            grid = [row[:] for row in src.grid]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith("@"):
                grid = apply_op(grid, lines[i].strip(), sp, f"{path}:{i+1}")
                i += 1
            frames.append(Frame(anim, idx, dur, grid))
            continue
        if stripped.startswith("@end"):
            break
        if stripped.startswith("@"):
            parts = stripped[1:].split()
            header[parts[0]] = parts[1:]
            i += 1
            continue
        if stripped.startswith("#"):
            i += 1
            continue
        raise ParseError(f"{path}:{i+1}: unexpected line: {raw!r}")

    sp = need_sprite()
    sp.frames = frames
    seen = set()
    for f in frames:
        if (f.anim, f.index) in seen:
            raise ParseError(f"{path}: duplicate frame {f.anim}[{f.index}]")
        seen.add((f.anim, f.index))
    return sp


def apply_op(grid: Grid, op: str, sp: Sprite, where: str) -> Grid:
    parts = op.split()
    h, w = len(grid), len(grid[0])
    if parts[0] == "shift":
        x0, y0, x1, y1, dx, dy = map(int, parts[1:7])
        region = {(x, y): grid[y][x] for y in range(y0, y1 + 1) for x in range(x0, x1 + 1)}
        out = [row[:] for row in grid]
        for (x, y) in region:
            out[y][x] = "."
        for (x, y), k in region.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and k not in TRANSPARENT_KEYS:
                out[ny][nx] = k
        return out
    if parts[0] == "paint":
        x, y, k = int(parts[1]), int(parts[2]), parts[3]
        if k not in TRANSPARENT_KEYS and k not in sp.palette.colours:
            raise ParseError(f"{where}: unknown palette key '{k}'")
        out = [row[:] for row in grid]
        out[y][x] = "." if k in TRANSPARENT_KEYS else k
        return out
    if parts[0] == "swap":
        a, b = parts[1], parts[2]
        return [[b if c == a else c for c in row] for row in grid]
    if parts[0] == "flipx":
        return [row[::-1] for row in grid]
    raise ParseError(f"{where}: unknown op '{parts[0]}'")


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------
def render_frame(sp: Sprite, frame: Frame) -> Image.Image:
    img = Image.new("RGBA", (sp.width, sp.height), (0, 0, 0, 0))
    px = img.load()
    for y, row in enumerate(frame.grid):
        for x, k in enumerate(row):
            if k not in TRANSPARENT_KEYS:
                px[x, y] = sp.palette.rgba(k)
    if sp.outline_mode != "none" and sp.outline_key:
        img = add_outline(img, frame.grid, sp)
    return img


def add_outline(img: Image.Image, grid: Grid, sp: Sprite) -> Image.Image:
    """Outline transparent pixels 4-adjacent to opaque ones.

    plain : every outline pixel uses the outline key.
    selout: outline pixels on the lit side (top/left neighbour is the source)
            take a darkened version of the neighbouring colour instead of the
            hard outline colour, softening the silhouette where light hits.
    """
    w, h = sp.width, sp.height
    out = img.copy()
    px = out.load()
    dark = sp.palette.rgba(sp.outline_key)  # type: ignore[arg-type]
    for y in range(h):
        for x in range(w):
            if grid[y][x] not in TRANSPARENT_KEYS:
                continue
            neighbours = []
            for dx, dy, side in ((0, 1, "below"), (0, -1, "above"), (1, 0, "right"), (-1, 0, "left")):
                nx, ny = x + dx, y + dy
                if 0 <= nx < w and 0 <= ny < h and grid[ny][nx] not in TRANSPARENT_KEYS:
                    neighbours.append((side, grid[ny][nx]))
            if not neighbours:
                continue
            if sp.outline_mode == "selout":
                lit = [k for side, k in neighbours if side in ("below", "right")]
                if lit and len(neighbours) == len(lit):
                    src = sp.palette.rgba(lit[0])
                    px[x, y] = tuple(int(c * 0.45 + d * 0.55) for c, d in zip(src[:3], dark[:3])) + (255,)
                    continue
            px[x, y] = dark
    return out


def build_outputs(sp: Sprite, out_dir: Path, scale: int) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    meta = {
        "sprite": sp.name,
        "frame_size": [sp.width, sp.height],
        "anchor": list(sp.anchor),
        "animations": {},
    }
    for anim, frames in sp.animations().items():
        sheet = Image.new("RGBA", (sp.width * len(frames), sp.height), (0, 0, 0, 0))
        entries = []
        for n, fr in enumerate(frames):
            sheet.paste(render_frame(sp, fr), (n * sp.width, 0))
            entries.append({"x": n * sp.width, "y": 0, "w": sp.width, "h": sp.height, "duration_ms": fr.duration_ms})
        sheet_name = f"{sp.name}_{anim}.png"
        sheet.save(out_dir / sheet_name)
        meta["animations"][anim] = {"sheet": sheet_name, "frames": entries,
                                    "loop": anim in ("idle", "walk", "run", "cast_loop")}
    (out_dir / f"{sp.name}.json").write_text(json.dumps(meta, indent=2))
    preview(sp, scale).save(out_dir / f"{sp.name}_preview.png")
    return meta


def checker(w: int, h: int, cell: int) -> Image.Image:
    img = Image.new("RGBA", (w, h), (46, 42, 56, 255))
    d = ImageDraw.Draw(img)
    for y in range(0, h, cell):
        for x in range(0, w, cell):
            if (x // cell + y // cell) % 2:
                d.rectangle([x, y, x + cell - 1, y + cell - 1], fill=(56, 52, 68, 255))
    return img


def preview(sp: Sprite, scale: int, gap: int = 2) -> Image.Image:
    """Contact sheet: one row per animation, integer-scaled, nearest neighbour."""
    anims = sp.animations()
    cols = max(len(f) for f in anims.values())
    cw, ch = (sp.width + gap) * scale, (sp.height + gap) * scale
    label_h = 0
    img = checker(cols * cw + gap * scale, len(anims) * ch + gap * scale, scale * 4)
    for r, (anim, frames) in enumerate(anims.items()):
        for c, fr in enumerate(frames):
            tile = render_frame(sp, fr).resize((sp.width * scale, sp.height * scale), Image.NEAREST)
            img.alpha_composite(tile, (gap * scale + c * cw, gap * scale + r * ch + label_h))
    return img


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("sprites", nargs="+", type=Path, help=".pxs files")
    ap.add_argument("-o", "--out", type=Path, required=True, help="output directory")
    ap.add_argument("--scale", type=int, default=8, help="preview integer scale")
    args = ap.parse_args(argv)
    ok = True
    for path in args.sprites:
        try:
            sp = parse_sprite(path)
            meta = build_outputs(sp, args.out, args.scale)
            n = sum(len(a["frames"]) for a in meta["animations"].values())
            print(f"ok   {path.name}: {len(meta['animations'])} animations, {n} frames")
        except (ParseError, ValueError, KeyError) as exc:
            ok = False
            print(f"FAIL {path.name}: {exc}", file=sys.stderr)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
