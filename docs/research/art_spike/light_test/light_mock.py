"""Lighting mock: tile-scale light pools with precomputed per-level palette variants.

Not engine code. Demonstrates the proposed 'warm light / cold dark' rule:
every colour has 4 precomputed variants (dark, dim, lit, bright); a pixel picks
a variant from its light level; level boundaries use 4x4 ordered (Bayer)
dithering so falloff stays pixel-clean (no alpha gradients). Enemies standing
in darkness render as silhouettes with only their eye glint visible.
"""
import math, sys
from pathlib import Path
from PIL import Image
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'tools' / 'pixelforge'))
from pixelforge import parse_sprite, render_frame
from ramps import oklch_to_srgb

def srgb_to_oklch(rgb):
    def lin(c):
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(v) for v in rgb)
    l = 0.4122214708*r + 0.5363325363*g + 0.0514459929*b
    m = 0.2119034982*r + 0.6806995451*g + 0.1073969566*b
    s = 0.0883024619*r + 0.2817188376*g + 0.6299787005*b
    l_, m_, s_ = l ** (1/3), m ** (1/3), s ** (1/3)
    L = 0.2104542553*l_ + 0.7936177850*m_ - 0.0040720468*s_
    A = 1.9779984951*l_ - 2.4285922050*m_ + 0.4505937099*s_
    B = 0.0259040371*l_ + 0.7827717662*m_ - 0.8086757660*s_
    return L, math.hypot(A, B), math.degrees(math.atan2(B, A)) % 360

def toward(h, t, amt):
    d = (t - h + 540) % 360 - 180
    return (h + max(-amt, min(amt, d))) % 360

LEVELS = {  # (L scale, L offset, chroma mult, hue target, hue degrees)
    0: (0.28, 0.06, 0.50, 285, 60),   # dark: cold, low value, compressed contrast
    1: (0.55, 0.05, 0.70, 285, 35),   # dim
    2: (1.00, 0.00, 1.00, 0, 0),      # lit (authored colours)
    3: (1.06, 0.04, 1.15, 70, 18),    # bright: warm
}
_cache = {}
def relight(rgb, level):
    key = (rgb, level)
    if key not in _cache:
        if level == 2:
            _cache[key] = rgb
        else:
            L, C, H = srgb_to_oklch(rgb)
            ls, lo, cm, ht, hd = LEVELS[level]
            _cache[key] = oklch_to_srgb(min(L * ls + lo, 0.97), C * cm + (0.012 if level == 3 else 0), toward(H, ht, hd))
    return _cache[key]

BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]
TILE, COLS, ROWS = 32, 7, 10
W, H = 270, 480
OX, OY = (W - COLS * TILE) // 2, 70

def light_level(x, y, lights):
    """Continuous light value -> level with ordered dither at band edges."""
    best = float("-inf")
    for (lx, ly, radius) in lights:
        d = math.hypot(x - lx, y - ly) / TILE
        best = max(best, radius - d)          # >0 inside the pool
    v = best + (BAYER[y % 4][x % 4] / 16 - 0.5) * 0.35
    if v > 1.4: return 3
    if v > 0.0: return 2
    if v > -0.9: return 1
    return 0

def main():
    here = Path(__file__).parent
    floor = render_frame(*(lambda s: (s, s.frames[0]))(parse_sprite(here / 'floor.pxs')))
    lantern_sp = parse_sprite(here / 'lantern.pxs')
    lantern = render_frame(lantern_sp, lantern_sp.frames[0])
    knight_sp = parse_sprite(here.parent / 'knight_v1.pxs')
    knight = render_frame(knight_sp, knight_sp.frames[0])
    pal = knight_sp.palette.colours
    # enemy faction: palette swap + mirror; visor glint becomes ember-red so the
    # glint colour is unique to the eyes (needed for veiled silhouettes)
    eye = pal['i'][:3]
    m = {pal['C'][:3]: eye}
    m.update({pal[k][:3]: pal[v][:3] for k, v in zip('fghi', 'AABD')})
    m.update({pal[k][:3]: pal[v][:3] for k, v in zip('bcde', 'abcd')})
    enemy = knight.copy(); px = enemy.load()
    for yy in range(enemy.height):
        for xx in range(enemy.width):
            c = px[xx, yy]
            if c[3] and c[:3] in m: px[xx, yy] = m[c[:3]] + (255,)
    enemy = enemy.transpose(Image.FLIP_LEFT_RIGHT)

    lights = [(OX + 1.5 * TILE, OY + 6.5 * TILE, 2.6), (OX + 5.5 * TILE, OY + 7.5 * TILE, 2.3)]
    scene = Image.new('RGBA', (W, H), (12, 9, 20, 255))
    # floor
    for ty in range(ROWS):
        for tx in range(COLS):
            for sy in range(2):
                for sx in range(2):
                    scene.alpha_composite(floor, (OX + tx * TILE + sx * 16, OY + ty * TILE + sy * 16))
    # place actors (light applied afterwards, per pixel, except veiled silhouettes)
    actors = []
    for (c, r) in [(0, 7), (2, 6), (3, 8), (4, 7), (6, 7)]:
        actors.append((knight, c, r, False))
    for (c, r) in [(1, 1), (3, 2), (5, 1), (6, 3), (4, 5)]:
        actors.append((enemy, c, r, True))
    for (c, r) in [(1, 6), (5, 7)]:
        actors.append(('lantern', c, r, False))
    actors.sort(key=lambda a: a[2])
    for img, c, r, is_enemy in actors:
        x0, y0 = OX + c * TILE, OY + r * TILE
        if img == 'lantern':
            scene.alpha_composite(lantern, (x0 + 8, y0 - 14))
            continue
        foot_level = light_level(x0 + 16, y0 + 24, lights)
        spr = img
        if is_enemy and foot_level == 0:   # Veiled: silhouette + eye glint only
            spr = img.copy(); p = spr.load()
            for yy in range(spr.height):
                for xx in range(spr.width):
                    cc = p[xx, yy]
                    if cc[3]:
                        p[xx, yy] = (eye + (255,)) if cc[:3] == eye else (9, 6, 16, 255)
        scene.alpha_composite(spr, (x0, y0 - 6))
    # apply lighting per pixel to everything except emissive pixels
    out = scene.copy(); po = out.load(); ps = scene.load()
    flame = {tuple(v[:3]) for k, v in lantern_sp.palette.colours.items() if k in 'FGHI'}
    for y in range(H):
        for x in range(W):
            c = ps[x, y][:3]
            if c in flame or c == eye or c == (9, 6, 16) or c == pal['C'][:3]:
                continue
            po[x, y] = relight(c, light_level(x, y, lights)) + (255,)
    out.save(here / 'light_mock_1x.png')
    out.resize((W * 4, H * 4), Image.NEAREST).save(here / 'light_mock_x4.png')
    out.crop((OX - 4, OY + 3 * TILE, OX + COLS * TILE + 4, OY + 9 * TILE)).resize(((COLS * TILE + 8) * 4, 6 * TILE * 4), Image.NEAREST).save(here / 'light_mock_detail_x4.png')
    print('ok')

if __name__ == '__main__':
    main()
