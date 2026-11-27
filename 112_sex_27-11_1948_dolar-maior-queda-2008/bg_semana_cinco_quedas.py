"""Fundo do post 27/11/2026 (noite): dólar fecha a R$ 5,51 e tem a maior
queda semanal desde 2008 (−7,07%), com cinco quedas seguidas.
Ilustração: um quadro da semana com cinco painéis (seg a sex), como placas de
pregão. Uma linha dourada parte do toque em R$ 6 na segunda e desce, painel a
painel, até o ponto luminoso de sexta (5,51). Ao fundo, um grande cifrão
gravado em padrão guilhochê, como o de uma cédula genérica. Embaixo, reflexo
no piso e fade para #0a0a0a. Sem marcas, cédulas reais ou pessoas."""
import math, random
from pathlib import Path

random.seed(2711)
W, H = 1080, 1350
HZ = 450
o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
o.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0e1016"/><stop offset="0.2" stop-color="#14161c"/>
 <stop offset="0.33" stop-color="#1d1a15"/><stop offset="0.40" stop-color="#0d0d0d"/>
 <stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<linearGradient id="panel" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#1a1916"/><stop offset="1" stop-color="#0f0f0e"/></linearGradient>
<linearGradient id="panelHi" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#2a2418"/><stop offset="1" stop-color="#14120e"/></linearGradient>
<linearGradient id="line" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#8a6c39"/><stop offset="0.6" stop-color="#d9b56d"/><stop offset="1" stop-color="#f3d58f"/></linearGradient>
<linearGradient id="area" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.20"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></linearGradient>
<radialGradient id="spark" cx="0.5" cy="0.5" r="0.5">
 <stop offset="0" stop-color="#fff1c8" stop-opacity="1"/><stop offset="0.3" stop-color="#f0c877" stop-opacity="0.65"/>
 <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<radialGradient id="halo" cx="0.5" cy="0.5" r="0.5">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.16"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<clipPath id="cifrao"><rect x="0" y="0" width="1080" height="450"/></clipPath>
