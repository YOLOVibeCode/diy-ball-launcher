#!/usr/bin/env python3
"""Draws the SVG diagrams in this folder from one set of dimensions.

Run:  python3 docs/diagrams/draw.py
No dependencies. Change a number in the DIMENSIONS block and every drawing follows.
All dimensions are inches.
"""
import math
import os

# ----------------------------------------------------------------- DIMENSIONS
BALL_D = 8.7                 # size 5 ball, 8.6 to 8.8
R = BALL_D / 2
WHEEL_D = 10.0               # 4.10/3.50-4 pneumatic tire
WHEEL_W = 3.5
GAP = 8.0                    # between tire faces; tune 7.5 to 8
CENTRES = WHEEL_D + GAP      # 18
DECK_W = 32.0                # wheels alone span 28, so the table is 32 wide
DECK_D = 36.0
CHUTE_W = 10.0
HALF_W = (DECK_W - CHUTE_W) / 2
PLY = 0.75
SPACER = 1.5                 # 2x2 under the deck's inner edges
CHUTE_DROP = PLY + SPACER    # chute floor below deck top: 2.25
SUB_W = 38.0                 # sub-base is wider so the elevation rods clear the table
LEG = 11.0                   # 2x4 legs: room for a motor hanging shaft-up
DECK_TOP = PLY + LEG + PLY   # 12.5 above ground
CHUTE_FLOOR = DECK_TOP - CHUTE_DROP          # 10.25
BALL_Z = CHUTE_FLOOR + R                     # 14.6, also the wheel mid-plane
WHEEL_BOTTOM = BALL_Z - WHEEL_W / 2          # 12.85
AXIS_FROM_FRONT = 6.0
MOTOR_D = 4.25
MOTOR_L = 9.5
GUARD_TOP = WHEEL_BOTTOM + WHEEL_W + 1.15    # about 17.5
ROD_TOP = 24.75

PVC = 1.315                  # 1 in schedule 40 outside diameter
RAIL_CC = 6.5                # rail centre to centre
BALL_ON_RAIL = math.sqrt((R + PVC / 2) ** 2 - (RAIL_CC / 2) ** 2)   # ball centre above rail centres, 3.81
RAMP_LEN = 96.0
RAMP_DEG = 10.0
RUNOUT = 36.0                # gate to the lower end of the ramp
RAIL_END_Z = CHUTE_FLOOR + (R - BALL_ON_RAIL)  # rail centre height where it meets the chute

GATE_A = 6.5                 # star axis to ramp centre line
ARM_W = 1.0                  # arm width as cut
TIP_C = 7.5                  # axis to the centre of the rounded tip (tips on a 16 in circle)
RP = R + ARM_W / 2           # ball centre to arm centre line when touching

# --------------------------------------------------------------------- STYLE
STYLE = """
text{fill:#1f2933;font-size:13px}
.title{font-size:21px;font-weight:700}
.sub{font-size:13px;fill:#52606d}
.small{font-size:11.5px;fill:#3e4c59}
.b{font-weight:700}
.dimt{font-size:12.5px;fill:#1d4ed8;font-weight:600}
.ply{fill:#ecd9b4;stroke:#1f2933;stroke-width:1.2}
.ply2{fill:#f8f1e0;stroke:#1f2933;stroke-width:1.2}
.lumber{fill:#d7b582;stroke:#1f2933;stroke-width:1.2}
.far{fill:#efe4cf;stroke:#9aa5b1;stroke-width:1}
.subbase{fill:#f1f3f5;stroke:#52606d;stroke-width:1.2;stroke-dasharray:6 4}
.subsolid{fill:#e4e7eb;stroke:#1f2933;stroke-width:1.2}
.tire{fill:#3e4c59;stroke:#1f2933;stroke-width:1.2}
.hub{fill:#b8c2cc;stroke:#1f2933;stroke-width:1}
.ball{fill:#fde2b3;stroke:#c2410c;stroke-width:1.6}
.ballg{fill:#fff6e5;stroke:#c2410c;stroke-width:1.2;stroke-dasharray:5 4}
.motor{fill:#a9bcd6;stroke:#1f2933;stroke-width:1.2}
.steel{fill:#b8c2cc;stroke:#1f2933;stroke-width:1}
.pvc{fill:#e4edf6;stroke:#486581;stroke-width:1.2}
.star{fill:#d7b582;stroke:#1f2933;stroke-width:1.2}
.guard{fill:none;stroke:#15803d;stroke-width:2;stroke-dasharray:7 4}
.hidden{fill:none;stroke:#52606d;stroke-width:1;stroke-dasharray:5 4}
.ghost{fill:none;stroke:#7b8794;stroke-width:1.1;stroke-dasharray:4 4}
.centre{stroke:#7b8794;stroke-width:.9;stroke-dasharray:12 4 2 4;fill:none}
.ink{stroke:#1f2933;stroke-width:1.2;fill:none}
.dim{stroke:#1d4ed8;stroke-width:1;fill:none}
.ext{stroke:#1d4ed8;stroke-width:.6;fill:none}
.lead{stroke:#52606d;stroke-width:.9;fill:none}
.flow{stroke:#c2410c;stroke-width:2.4;fill:none}
.spin{stroke:#fff;stroke-width:1.8;fill:none}
.box{fill:#f8fafc;stroke:#1f2933;stroke-width:1.3}
.encl{fill:#fbfcfd;stroke:#52606d;stroke-width:1.4;stroke-dasharray:9 5}
.hot{stroke:#111827;stroke-width:2.6;fill:none}
.neu{stroke:#8d99a6;stroke-width:2.6;fill:none}
.gnd{stroke:#15803d;stroke-width:2.6;fill:none}
.ap{stroke:#dc2626;stroke-width:2.6;fill:none}
.am{stroke:#2563eb;stroke-width:2.6;fill:none}
.vp{stroke:#ea580c;stroke-width:2.6;fill:none}
.vm{stroke:#475569;stroke-width:2.6;fill:none}
.halo{stroke:#fbfcfd;stroke-width:8;fill:none}
.bal{fill:#fff;font-size:12.5px;font-weight:700}
"""

