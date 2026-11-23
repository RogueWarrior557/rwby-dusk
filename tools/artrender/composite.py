#!/usr/bin/env python3
"""composite: raster finishing pass that lifts layered SVG art to key-art quality.

The SVG is authored with top-level groups named by convention:
    layer-bg     background (gets depth-of-field blur and haze)
    layer-char   character (gets automatic rim light and a separation halo)
    layer-fx     emissive effects (screen-blended, feeds bloom)
    layer-frame  card frame and nameplate (composited last, never graded)

Each layer is rendered on its own with headless Chromium (render.js --only),
then finished here in linear-ish float space:

    background DOF + haze -> character + rim light -> fx (screen)
    -> light shafts from the key light -> bloom -> floating motes
    -> split-tone colour grade + contrast curve -> vignette -> grain -> frame

These are the standard key-art finishing techniques (rim separation, bloom,
volumetric light, atmospheric depth, grading, film grain). Every parameter
lives in a JSON job file next to the artwork, so each piece is reproducible.

Usage: python3 composite.py <job.json>
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent


# ---------------------------------------------------------------- utilities
def render_layer(svg: Path, layer: str, scale: float, out: Path) -> np.ndarray:
    subprocess.run(["node", str(HERE / "render.js"), str(svg), str(out), str(scale), f"--only={layer}"],
                   check=True, capture_output=True)
    return np.asarray(Image.open(out).convert("RGBA")).astype(np.float32) / 255.0


def blur(img: np.ndarray, sigma: float) -> np.ndarray:
    if sigma <= 0:
        return img
    k = int(sigma * 6) | 1
    return cv2.GaussianBlur(img, (k, k), sigma, borderType=cv2.BORDER_REFLECT)


def over(dst_rgb: np.ndarray, src: np.ndarray) -> np.ndarray:
    a = src[..., 3:4]
    return src[..., :3] * a + dst_rgb * (1 - a)


def screen(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return 1 - (1 - a) * (1 - b)


def luminance(rgb: np.ndarray) -> np.ndarray:
    return rgb[..., 0] * 0.2126 + rgb[..., 1] * 0.7152 + rgb[..., 2] * 0.0722


def hex_rgb(h: str) -> np.ndarray:
    h = h.lstrip("#")
    return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], np.float32) / 255.0


# ---------------------------------------------------------------- effects
def rim_light(char: np.ndarray, light_xy, cfg: dict, s: float) -> np.ndarray:
    """Light the silhouette edge that faces the key light.

    rim = alpha - alpha shifted away from the light; that keeps only the edge
    band on the lit side. Blurred slightly and tinted, then screen-added.
    """
    a = char[..., 3]
    h, w = a.shape
    cy, cx = h / 2, w / 2
    lx, ly = light_xy[0] * s, light_xy[1] * s
    d = np.array([cx - lx, cy - ly], np.float32)
    d /= max(np.linalg.norm(d), 1e-6)
    width = cfg.get("width", 5) * s
    m = np.float32([[1, 0, d[0] * width], [0, 1, d[1] * width]])
    shifted = cv2.warpAffine(a, m, (w, h), borderMode=cv2.BORDER_CONSTANT, borderValue=0)
    band = np.clip(a - shifted, 0, 1)
    band = blur(band, cfg.get("softness", 1.2) * s) * a
    # stronger nearer the light
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    dist = np.sqrt((xx - lx) ** 2 + (yy - ly) ** 2) / max(h, w)
    falloff = np.clip(1.0 - dist * cfg.get("falloff", 1.1), 0, 1) ** 1.5
    return band[..., None] * falloff[..., None] * hex_rgb(cfg.get("color", "#ffc77a")) * cfg.get("strength", 0.9)


def light_shafts(rgb: np.ndarray, light_xy, cfg: dict, s: float) -> np.ndarray:
    """Volumetric shafts: radial (zoom) blur of the bright pixels from the light."""
    lum = luminance(rgb)
    mask = np.clip((lum - cfg.get("threshold", 0.72)) / 0.28, 0, 1)
    src = rgb * mask[..., None]
    h, w = lum.shape
    lx, ly = light_xy[0] * s, light_xy[1] * s
    acc = np.zeros_like(src)
    n = cfg.get("samples", 24)
    for i in range(n):
        z = 1.0 + cfg.get("length", 0.35) * i / n
        m = np.float32([[z, 0, lx * (1 - z)], [0, z, ly * (1 - z)]])
        acc += cv2.warpAffine(src, m, (w, h), borderMode=cv2.BORDER_CONSTANT) * (1 - i / n)
    acc /= n * 0.5
    return acc * hex_rgb(cfg.get("color", "#ffd59a")) * cfg.get("strength", 0.6)


def bloom(rgb: np.ndarray, cfg: dict, s: float) -> np.ndarray:
    lum = luminance(rgb)
    mask = np.clip((lum - cfg.get("threshold", 0.78)) / (1 - cfg.get("threshold", 0.78) + 1e-6), 0, 1)
    src = rgb * mask[..., None]
    out = np.zeros_like(rgb)
    for sigma, wgt in ((4, 0.45), (12, 0.35), (32, 0.2)):
        out += blur(src, sigma * s) * wgt
    return out * cfg.get("strength", 0.8)


def motes(shape, cfg: dict, s: float, seed: int) -> tuple[np.ndarray, np.ndarray]:
    """Floating light motes: sharp small midground motes and big soft foreground bokeh."""
    h, w = shape
    rng = np.random.default_rng(seed)
    mid = np.zeros((h, w), np.float32)
    fg = np.zeros((h, w), np.float32)
    region = cfg.get("region", [0, 0, 1, 1])  # normalised x0,y0,x1,y1 bias area
    for _ in range(cfg.get("count", 40)):
        x = int(rng.uniform(region[0], region[2]) * w)
        y = int(rng.uniform(region[1], region[3]) * h)
        r = rng.uniform(1.0, 2.6) * s
        cv2.circle(mid, (x, y), max(1, int(r)), float(rng.uniform(0.5, 1.0)), -1, lineType=cv2.LINE_AA)
    for _ in range(cfg.get("bokeh", 6)):
        x = int(rng.uniform(0, 1) * w)
        y = int(rng.uniform(0.55, 1) * h) if rng.random() < 0.6 else int(rng.uniform(0, 0.4) * h)
        r = rng.uniform(14, 34) * s
        cv2.circle(fg, (x, y), int(r), float(rng.uniform(0.15, 0.35)), -1, lineType=cv2.LINE_AA)
    mid = blur(mid, 0.8 * s) + blur(mid, 5 * s) * 1.5
    fg = blur(fg, 6 * s)
    col = hex_rgb(cfg.get("color", "#ffd9a0"))
    return mid[..., None] * col, fg[..., None] * col


def grade(rgb: np.ndarray, cfg: dict) -> np.ndarray:
    """Split toning (cool shadows / warm highlights), S-curve, saturation."""
    lum = luminance(rgb)[..., None]
    shadow_tint = hex_rgb(cfg.get("shadows", "#3a3a78"))
    high_tint = hex_rgb(cfg.get("highlights", "#ffcf8a"))
    st = cfg.get("split_strength", 0.12)
    rgb = rgb + (shadow_tint - 0.5) * st * (1 - lum) * 2 + (high_tint - 0.5) * st * lum * 2
    c = cfg.get("contrast", 0.12)  # S-curve around mid grey
    rgb = np.clip(rgb, 0, 1)
    rgb = rgb + c * (rgb - 0.5) * (1 - np.abs(rgb - 0.5) * 2) * 2
    sat = cfg.get("saturation", 1.08)
    lum = luminance(rgb)[..., None]
    rgb = lum + (rgb - lum) * sat
    return np.clip(rgb, 0, 1)


def vignette(rgb: np.ndarray, cfg: dict, light_xy, s: float) -> np.ndarray:
    h, w = rgb.shape[:2]
    cx, cy = cfg.get("center", [light_xy[0] * s / w * 0.5 + 0.25, 0.42])
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    d = np.sqrt(((xx / w - cx) / 0.75) ** 2 + ((yy / h - cy) / 0.9) ** 2)
    v = 1 - cfg.get("strength", 0.45) * np.clip(d - cfg.get("radius", 0.35), 0, 1) ** 1.4
    return rgb * v[..., None]


def grain(rgb: np.ndarray, cfg: dict, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed + 7)
    n = rng.normal(0, 1, rgb.shape[:2]).astype(np.float32)
    n = blur(n, 0.6)
    amt = cfg.get("amount", 0.025)
    lum = luminance(rgb)
    weight = 0.6 + 0.4 * (1 - np.abs(lum - 0.5) * 2)  # strongest in mid-tones
    return np.clip(rgb + (n * amt * weight)[..., None], 0, 1)


# ---------------------------------------------------------------- pipeline
def run(job_path: Path) -> Path:
    job = json.loads(job_path.read_text())
    base = job_path.parent
    svg = (base / job["svg"]).resolve()
    out = (base / job["out"]).resolve()
    s = float(job.get("scale", 2))
    light = job["light"]  # key light position in SVG user units [x, y]
    seed = int(job.get("seed", 1))
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        bg = render_layer(svg, "layer-bg", s, td / "bg.png")
        ch = render_layer(svg, "layer-char", s, td / "char.png")
        fx = render_layer(svg, "layer-fx", s, td / "fx.png")
        fr = render_layer(svg, "layer-frame", s, td / "frame.png")

    cfg = job.get("effects", {})
    rgb = bg[..., :3].copy()
    if "dof" in cfg:
        rgb = blur(rgb, cfg["dof"].get("sigma", 3) * s)
    if "haze" in cfg:
        hz = cfg["haze"]
        h = rgb.shape[0]
        ramp = np.linspace(0, 1, h, dtype=np.float32)[:, None, None]
        rgb = rgb * (1 - hz.get("strength", 0.2) * ramp) + hex_rgb(hz.get("color", "#8890b8")) * hz.get("strength", 0.2) * ramp
    if "halo" in cfg:  # soft light halo behind the character for separation
        a = blur(ch[..., 3], cfg["halo"].get("sigma", 18) * s)
        rgb = screen(rgb, a[..., None] * hex_rgb(cfg["halo"].get("color", "#ffb86a")) * cfg["halo"].get("strength", 0.25))
    rgb = over(rgb, ch)
    if "rim" in cfg:
        rgb = screen(rgb, rim_light(ch, light, cfg["rim"], s))
    rgb = screen(rgb, fx[..., :3] * fx[..., 3:4])
    if "shafts" in cfg:
        rgb = screen(rgb, light_shafts(rgb, light, cfg["shafts"], s))
    if "bloom" in cfg:
        rgb = screen(rgb, bloom(rgb, cfg["bloom"], s))
    if "motes" in cfg:
        mid, fg = motes(rgb.shape[:2], cfg["motes"], s, seed)
        rgb = screen(rgb, mid)
        rgb = screen(rgb, fg)
    if "grade" in cfg:
        rgb = grade(rgb, cfg["grade"])
    if "vignette" in cfg:
        rgb = vignette(rgb, cfg["vignette"], light, s)
    if "grain" in cfg:
        rgb = grain(rgb, cfg["grain"], seed)
    rgb = over(rgb, fr)
    # keep the card's rounded-corner transparency from the frame/background alpha
    alpha = np.clip(np.maximum.reduce([bg[..., 3], ch[..., 3], fr[..., 3]]), 0, 1)
    img = np.dstack([rgb, alpha])
    out.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray((img * 255 + 0.5).astype(np.uint8), "RGBA").save(out)
    return out


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        raise SystemExit(2)
    print("wrote", run(Path(sys.argv[1])))
