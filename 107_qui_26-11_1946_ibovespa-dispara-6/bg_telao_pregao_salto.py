"""Fundo: telão de pregão em perspectiva com gráfico de linha que salta no fim do dia, sobre fileiras de mesas com monitores (sem pessoas)."""
import random, math
random.seed(2611)
W, H = 1080, 1350
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
<linearGradient id="room" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0c1016"/><stop offset="0.22" stop-color="#121820"/>
 <stop offset="0.33" stop-color="#16140f"/><stop offset="0.42" stop-color="#0b0b0b"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<linearGradient id="panel" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0e13"/><stop offset="1" stop-color="#06080b"/></linearGradient>
<radialGradient id="halo" cx="0.5" cy="0.17" r="0.55">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.16"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="area" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.32"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></linearGradient>
<linearGradient id="line" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#8a7448"/><stop offset="0.75" stop-color="#c9a45c"/><stop offset="1" stop-color="#f3dfa8"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.25"/><stop offset="0.08" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.27" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.33" stop-color="#0a0a0a" stop-opacity="0.65"/>
 <stop offset="0.37" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<filter id="gl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="9"/></filter>
<filter id="gs" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3"/></filter>
<filter id="grain" x="0" y="0" width="100%" height="100%">
 <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="5"/><feColorMatrix type="saturate" values="0"/>
 <feComponentTransfer><feFuncA type="table" tableValues="0 0.06"/></feComponentTransfer></filter>
