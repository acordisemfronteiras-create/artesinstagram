"""Fundo Stories notícia: gráfico de linha do dólar subindo até encostar na linha tracejada de R$ 6."""
import math, random
random.seed(6)
W, H = 1080, 1920
TOP, BOT = 420, 900      # área do gráfico
L6 = 470                 # linha dos R$ 6
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0f141d"/><stop offset="0.28" stop-color="#18202b"/>
 <stop offset="0.45" stop-color="#15130f"/><stop offset="0.56" stop-color="#0a0a0a"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<linearGradient id="area" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.22"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></linearGradient>
<radialGradient id="glow" cx="0.82" cy="0.25" r="0.4">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.16"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.44" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.50" stop-color="#0a0a0a" stop-opacity="0.9"/><stop offset="0.53" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<filter id="gl"><feGaussianBlur stdDeviation="6"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/><rect width="100%" height="100%" fill="url(#glow)"/>''')
for _ in range(60):
    x, y = random.uniform(0, W), random.uniform(60, 400)
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="1" fill="#d8d2c4" opacity="{random.uniform(0.12,0.4):.2f}"/>')
# grade
for gy in range(L6 + 70, BOT, 70):
    s.append(f'<line x1="70" y1="{gy}" x2="1010" y2="{gy}" stroke="#c9a45c" stroke-opacity="0.07"/>')
for gx in range(70, 1011, 94):
    s.append(f'<line x1="{gx}" y1="{TOP}" x2="{gx}" y2="{BOT}" stroke="#c9a45c" stroke-opacity="0.05"/>')
# linha tracejada dos R$ 6
s.append(f'<line x1="70" y1="{L6}" x2="1010" y2="{L6}" stroke="#c9a45c" stroke-width="2.5" stroke-dasharray="14 10" opacity="0.85"/>')
s.append(f'<text x="1010" y="{L6-18}" text-anchor="end" font-family="Inter, sans-serif" font-size="26" letter-spacing="5" fill="#c9a45c">R$ 6,00</text>')
# série: oscila e sobe, termina logo abaixo da linha
n = 70; pts = []
y = 860
for i in range(n + 1):
    t = i / n
    x = 70 + t * 880
    target = 860 - 370 * (t ** 1.8)
    y = target + random.uniform(-14, 14) * (1 - t * 0.7)
    if i == n: y = L6 + 14
    pts.append((x, y))
d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
s.append(f'<path d="{d} L{pts[-1][0]:.1f},{BOT} L{pts[0][0]:.1f},{BOT} Z" fill="url(#area)"/>')
s.append(f'<path d="{d}" fill="none" stroke="#c9a45c" stroke-width="9" stroke-opacity="0.25" filter="url(#gl)"/>')
s.append(f'<path d="{d}" fill="none" stroke="#e2c27e" stroke-width="3.4" stroke-linejoin="round"/>')
ex, ey = pts[-1]
s.append(f'<circle cx="{ex:.0f}" cy="{ey:.0f}" r="26" fill="#c9a45c" opacity="0.2"/>')
s.append(f'<circle cx="{ex:.0f}" cy="{ey:.0f}" r="9" fill="#f1e1b8"/>')
s.append(f'<line x1="70" y1="{BOT}" x2="1010" y2="{BOT}" stroke="#2a2824" stroke-width="2"/>')
s.append('<rect width="100%" height="100%" fill="url(#fade)"/></svg>')
open("bg.svg", "w").write("\n".join(s)); print("ok")
