"""Fundo: colinas em curva de nível ao anoitecer (relevo do Oeste catarinense),
trator com plantadeira de faróis acesos, lua dourada e pés de milho em primeiro plano."""
import math, random, sys
from pathlib import Path

random.seed(23)
W, H = 1080, 1350
HZ = 430

s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0b111b"/>
    <stop offset="0.16" stop-color="#121b28"/>
    <stop offset="0.26" stop-color="#1f2530"/>
    <stop offset="0.30" stop-color="#3b3022"/>
    <stop offset="0.33" stop-color="#15110c"/>
    <stop offset="0.55" stop-color="#0b0b0b"/>
    <stop offset="1" stop-color="#0a0a0a"/>
  </linearGradient>
  <radialGradient id="moonglow" cx="0.74" cy="0.12" r="0.28">
    <stop offset="0" stop-color="#e6c27a" stop-opacity="0.30"/>
    <stop offset="0.35" stop-color="#c9a45c" stop-opacity="0.08"/>
    <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="dusk" cx="0.35" cy="0.31" r="0.5">
    <stop offset="0" stop-color="#d6a656" stop-opacity="0.32"/>
    <stop offset="0.3" stop-color="#c9a45c" stop-opacity="0.08"/>
    <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="hillA" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#1c1a14"/><stop offset="1" stop-color="#0e0d0a"/>
  </linearGradient>
  <linearGradient id="hillB" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#16150f"/><stop offset="1" stop-color="#0b0b09"/>
  </linearGradient>
  <linearGradient id="beam" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#f1d79a" stop-opacity="0.55"/>
    <stop offset="1" stop-color="#f1d79a" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.25"/>
    <stop offset="0.12" stop-color="#0a0a0a" stop-opacity="0"/>
    <stop offset="0.29" stop-color="#0a0a0a" stop-opacity="0.05"/>
    <stop offset="0.37" stop-color="#0a0a0a" stop-opacity="0.75"/>
    <stop offset="0.43" stop-color="#0a0a0a" stop-opacity="1"/>
    <stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/>
  </linearGradient>
  <radialGradient id="vign" cx="0.5" cy="0.28" r="0.8">
    <stop offset="0.55" stop-color="#000" stop-opacity="0"/>
    <stop offset="1" stop-color="#000" stop-opacity="0.6"/>
  </radialGradient>
