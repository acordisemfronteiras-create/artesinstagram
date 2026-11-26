"""Fundo Stories notícia: candles da bolsa em queda lenta e, no fim, um candle longo de alta (salto do dia)."""
import random
random.seed(26)
W, H = 1080, 1920
TOP, BOT = 400, 860
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0d1218"/><stop offset="0.25" stop-color="#141b22"/>
 <stop offset="0.42" stop-color="#14120e"/><stop offset="0.5" stop-color="#0a0a0a"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="glow" cx="0.84" cy="0.24" r="0.36">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.20"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="bar" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#f1dca6"/><stop offset="1" stop-color="#b8924a"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.44" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.47" stop-color="#0a0a0a" stop-opacity="0.9"/><stop offset="0.49" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<filter id="gl"><feGaussianBlur stdDeviation="10"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/><rect width="100%" height="100%" fill="url(#glow)"/>''')
for _ in range(55):
    x, y = random.uniform(0, W), random.uniform(60, 380)
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="1" fill="#d8d2c4" opacity="{random.uniform(0.1,0.35):.2f}"/>')
for gy in range(TOP + 40, BOT, 70):
    s.append(f'<line x1="70" y1="{gy}" x2="1010" y2="{gy}" stroke="#c9a45c" stroke-opacity="0.06"/>')
# candles: deriva levemente para baixo, depois o salto
n = 17; cw = 30; gap = 50
x0 = 90
price = 700
for i in range(n):
    x = x0 + i * gap
    o = price
    c = o + random.uniform(-26, 30) + 6   # y cresce para baixo: + = queda
    hi = min(o, c) - random.uniform(8, 26)
    lo = max(o, c) + random.uniform(8, 26)
    up = c < o
    col = "#c9a45c" if up else "#5a554c"
    s.append(f'<line x1="{x+cw/2}" y1="{hi:.0f}" x2="{x+cw/2}" y2="{lo:.0f}" stroke="{col}" stroke-width="2.5" opacity="0.8"/>')
    y1, y2 = min(o, c), max(o, c)
    if y2 - y1 < 4: y2 = y1 + 4
    if up:
        s.append(f'<rect x="{x}" y="{y1:.0f}" width="{cw}" height="{y2-y1:.0f}" fill="#c9a45c" opacity="0.55"/>')
    else:
        s.append(f'<rect x="{x}" y="{y1:.0f}" width="{cw}" height="{y2-y1:.0f}" fill="none" stroke="#6b655b" stroke-width="2.5"/>')
    price = c
# candle do salto
x = x0 + n * gap + 14; cw2 = 46
o = price; c = 470
s.append(f'<rect x="{x-10}" y="{c-10}" width="{cw2+20}" height="{o-c+20:.0f}" fill="#c9a45c" opacity="0.35" filter="url(#gl)"/>')
s.append(f'<line x1="{x+cw2/2}" y1="{c-34}" x2="{x+cw2/2}" y2="{o+18:.0f}" stroke="#e2c27e" stroke-width="3"/>')
s.append(f'<rect x="{x}" y="{c}" width="{cw2}" height="{o-c:.0f}" fill="url(#bar)"/>')
# nível tracejado na máxima
s.append(f'<line x1="70" y1="{c-34}" x2="1010" y2="{c-34}" stroke="#c9a45c" stroke-width="2" stroke-dasharray="12 10" opacity="0.6"/>')
s.append(f'<line x1="70" y1="{BOT}" x2="1010" y2="{BOT}" stroke="#2a2824" stroke-width="2"/>')
s.append('<rect width="100%" height="100%" fill="url(#fade)"/></svg>')
open("bg.svg", "w").write("\n".join(s)); print("ok")
