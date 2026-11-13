"""Fundo: plenário do Senado em semicírculo com painel de votação (45 x 31)."""
import math, random, sys
from pathlib import Path
random.seed(13)
W, H = 1080, 1350
s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#10161f"/><stop offset="0.22" stop-color="#18202b"/>
 <stop offset="0.33" stop-color="#1e1c1a"/><stop offset="0.42" stop-color="#0d0d0d"/>
 <stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="glow" cx="0.5" cy="0.17" r="0.42">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.16"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="panel" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0b0f15"/><stop offset="1" stop-color="#06080b"/></linearGradient>
<linearGradient id="wood" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#3a2c1c"/><stop offset="1" stop-color="#1a130c"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.30"/><stop offset="0.10" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.25" stop-color="#0a0a0a" stop-opacity="0.04"/><stop offset="0.31" stop-color="#0a0a0a" stop-opacity="0.65"/>
 <stop offset="0.36" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.25" r="0.85">
 <stop offset="0.5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.7"/></radialGradient>
<filter id="grain" x="0" y="0" width="100%" height="100%">
 <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="5"/>
 <feColorMatrix type="saturate" values="0"/>
 <feComponentTransfer><feFuncA type="table" tableValues="0 0.07"/></feComponentTransfer></filter>
<filter id="blur"><feGaussianBlur stdDeviation="3"/></filter>
<filter id="soft"><feGaussianBlur stdDeviation="1.2"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/>
<rect width="100%" height="100%" fill="url(#glow)"/>''')

# back wall: vertical wooden slats (acoustic panels)
for i in range(0, W, 18):
    op = 0.10 + 0.06 * ((i // 18) % 3 == 0)
    s.append(f'<rect x="{i}" y="128" width="9" height="200" fill="#5a4630" fill-opacity="{op:.2f}"/>')
s.append('<line x1="0" y1="128" x2="1080" y2="128" stroke="#c9a45c" stroke-opacity="0.18"/>')

# voting panel (board) at the center of the back wall
px0, py0, pw, ph = 300, 150, 480, 150
s.append(f'<rect x="{px0-8}" y="{py0-8}" width="{pw+16}" height="{ph+16}" fill="#1b1f25"/>')
s.append(f'<rect x="{px0}" y="{py0}" width="{pw}" height="{ph}" fill="url(#panel)"/>')
s.append(f'<rect x="{px0}" y="{py0}" width="{pw}" height="{ph}" fill="none" stroke="#c9a45c" stroke-opacity="0.35"/>')
# 76 voting lights: 45 gold (sim) + 31 grey (não), in rows
cols, rows = 19, 4
votes = ['y'] * 45 + ['n'] * 31
cw = (pw - 60) / (cols - 1)
rh = (ph - 56) / (rows - 1)
k = 0
for r in range(rows):
    for c in range(cols):
        if k >= len(votes):
            break
        cx = px0 + 30 + c * cw
        cy = py0 + 28 + r * rh
        if votes[k] == 'y':
            s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="7" fill="#e3b96a" fill-opacity="0.35" filter="url(#soft)"/>')
            s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="4.2" fill="#e3b96a" fill-opacity="0.85"/>')
        else:
            s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="4.2" fill="#6b737d" fill-opacity="0.55"/>')
        k += 1
# panel glow on wall
s.append(f'<rect x="{px0-30}" y="{py0-20}" width="{pw+60}" height="{ph+40}" fill="#c9a45c" fill-opacity="0.05" filter="url(#blur)"/>')
# side screens (dark, smaller)
for x in (110, 840):
    s.append(f'<rect x="{x}" y="175" width="130" height="80" fill="#0b0e13" stroke="#3a3f47" stroke-opacity="0.8"/>')
    for j in range(4):
        w = random.randint(50, 100)
        s.append(f'<rect x="{x+14}" y="{190+j*16}" width="{w}" height="4" fill="#8796a8" fill-opacity="0.22"/>')

# presiding table (mesa diretora), raised, below panel
s.append('<rect x="340" y="318" width="400" height="26" fill="url(#wood)"/>')
s.append('<rect x="340" y="318" width="400" height="3" fill="#c9a45c" fill-opacity="0.45"/>')
s.append('<rect x="380" y="344" width="320" height="14" fill="#140f0a"/>')
for x in range(372, 720, 44):
    s.append(f'<rect x="{x}" y="304" width="22" height="14" fill="#0d0f12"/>')  # chair backs
    s.append(f'<circle cx="{x+30}" cy="316" r="2.2" fill="#e3b96a" fill-opacity="0.7"/>')  # mic lights

# hemicycle: concentric arcs of desks seen from the back, center at (540, 300)
cx0, cy0 = 540, 300
for ring in range(5):
    rx = 300 + ring * 120
    ry = 58 + ring * 26
    th = 9 + ring * 2   # desk thickness grows toward viewer
    n = 14 + ring * 4
    a0, a1 = math.radians(200), math.radians(340)
    for i in range(n):
        t0 = a0 + (a1 - a0) * i / n + 0.012
        t1 = a0 + (a1 - a0) * (i + 1) / n - 0.012
        # front edge (lower arc: angles flipped to bottom half)
        pts = []
        for t in (t0, t1):
            pts.append((cx0 + rx * math.cos(t), cy0 - ry * math.sin(t)))
        (x0, y0), (x1, y1) = pts
        s.append(f'<polygon fill="url(#wood)" fill-opacity="0.95" points="{x0:.1f},{y0:.1f} {x1:.1f},{y1:.1f} {x1:.1f},{y1+th:.1f} {x0:.1f},{y0+th:.1f}"/>')
        s.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="#c9a45c" stroke-opacity="0.40" stroke-width="1.3"/>')
        # chair silhouette behind desk (toward viewer side)
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        cwid = (abs(x1 - x0)) * 0.45
        s.append(f'<rect x="{mx-cwid/2:.1f}" y="{my+th+2:.1f}" width="{cwid:.1f}" height="{th*1.3:.1f}" rx="3" fill="#0b0c0e"/>')
        # desk lamp / screen
        if random.random() < 0.45:
            s.append(f'<rect x="{mx-4:.1f}" y="{my-5:.1f}" width="8" height="4" fill="#e3b96a" fill-opacity="{random.uniform(0.35,0.75):.2f}"/>')
# carpet floor tone between rings
s.append('<ellipse cx="540" cy="300" rx="250" ry="44" fill="#2a2016" fill-opacity="0.35"/>')

# reflected glow on floor
s.append('<ellipse cx="540" cy="390" rx="420" ry="40" fill="#c9a45c" fill-opacity="0.04" filter="url(#blur)"/>')

s.append('<rect width="100%" height="100%" fill="url(#fade)"/>')
s.append('<rect width="100%" height="100%" fill="url(#vign)"/>')
s.append('<rect width="100%" height="100%" filter="url(#grain)"/>')
s.append('</svg>')
Path(sys.argv[1] if len(sys.argv) > 1 else 'bg.svg').write_text("\n".join(s))
print("ok")