<clipPath id="scr"><polygon points="150,150 930,150 950,372 130,372"/></clipPath>
</defs>
<rect width="100%" height="100%" fill="url(#room)"/><rect width="100%" height="100%" fill="url(#halo)"/>''')
# ceiling lights (perspective strips)
for i, x in enumerate(range(-200, 1300, 150)):
    s.append(f'<line x1="{540+(x-540)*0.35:.0f}" y1="40" x2="{x}" y2="-10" stroke="#d8d0bc" stroke-opacity="0.07" stroke-width="3"/>')
for y in (58, 92, 122):
    s.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#d8d0bc" stroke-opacity="0.035"/>')
# side panels (smaller screens) left and right in perspective
for side in (-1, 1):
    if side < 0:
        pts = "28,178 112,166 104,350 22,362"
    else:
        pts = "968,166 1052,178 1058,362 976,350"
    s.append(f'<polygon points="{pts}" fill="url(#panel)" stroke="#c9a45c" stroke-opacity="0.25" stroke-width="1.5"/>')
    bx = 40 if side < 0 else 984
    for r in range(9):
        w = random.randint(26, 58)
        col = "#c9a45c" if random.random() < 0.6 else "#8f8a82"
        s.append(f'<rect x="{bx}" y="{190+r*17}" width="{w}" height="6" rx="1" fill="{col}" opacity="{random.uniform(0.25,0.6):.2f}"/>')
# main board frame
s.append('<polygon points="138,138 942,138 964,384 116,384" fill="#050608" stroke="#2a2824" stroke-width="2"/>')
s.append('<polygon points="150,150 930,150 950,372 130,372" fill="url(#panel)"/>')
s.append('<g clip-path="url(#scr)">')
# LED dot matrix
for gy in range(156, 372, 9):
    for gx in range(130, 952, 9):
        s.append(f'<circle cx="{gx}" cy="{gy}" r="0.9" fill="#c9a45c" opacity="0.07"/>') if (gx+gy) % 2 == 0 else None
for gy in range(190, 372, 45):
    s.append(f'<line x1="120" y1="{gy}" x2="960" y2="{gy}" stroke="#c9a45c" stroke-opacity="0.10" stroke-dasharray="3 6"/>')
# price path: slow drift down, sideways, then sharp jump at the end
pts = []
n = 64
p = 300.0
for i in range(n):
    x = 170 + i * (740 / (n - 1))
    if i < 40:
        p += random.uniform(-3.5, 5.0) + 0.9
    elif i < 52:
        p += random.uniform(-4, 4)
    else:
        p -= random.uniform(7, 13)
    p = max(178, min(352, p))
    pts.append((x, p))
d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
s.append(f'<path d="{d} L{pts[-1][0]:.1f},372 L{pts[0][0]:.1f},372 Z" fill="url(#area)"/>')
s.append(f'<path d="{d}" fill="none" stroke="#c9a45c" stroke-width="10" opacity="0.35" filter="url(#gl)"/>')
s.append(f'<path d="{d}" fill="none" stroke="url(#line)" stroke-width="3.5" stroke-linejoin="round"/>')
ex, ey = pts[-1]
s.append(f'<line x1="{ex:.0f}" y1="160" x2="{ex:.0f}" y2="372" stroke="#f3dfa8" stroke-opacity="0.25" stroke-dasharray="2 5"/>')
s.append(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="16" fill="#f3dfa8" opacity="0.45" filter="url(#gs)"/>')
s.append(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="6" fill="#fff3d0"/>')
# previous close reference line
s.append(f'<line x1="130" y1="{pts[51][1]:.0f}" x2="950" y2="{pts[51][1]:.0f}" stroke="#8f8a82" stroke-opacity="0.35" stroke-dasharray="8 6"/>')
s.append('</g>')
# ticker strip under the board
s.append('<rect x="116" y="392" width="848" height="20" fill="#07080a" stroke="#2a2824"/>')
x = 124
while x < 950:
    w = random.randint(30, 70)
    up = random.random() < 0.85
    s.append(f'<rect x="{x}" y="399" width="{w}" height="6" rx="1" fill="{"#c9a45c" if up else "#6d6860"}" opacity="0.55"/>')
    s.append(f'<path d="M{x+w+6},{405 if up else 399} l4,{-6 if up else 6} l4,{6 if up else -6} z" fill="{"#c9a45c" if up else "#6d6860"}" opacity="0.7"/>')
    x += w + 26
# desks with monitors (rows in perspective), horizon ~ 430-480
for row, (y, sc) in enumerate([(430, 0.55), (462, 0.75), (500, 1.0)]):
    mw, mh = 58 * sc, 34 * sc
    cnt = int(1080 / (mw * 1.5)) + 2
    off = (row % 2) * mw * 0.7
    s.append(f'<rect x="0" y="{y+mh*0.9:.0f}" width="{W}" height="{8*sc:.0f}" fill="#141310"/>')
    for k in range(cnt):
        mx = -30 + off + k * mw * 1.5
        glow = random.random() < 0.7
        s.append(f'<rect x="{mx:.0f}" y="{y:.0f}" width="{mw:.0f}" height="{mh:.0f}" rx="2" fill="#0d1014" stroke="#2a2824"/>')
        if glow:
            s.append(f'<rect x="{mx+3*sc:.0f}" y="{y+3*sc:.0f}" width="{mw-6*sc:.0f}" height="{mh-6*sc:.0f}" fill="#c9a45c" opacity="{random.uniform(0.06,0.16):.2f}"/>')
            # tiny rising line on monitor
            lx = mx + 6 * sc
            s.append(f'<polyline points="{lx:.0f},{y+mh*0.7:.0f} {lx+mw*0.3:.0f},{y+mh*0.62:.0f} {lx+mw*0.55:.0f},{y+mh*0.66:.0f} {lx+mw*0.8:.0f},{y+mh*0.3:.0f}" fill="none" stroke="#c9a45c" stroke-opacity="0.5" stroke-width="{1.2*sc:.1f}"/>')
s.append('<rect width="100%" height="100%" fill="url(#fade)"/>')
s.append('<rect width="100%" height="100%" filter="url(#grain)"/>')
s.append('</svg>')
open("bg.svg", "w").write("\n".join(x for x in s if x))
