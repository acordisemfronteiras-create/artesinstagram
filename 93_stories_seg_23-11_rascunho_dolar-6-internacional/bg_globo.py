"""Fundo Stories: globo em arame com arco dourado ligando dois pontos (patrimônio em mais de uma moeda)."""
import math, random
random.seed(623)
W, H = 1080, 1920
cx, cy, R = 540, 620, 300
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0f141d"/><stop offset="0.25" stop-color="#18202b"/>
 <stop offset="0.42" stop-color="#14120f"/><stop offset="0.55" stop-color="#0a0a0a"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="g" cx="0.5" cy="0.5" r="0.5">
 <stop offset="0" stop-color="#1d2633"/><stop offset="0.8" stop-color="#121821"/><stop offset="1" stop-color="#0c1016"/></radialGradient>
<radialGradient id="halo" cx="0.5" cy="0.5" r="0.5">
 <stop offset="0.6" stop-color="#c9a45c" stop-opacity="0.14"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.43" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.51" stop-color="#0a0a0a" stop-opacity="0.9"/><stop offset="0.54" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<filter id="gl"><feGaussianBlur stdDeviation="5"/></filter>
<clipPath id="c"><circle cx="540" cy="620" r="300"/></clipPath>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/>''')
for _ in range(90):
    x, y = random.uniform(0, W), random.uniform(60, 900)
    if math.hypot(x - cx, y - cy) > R + 40:
        s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.choice([0.8,1.1,1.4])}" fill="#d8d2c4" opacity="{random.uniform(0.15,0.5):.2f}"/>')
s.append(f'<circle cx="{cx}" cy="{cy}" r="{R+90}" fill="url(#halo)"/>')
s.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#g)" stroke="#c9a45c" stroke-opacity="0.35" stroke-width="2"/>')
g = ['<g clip-path="url(#c)">']
for lat in range(-60, 61, 20):  # paralelos
    y = cy - R * math.sin(math.radians(lat)); rx = R * math.cos(math.radians(lat))
    g.append(f'<ellipse cx="{cx}" cy="{y:.1f}" rx="{rx:.1f}" ry="{rx*0.08:.1f}" fill="none" stroke="#c9a45c" stroke-opacity="0.14"/>')
for lon in range(-75, 76, 25):  # meridianos
    rx = abs(R * math.sin(math.radians(lon)))
    g.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx:.1f}" ry="{R}" fill="none" stroke="#c9a45c" stroke-opacity="0.14"/>')
# pontos de "cidades" (grade de pontos)
for _ in range(260):
    a = random.uniform(0, 2*math.pi); r = R*math.sqrt(random.uniform(0, 1))
    x, y = cx + r*math.cos(a), cy + r*math.sin(a)
    g.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="1.3" fill="#8f8a82" opacity="{random.uniform(0.15,0.45):.2f}"/>')
g.append('</g>')
s += g
# arco dourado entre dois pontos
p1 = (cx - 150, cy + 150); p2 = (cx + 170, cy - 140)
ctrl = (cx + 120, cy + 260 - 520)
d = f"M{p1[0]},{p1[1]} Q{ctrl[0]},{ctrl[1]} {p2[0]},{p2[1]}"
s.append(f'<path d="{d}" fill="none" stroke="#c9a45c" stroke-width="10" stroke-opacity="0.3" filter="url(#gl)"/>')
s.append(f'<path d="{d}" fill="none" stroke="#e2c27e" stroke-width="3" stroke-dasharray="2 0"/>')
for (x, y) in (p1, p2):
    s.append(f'<circle cx="{x}" cy="{y}" r="22" fill="#c9a45c" opacity="0.18"/>')
    s.append(f'<circle cx="{x}" cy="{y}" r="8" fill="#f1e1b8"/>')
# órbita externa
s.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{R+120}" ry="80" fill="none" stroke="#c9a45c" stroke-opacity="0.25" transform="rotate(-14 {cx} {cy})"/>')
s.append('<rect width="100%" height="100%" fill="url(#fade)"/></svg>')
open("bg.svg", "w").write("\n".join(s)); print("ok")
