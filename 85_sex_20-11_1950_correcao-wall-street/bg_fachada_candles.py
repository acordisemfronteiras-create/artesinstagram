"""Fundo: fachada neoclássica genérica de bolsa à noite, com gráfico de candles em queda
cruzando a linha de correção (-10% do topo) no céu."""
import random
random.seed(2011)
W, H = 1080, 1350
o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
o.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0c1018"/><stop offset="0.22" stop-color="#151a24"/>
 <stop offset="0.33" stop-color="#1a1b20"/><stop offset="0.45" stop-color="#0e0e0f"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="halo" cx="0.5" cy="0.30" r="0.45">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.16"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="stone" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#3a3630"/><stop offset="1" stop-color="#1d1b18"/></linearGradient>
<linearGradient id="col" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#1c1a17"/><stop offset="0.35" stop-color="#4a443a"/><stop offset="0.6" stop-color="#36322b"/><stop offset="1" stop-color="#15130f"/></linearGradient>
<linearGradient id="inner" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#2a2014"/><stop offset="1" stop-color="#120e09"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.315" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.355" stop-color="#0a0a0a" stop-opacity="0.85"/><stop offset="0.385" stop-color="#0a0a0a" stop-opacity="1"/>
 <stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<linearGradient id="topfade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.6"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="0"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.25" r="0.85">
 <stop offset="0.5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
