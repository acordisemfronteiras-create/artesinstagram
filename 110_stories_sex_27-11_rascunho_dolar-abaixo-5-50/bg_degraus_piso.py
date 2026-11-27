"""Fundo Stories notícia: dólar desce em degraus pela semana e atravessa o piso tracejado de R$ 5,50 (que se parte no ponto da queda)."""
import random
random.seed(27)
W, H = 1080, 1920
def py(p):  # preço -> y
    return 420 + (6.05 - p) / 0.65 * 440
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#101318"/><stop offset="0.25" stop-color="#1a1d22"/>
 <stop offset="0.44" stop-color="#14120e"/><stop offset="0.53" stop-color="#0a0a0a"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<linearGradient id="area" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.16"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></linearGradient>
<radialGradient id="glow" cx="0.78" cy="0.42" r="0.32">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.17"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.44" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.47" stop-color="#0a0a0a" stop-opacity="0.85"/><stop offset="0.49" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<filter id="gl"><feGaussianBlur stdDeviation="7"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/><rect width="100%" height="100%" fill="url(#glow)"/>''')
for _ in range(55):
    x, y = random.uniform(0, W), random.uniform(60, 380)
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="1" fill="#d8d2c4" opacity="{random.uniform(0.1,0.35):.2f}"/>')
# colunas dos dias (5 faixas sutis)
X0, X1 = 70, 1010
cw = (X1 - X0) / 5
for i in range(5):
    if i % 2 == 0:
        s.append(f'<rect x="{X0+i*cw:.0f}" y="420" width="{cw:.0f}" height="440" fill="#c9a45c" fill-opacity="0.025"/>')
# níveis de referência
y6, y575, y55 = py(6.0), py(5.75), py(5.5)
s.append(f'<line x1="{X0}" y1="{y6:.0f}" x2="{X1}" y2="{y6:.0f}" stroke="#8f8a82" stroke-width="1.6" stroke-dasharray="10 12" opacity="0.55"/>')
s.append(f'<text x="{X1}" y="{y6-16:.0f}" text-anchor="end" font-family="Inter, sans-serif" font-size="24" letter-spacing="5" fill="#8f8a82">R$ 6,00</text>')
s.append(f'<line x1="{X0}" y1="{y575:.0f}" x2="{X1}" y2="{y575:.0f}" stroke="#8f8a82" stroke-width="1" stroke-dasharray="4 12" opacity="0.35"/>')
# série: degraus diários com ruído
closes = [6.0, 5.93, 5.91, 5.81, 5.744]
pts = [(X0, py(5.96))]
for d in range(5):
    xa = X0 + d * cw
    start = closes[d - 1] if d else 5.96
    end = closes[d]
    if d == 0:
        path = [(0.3, 5.985), (0.55, 6.0), (0.8, 5.95), (1.0, end)]
    elif d < 4:
        path = [(0.25, start - 0.01), (0.5, (start + end) / 2 + 0.01), (0.75, end + 0.008), (1.0, end)]
    else:
        path = [(0.2, 5.765), (0.45, 5.72), (0.7, 5.75), (1.0, end)]
    for t, p in path:
        pts.append((xa + t * cw * 0.98, py(p + random.uniform(-0.006, 0.006))))
# sexta: abre em queda forte e fura o piso; é o último trecho (pequena faixa à direita)
gap_x = X1 - 120
fri = [(gap_x - 70, py(5.60)), (gap_x - 30, py(5.52)), (gap_x, py(5.479)), (gap_x + 40, py(5.50)), (gap_x + 80, py(5.53)), (X1 - 10, py(5.545))]
# reorganiza: comprime a semana para caber antes da sexta
week_end = gap_x - 110
sx = (week_end - X0) / (pts[-1][0] - X0)
pts = [(X0 + (x - X0) * sx, y) for x, y in pts] + fri
d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
s.append(f'<path d="{d} L{pts[-1][0]:.1f},860 L{pts[0][0]:.1f},860 Z" fill="url(#area)"/>')
# piso de R$ 5,50 em dourado, partido no ponto da queda
gx = gap_x
s.append(f'<line x1="{X0}" y1="{y55:.0f}" x2="{gx-34}" y2="{y55:.0f}" stroke="#c9a45c" stroke-width="2.6" stroke-dasharray="14 10" opacity="0.9"/>')
s.append(f'<line x1="{gx+34}" y1="{y55:.0f}" x2="{X1}" y2="{y55:.0f}" stroke="#c9a45c" stroke-width="2.6" stroke-dasharray="14 10" opacity="0.9"/>')
for dx, dy, ang in [(-30, -10, -25), (-22, 12, 20), (26, -12, 30), (32, 9, -18)]:
    s.append(f'<rect x="{gx+dx-6}" y="{y55+dy-1.5:.0f}" width="12" height="3" fill="#c9a45c" opacity="0.7" transform="rotate({ang} {gx+dx} {y55+dy:.0f})"/>')
s.append(f'<text x="{X0}" y="{y55+42:.0f}" font-family="Inter, sans-serif" font-size="24" letter-spacing="5" fill="#c9a45c">R$ 5,50</text>')
s.append(f'<path d="{d}" fill="none" stroke="#c9a45c" stroke-width="10" stroke-opacity="0.22" filter="url(#gl)"/>')
s.append(f'<path d="{d}" fill="none" stroke="#e2c27e" stroke-width="3.4" stroke-linejoin="round"/>')
mx, my = gap_x, py(5.479)
s.append(f'<circle cx="{mx}" cy="{my:.0f}" r="28" fill="#c9a45c" opacity="0.18"/>')
s.append(f'<circle cx="{mx}" cy="{my:.0f}" r="9" fill="#f1e1b8"/>')
s.append(f'<line x1="{X0}" y1="860" x2="{X1}" y2="860" stroke="#2a2824" stroke-width="2"/>')
s.append('<rect width="100%" height="100%" fill="url(#fade)"/></svg>')
open("bg.svg", "w").write("\n".join(s)); print("ok")
