"""Fundo: panorama da atividade econômica (indústria, cidade, rodovia, campo)
com a linha de um índice mensal desenhada no céu. Para o IBC-Br."""
import random, sys
random.seed(16)
W, H = 1080, 1350
HZ = 440  # horizonte

s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0f1620"/><stop offset="0.20" stop-color="#18212d"/>
 <stop offset="0.30" stop-color="#2a2a2b"/><stop offset="0.335" stop-color="#3e3122"/>
 <stop offset="0.36" stop-color="#121110"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="sun" cx="0.62" cy="0.33" r="0.42">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.30"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="line" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.15"/><stop offset="0.6" stop-color="#c9a45c" stop-opacity="0.7"/>
 <stop offset="1" stop-color="#e2c47f" stop-opacity="1"/></linearGradient>
<linearGradient id="area" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.16"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.35"/><stop offset="0.12" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.33" stop-color="#0a0a0a" stop-opacity="0.08"/><stop offset="0.41" stop-color="#0a0a0a" stop-opacity="0.85"/>
 <stop offset="0.46" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.3" r="0.8">
 <stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
<filter id="grain" x="0" y="0" width="100%" height="100%">
 <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="5"/><feColorMatrix type="saturate" values="0"/>
 <feComponentTransfer><feFuncA type="table" tableValues="0 0.07"/></feComponentTransfer></filter>
