"""inkkit: illustration primitives for code-authored official artwork.

Why this exists: uniform SVG strokes and hand-placed shadow blobs read as
clip-art. Professional vector illustration relies on two things this module
automates:

1. Tapered, variable-width line art. Brows, lashes, hair strands and
   contour lines thicken in the middle (or at the shadow side) and thin to
   points. Implemented by sampling a Catmull-Rom spline through control
   points and offsetting along normals with a width profile, emitting a
   filled polygon.
2. Consistent form shading from a single light. A shape's cel shadow is
   the shape minus a copy of itself shifted toward the light (SVG mask).
   The lit rim band is the shape minus a copy shifted away from it. Every
   shape in every hero therefore shares one light direction, and soft edges
   (semi-real undertone, for faces) are a blur on the mask copy.

All functions return SVG fragments (strings). An Art object collects <defs>
and body fragments and writes a complete document.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

Point = tuple[float, float]


# ------------------------------------------------------------ geometry
def catmull_rom(points: list[Point], samples: int = 12, closed: bool = False) -> list[Point]:
    """Dense polyline through points (centripetal-ish uniform Catmull-Rom)."""
    pts = list(points)
    if len(pts) < 2:
        return pts
    if closed:
        pts = [pts[-1]] + pts + [pts[0], pts[1]]
    else:
        pts = [pts[0]] + pts + [pts[-1]]
    out: list[Point] = []
    for i in range(1, len(pts) - 2):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[i + 1], pts[i + 2]
        for k in range(samples):
            t = k / samples
            t2, t3 = t * t, t * t * t
            x = 0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * t + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2
                       + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
            y = 0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * t + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2
                       + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
            out.append((x, y))
    if not closed:
        out.append(points[-1])
    return out


def smooth_path(points: list[Point], closed: bool = True, samples: int = 10) -> str:
    """SVG path data for a smooth curve through points."""
    poly = catmull_rom(points, samples, closed)
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in poly)
    return d + (" Z" if closed else "")


def width_profile(t: float, w0: float, wm: float, w1: float, peak: float = 0.4) -> float:
    """Ease from w0 up to wm at `peak`, then down to w1 (sine easing)."""
    if t <= peak:
        u = t / peak if peak > 0 else 1
        return w0 + (wm - w0) * math.sin(u * math.pi / 2)
    u = (t - peak) / (1 - peak) if peak < 1 else 1
    return wm + (w1 - wm) * (1 - math.cos(u * math.pi / 2))


def tapered(points: list[Point], w0: float = 0.4, wm: float = 3.0, w1: float = 0.3,
            peak: float = 0.4, samples: int = 10) -> str:
    """Filled-outline path data for a tapered stroke along a spline."""
    poly = catmull_rom(points, samples, False)
    n = len(poly)
    if n < 2:
        return ""
    left, right = [], []
    for i, (x, y) in enumerate(poly):
        xa, ya = poly[max(i - 1, 0)]
        xb, yb = poly[min(i + 1, n - 1)]
        dx, dy = xb - xa, yb - ya
        ln = math.hypot(dx, dy) or 1.0
        nx, ny = -dy / ln, dx / ln
        w = width_profile(i / (n - 1), w0, wm, w1, peak) / 2
        left.append((x + nx * w, y + ny * w))
        right.append((x - nx * w, y - ny * w))
    ring = left + right[::-1]
    return "M" + " L".join(f"{x:.2f} {y:.2f}" for x, y in ring) + " Z"


# ------------------------------------------------------------ document
@dataclass
class Art:
    width: int
    height: int
    light: Point = (-0.7, -0.7)  # unit-ish vector pointing FROM the subject TOWARD the key light
    defs: list[str] = field(default_factory=list)
    _uid: int = 0

    def uid(self, prefix: str) -> str:
        self._uid += 1
        return f"{prefix}{self._uid}"

    def light_offset(self, depth: float) -> Point:
        lx, ly = self.light
        ln = math.hypot(lx, ly) or 1
        return (lx / ln * depth, ly / ln * depth)

    # -- shading ---------------------------------------------------------
    def shaded(self, d: str, base: str, shadow: str | None = None, depth: float = 10,
               soft: float = 0.0, rim: str | None = None, rim_depth: float = 3,
               line: str | None = "#2a1b2e", line_w: float = 3.0, shadow_opacity: float = 1.0,
               extra: str = "") -> str:
        """Fill a shape, auto cel-shadow it away from the light, optional lit rim, outline.

        depth: how far (user units) the light-side copy shifts; bigger means a
               larger shadow. soft: blur on the shadow edge (0 = crisp cel;
               2–6 = semi-real faces).
        """
        out = [f'<path d="{d}" fill="{base}"/>']
        if shadow:
            mid = self.uid("sh")
            dx, dy = self.light_offset(depth)
            filt = ""
            if soft > 0:
                fid = self.uid("sb")
                self.defs.append(f'<filter id="{fid}" x="-30%" y="-30%" width="160%" height="160%">'
                                 f'<feGaussianBlur stdDeviation="{soft}"/></filter>')
                filt = f' filter="url(#{fid})"'
            self.defs.append(f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="{self.width}" height="{self.height}">'
                             f'<path d="{d}" fill="white"/>'
                             f'<path d="{d}" fill="black" transform="translate({dx:.1f} {dy:.1f})"{filt}/></mask>')
            out.append(f'<path d="{d}" fill="{shadow}" opacity="{shadow_opacity}" mask="url(#{mid})"/>')
        if rim:
            rid = self.uid("rm")
            dx, dy = self.light_offset(rim_depth)
            self.defs.append(f'<mask id="{rid}" maskUnits="userSpaceOnUse" x="0" y="0" width="{self.width}" height="{self.height}">'
                             f'<path d="{d}" fill="white"/>'
                             f'<path d="{d}" fill="black" transform="translate({-dx:.1f} {-dy:.1f})"/></mask>')
            out.append(f'<path d="{d}" fill="{rim}" mask="url(#{rid})"/>')
        if extra:
            out.append(extra)
        if line:
            out.append(f'<path d="{d}" fill="none" stroke="{line}" stroke-width="{line_w}" stroke-linejoin="round"/>')
        return "\n".join(out)

    def clip(self, d: str) -> str:
        cid = self.uid("cp")
        self.defs.append(f'<clipPath id="{cid}"><path d="{d}"/></clipPath>')
        return cid

    def blur_filter(self, std: float) -> str:
        fid = self.uid("bl")
        self.defs.append(f'<filter id="{fid}" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="{std}"/></filter>')
        return fid

    def document(self, layers: dict[str, str], extra_defs: str = "") -> str:
        body = "\n".join(f'<g id="layer-{name}">\n{content}\n</g>' for name, content in layers.items())
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" '
                f'viewBox="0 0 {self.width} {self.height}">\n<defs>\n' + "\n".join(self.defs) + extra_defs +
                "\n</defs>\n" + body + "\n</svg>\n")


def ink(points: list[Point], w0=0.4, wm=3.0, w1=0.3, color="#2a1b2e", peak=0.4, opacity: float = 1.0) -> str:
    """A tapered ink line."""
    op = f' opacity="{opacity}"' if opacity < 1 else ""
    return f'<path d="{tapered(points, w0, wm, w1, peak)}" fill="{color}"{op}/>'
