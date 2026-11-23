"""Fundo Stories notícia: skyline genérico + candles caindo por 7 dias e um candle dourado gigante de virada."""
import random
random.seed(23)
W, H = 1080, 1920
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0e1219"/><stop offset="0.3" stop-color="#171c25"/>
 <stop offset="0.46" stop-color="#14120e"/><stop offset="0.56" stop-color="#0a0a0a"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="glow" cx="0.8" cy="0.27" r="0.42">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.22"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="gold" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#f1d79a"/><stop offset="1" stop-color="#b08a45"/></linearGradient>
<linearGradient id="bld" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#1c2029"/><stop offset="1" stop-color="#0d0e11"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.44" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.50" stop-color="#0a0a0a" stop-opacity="0.9"/><stop offset="0.53" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<filter id="gl"><feGaussianBlur stdDeviation="14"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/><rect width="100%" height="100%" fill="url(#glow)"/>''')
for _ in range(55):
    x, y = random.uniform(0, W), random.uniform(60, 380)
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="1" fill="#d8d2c4" opacity="{random.uniform(0.12,0.4):.2f}"/>')
# skyline genérico (sem prédios reconhecíveis)
x = 0
BASE = 905
while x < W:
    w = random.randint(46, 96); h = random.randint(70, 250)
    s.append(f'<rect x="{x}" y="{BASE-h}" width="{w}" height="{h}" fill="url(#bld)" opacity="0.85"/>')
    for wy in range(BASE - h + 16, BASE - 10, 22):
        for wx in range(x + 9, x + w - 9, 15):
            if random.random() < 0.16:
                s.append(f'<rect x="{wx}" y="{wy}" width="5" height="8" fill="#c9a45c" opacity="{random.uniform(.15,.45):.2f}"/>')
    x += w + random.randint(2, 8)
# grade
for gy in range(440, 900, 64):
    s.append(f'<line x1="70" y1="{gy}" x2="1010" y2="{gy}" stroke="#c9a45c" stroke-opacity="0.06"/>')
# 7 candles de queda (apagados) e 1 candle de virada (dourado)
cw, gap, x0 = 62, 44, 90
top = 520
for i in range(7):
    cx = x0 + i * (cw + gap)
    o = top + i * 34 + random.randint(-6, 6)
    c = o + random.randint(38, 60)
    s.append(f'<line x1="{cx+cw/2}" y1="{o-22}" x2="{cx+cw/2}" y2="{c+22}" stroke="#6d6a66" stroke-width="2.5" opacity="0.8"/>')
    s.append(f'<rect x="{cx}" y="{o}" width="{cw}" height="{c-o}" fill="#2b2a2c" stroke="#6d6a66" stroke-width="2" opacity="0.92"/>')
    last_c = c
cx = x0 + 7 * (cw + gap) + 8
o, c = last_c + 10, 430
s.append(f'<rect x="{cx-14}" y="{c}" width="{cw+56}" height="{o-c}" fill="#c9a45c" opacity="0.35" filter="url(#gl)"/>')
s.append(f'<line x1="{cx+(cw+28)/2}" y1="{c-34}" x2="{cx+(cw+28)/2}" y2="{o+20}" stroke="#e2c27e" stroke-width="3.5"/>')
s.append(f'<rect x="{cx}" y="{c}" width="{cw+28}" height="{o-c}" fill="url(#gold)"/>')
# seta discreta
ax = cx + (cw + 28) / 2
s.append(f'<path d="M{ax-20},{c-48} L{ax},{c-76} L{ax+20},{c-48}" fill="none" stroke="#e2c27e" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>')
s.append(f'<line x1="70" y1="{BASE}" x2="1010" y2="{BASE}" stroke="#2a2824" stroke-width="2"/>')
s.append('<rect width="100%" height="100%" fill="url(#fade)"/></svg>')
open("bg.svg", "w").write("\n".join(s)); print("ok")
