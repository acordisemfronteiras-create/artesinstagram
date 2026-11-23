"""Fundo: amanhecer sobre skyline, sol nascendo atrás dos prédios e linha de gráfico
que desce até um vale e volta a subir (repique após a correção)."""
import random, math
random.seed(23)
W, H = 1080, 1350
HZ = 430  # horizonte
s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0e131c"/>
 <stop offset="0.16" stop-color="#18202c"/>
 <stop offset="0.27" stop-color="#2c2a2b"/>
 <stop offset="0.32" stop-color="#4a3a26"/>
 <stop offset="0.345" stop-color="#2a2118"/>
 <stop offset="0.42" stop-color="#0c0c0c"/>
 <stop offset="1" stop-color="#0a0a0a"/>
</linearGradient>
<radialGradient id="sun" cx="0.5" cy="0.5" r="0.5">
 <stop offset="0" stop-color="#f3d79a" stop-opacity="0.95"/>
 <stop offset="0.35" stop-color="#c9a45c" stop-opacity="0.75"/>
 <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/>
</radialGradient>
<radialGradient id="halo" cx="0.5" cy="0.5" r="0.5">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.28"/>
 <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/>
</radialGradient>
<linearGradient id="area" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.20"/>
 <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/>
</linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.30"/>
 <stop offset="0.12" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.31" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.37" stop-color="#0a0a0a" stop-opacity="0.85"/>
 <stop offset="0.41" stop-color="#0a0a0a" stop-opacity="1"/>
 <stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/>
</linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.28" r="0.8">
 <stop offset="0.55" stop-color="#000" stop-opacity="0"/>
 <stop offset="1" stop-color="#000" stop-opacity="0.6"/>
</radialGradient>
<filter id="blur"><feGaussianBlur stdDeviation="3"/></filter>
</defs>''')
s.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
# estrelas que somem perto do horizonte
for _ in range(70):
    x = random.uniform(0, W); y = random.uniform(130, 300)
    a = 0.45 * (1 - (y - 130) / 190)
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.choice([0.8,1,1.3])}" fill="#d8d2c4" opacity="{a:.2f}"/>')
# sol nascendo
sx, sy = 780, HZ - 6
s.append(f'<circle cx="{sx}" cy="{sy}" r="300" fill="url(#halo)"/>')
s.append(f'<circle cx="{sx}" cy="{sy}" r="120" fill="url(#sun)"/>')
s.append(f'<circle cx="{sx}" cy="{sy}" r="54" fill="#e9c983" opacity="0.9"/>')
# raios finos
for k in range(13):
    ang = math.radians(195 + k * 12.5)
    x1 = sx + 80 * math.cos(ang); y1 = sy + 80 * math.sin(ang)
    x2 = sx + 260 * math.cos(ang); y2 = sy + 260 * math.sin(ang)
    s.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#c9a45c" stroke-width="1.2" opacity="0.18"/>')
# grade horizontal discreta do gráfico
for gy in range(170, HZ, 52):
    s.append(f'<line x1="70" y1="{gy}" x2="1010" y2="{gy}" stroke="#c9a45c" stroke-opacity="0.07" stroke-dasharray="2 8"/>')
# linha: desce do alto à esquerda, vale, repique à direita
pts = []
n = 60
for i in range(n + 1):
    t = i / n
    x = 70 + t * 900
    base = 175 + 190 * math.sin(math.pi * min(t / 0.72, 1) * 0.5) ** 1.6 if t < 0.72 else 0
    if t < 0.72:
        y = 175 + 195 * (t / 0.72) ** 1.5
    else:
        u = (t - 0.72) / 0.28
        y = 370 - 120 * (u ** 0.85)
    y += random.uniform(-7, 7) if 0.03 < t < 0.97 else 0
    pts.append((x, y))
d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
s.append(f'<path d="{d} L{pts[-1][0]:.1f},{HZ} L{pts[0][0]:.1f},{HZ} Z" fill="url(#area)"/>')
s.append(f'<path d="{d}" fill="none" stroke="#8f8a82" stroke-width="2.4" opacity="0.75"/>')
# trecho do repique em dourado
k0 = int(n * 0.72)
d2 = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts[k0:])
s.append(f'<path d="{d2}" fill="none" stroke="#c9a45c" stroke-width="7" opacity="0.35" filter="url(#blur)"/>')
s.append(f'<path d="{d2}" fill="none" stroke="#e2c27e" stroke-width="3.2"/>')
ex, ey = pts[-1]
s.append(f'<circle cx="{ex:.0f}" cy="{ey:.0f}" r="16" fill="#c9a45c" opacity="0.25"/>')
s.append(f'<circle cx="{ex:.0f}" cy="{ey:.0f}" r="7" fill="#f1e1b8"/>')
# marca do vale
vx, vy = pts[k0]
s.append(f'<circle cx="{vx:.0f}" cy="{vy:.0f}" r="6" fill="none" stroke="#8f8a82" stroke-width="2"/>')
# skyline em silhueta
x = 0
while x < W:
    w = random.randint(38, 92); h = random.randint(40, 150)
    if 650 < x < 900: h = random.randint(30, 80)  # deixa o sol aparecer
    top = HZ - h
    s.append(f'<rect x="{x}" y="{top}" width="{w}" height="{h+4}" fill="#0d0e11"/>')
    s.append(f'<rect x="{x}" y="{top}" width="{w}" height="2" fill="#c9a45c" opacity="0.18"/>')
    for wy in range(top + 12, HZ - 8, 16):
        for wx in range(x + 8, x + w - 8, 14):
            if random.random() < 0.12:
                s.append(f'<rect x="{wx}" y="{wy}" width="5" height="7" fill="#c9a45c" opacity="{random.uniform(0.3,0.7):.2f}"/>')
    x += w + random.randint(2, 8)
# torre com antena
s.append(f'<rect x="210" y="{HZ-210}" width="70" height="214" fill="#0b0c0f"/>')
s.append(f'<rect x="232" y="{HZ-250}" width="26" height="42" fill="#0b0c0f"/>')
s.append(f'<line x1="245" y1="{HZ-250}" x2="245" y2="{HZ-300}" stroke="#2a2824" stroke-width="3"/>')
s.append(f'<circle cx="245" cy="{HZ-302}" r="3.5" fill="#c9a45c"/>')
for wy in range(HZ - 196, HZ - 8, 18):
    for wx in (220, 238, 256):
        if random.random() < 0.3:
            s.append(f'<rect x="{wx}" y="{wy}" width="6" height="8" fill="#c9a45c" opacity="0.55"/>')
s.append(f'<rect x="0" y="{HZ}" width="{W}" height="{H-HZ}" fill="#0a0a0a"/>')
s.append(f'<line x1="0" y1="{HZ}" x2="{W}" y2="{HZ}" stroke="#c9a45c" stroke-opacity="0.22"/>')
s.append(f'<rect width="{W}" height="{H}" fill="url(#fade)"/>')
s.append(f'<rect width="{W}" height="{H}" fill="url(#vign)"/>')
s.append('</svg>')
open("bg.svg", "w").write("\n".join(s))
print("ok")
