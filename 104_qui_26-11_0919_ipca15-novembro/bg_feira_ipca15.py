"""Fundo: feira de rua ao amanhecer, barracas com toldos listrados, caixotes de hortifrúti,
lousas de preço com valores genéricos e, no céu, a linha do IPCA-15 em 12 meses tocando a faixa do teto da meta."""
import random, sys
from pathlib import Path

random.seed(2611)
W, H = 1080, 1350
HZ = 430  # chão da feira

s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
 <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#0f141c"/><stop offset="0.20" stop-color="#18202b"/>
  <stop offset="0.29" stop-color="#2a2620"/><stop offset="0.33" stop-color="#1a1714"/>
  <stop offset="0.45" stop-color="#0b0b0b"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
 <radialGradient id="sun" cx="0.5" cy="0.30" r="0.45">
  <stop offset="0" stop-color="#c9a45c" stop-opacity="0.22"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
 <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.40"/><stop offset="0.12" stop-color="#0a0a0a" stop-opacity="0"/>
  <stop offset="0.28" stop-color="#0a0a0a" stop-opacity="0.04"/><stop offset="0.36" stop-color="#0a0a0a" stop-opacity="0.70"/>
  <stop offset="0.42" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
 <radialGradient id="vign" cx="0.5" cy="0.28" r="0.8">
  <stop offset="0.5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.7"/></radialGradient>
 <radialGradient id="lamp" cx="0.5" cy="0" r="1">
  <stop offset="0" stop-color="#e8c27a" stop-opacity="0.16"/><stop offset="1" stop-color="#e8c27a" stop-opacity="0"/></radialGradient>
