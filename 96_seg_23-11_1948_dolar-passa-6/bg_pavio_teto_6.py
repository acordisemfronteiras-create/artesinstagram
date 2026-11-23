"""Fundo do post 23/11/2026 (noite): dólar passa de R$ 6 durante o dia
(1ª vez desde abril de 2025) e fecha a R$ 5,92.
Ilustração: céu noturno com grade de cotação; uma sequência de candles sobe
até uma linha-teto dourada e luminosa (a marca de R$ 6). O último candle fura
a linha só com o pavio e fecha abaixo dela. Embaixo, horizonte com skyline
genérico de cidade financeira. Sem marcas, moedas ou pessoas reais."""
import random
from pathlib import Path

random.seed(2311)
W, H = 1080, 1350
HZ = 430
o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
o.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0d1118"/><stop offset="0.22" stop-color="#151820"/>
 <stop offset="0.31" stop-color="#211d17"/><stop offset="0.36" stop-color="#0d0d0d"/>
 <stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<linearGradient id="beam" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0"/><stop offset="0.25" stop-color="#e8c47a" stop-opacity="0.9"/>
 <stop offset="0.75" stop-color="#e8c47a" stop-opacity="0.9"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></linearGradient>
<linearGradient id="beamGlow" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0"/><stop offset="0.5" stop-color="#c9a45c" stop-opacity="0.22"/>
 <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></linearGradient>
<radialGradient id="spark" cx="0.5" cy="0.5" r="0.5">
 <stop offset="0" stop-color="#fff1c8" stop-opacity="1"/><stop offset="0.3" stop-color="#f0c877" stop-opacity="0.7"/>
 <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="up" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#d9b56d"/><stop offset="1" stop-color="#8a6c39"/></linearGradient>