</defs>''')
o.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
# estrelas discretas
for _ in range(70):
    x, y = random.uniform(0, W), random.uniform(130, 300)
    o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(.5,1.3):.1f}" fill="#efe6d6" opacity="{random.uniform(.15,.5):.2f}"/>')
o.append(f'<rect width="{W}" height="{H}" fill="url(#halo)"/>')

# skyline genérico ao fundo
x = 0
while x < W:
    w = random.randint(40, 90); h = random.randint(60, 190)
    top = 455 - h
    o.append(f'<rect x="{x}" y="{top}" width="{w}" height="{h}" fill="#101318"/>')
    for wy in range(top + 10, 450, 14):
        for wx in range(x + 6, x + w - 6, 11):
            if random.random() < 0.18:
                o.append(f'<rect x="{wx}" y="{wy}" width="4" height="6" fill="#c9a45c" opacity="{random.uniform(.15,.45):.2f}"/>')
    x += w + random.randint(2, 8)

# gráfico de candles no céu (topo -> queda)
gx0, gx1 = 90, 990
n = 34
closes = []
for k in range(n):
    if k < 12: v = 246 - k * 7.5 + random.uniform(-4, 4)
    elif k < 15: v = 160 + random.uniform(-3, 5)
    else: v = 164 + (k - 15) * 7.6 + random.uniform(-5, 5)
    closes.append(v)
closes[-1] = max(closes[-1], 314)
peak = min(closes)
step = (gx1 - gx0) / n
corr = 272
o.append(f'<line x1="{gx0}" y1="{peak-12:.0f}" x2="{gx1}" y2="{peak-12:.0f}" stroke="#c9a45c" stroke-opacity="0.35" stroke-dasharray="3 7"/>')
o.append(f'<line x1="{gx0}" y1="{corr}" x2="{gx1}" y2="{corr}" stroke="#c9a45c" stroke-opacity="0.75" stroke-width="1.6" stroke-dasharray="10 8"/>')
o.append(f'<text x="{gx0}" y="{corr+24}" font-family="Inter,Arial,sans-serif" font-size="15" letter-spacing="3" fill="#c9a45c" opacity="0.9">−10% DO TOPO</text>')
o.append(f'<text x="{gx0}" y="{peak-22:.0f}" font-family="Inter,Arial,sans-serif" font-size="14" letter-spacing="3" fill="#a9a39a" opacity="0.75">RECORDE</text>')
prev = closes[0] + 6
for k, c in enumerate(closes):
    xc = gx0 + step * (k + .5)
    op = prev
    up = c < op
    col = "#7f9a6e" if up else "#c96a5a"
    hi = min(op, c) - random.uniform(3, 10); lo = max(op, c) + random.uniform(3, 10)
    o.append(f'<line x1="{xc:.1f}" y1="{hi:.1f}" x2="{xc:.1f}" y2="{lo:.1f}" stroke="{col}" stroke-width="2" opacity="0.9"/>')
    hgt = max(4, abs(c - op))
    o.append(f'<rect x="{xc-9:.1f}" y="{min(op,c):.1f}" width="18" height="{hgt:.1f}" fill="{col}" opacity="0.92"/>')
    prev = c
lx = gx0 + step * (n - .5); ly = closes[-1]
o.append(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="16" fill="#c96a5a" opacity="0.22"/>')

# fachada neoclássica genérica
fx0, fx1 = 250, 830
base = 455
o.append(f'<rect x="{fx0-30}" y="{base-12}" width="{fx1-fx0+60}" height="12" fill="#2b2823"/>')
o.append(f'<rect x="{fx0-50}" y="{base}" width="{fx1-fx0+100}" height="10" fill="#22201c"/>')
ct = 378  # topo das colunas
o.append(f'<rect x="{fx0+10}" y="{ct}" width="{fx1-fx0-20}" height="{base-12-ct}" fill="url(#inner)"/>')
# portas iluminadas
for dx in (fx0+95, fx0+255, fx0+415):
    o.append(f'<rect x="{dx}" y="{base-62}" width="56" height="50" fill="#c9a45c" opacity="0.28"/>')
    o.append(f'<rect x="{dx+4}" y="{base-58}" width="48" height="46" fill="none" stroke="#c9a45c" stroke-opacity="0.4"/>')
ncol = 8
cw = 34
gap = (fx1 - fx0 - ncol * cw) / (ncol - 1)
for i in range(ncol):
    cx = fx0 + i * (cw + gap)
    o.append(f'<rect x="{cx-4:.1f}" y="{base-24}" width="{cw+8}" height="12" fill="#3a3630"/>')
    o.append(f'<rect x="{cx:.1f}" y="{ct+10}" width="{cw}" height="{base-24-ct-10}" fill="url(#col)"/>')
    for f in range(1, 4):
        o.append(f'<line x1="{cx+f*cw/4:.1f}" y1="{ct+12}" x2="{cx+f*cw/4:.1f}" y2="{base-26}" stroke="#000" stroke-opacity="0.35"/>')
    o.append(f'<rect x="{cx-5:.1f}" y="{ct}" width="{cw+10}" height="11" fill="#4a443a"/>')
# entablamento e frontão
o.append(f'<rect x="{fx0-20}" y="{ct-28}" width="{fx1-fx0+40}" height="28" fill="url(#stone)"/>')
o.append(f'<line x1="{fx0-20}" y1="{ct-28}" x2="{fx1+20}" y2="{ct-28}" stroke="#c9a45c" stroke-opacity="0.55" stroke-width="2"/>')
for k in range(0, fx1-fx0+40, 22):
    o.append(f'<rect x="{fx0-20+k+4}" y="{ct-12}" width="10" height="8" fill="#000" opacity="0.3"/>')
px = (fx0 + fx1) / 2
o.append(f'<polygon points="{fx0-34},{ct-28} {px},{ct-84} {fx1+34},{ct-28}" fill="#2e2b26" stroke="#c9a45c" stroke-opacity="0.6" stroke-width="2"/>')
o.append(f'<polygon points="{fx0+14},{ct-34} {px},{ct-74} {fx1-14},{ct-34}" fill="#1c1a16"/>')
# reflexo no chão molhado
o.append(f'<rect x="0" y="{base+10}" width="{W}" height="40" fill="#c9a45c" opacity="0.04"/>')

o.append(f'<rect width="{W}" height="140" fill="url(#topfade)"/>')
o.append(f'<rect width="{W}" height="{H}" fill="url(#fade)"/>')
o.append(f'<rect width="{W}" height="{H}" fill="url(#vign)"/>')
o.append('</svg>')
open("bg.svg", "w").write("\n".join(o))
print("bg.svg ok")