</defs>''')
s.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
s.append(f'<rect width="{W}" height="620" fill="url(#sun)"/>')

# estrelas discretas
for _ in range(40):
    x, y = random.uniform(0, W), random.uniform(20, 200)
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(.6,1.4):.1f}" fill="#d8d2c4" opacity="{random.uniform(.15,.45):.2f}"/>')

# linha do IPCA-15 em 12 meses (estilizada) e faixa do teto
cx0, cx1, cy_teto = 150, 930, 150
s.append(f'<line x1="{cx0}" y1="{cy_teto}" x2="{cx1}" y2="{cy_teto}" stroke="#c9a45c" stroke-width="1.5" stroke-dasharray="8 8" opacity="0.55"/>')
s.append(f'<text x="{cx0}" y="{cy_teto-12}" text-anchor="start" font-family="Inter,sans-serif" font-size="15" letter-spacing="3" fill="#c9a45c" opacity="0.7">TETO DA META</text>')
pts = [(150,250),(215,235),(280,228),(345,212),(410,196),(475,186),(540,172),(605,168),(670,160),(735,154),(800,147),(865,144),(930,138)]
d = "M" + " L".join(f"{x},{y}" for x, y in pts)
s.append(f'<path d="{d}" fill="none" stroke="#c9a45c" stroke-width="3" opacity="0.85" stroke-linejoin="round"/>')
s.append(f'<path d="{d} L930,300 L150,300 Z" fill="#c9a45c" opacity="0.05"/>')
s.append(f'<circle cx="930" cy="138" r="7" fill="#c9a45c"/><circle cx="930" cy="138" r="16" fill="#c9a45c" opacity="0.18"/>')

# prédios ao fundo (silhueta)
x = -10
while x < W:
    w = random.randint(50, 110); h = random.randint(40, 120)
    s.append(f'<rect x="{x}" y="{HZ-110-h}" width="{w}" height="{h+20}" fill="#12161c"/>')
    for wy in range(HZ-100-h, HZ-100, 16):
        for wx in range(x+8, x+w-8, 14):
            if random.random() < .12:
                s.append(f'<rect x="{wx}" y="{wy}" width="5" height="7" fill="#c9a45c" opacity="{random.uniform(.25,.6):.2f}"/>')
    x += w + random.randint(2, 10)

# chão
s.append(f'<rect x="0" y="{HZ-95}" width="{W}" height="{H}" fill="#121110"/>')

def barraca(x0, w, top, stripes, seed):
    r = random.Random(seed)
    base = HZ - 10
    roof_y = top; roof_h = 46
    # postes
    for px in (x0+6, x0+w-10):
        s.append(f'<rect x="{px}" y="{roof_y}" width="5" height="{base-roof_y}" fill="#2b2620"/>')
    # luz pendurada
    s.append(f'<ellipse cx="{x0+w/2}" cy="{roof_y+roof_h+40}" rx="{w*0.55}" ry="70" fill="url(#lamp)"/>')
    s.append(f'<line x1="{x0+w/2}" y1="{roof_y+roof_h}" x2="{x0+w/2}" y2="{roof_y+roof_h+18}" stroke="#3a332a" stroke-width="1.5"/>')
    s.append(f'<circle cx="{x0+w/2}" cy="{roof_y+roof_h+22}" r="5" fill="#f0d08a"/>')
    # toldo listrado
    sw = w / stripes
    for i in range(stripes):
        col = "#2c3542" if i % 2 == 0 else "#4a3c26"
        s.append(f'<path d="M{x0+i*sw:.1f},{roof_y} L{x0+(i+1)*sw:.1f},{roof_y} L{x0+(i+1)*sw:.1f},{roof_y+roof_h} '
                 f'Q{x0+(i+.5)*sw:.1f},{roof_y+roof_h+14} {x0+i*sw:.1f},{roof_y+roof_h} Z" fill="{col}"/>')
    s.append(f'<rect x="{x0-4}" y="{roof_y-6}" width="{w+8}" height="8" fill="#1d1a16"/>')
    # bancada
    bt = base - 62
    s.append(f'<rect x="{x0}" y="{bt}" width="{w}" height="62" fill="#1c1916"/>')
    s.append(f'<rect x="{x0}" y="{bt}" width="{w}" height="4" fill="#3a3128"/>')
    # caixotes com frutas/legumes
    cw = 52; n = int((w-10)//(cw+6))
    pal = [("#8a3b2a","#a8503a"),("#a87a2a","#c99a3c"),("#3e5a2a","#55783a"),("#7a5a2a","#9a7438"),("#5a2a30","#7a3a40")]
    for i in range(n):
        cx = x0 + 8 + i*(cw+6); cy = bt - 22
        c1, c2 = r.choice(pal)
        for k in range(9):
            fx = cx + 8 + (k % 5)*9 + r.uniform(-2,2); fy = cy + 4 - (k//5)*8 + r.uniform(-2,2)
            s.append(f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="{r.uniform(5,7):.1f}" fill="{r.choice([c1,c2])}" opacity="0.92"/>')
        s.append(f'<rect x="{cx}" y="{cy+2}" width="{cw}" height="22" fill="#2e2720"/>')
        s.append(f'<line x1="{cx}" y1="{cy+12}" x2="{cx+cw}" y2="{cy+12}" stroke="#1c1814" stroke-width="2"/>')
        # plaquinha de preço
        if r.random() < .6:
            s.append(f'<rect x="{cx+10}" y="{cy-26}" width="30" height="16" fill="#e9e1cf" opacity="0.85"/>')
            s.append(f'<line x1="{cx+25}" y1="{cy-10}" x2="{cx+25}" y2="{cy+2}" stroke="#6a5f50" stroke-width="1.5"/>')
            s.append(f'<rect x="{cx+14}" y="{cy-21}" width="{r.randint(10,20)}" height="3" fill="#2a2520"/>')
            s.append(f'<rect x="{cx+14}" y="{cy-15}" width="{r.randint(8,16)}" height="2" fill="#8a3b2a"/>')
    # lousa de preços
    lx = x0 + w/2 - 46; ly = roof_y + roof_h + 34
    s.append(f'<rect x="{lx}" y="{ly}" width="92" height="64" fill="#1a2420" stroke="#5a4a30" stroke-width="3"/>')
    for j in range(4):
        s.append(f'<rect x="{lx+10}" y="{ly+12+j*12}" width="{r.randint(30,46)}" height="2.5" fill="#d8d2c4" opacity="0.7"/>')
        s.append(f'<rect x="{lx+62}" y="{ly+11+j*12}" width="20" height="3" fill="#c9a45c" opacity="0.9"/>')

barraca(20, 300, 228, 8, 1)
barraca(392, 296, 214, 8, 2)
barraca(760, 300, 232, 8, 3)

# chão com reflexo e caixotes empilhados
s.append(f'<rect x="0" y="{HZ-10}" width="{W}" height="2" fill="#3a3128" opacity="0.6"/>')
for bx in (340, 712):
    for k in range(3):
        s.append(f'<rect x="{bx}" y="{HZ-30-k*22}" width="38" height="20" fill="#2a241e" stroke="#16130f"/>')

s.append(f'<rect width="{W}" height="{H}" fill="url(#fade)"/>')
s.append(f'<rect width="{W}" height="{H}" fill="url(#vign)"/>')
s.append(f'<rect x="0" y="560" width="{W}" height="{H-560}" fill="#0a0a0a"/>')
s.append('</svg>')
Path(sys.argv[1] if len(sys.argv) > 1 else "bg.svg").write_text("\n".join(s))
