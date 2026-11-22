"""Fundo: globo dividido (sem consenso) entre turbinas eólicas e cavalos de petróleo."""
import math, random
random.seed(31)
W, H = 1080, 1350
HZ = 430  # horizonte
s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0f1620"/><stop offset="0.22" stop-color="#18212d"/>
 <stop offset="0.31" stop-color="#2b2a28"/><stop offset="0.335" stop-color="#4a3a24"/>
 <stop offset="0.36" stop-color="#0e0e0e"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="halo" cx="0.5" cy="0.19" r="0.32">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.20"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<radialGradient id="gL" cx="0.35" cy="0.35" r="0.8">
 <stop offset="0" stop-color="#2c4a52"/><stop offset="0.6" stop-color="#15262c"/><stop offset="1" stop-color="#0a1215"/></radialGradient>
<radialGradient id="gR" cx="0.65" cy="0.35" r="0.8">
 <stop offset="0" stop-color="#5a4426"/><stop offset="0.6" stop-color="#2c2114"/><stop offset="1" stop-color="#140f09"/></radialGradient>
<clipPath id="cL"><path d="M0 0 H538 L530 60 L546 120 L528 180 L548 240 L532 300 L544 360 L536 460 H0Z"/></clipPath>
<clipPath id="cR"><path d="M1080 0 H550 L542 60 L558 120 L540 180 L560 240 L544 300 L556 360 L548 460 H1080Z"/></clipPath>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.35"/><stop offset="0.12" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.31" stop-color="#0a0a0a" stop-opacity="0.05"/><stop offset="0.40" stop-color="#0a0a0a" stop-opacity="0.8"/>
 <stop offset="0.46" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.25" r="0.8">
 <stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
