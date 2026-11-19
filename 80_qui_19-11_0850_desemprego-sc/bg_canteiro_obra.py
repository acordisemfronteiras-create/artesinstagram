"""Fundo: canteiro de obra ao amanhecer (prédio em estrutura, grua içando viga,
trabalhadores genéricos em silhueta, colinas do Oeste ao fundo). Para emprego em SC."""
import random, sys
random.seed(19)
W, H = 1080, 1350
HZ = 430
s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0e151f"/><stop offset="0.18" stop-color="#18212c"/>
 <stop offset="0.27" stop-color="#2b2a29"/><stop offset="0.315" stop-color="#4a3923"/>
 <stop offset="0.34" stop-color="#141210"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="sun" cx="0.28" cy="0.315" r="0.40">
 <stop offset="0" stop-color="#e2b86a" stop-opacity="0.42"/><stop offset="0.35" stop-color="#c9a45c" stop-opacity="0.14"/>
 <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.30"/><stop offset="0.10" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.30" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.37" stop-color="#0a0a0a" stop-opacity="0.75"/>
 <stop offset="0.43" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.3" r="0.8"><stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
<linearGradient id="win" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e6c47e"/><stop offset="1" stop-color="#a9823f"/></linearGradient>
<filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="5"/>
 <feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="table" tableValues="0 0.07"/></feComponentTransfer></filter>