DEFS = """
<marker id="da" viewBox="0 0 10 10" refX="9.2" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 1.2 10 5 0 8.8z" fill="#1d4ed8"/></marker>
<marker id="db" viewBox="0 0 10 10" refX=".8" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M10 1.2 0 5 10 8.8z" fill="#1d4ed8"/></marker>
<marker id="fa" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto"><path d="M0 0 10 5 0 10z" fill="#c2410c"/></marker>
<marker id="wa" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0 10 5 0 10z" fill="#fff"/></marker>
<marker id="ia" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 10 5 0 10z" fill="#1f2933"/></marker>
"""


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


class Svg:
    def __init__(self, w, h, title, desc):
        self.w, self.h, self.t, self.d, self.p = w, h, title, desc, []

    def add(self, s):
        self.p.append(s)

    def rect(self, x, y, w, h, cls, rx=0, extra=""):
        self.add(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" rx="{f(rx)}" class="{cls}" {extra}/>')

    def circle(self, cx, cy, r, cls, extra=""):
        self.add(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" class="{cls}" {extra}/>')

    def ellipse(self, cx, cy, rx, ry, cls):
        self.add(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" class="{cls}"/>')

    def line(self, x1, y1, x2, y2, cls, extra=""):
        self.add(f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" class="{cls}" {extra}/>')

    def poly(self, pts, cls, close=False, extra=""):
        d = "M" + " L".join(f"{f(x)} {f(y)}" for x, y in pts) + (" Z" if close else "")
        self.add(f'<path d="{d}" class="{cls}" {extra}/>')

    def path(self, d, cls, extra=""):
        self.add(f'<path d="{d}" class="{cls}" {extra}/>')

    def text(self, x, y, s, cls="", anchor="start", rot=None):
        tr = f' transform="rotate({rot} {f(x)} {f(y)})"' if rot is not None else ""
        c = f' class="{cls}"' if cls else ""
        self.add(f'<text x="{f(x)}" y="{f(y)}" text-anchor="{anchor}"{c}{tr}>{esc(s)}</text>')

    def lines(self, x, y, rows, cls="", anchor="start", lh=16):
        for i, row in enumerate(rows):
            self.text(x, y + i * lh, row, cls, anchor)

    def heading(self, title, sub):
        self.text(28, 40, title, "title")
        self.text(28, 62, sub, "sub")

    def dimh(self, x1, x2, y, label, e1=None, e2=None, ty=-6, tx=None, anchor="middle"):
        """Horizontal dimension. e1/e2: y where each extension line starts."""
        for x, e in ((x1, e1), (x2, e2)):
            if e is not None:
                self.line(x, e, x, y + (5 if y > e else -5), "ext")
        self.line(x1, y, x2, y, "dim", 'marker-start="url(#db)" marker-end="url(#da)"')
        self.text((x1 + x2) / 2 if tx is None else tx, y + ty, label, "dimt", anchor)

    def dimv(self, y1, y2, x, label, e1=None, e2=None, side=-1, flat=False, tdy=0):
        """Vertical dimension. e1/e2: x where each extension line starts."""
        for y, e in ((y1, e1), (y2, e2)):
            if e is not None:
                self.line(e, y, x + (5 if x > e else -5), y, "ext")
        self.line(x, y1, x, y2, "dim", 'marker-start="url(#db)" marker-end="url(#da)"')
        ym = (y1 + y2) / 2 + tdy
        if flat:
            self.text(x + side * 7, ym + 4, label, "dimt", "end" if side < 0 else "start")
        else:
            self.text(x + side * 6 + (0 if side < 0 else 9), ym, label, "dimt", "middle", rot=-90)

    def label(self, x, y, rows, target, anchor="start", cls="", elbow=None):
        """Text block with a leader line to target."""
        tx, ty = target
        sx = x - 6 if anchor == "start" else x + 6
        sy = y - 4
        pts = [(tx, ty)] + ([elbow] if elbow else []) + [(sx, sy)]
        self.poly(pts, "lead")
        self.circle(tx, ty, 2.2, "", 'fill="#52606d"')
        self.lines(x, y, rows, cls, anchor)

    def note(self, x, y, rows, target, attach, cls="", anchor="start", lh=16):
        """Text block with a straight leader from an explicit attach point to target."""
        self.line(attach[0], attach[1], target[0], target[1], "lead")
        self.circle(target[0], target[1], 2.2, "", 'fill="#52606d"')
        self.lines(x, y, rows, cls, anchor, lh)

    def balloon(self, x, y, n):
        self.circle(x, y, 10, "", 'fill="#1f2933"')
        self.text(x, y + 4.5, str(n), "bal", "middle")

    def save(self, name):
        here = os.path.dirname(os.path.abspath(__file__))
        body = "\n".join(self.p)
        out = (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}" '
            f'role="img" aria-labelledby="t d" font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif">\n'
            f'<title id="t">{esc(self.t)}</title>\n<desc id="d">{esc(self.d)}</desc>\n'
            f"<defs>{DEFS}</defs>\n<style>{STYLE}</style>\n"
            f'<rect width="{self.w}" height="{self.h}" fill="#ffffff"/>\n{body}\n</svg>\n'
        )
        with open(os.path.join(here, name), "w") as fh:
            fh.write(out)
        print("wrote", name)


def arc(cx, cy, r, t1, t2):
    """SVG arc from angle t1 to t2 (degrees, counter-clockwise positive as seen on the page)."""
    a1, a2 = math.radians(t1), math.radians(t2)
    x1, y1 = cx + r * math.cos(a1), cy - r * math.sin(a1)
    x2, y2 = cx + r * math.cos(a2), cy - r * math.sin(a2)
    large = 1 if abs(t2 - t1) > 180 else 0
    sweep = 0 if t2 > t1 else 1
    return f"M{f(x1)} {f(y1)} A{f(r)} {f(r)} 0 {large} {sweep} {f(x2)} {f(y2)}"


# ------------------------------------------------------------- 1. TOP VIEW
def top_view():
    W, H, s, CX, YF = 1080, 940, 16.0, 410, 205

    def P(x, y):
        return CX + s * x, YF + s * (DECK_D - y)

    d = Svg(W, H, "Launcher, top view",
            "Plan of the launcher table: two deck panels either side of a dropped ball chute, two 10 inch wheels "
            "18 inches apart at the front with guards, hinges at the rear edge and an elevation rod at each front corner.")
    d.heading("1 · Launcher, top view", "Dimensions in inches, drawn to scale. The shot leaves at the top of the page.")

    x, y = P(-SUB_W / 2, DECK_D)
    d.rect(x, y, SUB_W * s, DECK_D * s, "subbase")
    for x0 in (-DECK_W / 2, CHUTE_W / 2):
        x, y = P(x0, DECK_D)
        d.rect(x, y, HALF_W * s, DECK_D * s, "ply")
    x, y = P(-CHUTE_W / 2, DECK_D)
    d.rect(x, y, CHUTE_W * s, DECK_D * s, "ply2")
    for sg in (-1, 1):                       # 2x2 spacers under the deck edges
        xa, ya = P(sg * (CHUTE_W / 2 + SPACER), DECK_D)
        xb, yb = P(sg * (CHUTE_W / 2 + SPACER), 0)
        d.line(xa, ya, xb, yb, "hidden")
    xa, ya = P(0, -1.2)
    xb, yb = P(0, DECK_D + 1.2)
    d.line(xa, ya, xb, yb, "centre")

    wy = DECK_D - AXIS_FROM_FRONT
    for sg in (-1, 1):                       # outrigger blocks and rods
        x, y = P(DECK_W / 2 if sg > 0 else -DECK_W / 2 - 3, DECK_D)
        d.rect(x, y, 3 * s, 3 * s, "lumber")
        cx, cy = P(sg * 17.5, DECK_D - 1.5)
        d.circle(cx, cy, 0.34 * s, "steel")
    for sg in (-1, 1):                       # hinges
        x, y = P(sg * 10 - 1.75, 0.55)
        d.rect(x, y, 3.5 * s, 1.1 * s, "steel")

    # incoming ball, ball in the nip
    cx, cy = P(0, 9)
    d.circle(cx, cy, R * s, "ballg")
    cx, cy = P(0, wy)
    d.ellipse(cx, cy, GAP / 2 * s, (R + 0.2) * s, "ball")
    for sg in (-1, 1):                       # wheels
        cx, cy = P(sg * CENTRES / 2, wy)
        d.circle(cx, cy, WHEEL_D / 2 * s, "tire")
        d.circle(cx, cy, 1.7 * s, "hub")
        d.circle(cx, cy, 0.33 * s, "steel")
        d.path(arc(cx, cy, 3.3 * s, 215, 325) if sg < 0 else arc(cx, cy, 3.3 * s, 325, 215),
               "spin", 'marker-end="url(#wa)"')
        xa, ya = P(sg * CENTRES / 2, wy - 6.2)
        xb, yb = P(sg * CENTRES / 2, DECK_D + 2.6)
        d.line(xa, ya, xb, yb, "centre")
    for sg in (-1, 1):                       # guards, open toward the ball
        pts = [P(sg * CHUTE_W / 2, wy - 6), P(sg * 15.5, wy - 6), P(sg * 15.5, DECK_D), P(sg * CHUTE_W / 2, DECK_D)]
        d.poly(pts, "guard")

    # flow arrows
    xa, ya = P(0, -3.6)
    xb, yb = P(0, -0.7)
    d.line(xa, ya, xb, yb, "flow", 'marker-end="url(#fa)"')
    d.text(xa + 14, ya - 14, "balls roll in from the feeder ramp", "small")
    xa, ya = P(0, 14)
    xb, yb = P(0, 19.6)
    d.line(xa, ya, xb, yb, "flow", 'marker-end="url(#fa)"')
    xa, ya = P(0, DECK_D + 3.6)
    xb, yb = P(0, DECK_D + 7.4)
    d.line(xa, ya, xb, yb, "flow", 'marker-end="url(#fa)"')
    d.text(xb + 14, yb + 14, "SHOT", "b")

    # dimensions
    yr = P(0, 0)[1]
    yf = P(0, DECK_D)[1]
    d.dimh(P(-CHUTE_W / 2, 0)[0], P(CHUTE_W / 2, 0)[0], P(0, 2.4)[1], "chute 10")
    d.dimh(P(-DECK_W / 2, 0)[0], P(DECK_W / 2, 0)[0], yr + 88, "table 32", yr, yr)
    d.dimh(P(-SUB_W / 2, 0)[0], P(SUB_W / 2, 0)[0], yr + 114, "sub-base 38", yr, yr)
    d.dimh(P(-CENTRES / 2, 0)[0], P(CENTRES / 2, 0)[0], yf - 34, "wheel centres 18", tx=P(-4.6, 0)[0])
    yg = P(0, wy - 7.4)[1]
    d.dimh(P(-GAP / 2, 0)[0], P(GAP / 2, 0)[0], yg, "gap 7-1/2 to 8", P(0, wy)[1], P(0, wy)[1], ty=17)
    xl = P(-SUB_W / 2, 0)[0] - 30
    d.dimv(yf, yr, xl, "depth 36", P(-SUB_W / 2, 0)[0], P(-SUB_W / 2, 0)[0])
    xr = P(SUB_W / 2, 0)[0] + 20
    d.dimv(yf, P(0, wy)[1], xr, "6", P(SUB_W / 2, 0)[0], P(CENTRES / 2 + WHEEL_D / 2, 0)[0], side=1, flat=True)

    # labels
    lx = 770
    d.label(lx, 150, ["Outrigger block and 1/2 in threaded rod,", "one each side: sets the elevation"], P(18.6, DECK_D - 0.6))
    d.label(lx, 232, ["Wheel guard: expanded metal with a", "plywood top. Open only toward the ball."], P(15.5, wy + 3.5))
    d.label(lx, 318, ["10 in pneumatic wheel on a treadmill", "motor. The motor hangs under the deck,", "shaft up."], P(CENTRES / 2 + 3.6, wy - 3.4))
    d.label(lx, 420, ["This motor sits on slotted holes.", "Slide it to set the gap."], P(CENTRES / 2, wy - 0.3), elbow=(lx - 40, 416))
    d.label(lx, 500, ["Deck: two 11 x 36 panels of 3/4 in", "plywood on a 2x4 frame"], P(13, 16))
    d.label(lx, 580, ["Chute floor, 2-1/4 in below the deck top,", "so the ball centre sits level with the", "middle of the tires"], P(3.4, 12.5), elbow=(lx - 60, 576))
    d.label(lx, 690, ["Sub-base (dashed): 38 x 36, 3/4 in", "plywood, stays flat on the ground"], P(18.2, 5))
    d.label(lx, 770, ["Two heavy hinges join the table's rear", "rail to the sub-base"], P(11.75, 0.2), elbow=(lx - 30, 766))
    d.text(28, H - 22, "Wheels turn toward each other (white arrows). Both speeds set the power; a speed difference curves the shot.", "small")
    d.save("01-launcher-top-view.svg")


# ------------------------------------------------------- 2. FRONT SECTION
def front_section():
    W, H, s, CX, YG = 1160, 780, 19.0, 480, 660

    def P(x, z):
        return CX + s * x, YG - s * z

    d = Svg(W, H, "Launcher, section through the wheels",
            "Cross-section looking from the front: the ball sits in a dropped chute between two horizontal wheels, "
            "each on a motor hanging under the deck inside an 11 inch tall frame.")
    d.heading("2 · Launcher, section through the wheels", "Looking from the front toward the feeder. Dimensions in inches, drawn to scale.")

    d.line(P(-23, 0)[0], YG, P(23, 0)[0], YG, "ground")
    x, y = P(-SUB_W / 2, PLY)
    d.rect(x, y, SUB_W * s, PLY * s, "subsolid")
    # cross rails beyond the cut
    for z0 in (PLY, CHUTE_FLOOR - PLY - 3.5):
        x, y = P(-14.5, z0 + 3.5)
        d.rect(x, y, 29 * s, 3.5 * s, "far")
    for sg in (-1, 1):
        xl = 14.5 if sg > 0 else -16
        x, y = P(xl, PLY + LEG)
        d.rect(x, y, 1.5 * s, LEG * s, "far")                       # leg beyond
        for z0 in (PLY, PLY + LEG - 3.5):                           # side rails, cut
            x, y = P(xl, z0 + 3.5)
            d.rect(x, y, 1.5 * s, 3.5 * s, "lumber")
            d.line(x, y, x + 1.5 * s, y + 3.5 * s, "ink")
            d.line(x + 1.5 * s, y, x, y + 3.5 * s, "ink")
        # outrigger and rod
        xo = 16 if sg > 0 else -19
        x, y = P(xo, 6.5)
        d.rect(x, y, 3 * s, 1.5 * s, "lumber")
        x, y = P(sg * 17.5 - 0.25, ROD_TOP)
        d.rect(x, y, 0.5 * s, (ROD_TOP - PLY) * s, "steel")
        x, y = P(sg * 17.5 - 0.8, 5.0)
        d.rect(x, y, 1.6 * s, 0.45 * s, "steel")                     # wing nut under the block
    # chute floor, spacers, deck
    x, y = P(-CHUTE_W / 2 - SPACER, CHUTE_FLOOR)
    d.rect(x, y, (CHUTE_W + 2 * SPACER) * s, PLY * s, "ply2")
    for sg in (-1, 1):
        xl = CHUTE_W / 2 if sg > 0 else -CHUTE_W / 2 - SPACER
        x, y = P(xl, CHUTE_FLOOR + SPACER)
        d.rect(x, y, SPACER * s, SPACER * s, "lumber")
        d.line(x, y, x + SPACER * s, y + SPACER * s, "ink")
        d.line(x + SPACER * s, y, x, y + SPACER * s, "ink")
        xl = CHUTE_W / 2 if sg > 0 else -DECK_W / 2
        x, y = P(xl, DECK_TOP)
        d.rect(x, y, HALF_W * s, PLY * s, "ply")
    # motors, shafts, wheels
    for sg in (-1, 1):
        cx = sg * CENTRES / 2
        x, y = P(cx - MOTOR_D / 2, DECK_TOP - PLY)
        d.rect(x, y, MOTOR_D * s, MOTOR_L * s, "motor", rx=10)
        x, y = P(cx - 0.33, WHEEL_BOTTOM + WHEEL_W + 0.5)
        d.rect(x, y, 0.66 * s, (WHEEL_BOTTOM + WHEEL_W + 0.5 - (DECK_TOP - PLY)) * s, "steel")
        x, y = P(cx - WHEEL_D / 2, WHEEL_BOTTOM + WHEEL_W)
        d.rect(x, y, WHEEL_D * s, WHEEL_W * s, "tire", rx=22)
        x, y = P(cx - 1.7, WHEEL_BOTTOM + WHEEL_W + 0.25)
        d.rect(x, y, 3.4 * s, (WHEEL_W + 0.5) * s, "hub", rx=4)
        xa, ya = P(cx, 1.2)
        xb, yb = P(cx, GUARD_TOP + 5.0)
        d.line(xa, ya, xb, yb, "centre")
    cx, cy = P(0, BALL_Z)
    d.ellipse(cx, cy, GAP / 2 * s, R * s, "ball")
    xa, ya = P(-CENTRES / 2 - WHEEL_D / 2 - 1, BALL_Z)
    xb, yb = P(CENTRES / 2 + WHEEL_D / 2 + 1, BALL_Z)
    d.line(xa, ya, xb, yb, "centre")
    for sg in (-1, 1):                       # guards
        pts = [P(sg * CHUTE_W / 2, GUARD_TOP), P(sg * 15.5, GUARD_TOP), P(sg * 15.5, DECK_TOP)]
        d.poly(pts, "guard")

    # dimensions
    xl = P(-SUB_W / 2, 0)[0] - 50
    d.dimv(P(0, DECK_TOP)[1], YG, xl, "deck top 12-1/2", P(-DECK_W / 2, 0)[0], P(-SUB_W / 2, 0)[0])
    yt = P(0, GUARD_TOP + 5.4)[1]
    d.dimh(P(-CENTRES / 2, 0)[0], P(CENTRES / 2, 0)[0], yt, "wheel centres 18")
    yt2 = P(0, BALL_Z + R + 1.5)[1]
    d.dimh(P(-GAP / 2, 0)[0], P(GAP / 2, 0)[0], yt2, "gap 7-1/2 to 8", P(0, WHEEL_BOTTOM + WHEEL_W)[1], P(0, WHEEL_BOTTOM + WHEEL_W)[1])
    xc = P(0.9, 0)[0]
    d.dimv(P(0, BALL_Z)[1], P(0, CHUTE_FLOOR)[1], xc, "4-3/8", side=-1, flat=True)
    xm = P(-CENTRES / 2 - MOTOR_D / 2 - 1.3, 0)[0]
    d.dimv(P(0, DECK_TOP - PLY)[1], P(0, DECK_TOP - PLY - MOTOR_L)[1], xm, "motor about 9-1/2",
           P(-CENTRES / 2 - MOTOR_D / 2, 0)[0], P(-CENTRES / 2 - MOTOR_D / 2, 0)[0])
    d.dimh(P(-DECK_W / 2, 0)[0], P(DECK_W / 2, 0)[0], YG + 34, "table 32", YG, YG)
    d.dimh(P(-SUB_W / 2, 0)[0], P(SUB_W / 2, 0)[0], YG + 62, "sub-base 38", YG, YG)

    # labels
    lx = 900
    d.label(lx, 120, ["1/2 in threaded rod. A wing nut", "under the outrigger block lifts", "the front of the table."], P(17.75, 20))
    d.label(lx, 206, ["Guard (dashed green)"], P(15.5, 15.6))
    d.label(lx, 252, ["Tire sits about 3/8 in above the", "deck. Its middle is level with", "the ball centre."], P(13.2, WHEEL_BOTTOM + 0.4))
    d.label(lx, 338, ["Deck panel on 2x2 spacers.", "The spacers set the chute depth:", "2-1/4 in below the deck top."], P(5.75, CHUTE_FLOOR + 0.75), elbow=(lx - 40, 334))
    d.label(lx, 430, ["Treadmill motor, shaft up, on its", "own bracket or U-bolts. One is on", "slotted holes to set the gap."], P(CENTRES / 2 + MOTOR_D / 2, 6.5))
    d.label(lx, 520, ["2x4 frame, 11 in legs: room for", "the motors. Measure yours first."], P(15.25, 6.0), elbow=(lx - 30, 516))
    d.label(lx, 590, ["Sub-base"], P(18.4, 0.4))
    d.text(28, H - 20, "Chute depth rule: ball centre (4-3/8 above the chute floor) must equal the height of the middle of the tires. "
           "Re-measure once the wheels are on the motors.", "small")
    d.save("02-launcher-front-section.svg")


# ------------------------------------------------------- 3. SIDE ELEVATION
def side_elevation():
    W, H, s, X0, YG = 1290, 670, 7.6, 200, 520
    b = math.radians(RAMP_DEG)

    def P(x, z):
        return X0 + s * x, YG - s * z

    def ramp(dist, off=0.0):
        """Point at dist along the ramp from its lower end, off = height above rail centres."""
        return P(DECK_D + dist * math.cos(b) - off * math.sin(b), RAIL_END_Z + dist * math.sin(b) + off * math.cos(b))

    d = Svg(W, H, "Whole machine, side view",
            "Side view: balls queue on a sloped PVC ramp, a star-wheel gate lets one through at a time, it rolls down a "
            "run-out into the chute and between the wheels, and the shot leaves to the left. The table tilts on a rear hinge.")
    d.heading("3 · Whole machine, side view", "Dimensions in inches, drawn to scale. Ramp drawn at 10 degrees. The shot leaves to the left.")

    d.line(P(-24, 0)[0], YG, P(136, 0)[0], YG, "ground")
    th = math.radians(15)

    def T(x, z):                              # the table tilted 15 degrees about the hinge
        dx, dz = x - DECK_D, z - PLY
        return P(DECK_D + dx * math.cos(th) + dz * math.sin(th), PLY - dx * math.sin(th) + dz * math.cos(th))

    d.poly([T(0, DECK_TOP - PLY), T(DECK_D, DECK_TOP - PLY), T(DECK_D, DECK_TOP), T(0, DECK_TOP)], "ghost", close=True)
    d.poly([T(1, WHEEL_BOTTOM), T(11, WHEEL_BOTTOM), T(11, WHEEL_BOTTOM + WHEEL_W), T(1, WHEEL_BOTTOM + WHEEL_W)], "ghost", close=True)
    xa, ya = T(-1, BALL_Z)
    xb, yb = T(-12, BALL_Z)
    d.line(xa, ya, xb, yb, "ghost", 'marker-end="url(#ia)"')

    # launcher
    x, y = P(0, PLY)
    d.rect(x, y, DECK_D * s, PLY * s, "subsolid")
    for x0 in (0, DECK_D - 3.5):
        x, y = P(x0, PLY + LEG)
        d.rect(x, y, 3.5 * s, LEG * s, "lumber")
    for z0 in (PLY, PLY + LEG - 3.5):
        x, y = P(3.5, z0 + 3.5)
        d.rect(x, y, (DECK_D - 7) * s, 3.5 * s, "lumber")
    x, y = P(0, DECK_TOP)
    d.rect(x, y, DECK_D * s, PLY * s, "ply")
    x, y = P(AXIS_FROM_FRONT - MOTOR_D / 2, DECK_TOP - PLY)
    d.rect(x, y, MOTOR_D * s, MOTOR_L * s, "hidden", rx=4)
    d.text(P(9.4, 0)[0], P(0, 5.5)[1], "motor (dashed)", "small")
    xa, ya = P(0, CHUTE_FLOOR)
    xb, yb = P(DECK_D, CHUTE_FLOOR)
    d.line(xa, ya, xb, yb, "hidden")
    x, y = P(1, WHEEL_BOTTOM + WHEEL_W)
    d.rect(x, y, WHEEL_D * s, WHEEL_W * s, "tire", rx=9)
    x, y = P(0, GUARD_TOP)
    d.rect(x, y, 12 * s, (GUARD_TOP - DECK_TOP) * s, "guard")
    x, y = P(1.5, ROD_TOP)
    d.rect(x, y, 0.5 * s, (ROD_TOP - PLY) * s, "steel")
    x, y = P(0.3, 6.5)
    d.rect(x, y, 2.9 * s, 1.5 * s, "lumber")
    cx, cy = P(DECK_D, PLY)
    d.circle(cx, cy, 5, "steel")
    cx, cy = P(-12, BALL_Z)
    d.circle(cx, cy, R * s, "ball")
    xa, ya = P(-17.2, BALL_Z)
    xb, yb = P(-22.2, BALL_Z)
    d.line(xa, ya, xb, yb, "flow", 'marker-end="url(#fa)"')

    # feeder
    for dist in (8, 50, 92):
        xa, ya = ramp(dist)
        d.rect(xa - PVC * s / 2, ya, PVC * s, YG - ya, "pvc")
        d.rect(xa - 14, YG - 5, 28, 5, "pvc")
    deg = -RAMP_DEG

    def slanted(dist, off, w, h, cls):
        x, y = ramp(dist, off)
        d.add(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w * s)}" height="{f(h * s)}" rx="3" class="{cls}" '
              f'transform="rotate({deg} {f(x)} {f(y)})"/>')

    slanted(0, PVC / 2, RAMP_LEN, PVC, "pvc")
    slanted(RUNOUT - 9, -1.4, 20, 0.75, "ply")
    slanted(RUNOUT - 2.2, 2.9, 4.4, 4.2, "lumber")
    slanted(RUNOUT - 8, BALL_ON_RAIL + 0.4, 16, 0.75, "star")
    cx, cy = ramp(15, BALL_ON_RAIL)
    d.circle(cx, cy, R * s, "ballg")
    xa, ya = ramp(8.6, BALL_ON_RAIL)
    xb, yb = ramp(3.4, BALL_ON_RAIL)
    d.line(xa, ya, xb, yb, "flow", 'marker-end="url(#fa)"')
    for i in range(6):
        cx, cy = ramp(RUNOUT + RP + i * BALL_D, BALL_ON_RAIL)
        d.circle(cx, cy, R * s, "ball")

    # dimensions
    d.dimh(P(0, 0)[0], P(DECK_D, 0)[0], YG + 56, "launcher 36", YG, YG)
    xe = ramp(RAMP_LEN)[0]
    d.dimh(P(DECK_D, 0)[0], xe, YG + 56, "ramp 96 long (about 95 along the ground)", YG, YG)
    d.dimh(P(0, 0)[0], xe, YG + 86, "about 11 ft overall", YG, YG)
    d.dimv(P(0, DECK_TOP)[1], YG, P(-4, 0)[0], "12-1/2", P(0, 0)[0], None, side=-1, flat=True)
    xt, yt = ramp(RAMP_LEN)
    d.dimv(yt, YG, xt + 30, "top of rails about 27-1/2", xt, None, side=1)

    # notes
    d.note(36, 150, ["Dashed outline: the table tilted 15 degrees.", "The rods allow 0 to 30 degrees."], T(12, DECK_TOP), (150, 174))
    d.note(36, 292, ["Threaded rod and wing nut,", "one each side"], P(1.75, ROD_TOP - 0.5), (198, 290))
    d.note(330, 215, ["Wheel guard"], P(11.6, GUARD_TOP - 0.2), (334, 222))
    d.note(520, 200, ["Star-wheel gate on a 12 V worm gearmotor:", "one ball per quarter turn"],
           ramp(RUNOUT - 5.6, BALL_ON_RAIL + 0.4), (560, 224))
    d.note(880, 150, ["Queue: 6 balls on two 1 in PVC rails,", "6-1/2 in centre to centre"],
           ramp(RUNOUT + RP + 2 * BALL_D, BALL_ON_RAIL + R), (930, 174))
    d.note(566, 470, ["Run-out, 36 in: the ball gathers speed", "to roll through the chute"], ramp(21, -PVC / 2 - 0.2), (640, 456))
    d.note(490, YG + 26, ["Hinge: the table's rear rail to the sub-base"], P(DECK_D + 0.5, PLY), (486, YG + 20), cls="small")
    d.text(28, H - 22, "Raising the tilt lifts the chute, so the ball has to roll uphill to the wheels. For high shots, stand the ramp "
           "higher or steeper (8 to 15 degrees) until the ball still reaches the wheels.", "small")
    d.save("03-machine-side-view.svg")


# ------------------------------------------------------------ 4. FEED GATE
def gate_state(phi_deg):
    """Ball centre positions along the ramp (x downstream, axis at 0) for a star angle.

    Returns (ball 1, ball 2). Ball 1 is None once it has left the arm tip."""
    p = math.radians(phi_deg)
    s_on_face = (GATE_A - RP * math.sin(p)) / math.cos(p)
    if s_on_face <= TIP_C:
        x1 = (GATE_A * math.sin(p) - RP) / math.cos(p)
        natural = x1 - BALL_D
    else:
        x1 = None
        natural = 1e9
    tbx, tby = -TIP_C * math.cos(p), TIP_C * math.sin(p)       # tip of the next arm
    lim = [natural]
    if abs(GATE_A - tby) < RP:
        lim.append(tbx - math.sqrt(RP ** 2 - (GATE_A - tby) ** 2))
    pb = p - math.pi / 2
    if abs(math.cos(pb)) > 1e-6:
        sb = (GATE_A - RP * math.sin(pb)) / math.cos(pb)
        if 0 < sb <= TIP_C:
            lim.append((GATE_A * math.sin(pb) - RP) / math.cos(pb))
    return x1, min(lim)


def gate_check():
    """Smallest clearance between ball 1 and the next arm's tip over a quarter turn (negative = squeeze)."""
    worst = 9.0
    for i in range(0, 760):
        phi = i / 10
        x1, _ = gate_state(phi)
        if x1 is None:
            break
        p = math.radians(phi)
        tbx, tby = -TIP_C * math.cos(p), TIP_C * math.sin(p)
        worst = min(worst, math.hypot(x1 - tbx, GATE_A - tby) - RP)
    return worst


def feed_gate():
    W, H, s = 1220, 900, 9.0
    d = Svg(W, H, "Feed gate",
            "Three plan views of the four-arm star wheel beside the ramp at 0, 45 and 80 degrees, showing one arm holding "
            "the first ball while the next arm slips between the first and second balls, plus a section across the ramp.")
    d.heading("4 · Feed gate: four-arm star wheel", "Dimensions in inches, drawn to scale. Balls move right to left. One ball passes per quarter turn.")

    def panel(cx, cy, phi, name, note):
        def P(x, y):
            return cx - s * x, cy - s * y

        xl, xr = P(15, 0)[0], P(-28, 0)[0]
        for off in (-RAIL_CC / 2, RAIL_CC / 2):
            y = P(0, GATE_A + off)[1]
            d.rect(xl, y - PVC * s / 2, xr - xl, PVC * s, "pvc", rx=3)
        x1, x2 = gate_state(phi)
        balls = [(12.0, "ballg")] if x1 is None else [(x1, "ball")]
        balls += [(x2 - i * BALL_D, "ball") for i in range(4)]
        for bx, cls in balls:
            px, py = P(bx, GATE_A)
            if px < xr + 20:
                d.circle(px, py, R * s, cls)
        for k in range(4):
            a = math.radians(phi + 90 * k)
            ux, uy = math.sin(a), math.cos(a)
            x1p, y1p = P(0, 0)
            x2p, y2p = P(TIP_C * ux, TIP_C * uy)
            d.line(x1p, y1p, x2p, y2p, "", f'stroke="#1f2933" stroke-width="{f(ARM_W * s + 2.4)}" stroke-linecap="round"')
            d.line(x1p, y1p, x2p, y2p, "", f'stroke="#d7b582" stroke-width="{f(ARM_W * s)}" stroke-linecap="round"')
        px, py = P(0, 0)
        d.circle(px, py, 1.7 * s, "star")
        d.circle(px, py, 0.3 * s, "steel")
        d.path(arc(px, py, 3.0 * s, 200, 250), "ink", 'marker-end="url(#ia)"')
        d.text(xl, P(0, GATE_A + R + 2.2)[1], name, "b")
        d.lines(xl, P(0, -9.8)[1], note, "small", lh=15)
        return P

    PA = panel(300, 232, 0, "A · Hold (0 degrees)",
               ["An arm stands across the rails and holds ball 1. The queue rests", "against ball 1."])
    panel(300, 492, 45, "B · Split (45 degrees)",
          ["The next arm has slipped into the gap between balls 1 and 2", "and now holds the queue back. Ball 1 follows the first arm."])
    panel(300, 752, 80, "C · Release (80 degrees)",
          ["Ball 1 clears the arm tip and rolls away down the run-out.", "At 90 degrees the gate is back at A with ball 2 in place."])

    ya = PA(0, GATE_A)[1]
    y0 = PA(0, 0)[1]
    xl = PA(15, 0)[0]
    d.line(xl, ya, PA(-28, 0)[0], ya, "centre")
    d.dimv(ya, y0, xl - 18, "6-1/2", xl, PA(TIP_C + 0.7, 0)[0], side=-1, flat=True)
    xa = PA(0, 0)[0]
    xt = PA(-TIP_C - ARM_W / 2, 0)[0]
    d.dimh(xa, xt, y0 + 34, "8 to tip", y0, y0)

    # section across the ramp
    SX, SY, ss = 930, 300, 15.0

    def Q(y, z):
        return SX + ss * y, SY - ss * z

    d.text(720, 118, "Section across the ramp at the gate", "b")
    plate_top = -PVC / 2 - 0.75
    x, y = Q(-10.6, plate_top)
    d.rect(x, y, 16.6 * ss, 0.75 * ss, "ply")
    for off in (-RAIL_CC / 2, RAIL_CC / 2):
        x, y = Q(off - 1.0, -PVC / 2)
        d.rect(x, y, 2.0 * ss, 0.75 * ss, "lumber")
        cx, cy = Q(off, 0)
        d.circle(cx, cy, PVC / 2 * ss, "pvc")
    ped_top = plate_top + 3.5 + 0.75
    for y0b in (-9.6, -5.35):
        x, y = Q(y0b, plate_top + 3.5)
        d.rect(x, y, 0.75 * ss, 3.5 * ss, "lumber")
    x, y = Q(-9.6, ped_top)
    d.rect(x, y, 5.0 * ss, 0.75 * ss, "ply")
    x, y = Q(-GATE_A - 1.15, ped_top - 0.75)
    d.rect(x, y, 2.3 * ss, 1.5 * ss, "motor", rx=3)
    x, y = Q(-GATE_A - 3.2, ped_top - 0.95)
    d.rect(x, y, 2.1 * ss, 1.1 * ss, "motor", rx=3)
    cx, cy = Q(0, BALL_ON_RAIL)
    d.circle(cx, cy, R * ss, "ball")
    star_z = BALL_ON_RAIL + 0.375
    x, y = Q(-GATE_A - 8.0, star_z)
    d.rect(x, y, 16.0 * ss, 0.75 * ss, "star", extra='fill-opacity=".8"')
    x, y = Q(-GATE_A - 0.16, star_z - 0.75)
    d.rect(x, y, 0.32 * ss, (star_z - 0.75 - ped_top + 0.75) * ss, "steel")
    xa, ya2 = Q(-GATE_A, star_z + 1.6)
    xb, yb = Q(-GATE_A, plate_top - 1.0)
    d.line(xa, ya2, xb, yb, "centre")
    xa, ya2 = Q(0, BALL_ON_RAIL + R + 1.0)
    xb, yb = Q(0, plate_top - 1.0)
    d.line(xa, ya2, xb, yb, "centre")
    yd = Q(0, plate_top - 1.6)[1]
    d.dimh(Q(-GATE_A, 0)[0], Q(0, 0)[0], yd, "6-1/2")
    yd2 = Q(0, plate_top - 3.6)[1]
    d.dimh(Q(-RAIL_CC / 2, 0)[0], Q(RAIL_CC / 2, 0)[0], yd2, "rails 6-1/2", yd + 6, yd + 6)
    xv = Q(R + 1.6, 0)[0]
    d.dimv(Q(0, BALL_ON_RAIL)[1], Q(0, 0)[1], xv, "3-13/16", Q(0, 0)[0], Q(RAIL_CC / 2, 0)[0], side=1, flat=True)
    bx, by = Q(-GATE_A - 6.4, star_z + 1.3)
    d.balloon(bx, by, 1)
    bx, by = Q(-GATE_A - 4.6, ped_top - 2.1)
    d.balloon(bx, by, 2)
    bx, by = Q(-9.6, plate_top - 1.5)
    d.balloon(bx, by, 3)

    tx = 720
    for n, y, rows in (
        (1, 500, ["Star wheel: 3/4 in plywood, four arms 1 in wide, tips", "on a 16 in circle. It turns level with the ball centre,", "above the rails."]),
        (2, 572, ["12 V worm gearmotor bolted under a small pedestal,", "shaft up. Worm gearing cannot be pushed round by", "the weight of the queue."]),
        (3, 644, ["Gate plate: plywood under both rails, on blocks so the", "ball clears it. Slot the pedestal bolts about 1/2 in", "each way for tuning."]),
    ):
        d.balloon(tx + 10, y - 4, n)
        d.lines(tx + 30, y, rows)
    d.lines(tx, 730, ["Speed: one ball per quarter turn. A 6 RPM gearmotor feeds a ball", "every 2.5 seconds flat out; the PWM knob slows it to the 4 to 6",
                      "seconds you start with.", "",
                      "The geometry is calculated for a size 5 ball and has not been", "built yet. Test it by hand before fitting the motor."], "small", lh=16)
    d.save("04-feed-gate.svg")


# --------------------------------------------------------------- 5. WIRING
def wiring():
    W, H = 1120, 780
    d = Svg(W, H, "Wiring",
            "Wiring: wall outlet, GFCI plug, cord, then inside a closed control box an emergency stop switch feeding two fused "
            "DC drives for the wheel motors and a 12 volt supply for the feed gate. Every metal part is bonded to ground.")
    d.heading("5 · Wiring", "120 V AC side and 12 V feeder side. The stop switch cuts everything, including the feeder.")

    def box(x, y, w, h, rows, small=False):
        d.rect(x, y, w, h, "box", rx=6)
        n = len(rows)
        y0 = y + h / 2 - (n - 1) * 7.5 + 4.5
        for i, r in enumerate(rows):
            d.text(x + w / 2, y0 + i * 15, r, "b" if i == 0 and not small else "small", "middle")

    d.rect(300, 104, 600, 476, "encl", rx=10)
    d.text(316, 126, "Control box: closed, outdoor rated, within the operator's reach", "small")

    # hot
    d.poly([(110, 170), (130, 170)], "hot")
    d.poly([(240, 170), (330, 170)], "hot")
    d.poly([(450, 170), (500, 170), (500, 460), (530, 460)], "hot")
    d.poly([(500, 170), (530, 170)], "hot")
    d.poly([(594, 170), (630, 170)], "hot")
    d.poly([(500, 320), (530, 320)], "hot")
    d.poly([(594, 320), (630, 320)], "hot")
    for y in (170, 320):
        d.circle(500, y, 4, "", 'fill="#111827"')
    # neutral, crossing the hot bus on a white halo
    d.poly([(110, 190), (130, 190)], "neu")
    d.poly([(476, 365), (630, 365)], "halo")
    d.poly([(240, 190), (262, 190), (262, 215), (630, 215)], "halo")
    d.poly([(240, 190), (262, 190), (262, 215), (630, 215)], "neu")
    d.poly([(476, 215), (476, 495), (530, 495)], "neu")
    d.poly([(476, 365), (630, 365)], "neu")
    d.poly([(500, 205), (500, 225)], "hot")
    d.poly([(500, 355), (500, 375)], "hot")
    for y in (215, 365):
        d.circle(476, y, 4, "", 'fill="#8d99a6"')
    # ground
    d.poly([(110, 210), (130, 210)], "gnd")
    d.poly([(240, 210), (250, 210), (250, 545), (320, 545)], "gnd")
    d.poly([(620, 545), (1066, 545), (1066, 185), (1028, 185)], "gnd")
    d.poly([(1066, 335), (1028, 335)], "gnd")
    d.poly([(985, 545), (985, 610)], "gnd")
    for p in ((1066, 335), (985, 545)):
        d.circle(p[0], p[1], 4, "", 'fill="#15803d"')
    # armature and 12 V
    d.poly([(750, 170), (957, 170)], "ap")
    d.poly([(750, 200), (957, 200)], "am")
    d.poly([(750, 320), (957, 320)], "ap")
    d.poly([(750, 350), (957, 350)], "am")
    d.poly([(630, 460), (650, 460)], "vp")
    d.poly([(700, 460), (715, 460)], "vp")
    d.poly([(771, 460), (790, 460)], "vp")
    d.poly([(630, 495), (790, 495)], "vm")
    d.poly([(870, 462), (964, 462)], "vp")
    d.poly([(870, 492), (964, 492)], "vm")

    box(20, 150, 90, 80, ["Wall", "outlet", "120 V"])
    box(130, 150, 110, 80, ["GFCI plug", "15 A, at the", "outlet end"])
    d.text(294, 141, "12 AWG cord", "small", "end")
    box(330, 146, 120, 48, ["E-STOP", "paddle switch"])
    box(530, 153, 64, 34, ["Fuse A"], small=True)
    box(630, 140, 120, 90, ["DC drive A", "120 V AC in", "0-90 V DC out"])
    box(530, 303, 64, 34, ["Fuse B"], small=True)
    box(630, 290, 120, 90, ["DC drive B", "120 V AC in", "0-90 V DC out"])
    box(530, 440, 100, 72, ["12 V supply", "2 A or more"])
    box(650, 443, 50, 34, ["3 A fuse"], small=True)
    box(715, 443, 56, 34, ["FEED", "on / off"], small=True)
    box(790, 436, 80, 80, ["PWM", "feed rate"])
    d.rect(320, 535, 300, 20, "box", rx=3)
    d.text(470, 549, "ground bar", "small", "middle")
    for (cy, name) in ((185, "A"), (335, "B")):
        d.circle(992, cy, 36, "motor")
        d.text(992, cy - 2, "Motor " + name, "b", "middle")
        d.text(992, cy + 14, "treadmill", "small", "middle")
    d.circle(996, 477, 36, "motor")
    d.text(996, 474, "Gate", "b", "middle")
    d.text(996, 489, "gearmotor", "small", "middle")
    box(900, 610, 170, 40, ["Frame and metal guards"], small=True)
    for (x, y, t) in ((690, 248, "speed knob A"), (690, 398, "speed knob B")):
        d.circle(x - 48, y - 4, 7, "hub")
        d.text(x - 36, y, t, "small")
    for y0 in (0, 150):
        d.text(762, 161 + y0, "armature +", "small")
        d.text(762, 218 + y0, "armature -", "small")
    d.text(906, 453, "12 V +", "small")
    d.text(906, 509, "12 V -", "small")

    # legend
    lx, ly = 28, 640
    items = [("hot", "Hot (black), through the switch and fuses"), ("neu", "Neutral (white)"), ("gnd", "Ground (green): cord, box, motor frames, guards"),
             ("ap", "Motor armature +"), ("am", "Motor armature -"), ("vp", "12 V +"), ("vm", "12 V -")]
    for i, (cls, t) in enumerate(items):
        col, row = divmod(i, 4)
        x = lx + col * 400
        y = ly + row * 22
        d.line(x, y, x + 36, y, cls)
        d.text(x + 46, y + 4, t, "small")
    d.lines(28, 738, ["Fuse each drive as its manual says. Cap each drive's top speed and check it with a tachometer: neither wheel should pass 2,000 RPM.",
                      "Swap a motor's two armature leads to reverse it. Treadmill motors run on about 90 to 130 V DC: keep every terminal inside the",
                      "closed box and unplug before opening it."], "small", lh=16)
    d.save("05-wiring.svg")


if __name__ == "__main__":
    top_view()
    front_section()
    side_elevation()
    feed_gate()
    wiring()
    print("feed gate: tightest clearance between ball 1 and the next arm tip = %.2f in" % gate_check())
