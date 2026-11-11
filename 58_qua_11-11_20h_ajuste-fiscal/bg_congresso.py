"""Fundo 1080x1350: Congresso Nacional ao entardecer, com espelho d'água e
barras douradas decrescentes no céu (ajuste / corte de gastos)."""
import random, sys
from pathlib import Path
random.seed(11)
W, H = 1080, 1350
HZ = 410  # linha do platô
o = []
o.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
o.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0d131d"/><stop offset="0.18" stop-color="#151d2a"/>
 <stop offset="0.27" stop-color="#2a2a30"/><stop offset="0.305" stop-color="#5a4128"/>
 <stop offset="0.33" stop-color="#2b2118"/><stop offset="0.40" stop-color="#0c0c0c"/>
 <stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="sun" cx="0.5" cy="0.30" r="0.42">
 <stop offset="0" stop-color="#e0b56a" stop-opacity="0.38"/><stop offset="0.35" stop-color="#c9a45c" stop-opacity="0.12"/>
 <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="tower" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#1c222c"/><stop offset="0.5" stop-color="#2a313c"/><stop offset="1" stop-color="#14181f"/></linearGradient>
<linearGradient id="slab" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#2c3038"/><stop offset="1" stop-color="#15181d"/></linearGradient>
<linearGradient id="dome" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#3a3f48"/><stop offset="0.45" stop-color="#cfc7b8"/><stop offset="0.6" stop-color="#8d8a84"/><stop offset="1" stop-color="#22262d"/></linearGradient>
<linearGradient id="bowl" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#22262d"/><stop offset="0.4" stop-color="#9a958c"/><stop offset="0.55" stop-color="#d8cfbe"/><stop offset="1" stop-color="#2a2e35"/></linearGradient>
<linearGradient id="bar" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.55"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0.04"/></linearGradient>
<linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#1a1712"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.35"/><stop offset="0.13" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.315" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.37" stop-color="#0a0a0a" stop-opacity="0.8"/>
 <stop offset="0.42" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.3" r="0.8">
 <stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="5"/>
 <feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="table" tableValues="0 0.07"/></feComponentTransfer></filter>