<filter id="blur"><feGaussianBlur stdDeviation="3"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/><rect width="100%" height="100%" fill="url(#sun)"/>''')

# estrelas tênues
for _ in range(60):
    x, y = random.uniform(0, W), random.uniform(0, 230)
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(.6,1.4):.1f}" fill="#d9cdb5" opacity="{random.uniform(.15,.45):.2f}"/>')

# colinas do Oeste (três planos)
def hills(base, amp, col, op, seed):
    random.seed(seed); pts = []; x = -20
    while x <= W + 40:
        pts.append((x, base - random.uniform(0, amp))); x += random.randint(60, 120)
    d = f'M -20 {HZ+80} L ' + ' '.join(f'{a:.0f} {b:.0f}' for a, b in pts) + f' L {W+40} {HZ+80} Z'
    s.append(f'<path d="{d}" fill="{col}" opacity="{op}"/>')
hills(HZ - 18, 34, '#2a2620', .9, 3)
hills(HZ - 4, 22, '#1b1916', 1, 4)
# araucárias distantes
random.seed(21)
for i in range(16):
    x = random.uniform(20, W - 20); b = HZ - random.uniform(4, 16); h = random.uniform(26, 44)
    s.append(f'<line x1="{x:.0f}" y1="{b:.0f}" x2="{x:.0f}" y2="{b-h:.0f}" stroke="#151412" stroke-width="2"/>')
    s.append(f'<path d="M {x-h*.45:.0f} {b-h+6:.0f} Q {x:.0f} {b-h-8:.0f} {x+h*.45:.0f} {b-h+6:.0f} Z" fill="#151412"/>')

# cidade ao fundo à esquerda (pequena)
random.seed(8); x = 40
while x < 300:
    w = random.randint(22, 44); h = random.randint(30, 90)
    s.append(f'<rect x="{x}" y="{HZ-h}" width="{w}" height="{h}" fill="#1a1917"/>')
    for wy in range(HZ - h + 8, HZ - 6, 12):
        for wx in range(x + 5, x + w - 5, 9):
            if random.random() < .25:
                s.append(f'<rect x="{wx}" y="{wy}" width="4" height="5" fill="#c9a45c" opacity="{random.uniform(.35,.8):.2f}"/>')
    x += w + random.randint(2, 10)

# prédio em construção (centro-direita)
bx, bw, floors, fh = 520, 300, 6, 36
top = HZ - floors * fh
# lajes concluídas (parte de baixo fechada) e estrutura acima
for f in range(floors):
    y = HZ - (f + 1) * fh
    closed = f < 3
    if closed:
        s.append(f'<rect x="{bx}" y="{y}" width="{bw}" height="{fh}" fill="#16171a"/>')
        random.seed(100 + f)
        for k in range(7):
            wx = bx + 12 + k * 41
            lit = random.random() < .6
            fill = 'url(#win)' if lit else '#23252a'
            s.append(f'<rect x="{wx}" y="{y+9}" width="28" height="20" fill="{fill}" opacity="{.85 if lit else 1}"/>')
    # laje
    s.append(f'<rect x="{bx-6}" y="{y-3}" width="{bw+12}" height="5" fill="#3a352d"/>')
    if not closed:
        for k in range(0, 7):
            px = bx + k * (bw / 6)
            s.append(f'<rect x="{px-3:.0f}" y="{y}" width="6" height="{fh}" fill="#2c2924"/>')
# andaimes (lado esquerdo do prédio)
for f in range(floors):
    y = HZ - (f + 1) * fh
    s.append(f'<line x1="{bx-26}" y1="{y}" x2="{bx-6}" y2="{y}" stroke="#7a6640" stroke-width="2" opacity=".8"/>')
    s.append(f'<line x1="{bx-26}" y1="{y}" x2="{bx-6}" y2="{y+fh}" stroke="#7a6640" stroke-width="1.2" opacity=".6"/>')
for xx in (bx - 26, bx - 6):
    s.append(f'<line x1="{xx}" y1="{top-3}" x2="{xx}" y2="{HZ}" stroke="#7a6640" stroke-width="2" opacity=".85"/>')
# vergalhões no topo
for k in range(7):
    px = bx + k * (bw / 6)
    s.append(f'<line x1="{px:.0f}" y1="{top-3}" x2="{px:.0f}" y2="{top-24}" stroke="#4a4337" stroke-width="2"/>')

# grua (torre à direita do prédio)
tx, tw = 880, 26
ttop = 170
s.append(f'<rect x="{tx}" y="{ttop}" width="{tw}" height="{HZ-ttop}" fill="none" stroke="#c9a45c" stroke-width="2.4"/>')
y = ttop
while y < HZ:
    s.append(f'<line x1="{tx}" y1="{y}" x2="{tx+tw}" y2="{y+tw}" stroke="#c9a45c" stroke-width="1.6" opacity=".9"/>')
    s.append(f'<line x1="{tx+tw}" y1="{y}" x2="{tx}" y2="{y+tw}" stroke="#c9a45c" stroke-width="1.0" opacity=".45"/>')
    y += tw
# lança e contralança
jy = ttop
jl, cl = 560, 130
s.append(f'<line x1="{tx-jl}" y1="{jy}" x2="{tx+tw+cl}" y2="{jy}" stroke="#c9a45c" stroke-width="3"/>')
s.append(f'<line x1="{tx-jl}" y1="{jy+16}" x2="{tx+tw+cl}" y2="{jy+16}" stroke="#c9a45c" stroke-width="2"/>')
xx = tx - jl
while xx < tx + tw + cl:
    s.append(f'<line x1="{xx}" y1="{jy}" x2="{xx+16}" y2="{jy+16}" stroke="#c9a45c" stroke-width="1.2" opacity=".8"/>')
    xx += 16
# topo (cabeça) e tirantes
s.append(f'<path d="M {tx} {ttop} L {tx+tw/2} {ttop-48} L {tx+tw} {ttop}" fill="none" stroke="#c9a45c" stroke-width="2.4"/>')
s.append(f'<line x1="{tx+tw/2}" y1="{ttop-48}" x2="{tx-jl+60}" y2="{jy}" stroke="#c9a45c" stroke-width="1.2" opacity=".75"/>')
s.append(f'<line x1="{tx+tw/2}" y1="{ttop-48}" x2="{tx+tw+cl-10}" y2="{jy}" stroke="#c9a45c" stroke-width="1.2" opacity=".75"/>')
# contrapeso
s.append(f'<rect x="{tx+tw+cl-58}" y="{jy+16}" width="50" height="30" fill="#2a2620" stroke="#c9a45c" stroke-width="1.5"/>')
# cabine
s.append(f'<rect x="{tx-18}" y="{jy+18}" width="22" height="20" fill="#1c1a17" stroke="#c9a45c" stroke-width="1.5"/>')
s.append(f'<rect x="{tx-15}" y="{jy+22}" width="14" height="9" fill="#e2bf78" opacity=".9"/>')
# luz de sinalização
s.append(f'<circle cx="{tx+tw/2}" cy="{ttop-50}" r="9" fill="#e6a85a" opacity=".35" filter="url(#blur)"/>')
s.append(f'<circle cx="{tx+tw/2}" cy="{ttop-50}" r="3.2" fill="#f0c47a"/>')
# carrinho, cabo e viga içada
cx = 400
s.append(f'<rect x="{cx-12}" y="{jy+14}" width="24" height="8" fill="#c9a45c"/>')
hook_y = 236
s.append(f'<line x1="{cx-4}" y1="{jy+22}" x2="{cx-4}" y2="{hook_y}" stroke="#bfa16a" stroke-width="1.2"/>')
s.append(f'<line x1="{cx+4}" y1="{jy+22}" x2="{cx+4}" y2="{hook_y}" stroke="#bfa16a" stroke-width="1.2"/>')
s.append(f'<path d="M {cx-6} {hook_y} h12 v8 q0 10 -8 10 q-6 0 -6 -6" fill="none" stroke="#c9a45c" stroke-width="2.4"/>')
s.append(f'<line x1="{cx}" y1="{hook_y+14}" x2="{cx-70}" y2="{hook_y+42}" stroke="#bfa16a" stroke-width="1.2"/>')
s.append(f'<line x1="{cx}" y1="{hook_y+14}" x2="{cx+70}" y2="{hook_y+42}" stroke="#bfa16a" stroke-width="1.2"/>')
s.append(f'<rect x="{cx-110}" y="{hook_y+42}" width="220" height="12" fill="#c9a45c"/>')
s.append(f'<rect x="{cx-110}" y="{hook_y+44}" width="220" height="3" fill="#ead39c" opacity=".8"/>')

# trabalhadores genéricos em silhueta (capacete)
def worker(x, yb, sc=1.0, flip=1):
    h = 30 * sc
    s.append(f'<g transform="translate({x},{yb}) scale({flip*sc},{sc})" fill="#0d0d0e">'
             '<rect x="-3.5" y="-30" width="7" height="14" rx="2"/>'
             '<rect x="-3" y="-16" width="2.6" height="16"/><rect x="0.6" y="-16" width="2.6" height="16"/>'
             '<rect x="3" y="-28" width="2.2" height="11" transform="rotate(-25 3 -28)"/>'
             '<circle cx="0" cy="-34" r="3.6"/>'
             '<path d="M -5 -35 Q 0 -42 5 -35 Z" fill="#c9a45c"/></g>')
y5 = HZ - 4 * fh - 3
worker(bx + 60, y5, 1.0, 1); worker(bx + 190, y5, 1.0, -1)
y7 = HZ - 5 * fh - 3
worker(bx + 120, y7, .95, 1)
yt = top - 3
worker(bx + 250, yt, .95, -1)
for xw, sc, fl in [(350, 1.1, 1), (392, 1.1, -1), (448, 1.05, 1)]:
    worker(xw, HZ + 2, sc, fl)

# chão e cerca do canteiro
s.append(f'<rect x="0" y="{HZ}" width="{W}" height="6" fill="#1f1c18"/>')
for xx in range(300, 1000, 22):
    s.append(f'<line x1="{xx}" y1="{HZ+6}" x2="{xx}" y2="{HZ-14}" stroke="#2c2823" stroke-width="2"/>')
s.append(f'<line x1="300" y1="{HZ-12}" x2="1000" y2="{HZ-12}" stroke="#2c2823" stroke-width="2"/>')

# poeira dourada no ar
random.seed(33)
for _ in range(70):
    x, y = random.uniform(300, 1000), random.uniform(150, HZ)
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(.6,1.6):.1f}" fill="#e2bf78" opacity="{random.uniform(.1,.35):.2f}"/>')

s.append('<rect width="100%" height="100%" fill="url(#fade)"/><rect width="100%" height="100%" fill="url(#vign)"/>')
s.append('<rect width="100%" height="100%" filter="url(#grain)"/></svg>')
open(sys.argv[1] if len(sys.argv) > 1 else 'bg.svg', 'w').write('\n'.join(s))
