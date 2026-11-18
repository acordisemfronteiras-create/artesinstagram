"""Fundo: sala de reuniões do comitê de juros americano ao anoitecer.
Mesa longa em perspectiva com 12 cadeiras (12 votos), duas destacadas em dourado
(os dois votos por alta), a ata sobre a mesa e, pela janela, uma cúpula genérica."""
import random
from pathlib import Path
random.seed(29)
W, H = 1080, 1350
VX, VY = 540, 236          # ponto de fuga
o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
o.append('''<defs>
<linearGradient id="wall" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#121820"/><stop offset="0.25" stop-color="#18202a"/><stop offset="0.42" stop-color="#14161a"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<linearGradient id="dusk" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#1b2a3d"/><stop offset="0.55" stop-color="#3b3a3c"/><stop offset="0.85" stop-color="#7a5a32"/><stop offset="1" stop-color="#a87a3e"/></linearGradient>
<linearGradient id="table" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#3a2a1a"/><stop offset="0.5" stop-color="#2a1e14"/><stop offset="1" stop-color="#140f0b"/></linearGradient>
<linearGradient id="refl" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.35"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></linearGradient>
<linearGradient id="chair" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#26272b"/><stop offset="1" stop-color="#16171a"/></linearGradient>
<linearGradient id="chairG" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#d9b56a"/><stop offset="1" stop-color="#7a5a26"/></linearGradient>
<linearGradient id="floor" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#1a1714"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="lamp" cx="0.5" cy="0.5" r="0.5">
 <stop offset="0" stop-color="#f0d08a" stop-opacity="0.55"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<radialGradient id="winglow" cx="0.5" cy="0.6" r="0.6">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.20"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.30"/><stop offset="0.10" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.29" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.335" stop-color="#0a0a0a" stop-opacity="0.55"/>
 <stop offset="0.37" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.25" r="0.75">
 <stop offset="0.5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.65"/></radialGradient>
<filter id="blur"><feGaussianBlur stdDeviation="5"/></filter>
<filter id="blur2"><feGaussianBlur stdDeviation="14"/></filter>
<clipPath id="win"><path d="M330,300 L330,215 Q330,150 395,150 L685,150 Q750,150 750,215 L750,300 Z"/></clipPath>
</defs>''')
o.append(f'<rect width="{W}" height="{H}" fill="url(#wall)"/>')
# lambris na parede de fundo (painéis verticais)
for x in range(60, 1030, 90):
    o.append(f'<rect x="{x}" y="70" width="70" height="230" rx="2" fill="none" stroke="#c9a45c" stroke-opacity="0.06"/>')
# paredes laterais em perspectiva
o.append(f'<path d="M0,0 L250,70 L250,300 L0,470 Z" fill="#0d1116" opacity="0.85"/>')
o.append(f'<path d="M1080,0 L830,70 L830,300 L1080,470 Z" fill="#0d1116" opacity="0.85"/>')
for i in range(5):  # frisos nas paredes laterais
    t = i / 5
    xl = 250 * (1 - t) ; o.append(f'<line x1="{250-250*t:.0f}" y1="{70-70*t:.0f}" x2="{250-250*t:.0f}" y2="{300+260*t:.0f}" stroke="#c9a45c" stroke-opacity="0.05"/>')
    o.append(f'<line x1="{830+250*t:.0f}" y1="{70-70*t:.0f}" x2="{830+250*t:.0f}" y2="{300+260*t:.0f}" stroke="#c9a45c" stroke-opacity="0.05"/>')
# janela em arco com céu de fim de tarde e cúpula genérica
o.append('<g clip-path="url(#win)">')
o.append('<rect x="330" y="146" width="420" height="160" fill="url(#dusk)"/>')
for _ in range(25):
    o.append(f'<circle cx="{random.uniform(335,745):.0f}" cy="{random.uniform(156,200):.0f}" r="{random.uniform(.5,1.2):.1f}" fill="#efe6d6" opacity="{random.uniform(.2,.6):.2f}"/>')
# cúpula
o.append('<path d="M470,300 L470,262 L490,262 L490,250 Q540,200 590,250 L590,262 L610,262 L610,300 Z" fill="#141a22"/>')
o.append('<rect x="534" y="196" width="12" height="16" fill="#141a22"/><circle cx="540" cy="194" r="4" fill="#141a22"/>')
for cx in range(478, 606, 12):
    o.append(f'<rect x="{cx}" y="266" width="4" height="34" fill="#c9a45c" opacity="0.18"/>')
# horizonte da cidade
x = 330
while x < 750:
    w = random.randint(18, 42); h = random.randint(14, 46)
    if 462 < x < 612: x += w; continue
    o.append(f'<rect x="{x}" y="{300-h}" width="{w}" height="{h}" fill="#10151c"/>')
    for wy in range(300-h+6, 296, 9):
        for wx in range(x+4, x+w-4, 8):
            if random.random() < .18:
                o.append(f'<rect x="{wx}" y="{wy}" width="3" height="4" fill="#e8c27a" opacity="0.55"/>')
    x += w
o.append('</g>')
# caixilhos da janela
o.append('<path d="M330,300 L330,215 Q330,150 395,150 L685,150 Q750,150 750,215 L750,300 Z" fill="none" stroke="#3a3328" stroke-width="10"/>')
o.append('<path d="M330,300 L330,215 Q330,150 395,150 L685,150 Q750,150 750,215 L750,300 Z" fill="none" stroke="#c9a45c" stroke-opacity="0.35" stroke-width="2"/>')
for xm in (470, 610):
    o.append(f'<line x1="{xm}" y1="152" x2="{xm}" y2="300" stroke="#3a3328" stroke-width="6"/>')