<filter id="blur" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="9"/></filter>
<filter id="glowf"><feGaussianBlur stdDeviation="3"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/>
<rect width="100%" height="100%" fill="url(#sun)"/>''')

# grade fina no céu (papel de gráfico)
for y in range(150, HZ - 40, 46):
    s.append(f'<line x1="60" y1="{y}" x2="1020" y2="{y}" stroke="#c9a45c" stroke-opacity="0.05" stroke-width="1"/>')
for x in range(60, 1021, 80):
    s.append(f'<line x1="{x}" y1="140" x2="{x}" y2="{HZ-50}" stroke="#c9a45c" stroke-opacity="0.035" stroke-width="1"/>')

# linha do índice (série mensal estilizada, sem dados reais)
vals = [0.42,0.52,0.48,0.60,0.68,0.64,0.74,0.82,0.78,0.70,0.74,0.66,0.58]
x0, x1, ytop, ybot = 70, 1010, 175, 330
pts = []
for i, v in enumerate(vals):
    x = x0 + (x1 - x0) * i / (len(vals) - 1)
    y = ybot - (ybot - ytop) * v
    pts.append((x, y))
d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)
s.append(f'<path d="{d} L{x1},{HZ-50} L{x0},{HZ-50} Z" fill="url(#area)"/>')
s.append(f'<path d="{d}" fill="none" stroke="#c9a45c" stroke-width="7" stroke-opacity="0.25" filter="url(#glowf)"/>')
s.append(f'<path d="{d}" fill="none" stroke="url(#line)" stroke-width="2.6" stroke-linejoin="round"/>')
for i, (x, y) in enumerate(pts):
    last = i == len(pts) - 1
    r = 6 if last else 3
    op = 1 if last else 0.35 + 0.5 * i / len(pts)
    if last:
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="16" fill="#c9a45c" fill-opacity="0.18"/>')
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#0f1620" stroke="#c9a45c" stroke-opacity="{op:.2f}" stroke-width="2"/>')

# colinas ao fundo
s.append(f'<path d="M0,{HZ-30} C160,{HZ-62} 300,{HZ-40} 420,{HZ-52} C560,{HZ-66} 700,{HZ-38} 840,{HZ-56} C940,{HZ-66} 1010,{HZ-48} 1080,{HZ-54} L1080,{HZ+40} L0,{HZ+40} Z" fill="#14161a"/>')

# cidade (centro-direita)
bx = 560
while bx < 900:
    w = random.randint(26, 52); h = random.randint(50, 150)
    s.append(f'<rect x="{bx}" y="{HZ-h}" width="{w}" height="{h+20}" fill="#101318" stroke="#1d222a" stroke-width="1"/>')
    for wy in range(HZ - h + 10, HZ - 6, 13):
        for wx in range(bx + 5, bx + w - 6, 9):
            if random.random() < 0.18:
                s.append(f'<rect x="{wx}" y="{wy}" width="4" height="6" fill="#c9a45c" fill-opacity="{random.uniform(0.35,0.85):.2f}"/>')
    bx += w + random.randint(2, 8)

# fábrica (esquerda)
fx = 110
s.append(f'<path d="M{fx},{HZ} L{fx},{HZ-70} L{fx+50},{HZ-100} L{fx+50},{HZ-70} L{fx+100},{HZ-100} L{fx+100},{HZ-70} L{fx+150},{HZ-100} L{fx+150},{HZ-70} L{fx+200},{HZ-100} L{fx+200},{HZ} Z" fill="#111317" stroke="#22262d" stroke-width="1.2"/>')
for i, (cx, ch) in enumerate([(fx+225, 175), (fx+258, 145)]):
    s.append(f'<rect x="{cx}" y="{HZ-ch}" width="18" height="{ch}" fill="#121418" stroke="#22262d"/>')
    s.append(f'<rect x="{cx}" y="{HZ-ch+14}" width="18" height="4" fill="#c9a45c" fill-opacity="0.35"/>')
    pass
for wx in range(fx + 14, fx + 196, 26):
    s.append(f'<rect x="{wx}" y="{HZ-52}" width="12" height="16" fill="#c9a45c" fill-opacity="0.45"/>')

# silos (entre fábrica e cidade)
for i, sx in enumerate([420, 462]):
    sh = 110 - i * 16
    s.append(f'<rect x="{sx}" y="{HZ-sh}" width="34" height="{sh}" fill="#13151a" stroke="#262a31"/>')
    s.append(f'<path d="M{sx},{HZ-sh} Q{sx+17},{HZ-sh-20} {sx+34},{HZ-sh} Z" fill="#171a20" stroke="#262a31"/>')
    for ry in range(HZ - sh + 12, HZ, 14):
        s.append(f'<line x1="{sx}" y1="{ry}" x2="{sx+34}" y2="{ry}" stroke="#262a31" stroke-width="1"/>')
s.append(f'<rect x="503" y="{HZ-128}" width="10" height="128" fill="#15181d"/><line x1="508" y1="{HZ-128}" x2="440" y2="{HZ-92}" stroke="#262a31" stroke-width="3"/>')

# guindaste de porto (direita)
cx = 950
s.append(f'<path d="M{cx},{HZ} L{cx+8},{HZ-150} L{cx+20},{HZ-150} L{cx+28},{HZ} Z" fill="#14171c" stroke="#262a31"/>')
s.append(f'<line x1="{cx-110}" y1="{HZ-150}" x2="{cx+70}" y2="{HZ-150}" stroke="#2a2f37" stroke-width="7"/>')
s.append(f'<line x1="{cx+14}" y1="{HZ-190}" x2="{cx-110}" y2="{HZ-152}" stroke="#2a2f37" stroke-width="2"/><line x1="{cx+14}" y1="{HZ-190}" x2="{cx+70}" y2="{HZ-152}" stroke="#2a2f37" stroke-width="2"/>')
s.append(f'<line x1="{cx-60}" y1="{HZ-150}" x2="{cx-60}" y2="{HZ-90}" stroke="#2a2f37" stroke-width="1.5"/><rect x="{cx-72}" y="{HZ-90}" width="24" height="12" fill="#c9a45c" fill-opacity="0.55"/>')
s.append(f'<circle cx="{cx+14}" cy="{HZ-192}" r="3" fill="#c9a45c"/>')

# rodovia em primeiro plano com rastros de luz
s.append(f'<path d="M0,{HZ+6} L1080,{HZ-8} L1080,{HZ+20} L0,{HZ+34} Z" fill="#0e0f11"/>')
for k in range(9):
    x = random.randint(0, 1000); L = random.randint(50, 140)
    y = HZ + 20 - 14 * x / 1080 + random.choice([-5, 4])
    col = '#c9a45c' if k % 3 else '#b8503c'
    s.append(f'<line x1="{x}" y1="{y:.1f}" x2="{x+L}" y2="{y-14*L/1080:.1f}" stroke="{col}" stroke-opacity="{random.uniform(0.35,0.7):.2f}" stroke-width="2" stroke-linecap="round"/>')

# campo/lavoura em fileiras abaixo
for k in range(6):
    y = HZ + 44 + k * 14
    s.append(f'<path d="M0,{y} Q540,{y-10} 1080,{y}" stroke="#1d1a14" stroke-opacity="{0.9-k*0.13:.2f}" stroke-width="2" fill="none"/>')

s.append('<rect width="100%" height="100%" fill="url(#fade)"/>')
s.append('<rect width="100%" height="100%" fill="url(#vign)"/>')
s.append('<rect width="100%" height="100%" filter="url(#grain)"/>')
s.append('</svg>')
out = sys.argv[1] if len(sys.argv) > 1 else 'bg.svg'
open(out, 'w').write('\n'.join(s))
print('ok', out)