<linearGradient id="down" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#4a3f31"/><stop offset="1" stop-color="#2a241c"/></linearGradient>
<linearGradient id="bld" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#1c1b1a"/><stop offset="1" stop-color="#0c0c0c"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="halo" cx="0.5" cy="0.5" r="0.5">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.18"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
</defs>''')
o.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
# estrelas
for _ in range(90):
    x, y = random.uniform(0, W), random.uniform(0, HZ - 120)
    o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{random.uniform(.5,1.4):.2f}" fill="#efe6d6" opacity="{random.uniform(.12,.45):.2f}"/>')
# grade de cotação
for gy in range(150, HZ, 40):
    o.append(f'<line x1="60" y1="{gy}" x2="{W-60}" y2="{gy}" stroke="#efe6d6" stroke-opacity="0.05"/>')
for gx in range(100, W - 40, 80):
    o.append(f'<line x1="{gx}" y1="140" x2="{gx}" y2="{HZ}" stroke="#efe6d6" stroke-opacity="0.04"/>')

# linha-teto (R$ 6) em y=212
TY = 212
o.append(f'<ellipse cx="{W/2}" cy="{TY}" rx="560" ry="70" fill="url(#halo)"/>')
o.append(f'<rect x="0" y="{TY-22}" width="{W}" height="44" fill="url(#beamGlow)"/>')
o.append(f'<line x1="40" y1="{TY}" x2="{W-40}" y2="{TY}" stroke="url(#beam)" stroke-width="3" stroke-dasharray="18 10"/>')
# marcador "6,00" no eixo à direita
o.append(f'<rect x="{W-150}" y="{TY-19}" width="92" height="38" rx="3" fill="#0d0d0d" stroke="#c9a45c" stroke-width="1.5"/>')
o.append(f'<text x="{W-104}" y="{TY+8}" text-anchor="middle" font-family="Georgia,serif" font-size="22" fill="#e8c47a">6,00</text>')
for lvl, yy in (("5,90", TY + 80),):
    o.append(f'<text x="{W-104}" y="{yy+7}" text-anchor="middle" font-family="Georgia,serif" font-size="18" fill="#8f8a82" opacity="0.7">{lvl}</text>')

# candles subindo da esquerda até a linha
cw = 34
xs = list(range(110, 860, 58))
n = len(xs)
base_y = 340
prev_close = base_y
for i, x in enumerate(xs):
    t = i / (n - 1)
    target = base_y - t * (base_y - (TY + 26))
    up = True if i < n - 1 else False
    if i in (3, 7):
        up = False
    if up:
        o_ = prev_close + random.uniform(4, 10)
        c_ = target + random.uniform(-6, 6)
        top, bot = min(o_, c_), max(o_, c_)
        hi, lo = top - random.uniform(8, 18), bot + random.uniform(6, 14)
        fill = "url(#up)"; stroke = "#e0bd76"
    else:
        o_ = prev_close - 4
        c_ = o_ + random.uniform(14, 24)
        top, bot = o_, c_
        hi, lo = top - random.uniform(8, 14), bot + random.uniform(6, 12)
        fill = "url(#down)"; stroke = "#7a6a52"
    if i == n - 1:
        # último candle: pavio fura a linha, corpo fecha abaixo
        o_ = TY + 30; c_ = TY + 48
        top, bot = o_, c_
        hi, lo = TY - 46, bot + 14
        fill = "url(#down)"; stroke = "#c9a45c"
    prev_close = c_
    op = 0.35 + 0.65 * t
    o.append(f'<line x1="{x+cw/2}" y1="{hi:.1f}" x2="{x+cw/2}" y2="{lo:.1f}" stroke="{stroke}" stroke-width="2.4" opacity="{op:.2f}"/>')
    o.append(f'<rect x="{x}" y="{top:.1f}" width="{cw}" height="{max(bot-top,4):.1f}" rx="2" fill="{fill}" stroke="{stroke}" stroke-width="1.4" opacity="{op:.2f}"/>')
    if i == n - 1:
        sx = x + cw / 2
        o.append(f'<circle cx="{sx}" cy="{TY}" r="34" fill="url(#spark)"/>')
        o.append(f'<circle cx="{sx}" cy="{hi:.1f}" r="4" fill="#fff1c8"/>')
        for k in range(10):
            ang = k * 36
            o.append(f'<line x1="{sx}" y1="{TY}" x2="{sx}" y2="{TY-22}" stroke="#f0c877" stroke-width="1.2" opacity="0.55" transform="rotate({ang} {sx} {TY})"/>')
# linha de tendência fina ligando fechamentos
pts = " ".join(f"{x+cw/2},{base_y - (i/(n-1))*(base_y-(TY+26)) - 6:.1f}" for i, x in enumerate(xs))
o.append(f'<polyline points="{pts}" fill="none" stroke="#c9a45c" stroke-width="1.2" stroke-opacity="0.35" stroke-dasharray="4 6"/>')

# skyline genérico no horizonte
x = -10
while x < W + 10:
    w = random.randint(40, 95)
    h = random.randint(22, 70)
    if 380 < x < 620:
        h = random.randint(45, 85)
    o.append(f'<rect x="{x}" y="{HZ-h}" width="{w}" height="{h+40}" fill="url(#bld)" stroke="#2a2824" stroke-width="1"/>')
    for wy in range(HZ - h + 10, HZ, 14):
        for wx in range(x + 6, x + w - 6, 12):
            if random.random() < 0.18:
                o.append(f'<rect x="{wx}" y="{wy}" width="5" height="7" fill="#e8c47a" opacity="{random.uniform(.25,.7):.2f}"/>')
    if random.random() < 0.25:
        o.append(f'<line x1="{x+w/2}" y1="{HZ-h}" x2="{x+w/2}" y2="{HZ-h-24}" stroke="#2a2824" stroke-width="2"/>')
        o.append(f'<circle cx="{x+w/2}" cy="{HZ-h-24}" r="2.2" fill="#c9a45c" opacity="0.8"/>')
    x += w + random.randint(2, 10)
# reflexo / chão
o.append(f'<rect x="0" y="{HZ}" width="{W}" height="60" fill="#0d0d0d"/>')
o.append(f'<line x1="0" y1="{HZ}" x2="{W}" y2="{HZ}" stroke="#c9a45c" stroke-opacity="0.25"/>')
o.append(f'<rect x="0" y="{HZ-40}" width="{W}" height="140" fill="url(#fade)"/>')
o.append(f'<rect x="0" y="{HZ+100}" width="{W}" height="{H-HZ-100}" fill="#0a0a0a"/>')
o.append('</svg>')
Path(__file__).with_name("bg.svg").write_text("\n".join(o))
print("ok")