</defs>''')
o.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')

# guilhochê: rosetas concêntricas atrás, como fundo de cédula genérica
cx, cy = 540, 300
g = ['<g clip-path="url(#cifrao)" opacity="0.10" fill="none" stroke="#c9a45c" stroke-width="0.8">']
for k in range(14):
    R = 120 + k * 22
    pts = []
    for s in range(0, 721):
        a = math.radians(s / 2)
        r = R + 9 * math.sin(18 * a + k * 0.6)
        pts.append(f'{cx + r*math.cos(a):.1f},{cy + r*0.72*math.sin(a):.1f}')
    g.append(f'<polyline points="{" ".join(pts)}"/>')
g.append('</g>')
o += g
# grande cifrão fantasma
o.append(f'<text x="{cx}" y="{cy+150}" text-anchor="middle" font-family="Georgia,serif" font-size="440" fill="#c9a45c" opacity="0.045">$</text>')

# painéis da semana
days = ["SEG", "TER", "QUA", "QUI", "SEX"]
nums = ["23", "24", "25", "26", "27"]
PX0, PW, GAP = 104, 160, 20
PT, PB = 170, 420
for i, d in enumerate(days):
    x = PX0 + i * (PW + GAP)
    fill = "url(#panelHi)" if i == 4 else "url(#panel)"
    stroke = "#c9a45c" if i == 4 else "#2c2a26"
    so = "0.75" if i == 4 else "1"
    o.append(f'<rect x="{x}" y="{PT}" width="{PW}" height="{PB-PT}" rx="6" fill="{fill}" stroke="{stroke}" stroke-opacity="{so}" stroke-width="1.4"/>')
    # cabeçalho do painel
    o.append(f'<line x1="{x+14}" y1="{PT+46}" x2="{x+PW-14}" y2="{PT+46}" stroke="#efe6d6" stroke-opacity="0.08"/>')
    col = "#e8c47a" if i == 4 else "#8f8a82"
    o.append(f'<text x="{x+16}" y="{PT+31}" font-family="Helvetica,Arial,sans-serif" font-size="17" letter-spacing="4" fill="{col}">{d}</text>')
    o.append(f'<text x="{x+PW-16}" y="{PT+31}" text-anchor="end" font-family="Georgia,serif" font-size="19" fill="{col}" opacity="0.8">{nums[i]}</text>')
    # linhas de grade internas
    for gy in range(PT + 80, PB - 10, 36):
        o.append(f'<line x1="{x+14}" y1="{gy}" x2="{x+PW-14}" y2="{gy}" stroke="#efe6d6" stroke-opacity="0.04"/>')
    # pequenas barras de ruído (mini-candles) caindo dentro de cada painel
    yb = 262 + i * 28
    for j in range(6):
        bx = x + 22 + j * 23
        yy = yb + j * 5 + random.uniform(-6, 6)
        hgt = random.uniform(10, 26)
        o.append(f'<line x1="{bx+5}" y1="{yy-8}" x2="{bx+5}" y2="{yy+hgt+8}" stroke="#5a4e3c" stroke-width="1.2" opacity="0.7"/>')
        o.append(f'<rect x="{bx}" y="{yy:.1f}" width="10" height="{hgt:.1f}" fill="#3a3226" stroke="#5a4e3c" stroke-width="1" opacity="0.85"/>')

# linha principal: pontos de fechamento descendo
pts = [(PX0 + PW/2 + i*(PW+GAP), y) for i, y in enumerate([266, 278, 308, 332, 392])]
# toque em 6,00 na segunda (pavio acima)
mx, my = pts[0]
TOP6 = 236
o.append(f'<line x1="{mx}" y1="{TOP6}" x2="{mx}" y2="{my}" stroke="#d9b56d" stroke-width="2" stroke-dasharray="4 4"/>')
o.append(f'<circle cx="{mx}" cy="{TOP6}" r="4" fill="#e8c47a"/>')
o.append(f'<rect x="{mx+12}" y="{TOP6-15}" width="64" height="28" rx="3" fill="#0d0d0d" stroke="#8a6c39" stroke-width="1.2"/>')
o.append(f'<text x="{mx+44}" y="{TOP6+5}" text-anchor="middle" font-family="Georgia,serif" font-size="18" fill="#c9a45c">6,00</text>')
# área sob a linha
poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
o.append(f'<polygon points="{pts[0][0]},{PB-4} {poly} {pts[-1][0]},{PB-4}" fill="url(#area)"/>')
d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
o.append(f'<path d="{d}" fill="none" stroke="#c9a45c" stroke-opacity="0.25" stroke-width="10" stroke-linejoin="round"/>')
o.append(f'<path d="{d}" fill="none" stroke="url(#line)" stroke-width="3.2" stroke-linejoin="round"/>')
for i, (x, y) in enumerate(pts[:-1]):
    o.append(f'<circle cx="{x}" cy="{y}" r="5.5" fill="#0d0d0d" stroke="#d9b56d" stroke-width="2"/>')
fx, fy = pts[-1]
o.append(f'<ellipse cx="{fx}" cy="{fy}" rx="120" ry="70" fill="url(#halo)"/>')
o.append(f'<circle cx="{fx}" cy="{fy}" r="30" fill="url(#spark)"/>')
o.append(f'<circle cx="{fx}" cy="{fy}" r="6.5" fill="#fff1c8"/>')
o.append(f'<text x="{fx}" y="{fy-22}" text-anchor="middle" font-family="Georgia,serif" font-size="24" fill="#f3d58f">5,51</text>')

# piso e reflexo
o.append(f'<line x1="60" y1="{PB+14}" x2="{W-60}" y2="{PB+14}" stroke="#c9a45c" stroke-opacity="0.18"/>')
for i in range(5):
    x = PX0 + i * (PW + GAP)
    o.append(f'<rect x="{x}" y="{PB+18}" width="{PW}" height="60" rx="6" fill="#1a1916" opacity="0.18"/>')
o.append(f'<rect x="0" y="{PB+10}" width="{W}" height="150" fill="url(#fade)"/>')
o.append(f'<rect x="0" y="{PB+150}" width="{W}" height="{H-PB-150}" fill="#0a0a0a"/>')
o.append('</svg>')
Path("bg.svg").write_text("\n".join(o))
print("ok")