<filter id="blur"><feGaussianBlur stdDeviation="2"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/>
<rect width="100%" height="100%" fill="url(#sun)"/>''')

# estrelas
for _ in range(70):
    x, y = random.uniform(0, W), random.uniform(0, 240)
    o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.choice([0.6,0.8,1.1])}" fill="#efe6d6" opacity="{random.uniform(.15,.5):.2f}"/>')

# barras douradas decrescentes no céu (despesa sendo contida)
bx0, bw, gap = 120, 46, 20
heights = [210, 198, 184, 171, 158, 145, 132, 120, 108, 97, 86, 76, 66]
for i, h in enumerate(heights):
    x = bx0 + i * (bw + gap)
    o.append(f'<rect x="{x}" y="{HZ-h-40}" width="{bw}" height="{h}" fill="url(#bar)" opacity="0.16"/>')
    o.append(f'<line x1="{x}" y1="{HZ-h-40}" x2="{x+bw}" y2="{HZ-h-40}" stroke="#c9a45c" stroke-width="2" opacity="0.4"/>')
# linha de tendência
pts = " ".join(f"{bx0 + i*(bw+gap) + bw/2:.0f},{HZ-h-40:.0f}" for i, h in enumerate(heights))
o.append(f'<polyline points="{pts}" fill="none" stroke="#e3c27e" stroke-width="2.5" opacity="0.65" stroke-dasharray="6 7"/>')

# horizonte distante (cerrado)
p = [(0, HZ)]
x = 0
while x < W:
    h = random.choice([4, 7, 10, 14, 6]); w = random.randint(30, 80)
    p += [(x, HZ - h), (x + w, HZ - h)]; x += w
p += [(W, HZ), (W, HZ + 40), (0, HZ + 40)]
o.append('<polygon fill="#0e0f12" points="' + " ".join(f"{a},{b}" for a, b in p) + '"/>')

# platô horizontal
o.append(f'<rect x="90" y="{HZ-38}" width="900" height="38" fill="url(#slab)"/>')
o.append(f'<line x1="90" y1="{HZ-38}" x2="990" y2="{HZ-38}" stroke="#c9a45c" stroke-opacity="0.45" stroke-width="1.5"/>')
for i in range(30):
    xx = 100 + i * 30
    o.append(f'<rect x="{xx}" y="{HZ-26}" width="16" height="10" fill="#c9a45c" opacity="{random.choice([0.08,0.15,0.25,0.4])}"/>')
# rampa
o.append(f'<polygon points="430,{HZ} 520,{HZ-38} 534,{HZ-38} 452,{HZ}" fill="#3a3d44" opacity="0.8"/>')

# cúpula (voltada para baixo, à esquerda) -> semiesfera sobre o platô
cx, r = 300, 84
o.append(f'<path d="M{cx-r},{HZ-38} A{r},{r*0.62} 0 0 1 {cx+r},{HZ-38} Z" fill="url(#dome)"/>')
o.append(f'<path d="M{cx-r},{HZ-38} A{r},{r*0.62} 0 0 1 {cx+r},{HZ-38}" fill="none" stroke="#efe6d6" stroke-opacity="0.35" stroke-width="1.5"/>')
# cúpula invertida (tigela, à direita)
cx2, r2 = 790, 112
o.append(f'<path d="M{cx2-r2},{HZ-98} A{r2},{r2*0.58} 0 0 0 {cx2+r2},{HZ-98} Z" fill="url(#bowl)"/>')
o.append(f'<ellipse cx="{cx2}" cy="{HZ-98}" rx="{r2}" ry="9" fill="#1a1d22" stroke="#efe6d6" stroke-opacity="0.4" stroke-width="1.5"/>')
o.append(f'<rect x="{cx2-14}" y="{HZ-52}" width="28" height="18" fill="#1a1d22"/>')

# torres gêmeas
tw, ttop = 52, 138
for tx in (480, 548):
    o.append(f'<rect x="{tx}" y="{ttop}" width="{tw}" height="{HZ-38-ttop}" fill="url(#tower)"/>')
    for yy in range(ttop + 10, HZ - 50, 13):
        for k in range(4):
            op = random.choice([0.05, 0.05, 0.1, 0.18, 0.5]) if random.random() < 0.9 else 0.85
            o.append(f'<rect x="{tx+5+k*12}" y="{yy}" width="8" height="6" fill="#d9b46a" opacity="{op}"/>')
    o.append(f'<line x1="{tx}" y1="{ttop}" x2="{tx}" y2="{HZ-38}" stroke="#c9a45c" stroke-opacity="0.35"/>')
# passarela entre as torres
for by in (ttop + 120, ttop + 220):
    o.append(f'<rect x="{480+tw}" y="{by}" width="{548-480-tw}" height="22" fill="#262b33" stroke="#c9a45c" stroke-opacity="0.3"/>')

# espelho d'água com reflexo
o.append(f'<rect x="0" y="{HZ}" width="{W}" height="120" fill="url(#water)"/>')
refl = []
for tx in (480, 548):
    refl.append(f'<rect x="{tx}" y="{HZ+4}" width="{tw}" height="90" fill="#c9a45c" opacity="0.10"/>')
refl.append(f'<path d="M{cx-r},{HZ+2} A{r},{r*0.5} 0 0 0 {cx+r},{HZ+2} Z" fill="#cfc7b8" opacity="0.08"/>')
o.append('<g filter="url(#blur)">' + "".join(refl) + '</g>')
for i in range(20):
    y = HZ + 8 + i * 5
    x1 = random.uniform(80, 700); L = random.uniform(40, 220)
    o.append(f'<line x1="{x1:.0f}" y1="{y}" x2="{x1+L:.0f}" y2="{y}" stroke="#c9a45c" stroke-opacity="{random.uniform(.05,.18):.2f}"/>')

o.append('<rect width="100%" height="100%" fill="url(#fade)"/>')
o.append('<rect width="100%" height="100%" fill="url(#vign)"/>')
o.append('<rect width="100%" height="100%" filter="url(#grain)"/>')
o.append('</svg>')
Path(sys.argv[1] if len(sys.argv) > 1 else "bg.svg").write_text("\n".join(o))