</defs>''')
s.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
# estrelas
for _ in range(90):
    x, y = random.uniform(0, W), random.uniform(0, 330)
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(.5,1.4):.1f}" fill="#efe6d6" opacity="{random.uniform(.15,.5):.2f}"/>')
s.append(f'<rect width="{W}" height="{H}" fill="url(#halo)"/>')

# globo
cx, cy, R = 544, 272, 136
def globe(side, grad, shift):
    g = [f'<g clip-path="url(#c{side})" transform="translate({shift},0)">']
    g.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#{grad})"/>')
    # paralelos
    for lat in range(-60, 90, 30):
        yy = cy - R * math.sin(math.radians(lat)); rx = R * math.cos(math.radians(lat))
        g.append(f'<ellipse cx="{cx}" cy="{yy:.1f}" rx="{rx:.1f}" ry="{rx*0.16:.1f}" fill="none" stroke="#c9a45c" stroke-opacity="0.32" stroke-width="1.2"/>')
    # meridianos
    for lon in range(-75, 90, 25):
        rx = abs(R * math.sin(math.radians(lon)))
        g.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx:.1f}" ry="{R}" fill="none" stroke="#c9a45c" stroke-opacity="0.30" stroke-width="1.2"/>')
    # continentes estilizados (manchas)
    blobs = [(-52,-26,38,26),(-18,34,30,19),(34,-8,44,29),(60,34,26,17),(-78,52,24,15),(8,-60,34,15)]
    for bx, by, rw, rh in blobs:
        g.append(f'<ellipse cx="{cx+bx}" cy="{cy+by}" rx="{rw}" ry="{rh}" fill="#c9a45c" opacity="0.12" transform="rotate({bx/3:.0f} {cx+bx} {cy+by})"/>')
    g.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#c9a45c" stroke-opacity="0.75" stroke-width="2.2"/>')
    g.append('</g>')
    return "".join(g)
s.append(globe("L", "gL", -10))
s.append(globe("R", "gR", 10))
# linha da fratura (brilho)
s.append('<path d="M538 136 L530 160 L546 160 L528 200 L548 250 L532 300 L544 350 L536 410" fill="none" stroke="#c9a45c" stroke-opacity="0.55" stroke-width="1.5" transform="translate(4,0)"/>')
# órbita / anel de negociação
s.append(f'<ellipse cx="{cx}" cy="{cy+8}" rx="230" ry="42" fill="none" stroke="#c9a45c" stroke-opacity="0.35" stroke-width="1.4" stroke-dasharray="3 9"/>')
for i in range(28):
    a = 2*math.pi*i/28
    x = cx + 230*math.cos(a); y = cy + 8 + 42*math.sin(a)
    if math.sin(a) < 0 and abs(x-cx) < R-10: continue  # atrás do globo
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.2" fill="#c9a45c" opacity="0.7"/>')

# solo
s.append(f'<path d="M0 {HZ} Q270 {HZ-8} 540 {HZ} T1080 {HZ-4} V{H} H0Z" fill="#0d0d0c"/>')
s.append(f'<line x1="0" y1="{HZ}" x2="{W}" y2="{HZ-3}" stroke="#c9a45c" stroke-opacity="0.35" stroke-width="1"/>')

# turbinas eólicas (esquerda)
def turbine(x, base, h, ang, op):
    t = [f'<g opacity="{op}">']
    t.append(f'<path d="M{x-4} {base} L{x-1.5} {base-h} L{x+1.5} {base-h} L{x+4} {base}Z" fill="#9aa7ad"/>')
    hx, hy = x, base-h
    for k in range(3):
        a = math.radians(ang + 120*k); L = h*0.55
        ex, ey = hx + L*math.cos(a), hy + L*math.sin(a)
        px, py = -math.sin(a)*4, math.cos(a)*4
        t.append(f'<path d="M{hx:.1f} {hy:.1f} L{hx+px:.1f} {hy+py:.1f} L{ex:.1f} {ey:.1f}Z" fill="#c7d0d4"/>')
    t.append(f'<circle cx="{hx}" cy="{hy}" r="3.5" fill="#dfe5e7"/></g>')
    return "".join(t)
for x, h, a, op in [(70,150,-80,.55),(170,190,-20,.8),(290,130,40,.5),(370,95,10,.35),(30,80,60,.3)]:
    s.append(turbine(x, HZ+2, h, a, op))

# cavalos de petróleo (direita)
def pumpjack(x, base, sc, op):
    p = [f'<g transform="translate({x},{base}) scale({sc})" opacity="{op}" fill="#2a2116" stroke="#c9a45c" stroke-opacity="0.6" stroke-width="1.6">']
    p.append('<path d="M-30 0 L0 -70 L30 0" fill="none"/>')              # tripé
    p.append('<path d="M-70 -84 L60 -66 L62 -76 L-68 -94Z"/>')            # balancim
    p.append('<path d="M60 -72 Q82 -68 78 -44 L68 -46 Q70 -60 58 -62Z"/>') # cabeça
    p.append('<line x1="72" y1="-44" x2="72" y2="0"/>')                   # haste
    p.append('<circle cx="-52" cy="-30" r="16"/>')                        # contrapeso
    p.append('<line x1="-52" y1="-30" x2="-60" y2="-86"/>')
    p.append('<rect x="-80" y="-6" width="170" height="6"/></g>')
    return "".join(p)
for x, sc, op in [(980,1.25,.85),(800,0.95,.65),(690,0.6,.4),(1060,0.55,.35)]:
    s.append(pumpjack(x, HZ+2, sc, op))
# chama de queimador distante
s.append(f'<line x1="890" y1="{HZ}" x2="890" y2="{HZ-120}" stroke="#4a3b25" stroke-width="3"/>')
s.append(f'<path d="M890 {HZ-122} q-9 -18 0 -38 q9 20 0 38Z" fill="#c9a45c" opacity="0.8"/>')

s.append(f'<rect width="{W}" height="{H}" fill="url(#fade)"/>')
s.append(f'<rect width="{W}" height="{H}" fill="url(#vign)"/>')
s.append('</svg>')
open("bg.svg", "w").write("\n".join(s))
print("bg.svg ok")