</defs>
<rect width="1080" height="1350" fill="url(#sky)"/>
<rect width="1080" height="1350" fill="url(#dusk)"/>
<rect width="1080" height="1350" fill="url(#moonglow)"/>
''')

# estrelas
for _ in range(110):
    x, y = random.uniform(0, W), random.uniform(0, 300)
    r = random.choice([0.7, 0.9, 1.1, 1.4])
    o = random.uniform(0.15, 0.6) * (1 - y / 380)
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#efe6d6" opacity="{o:.2f}"/>')

# lua crescente
s.append('<mask id="cres"><rect width="1080" height="1350" fill="#fff"/><circle cx="816" cy="150" r="34" fill="#000"/></mask>')
s.append('<circle cx="800" cy="160" r="38" fill="#e7c98a" opacity="0.92" mask="url(#cres)"/>')

# colina distante (azulada) + silhueta de armazém e silos ao longe
def ridge(base, amp, freq, phase, step=6):
    pts = []
    for x in range(-10, W + 11, step):
        y = base - amp * math.sin(x / freq + phase) - amp * 0.4 * math.sin(x / (freq * 0.43) + phase * 1.7)
        pts.append((x, y))
    return pts

far = ridge(352, 16, 160, 0.6)
d = "M -10 460 " + " ".join(f"L {x} {y:.1f}" for x, y in far) + " L 1090 460 Z"
s.append(f'<path d="{d}" fill="#141a22" opacity="0.95"/>')
# armazém pequeno na crista distante
def far_y(x):
    return min(y for xx, y in far if abs(xx - x) <= 6)
ax = 182; ay = far_y(ax)
s.append(f'<rect x="{ax}" y="{ay-22:.1f}" width="54" height="24" fill="#0d1218"/>')
s.append(f'<path d="M {ax-3} {ay-22:.1f} L {ax+27} {ay-36:.1f} L {ax+57} {ay-22:.1f} Z" fill="#0d1218"/>')
for i, sx in enumerate([ax + 66, ax + 84]):
    s.append(f'<rect x="{sx}" y="{ay-34:.1f}" width="14" height="36" fill="#0d1218"/>')
    s.append(f'<path d="M {sx} {ay-34:.1f} L {sx+7} {ay-42:.1f} L {sx+14} {ay-34:.1f} Z" fill="#0d1218"/>')
s.append(f'<circle cx="{ax+20}" cy="{ay-12:.1f}" r="2.2" fill="#e8c07a" opacity="0.9"/>')

# colina média com curvas de nível
mid = ridge(385, 22, 120, 2.1)
d = "M -10 520 " + " ".join(f"L {x} {y:.1f}" for x, y in mid) + " L 1090 520 Z"
s.append(f'<path d="{d}" fill="url(#hillA)"/>')
for k in range(1, 7):
    off = k * 9
    pts = [(x, y + off + 2 * math.sin(x / 40 + k)) for x, y in mid]
    dd = "M " + " L ".join(f"{x} {y:.1f}" for x, y in pts)
    s.append(f'<path d="{dd}" fill="none" stroke="#c9a45c" stroke-opacity="{0.20 - k*0.02:.2f}" stroke-width="1.2"/>')

# colina da frente: lavoura em linhas (convergindo), com trator
near = ridge(415, 14, 210, 4.0)
d = "M -10 640 " + " ".join(f"L {x} {y:.1f}" for x, y in near) + " L 1090 640 Z"
s.append(f'<path d="{d}" fill="url(#hillB)"/>')
for k in range(1, 12):
    off = k * 6 + k * k * 0.9
    pts = [(x, y + off + 1.5 * math.sin(x / 55 + k * 0.7)) for x, y in near]
    dd = "M " + " L ".join(f"{x} {y:.1f}" for x, y in pts)
    s.append(f'<path d="{dd}" fill="none" stroke="#c9a45c" stroke-opacity="{max(0.04, 0.26 - k*0.02):.2f}" stroke-width="{1.0 + k*0.12:.2f}"/>')

# trator + plantadeira na crista da frente
def near_y(x):
    return min(y for xx, y in near if abs(xx - x) <= 6)
tx = 600; ty = near_y(tx + 30) + 1
g = []
# feixe dos faróis
g.append(f'<path d="M {tx+66} {ty-22} L {tx+330} {ty-62} L {tx+330} {ty+16} Z" fill="url(#beam)" opacity="0.55"/>')
# plantadeira (atrás, à esquerda)
g.append(f'<rect x="{tx-118}" y="{ty-16}" width="92" height="10" fill="#0a0c0e"/>')
for i in range(6):
    px = tx - 112 + i * 16
    g.append(f'<rect x="{px}" y="{ty-30}" width="10" height="14" rx="2" fill="#0a0c0e"/>')
    g.append(f'<line x1="{px+5}" y1="{ty-6}" x2="{px+5}" y2="{ty+2}" stroke="#0a0c0e" stroke-width="3"/>')
g.append(f'<line x1="{tx-26}" y1="{ty-11}" x2="{tx+6}" y2="{ty-11}" stroke="#0a0c0e" stroke-width="4"/>')
# trator
g.append(f'<path d="M {tx+4} {ty-14} L {tx+4} {ty-34} L {tx+30} {ty-34} L {tx+30} {ty-66} L {tx+58} {ty-66} L {tx+62} {ty-34} L {tx+70} {ty-30} L {tx+70} {ty-12} Z" fill="#0a0c0e"/>')
g.append(f'<rect x="{tx+34}" y="{ty-61}" width="20" height="22" fill="#d9b46a" opacity="0.55"/>')
g.append(f'<line x1="{tx+40}" y1="{ty-66}" x2="{tx+40}" y2="{ty-78}" stroke="#0a0c0e" stroke-width="3"/>')
g.append(f'<circle cx="{tx+18}" cy="{ty-10}" r="18" fill="#0a0c0e"/><circle cx="{tx+18}" cy="{ty-10}" r="6" fill="#2a2a26"/>')
g.append(f'<circle cx="{tx+60}" cy="{ty-4}" r="11" fill="#0a0c0e"/><circle cx="{tx+60}" cy="{ty-4}" r="4" fill="#2a2a26"/>')
g.append(f'<circle cx="{tx+70}" cy="{ty-24}" r="3" fill="#fbe7b5"/>')
g.append(f'<circle cx="{tx+32}" cy="{ty-70}" r="2.4" fill="#e8a35a" opacity="0.9"/>')
s.extend(g)

# pés de milho em primeiro plano (bordas)
def corn(x0, base, hgt, lean, scale=1.0, tone="#0d0e0a", edge="#c9a45c"):
    out = []
    top = base - hgt
    cx = x0 + lean
    out.append(f'<path d="M {x0} {base} Q {x0+lean*0.3} {base-hgt*0.5} {cx} {top}" fill="none" stroke="{tone}" stroke-width="{7*scale:.1f}" stroke-linecap="round"/>')
    out.append(f'<path d="M {x0} {base} Q {x0+lean*0.3} {base-hgt*0.5} {cx} {top}" fill="none" stroke="{edge}" stroke-opacity="0.18" stroke-width="{1.2*scale:.1f}"/>')
    # pendão
    for a in (-38, -18, 0, 20, 40):
        r = math.radians(a - 90)
        L = 40 * scale
        out.append(f'<line x1="{cx}" y1="{top}" x2="{cx + L*math.cos(r):.1f}" y2="{top + L*math.sin(r) + 22*scale:.1f}" stroke="{edge}" stroke-opacity="0.45" stroke-width="{1.6*scale:.1f}"/>')
    # folhas
    for i in range(7):
        t = 0.18 + i * 0.11
        yy = base - hgt * t
        xx = x0 + lean * 0.3 * t * 2 if t < 0.5 else x0 + lean * (t)
        side = 1 if i % 2 == 0 else -1
        L = (150 - i * 12) * scale
        ex = xx + side * L
        ey = yy - L * 0.18 + L * 0.45
        out.append(f'<path d="M {xx:.1f} {yy:.1f} Q {xx + side*L*0.55:.1f} {yy - L*0.45:.1f} {ex:.1f} {ey:.1f} Q {xx + side*L*0.45:.1f} {yy - L*0.28:.1f} {xx:.1f} {yy+6*scale:.1f} Z" fill="{tone}"/>')
        out.append(f'<path d="M {xx:.1f} {yy:.1f} Q {xx + side*L*0.55:.1f} {yy - L*0.45:.1f} {ex:.1f} {ey:.1f}" fill="none" stroke="{edge}" stroke-opacity="0.22" stroke-width="{1.1*scale:.1f}"/>')
    # espiga
    ey0 = base - hgt * 0.52
    ex0 = x0 + lean * 0.35
    out.append(f'<ellipse cx="{ex0 + 12*scale:.1f}" cy="{ey0:.1f}" rx="{9*scale:.1f}" ry="{30*scale:.1f}" transform="rotate(14 {ex0 + 12*scale:.1f} {ey0:.1f})" fill="#2d2416"/>')
    out.append(f'<ellipse cx="{ex0 + 12*scale:.1f}" cy="{ey0:.1f}" rx="{9*scale:.1f}" ry="{30*scale:.1f}" transform="rotate(14 {ex0 + 12*scale:.1f} {ey0:.1f})" fill="none" stroke="#c9a45c" stroke-opacity="0.5" stroke-width="1.3"/>')
    return out

s.extend(corn(50, 520, 330, 22, 1.0))
s.extend(corn(140, 545, 270, -14, 0.8, tone="#0b0c09"))
s.extend(corn(1025, 520, 335, -26, 1.0))
s.extend(corn(940, 548, 265, 12, 0.78, tone="#0b0c09"))

s.append('<rect width="1080" height="1350" fill="url(#fade)"/>')
s.append('<rect width="1080" height="1350" fill="url(#vign)"/>')
s.append('<rect y="640" width="1080" height="710" fill="#0a0a0a"/>')
s.append('</svg>')
Path(sys.argv[1] if len(sys.argv) > 1 else "bg.svg").write_text("\n".join(s))
