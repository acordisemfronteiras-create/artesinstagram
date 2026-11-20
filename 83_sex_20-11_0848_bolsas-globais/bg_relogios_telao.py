"""Fundo: parede de relógios mundiais (bolsas globais) sobre telão com gráfico em queda."""
import math, random
random.seed(20)
W, H = 1080, 1350
o = []
o.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
o.append('''<defs>
<linearGradient id="wall" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#14181f"/><stop offset="0.30" stop-color="#191c22"/>
 <stop offset="0.42" stop-color="#121214"/><stop offset="0.55" stop-color="#0b0b0b"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="glow" cx="0.5" cy="0.22" r="0.55">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.14"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="screen" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0e131b"/><stop offset="1" stop-color="#070a0e"/></linearGradient>
<linearGradient id="area" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#b0574a" stop-opacity="0.35"/><stop offset="1" stop-color="#b0574a" stop-opacity="0"/></linearGradient>
<radialGradient id="face" cx="0.45" cy="0.4" r="0.7">
 <stop offset="0" stop-color="#1f232a"/><stop offset="1" stop-color="#0d0f13"/></radialGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.335" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.37" stop-color="#0a0a0a" stop-opacity="0.8"/><stop offset="0.40" stop-color="#0a0a0a" stop-opacity="1"/>
 <stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<linearGradient id="topfade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.55"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="0"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.25" r="0.85">
 <stop offset="0.5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
</defs>''')
o.append(f'<rect width="{W}" height="{H}" fill="url(#wall)"/>')
o.append(f'<rect width="{W}" height="{H}" fill="url(#glow)"/>')
# painéis de parede (madeira escura vertical)
for x in range(0, W, 90):
    o.append(f'<line x1="{x}" y1="0" x2="{x}" y2="500" stroke="#000" stroke-opacity="0.35" stroke-width="1"/>')
# friso dourado
# (friso removido)

# relógios: cidade, hora local às ~9h de Brasília
clocks = [("NOVA YORK", 7, 5), ("SÃO PAULO", 9, 5), ("TÓQUIO", 21, 5), ("SEUL", 21, 5)]
cx0, gap, cy, r = 195, 230, 205, 54
for i, (city, hh, mm) in enumerate(clocks):
    cx = cx0 + i * gap
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r+9}" fill="#0b0c0f" stroke="#c9a45c" stroke-opacity="0.75" stroke-width="3"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#face)" stroke="#3a3328" stroke-width="1.5"/>')
    for k in range(60):
        a = math.radians(k * 6)
        r1 = r - (11 if k % 5 == 0 else 5)
        w = 2.4 if k % 5 == 0 else 1
        col = "#c9a45c" if k % 5 == 0 else "#6d6656"
        o.append(f'<line x1="{cx+math.sin(a)*r1:.1f}" y1="{cy-math.cos(a)*r1:.1f}" x2="{cx+math.sin(a)*(r-3):.1f}" y2="{cy-math.cos(a)*(r-3):.1f}" stroke="{col}" stroke-width="{w}"/>')
    ha = math.radians(((hh % 12) + mm / 60) * 30)
    ma = math.radians(mm * 6)
    o.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+math.sin(ha)*r*0.5:.1f}" y2="{cy-math.cos(ha)*r*0.5:.1f}" stroke="#efe6d6" stroke-width="5" stroke-linecap="round"/>')
    o.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+math.sin(ma)*r*0.78:.1f}" y2="{cy-math.cos(ma)*r*0.78:.1f}" stroke="#efe6d6" stroke-width="3" stroke-linecap="round"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="#c9a45c"/>')
    noite = hh >= 18 or hh < 6
    o.append(f'<text x="{cx}" y="{cy+r+34}" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="15" letter-spacing="4" fill="#a9a39a">{city}</text>')
    # pequeno indicador de pregão: ponto aceso/apagado
    o.append(f'<circle cx="{cx}" cy="{cy+r+50}" r="4" fill="{"#b0574a" if noite else "#6d6656"}" opacity="0.9"/>')

# telão
sx, sy, sw, sh = 90, 330, 900, 150
o.append(f'<rect x="{sx-8}" y="{sy-8}" width="{sw+16}" height="{sh+16}" rx="6" fill="#050608" stroke="#2a2824" stroke-width="2"/>')
o.append(f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" fill="url(#screen)"/>')
for gy in range(sy + 30, sy + sh, 36):
    o.append(f'<line x1="{sx}" y1="{gy}" x2="{sx+sw}" y2="{gy}" stroke="#c9a45c" stroke-opacity="0.07"/>')
for gx in range(sx + 60, sx + sw, 75):
    o.append(f'<line x1="{gx}" y1="{sy}" x2="{gx}" y2="{sy+sh}" stroke="#c9a45c" stroke-opacity="0.05"/>')
# série descendente com 6 quedas
pts = []
n = 64
y = sy + 40
for k in range(n):
    x = sx + 20 + k * (sw - 40) / (n - 1)
    drift = 2.3 if k > 14 else -0.6
    y += drift + random.uniform(-4.5, 4.0)
    if k in (50, 51, 52, 53): y += 6
    y = max(sy + 22, min(sy + sh - 18, y))
    pts.append((x, y))
line = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
area = f"{sx+20},{sy+sh} " + line + f" {pts[-1][0]:.1f},{sy+sh}"
o.append(f'<polygon points="{area}" fill="url(#area)"/>')
o.append(f'<polyline points="{line}" fill="none" stroke="#c96a5a" stroke-width="3" stroke-linejoin="round"/>')
lx, ly = pts[-1]
o.append(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="7" fill="#c96a5a"/><circle cx="{lx:.1f}" cy="{ly:.1f}" r="14" fill="#c96a5a" opacity="0.25"/>')
# letreiro corrido no topo do telão (genérico)
o.append(f'<rect x="{sx}" y="{sy}" width="{sw}" height="26" fill="#000" opacity="0.55"/>')
ticks = ["▼ NY", "▼ TÓQUIO", "▼ SEUL", "▼ NASDAQ", "▼ S&amp;P", "▼ DOW", "▼ ÁSIA"]
tx = sx + 16
for t in ticks:
    o.append(f'<text x="{tx}" y="{sy+18}" font-family="Inter,Arial,sans-serif" font-size="13" letter-spacing="2" fill="#c96a5a">{t}</text>')
    tx += 128
o.append(f'<rect width="{W}" height="130" fill="url(#topfade)"/>')
o.append(f'<rect width="{W}" height="{H}" fill="url(#fade)"/>')
o.append(f'<rect width="{W}" height="{H}" fill="url(#vign)"/>')
o.append('</svg>')
open("bg.svg", "w").write("\n".join(o))
print("bg.svg ok")
