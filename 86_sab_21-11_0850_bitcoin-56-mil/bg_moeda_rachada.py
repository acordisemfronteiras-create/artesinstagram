"""Fundo: moeda digital genérica dourada rachada no céu noturno, gráfico de preço em queda
rompendo a linha de mínima de 2024 e uma corrente de blocos com um elo partido no horizonte."""
import math, random
random.seed(2111)
W, H = 1080, 1350
o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
o.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0b0f17"/><stop offset="0.2" stop-color="#141925"/>
 <stop offset="0.32" stop-color="#17171c"/><stop offset="0.45" stop-color="#0d0d0e"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="halo" cx="0.74" cy="0.2" r="0.32">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.22"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<radialGradient id="coin" cx="0.38" cy="0.32" r="0.8">
 <stop offset="0" stop-color="#f0d592"/><stop offset="0.45" stop-color="#c9a45c"/><stop offset="1" stop-color="#6e5527"/></radialGradient>
<linearGradient id="edge" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#5a4520"/><stop offset="0.5" stop-color="#8a6c34"/><stop offset="1" stop-color="#3d2f16"/></linearGradient>
<linearGradient id="area" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#b8584a" stop-opacity="0.28"/><stop offset="1" stop-color="#b8584a" stop-opacity="0"/></linearGradient>
<linearGradient id="blk" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#2c2a26"/><stop offset="1" stop-color="#16150f"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.32" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.36" stop-color="#0a0a0a" stop-opacity="0.85"/><stop offset="0.39" stop-color="#0a0a0a" stop-opacity="1"/>
 <stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.25" r="0.85">
 <stop offset="0.5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