o.append('<line x1="330" y1="222" x2="750" y2="222" stroke="#3a3328" stroke-width="5"/>')
o.append('<rect x="320" y="298" width="440" height="10" fill="#2a251e"/>')
o.append('<ellipse cx="540" cy="240" rx="330" ry="160" fill="url(#winglow)"/>')
# piso
o.append('<path d="M0,560 L250,300 L830,300 L1080,470 Z" fill="url(#floor)"/>')
# mesa em perspectiva: topo de y=322 (fundo) a y=520 (frente)
def edge(y):
    """meia-largura da mesa na profundidade y"""
    t = (y - 322) / (430 - 322)
    return 120 + t * 300
yb, yf = 322, 430
o.append(f'<path d="M{540-edge(yb):.0f},{yb} L{540+edge(yb):.0f},{yb} L{540+edge(yf):.0f},{yf} L{540-edge(yf):.0f},{yf} Z" fill="url(#table)"/>')
o.append(f'<path d="M{540-edge(yf):.0f},{yf} L{540+edge(yf):.0f},{yf} L{540+edge(yf):.0f},{yf+22} L{540-edge(yf):.0f},{yf+22} Z" fill="#0f0b08"/>')
# reflexo da janela na mesa
o.append(f'<path d="M470,{yb} L610,{yb} L650,{yf} L430,{yf} Z" fill="url(#refl)" opacity="0.7"/>')
o.append(f'<line x1="{540-edge(yb):.0f}" y1="{yb}" x2="{540+edge(yb):.0f}" y2="{yb}" stroke="#c9a45c" stroke-opacity="0.4" stroke-width="1.5"/>')
# cadeiras: 6 por lado; duas em dourado (votos por alta)
gold = {(0, 3), (1, 4)}
rows = [334, 348, 364, 383, 405, 431]
for side in (0, 1):
    for i, y in enumerate(rows):
        s = 0.42 + (y - 322) / 108 * 0.75
        cw, ch = 46 * s, 86 * s
        ex = edge(y) + 18 * s
        cx = 540 - ex - cw if side == 0 else 540 + ex
        fill = "url(#chairG)" if (side, i) in gold else "url(#chair)"
        if (side, i) in gold:
            o.append(f'<ellipse cx="{cx+cw/2:.1f}" cy="{y-ch*0.45:.1f}" rx="{cw*1.3:.1f}" ry="{ch*0.8:.1f}" fill="#c9a45c" opacity="0.18" filter="url(#blur2)"/>')
        o.append(f'<rect x="{cx:.1f}" y="{y-ch:.1f}" width="{cw:.1f}" height="{ch:.1f}" rx="{8*s:.1f}" fill="{fill}" stroke="#000" stroke-opacity="0.4"/>')
        o.append(f'<rect x="{cx+cw*0.12:.1f}" y="{y-ch*0.92:.1f}" width="{cw*0.76:.1f}" height="{ch*0.5:.1f}" rx="{6*s:.1f}" fill="#fff" opacity="0.04"/>')
# a ata sobre a mesa (papéis em perspectiva, perto da frente)
def page(x0, y0, w, h, sk, fill, op):
    return f'<path d="M{x0},{y0} L{x0+w},{y0} L{x0+w+sk},{y0+h} L{x0-sk},{y0+h} Z" fill="{fill}" opacity="{op}"/>'
o.append(page(488, 392, 108, 44, 14, "#000", 0.35).replace('M488', 'M494'))
o.append(page(480, 386, 108, 44, 14, "#cfc4b0", 0.92))
o.append(page(486, 382, 104, 42, 13, "#e9e0cf", 1))
for k in range(6):
    yy = 389 + k * 5.6
    o.append(f'<line x1="{482+k*1.6:.1f}" y1="{yy:.1f}" x2="{575+k*2.2 - (30 if k==5 else 0):.1f}" y2="{yy:.1f}" stroke="#6b6152" stroke-width="1.4" opacity="0.8"/>')
o.append('<rect x="492" y="383" width="38" height="3" fill="#c9a45c"/>')
# caneta dourada
o.append('<line x1="606" y1="410" x2="650" y2="392" stroke="#c9a45c" stroke-width="4" stroke-linecap="round"/>')
# luminárias pendentes
for lx, ly, r in ((380, 132, 60), (540, 120, 70), (700, 132, 60)):
    o.append(f'<line x1="{lx}" y1="0" x2="{lx}" y2="{ly-8}" stroke="#3a3328" stroke-width="2"/>')
    o.append(f'<ellipse cx="{lx}" cy="{ly+40}" rx="{r*1.8}" ry="{r}" fill="url(#lamp)" opacity="0.6"/>')
    o.append(f'<path d="M{lx-26},{ly+6} Q{lx},{ly-14} {lx+26},{ly+6} Z" fill="#c9a45c" opacity="0.85"/>')
    o.append(f'<ellipse cx="{lx}" cy="{ly+6}" rx="26" ry="4" fill="#f5dc9c"/>')
o.append(f'<rect width="{W}" height="{H}" fill="url(#vign)"/>')
o.append(f'<rect width="{W}" height="{H}" fill="url(#fade)"/>')
o.append('</svg>')
Path(__file__).with_name("bg.svg").write_text("\n".join(o))
print("bg.svg ok")