</defs>''')
o.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
for _ in range(80):
    x, y = random.uniform(0, W), random.uniform(130, 360)
    o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(.5,1.3):.1f}" fill="#efe6d6" opacity="{random.uniform(.12,.45):.2f}"/>')
o.append(f'<rect width="{W}" height="{H}" fill="url(#halo)"/>')

# grade discreta do gráfico
for gy in range(150, 400, 50):
    o.append(f'<line x1="90" y1="{gy}" x2="990" y2="{gy}" stroke="#efe6d6" stroke-opacity="0.05"/>')

# linha de preço: sobe, faz topo, cai e rompe a mínima de 2024
pts = []
n = 60
for k in range(n + 1):
    x = 90 + k * (650 / n)
    if k < 14: y = 300 - k * 9
    elif k < 22: y = 174 + math.sin(k) * 8
    else: y = 180 + (k - 22) * 5.6
    y += random.uniform(-7, 7)
    pts.append((x, y))
pts[-1] = (740, 392)
line = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
o.append(f'<polygon points="90,440 {line} 740,440" fill="url(#area)"/>')
o.append(f'<polyline points="{line}" fill="none" stroke="#c96a58" stroke-width="3" stroke-linejoin="round"/>')
# linha de mínima (set/2024)
o.append('<line x1="90" y1="372" x2="990" y2="372" stroke="#c9a45c" stroke-opacity="0.55" stroke-dasharray="4 8"/>')
o.append('<text x="92" y="362" font-family="Inter, sans-serif" font-size="15" letter-spacing="3" fill="#c9a45c" fill-opacity="0.75">MÍNIMA DESDE SET/2024</text>')
o.append('<circle cx="740" cy="392" r="16" fill="#c96a58" fill-opacity="0.22"/><circle cx="740" cy="392" r="6" fill="#e07e69"/>')

# moeda genérica rachada, inclinada, caindo
cx, cy, r = 845, 262, 100
o.append(f'<g transform="rotate(-18 {cx} {cy})">')
o.append(f'<ellipse cx="{cx+14}" cy="{cy+6}" rx="{r*0.92}" ry="{r}" fill="url(#edge)"/>')
o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{r*0.92}" ry="{r}" fill="url(#coin)"/>')
o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{r*0.78}" ry="{r*0.85}" fill="none" stroke="#7a5d2a" stroke-width="3" stroke-opacity="0.7"/>')
for a in range(0, 360, 10):
    t = math.radians(a)
    x1, y1 = cx + math.cos(t) * r * 0.82, cy + math.sin(t) * r * 0.89
    x2, y2 = cx + math.cos(t) * r * 0.87, cy + math.sin(t) * r * 0.95
    o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#7a5d2a" stroke-width="2" stroke-opacity="0.6"/>')
# circuito estilizado no centro (moeda digital genérica)
o.append(f'<g stroke="#6b5024" stroke-width="5" fill="none" stroke-linecap="round" opacity="0.85">'
         f'<path d="M{cx-30},{cy-48} L{cx-30},{cy+48}"/><path d="M{cx-30},{cy-48} L{cx+12},{cy-48} Q{cx+40},{cy-48} {cx+40},{cy-22} Q{cx+40},{cy} {cx+10},{cy} L{cx-30},{cy}"/>'
         f'<path d="M{cx+10},{cy} Q{cx+46},{cy} {cx+46},{cy+24} Q{cx+46},{cy+48} {cx+14},{cy+48} L{cx-30},{cy+48}"/>'
         f'<path d="M{cx-14},{cy-62} L{cx-14},{cy-48}"/><path d="M{cx+8},{cy-62} L{cx+8},{cy-48}"/>'
         f'<path d="M{cx-14},{cy+48} L{cx-14},{cy+62}"/><path d="M{cx+8},{cy+48} L{cx+8},{cy+62}"/></g>')
# rachadura
crack = f"M{cx-8},{cy-r} L{cx+6},{cy-60} L{cx-10},{cy-20} L{cx+14},{cy+18} L{cx-4},{cy+58} L{cx+10},{cy+r}"
o.append(f'<path d="{crack}" fill="none" stroke="#0a0a0a" stroke-width="7" stroke-linejoin="round"/>')
o.append(f'<path d="{crack}" fill="none" stroke="#f3dc9e" stroke-width="1.5" stroke-opacity="0.6" transform="translate(3,0)"/>')
o.append('</g>')
# fragmentos caindo
for fx, fy, s, rot in [(770, 345, 14, 20), (935, 360, 10, -35), (985, 318, 7, 50), (805, 385, 8, 70)]:
    o.append(f'<polygon points="{fx},{fy} {fx+s},{fy+s*0.4} {fx+s*0.3},{fy+s}" fill="#c9a45c" opacity="0.75" transform="rotate({rot} {fx} {fy})"/>')
# rastros de queda


# corrente de blocos no horizonte, com um elo partido
by = 412
xs = list(range(70, 1010, 92))
for i, x in enumerate(xs):
    broken = i == 7
    dy = 14 if broken else 0
    rot = 14 if broken else 0
    o.append(f'<g transform="rotate({rot} {x+28} {by+dy+20})">')
    o.append(f'<rect x="{x}" y="{by+dy}" width="56" height="40" rx="4" fill="url(#blk)" stroke="#c9a45c" stroke-opacity="{0.55 if broken else 0.3}"/>')
    o.append(f'<rect x="{x+8}" y="{by+dy+8}" width="40" height="5" fill="#c9a45c" opacity="0.25"/>')
    o.append(f'<rect x="{x+8}" y="{by+dy+18}" width="26" height="4" fill="#c9a45c" opacity="0.15"/>')
    o.append('</g>')
    if i < len(xs) - 1 and i not in (6, 7):
        o.append(f'<line x1="{x+56}" y1="{by+20}" x2="{x+92}" y2="{by+20}" stroke="#c9a45c" stroke-opacity="0.4" stroke-width="2"/>')
# elos partidos
o.append(f'<line x1="{xs[6]+56}" y1="{by+20}" x2="{xs[6]+70}" y2="{by+24}" stroke="#c9a45c" stroke-opacity="0.4" stroke-width="2"/>')
o.append(f'<line x1="{xs[7]+66}" y1="{by+30}" x2="{xs[8]}" y2="{by+20}" stroke="#c9a45c" stroke-opacity="0.4" stroke-width="2"/>')

o.append(f'<rect width="{W}" height="{H}" fill="url(#fade)"/>')
o.append(f'<rect width="{W}" height="{H}" fill="url(#vign)"/>')
o.append('</svg>')
open("bg.svg", "w").write("\n".join(o))
