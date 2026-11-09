"""Fundo do post de exportação de frango: aviários no Oeste catarinense ao amanhecer,
com silos de ração, araucárias e, no horizonte, guindaste e navio de contêineres."""
import math, random, sys
from pathlib import Path

random.seed(19)
W, H = 1080, 1350
GOLD = "#c9a45c"
VP = (905.0, 418.0)  # ponto de fuga

def lerp(a, b, t):
    return a + (b - a) * t

def to_vp(p, t):
    return (lerp(p[0], VP[0], t), lerp(p[1], VP[1], t))

def pts(*ps):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in ps)

svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
svg.append(f'''
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0f1622"/>
    <stop offset="0.16" stop-color="#172232"/>
    <stop offset="0.20" stop-color="#2c3440"/>
    <stop offset="0.25" stop-color="#6b5236"/>
    <stop offset="0.283" stop-color="#b98a4e"/>
    <stop offset="0.31" stop-color="#3a2f22"/>
    <stop offset="0.60" stop-color="#0c0c0c"/>
    <stop offset="1" stop-color="#0a0a0a"/>
  </linearGradient>
  <radialGradient id="sun" cx="0.80" cy="0.273" r="0.42" gradientUnits="objectBoundingBox">
    <stop offset="0" stop-color="#f2c777" stop-opacity="0.50"/>
    <stop offset="0.35" stop-color="#c9a45c" stop-opacity="0.16"/>
    <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="roof" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#39404a"/>
    <stop offset="0.65" stop-color="#5c5a55"/>
    <stop offset="1" stop-color="#8a7350"/>
  </linearGradient>
  <linearGradient id="wall" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#171b21"/>
    <stop offset="1" stop-color="#2a2a29"/>
  </linearGradient>
  <linearGradient id="gable" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#20252c"/>
    <stop offset="1" stop-color="#101318"/>
  </linearGradient>
  <linearGradient id="steel" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#232830"/>
    <stop offset="0.45" stop-color="#6f757d"/>
    <stop offset="0.62" stop-color="#9a9385"/>
    <stop offset="1" stop-color="#2a2d33"/>
  </linearGradient>
  <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.42"/>
    <stop offset="0.13" stop-color="#0a0a0a" stop-opacity="0"/>
    <stop offset="0.325" stop-color="#0a0a0a" stop-opacity="0"/>
    <stop offset="0.375" stop-color="#0a0a0a" stop-opacity="0.75"/>
    <stop offset="0.405" stop-color="#0a0a0a" stop-opacity="1"/>
    <stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/>
  </linearGradient>
  <radialGradient id="vign" cx="0.5" cy="0.3" r="0.8">
    <stop offset="0.55" stop-color="#000" stop-opacity="0"/>
    <stop offset="1" stop-color="#000" stop-opacity="0.65"/>
  </radialGradient>
  <filter id="grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="5"/>
    <feColorMatrix type="saturate" values="0"/>
    <feComponentTransfer><feFuncA type="table" tableValues="0 0.07"/></feComponentTransfer>
  </filter>
  <filter id="soft"><feGaussianBlur stdDeviation="2.2"/></filter>
  <filter id="softer"><feGaussianBlur stdDeviation="7"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/>
<rect width="100%" height="100%" fill="url(#sun)"/>
''')

# estrelas discretas no alto
for _ in range(70):
    x, y = random.uniform(0, W), random.uniform(130, 250)
    svg.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(.5,1.3):.1f}" fill="#d9d4c7" fill-opacity="{random.uniform(.08,.35):.2f}"/>')

svg.append('<g transform="translate(0,-72)">')
# ---------- Horizonte: guindaste, pilhas de contêineres e navio ----------
hz = 432
# navio
sx0, sx1 = 790, 1020
svg.append(f'<polygon fill="#0c0f14" points="{pts((sx0,hz-6),(sx1+10,hz-6),(sx1-8,hz+10),(sx0+14,hz+10))}"/>')
svg.append(f'<rect x="{sx1-32}" y="{hz-40}" width="26" height="34" fill="#10141a"/>')
svg.append(f'<rect x="{sx1-28}" y="{hz-34}" width="18" height="3" fill="#e3b96a" fill-opacity=".7"/>')
palette = ["#1c2530", "#2a2520", "#242a33", "#3a2f22", "#20262d", "#46381f"]
cx = sx0 + 16
while cx < sx1 - 42:
    n = random.choice([2, 3, 3, 4])
    for k in range(n):
        svg.append(f'<rect x="{cx}" y="{hz-14-k*8}" width="13" height="7.2" fill="{random.choice(palette)}" stroke="#000" stroke-opacity=".4" stroke-width=".4"/>')
    cx += 14
# guindaste de pórtico
gx = 748
svg.append(f'<g stroke="#10141a" stroke-width="3.2" fill="none">'
           f'<line x1="{gx}" y1="{hz+6}" x2="{gx}" y2="{hz-88}"/>'
           f'<line x1="{gx+26}" y1="{hz+6}" x2="{gx+26}" y2="{hz-88}"/>'
           f'<line x1="{gx-36}" y1="{hz-88}" x2="{gx+120}" y2="{hz-88}" stroke-width="4"/>'
           f'<line x1="{gx}" y1="{hz-46}" x2="{gx+26}" y2="{hz-46}"/>'
           f'<line x1="{gx+13}" y1="{hz-118}" x2="{gx-34}" y2="{hz-88}" stroke-width="1.6"/>'
           f'<line x1="{gx+13}" y1="{hz-118}" x2="{gx+118}" y2="{hz-88}" stroke-width="1.6"/>'
           f'<line x1="{gx+13}" y1="{hz-118}" x2="{gx+13}" y2="{hz-88}" stroke-width="2.4"/>'
           f'<line x1="{gx+92}" y1="{hz-88}" x2="{gx+92}" y2="{hz-50}" stroke-width="1.2"/></g>')
svg.append(f'<rect x="{gx+85}" y="{hz-50}" width="14" height="8" fill="#10141a"/>')
svg.append(f'<circle cx="{gx+13}" cy="{hz-120}" r="2.2" fill="#e3b96a"/>')

# ---------- Coxilhas (duas camadas) ----------
def ridge(base, a1, f1, a2, f2, phase):
    out = [(0, 620)]
    for x in range(0, W + 1, 8):
        y = base - a1 * math.sin(x * f1 + phase) - a2 * math.sin(x * f2 + phase * 1.7)
        out.append((x, y))
    out.append((W, 620))
    return out

far = ridge(424, 14, 0.0058, 6, 0.021, 0.8)
svg.append(f'<polygon fill="#171a1e" points="{pts(*far)}"/>')
near = ridge(452, 16, 0.0041, 5, 0.017, 2.2)

# araucárias na coxilha distante
def araucaria(x, base, h, color="#0b0d10"):
    """Silhueta em taça: tronco reto, galhos que sobem em leque até uma copa plana."""
    w = h * 0.74
    top = base - h
    rnd = random.Random(int(x * 7 + h))
    g = [f'<line x1="{x}" y1="{base}" x2="{x}" y2="{top+h*.12:.1f}" stroke="{color}" stroke-width="{max(2,h*.032):.1f}" stroke-linecap="round"/>']
    n = 7
    for i in range(n):
        t = i / (n - 1)
        y0 = base - h * lerp(.52, .86, t)
        half = w * lerp(.52, .08, t)
        for sgn in (-1, 1):
            xt = x + sgn * half
            ytip = top + h * (.035 + .05 * (half / (w * .52)) ** 2) + rnd.uniform(-h*.008, h*.008)
            # galho sobe reto e abre perto da ponta
            g.append(f'<path d="M{x} {y0:.1f} Q{x+sgn*half*.82:.1f} {lerp(y0,ytip,.42):.1f} {xt:.1f} {ytip:.1f}" fill="none" stroke="{color}" stroke-width="{max(1.1,h*.016):.1f}" stroke-linecap="round"/>')
            g.append(f'<ellipse cx="{xt:.1f}" cy="{ytip-h*.012:.1f}" rx="{w*.13:.1f}" ry="{h*.034:.1f}" fill="{color}"/>')
    g.append(f'<ellipse cx="{x}" cy="{top+h*.03:.1f}" rx="{w*.16:.1f}" ry="{h*.036:.1f}" fill="{color}"/>')
    return "".join(g)

for x, h in ((58, 150), (612, 118), (664, 94), (706, 104)):
    y = next(p[1] for p in far if p[0] >= x)
    svg.append(araucaria(x, y + 6, h, "#101317"))
svg.append(f'<polygon fill="#0e1014" points="{pts(*near)}"/>')
for x, h in ((480, 164), (548, 132)):
    y = next(p[1] for p in near if p[0] >= x)
    svg.append(araucaria(x, y + 8, h, "#090b0e"))

# ---------- Aviários em perspectiva ----------
def barn(gl, gr, base, wall, roof_h, tmax, bays):
    """gl/gr: x da empena; base: y do chão; wall: altura da parede; roof_h: altura da cumeeira."""
    bl, br = (gl, base), (gr, base)
    tl, tr = (gl, base - wall), (gr, base - wall)
    rd = ((gl + gr) / 2, base - wall - roof_h)
    far_br, far_tr, far_rd = to_vp(br, tmax), to_vp(tr, tmax), to_vp(rd, tmax)
    # telhado (água direita)
    svg.append(f'<polygon fill="url(#roof)" points="{pts(rd,tr,far_tr,far_rd)}"/>')
    # ondulação do telhado
    for i in range(1, 46):
        t = tmax * (1 - (1 - i / 46) ** 1.5)
        a, b = to_vp(rd, t), to_vp(tr, t)
        svg.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#0a0c10" stroke-opacity=".32" stroke-width=".9"/>')
    for k in range(1, 6):
        f = k / 6
        a = (lerp(rd[0], tr[0], f), lerp(rd[1], tr[1], f))
        b = to_vp(a, tmax)
        svg.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#d9c49a" stroke-opacity=".10" stroke-width="1"/>')
    svg.append(f'<line x1="{rd[0]:.1f}" y1="{rd[1]:.1f}" x2="{far_rd[0]:.1f}" y2="{far_rd[1]:.1f}" stroke="#e0c58e" stroke-opacity=".55" stroke-width="1.6"/>')
    # lanternim na cumeeira
    # parede lateral
    svg.append(f'<polygon fill="url(#wall)" points="{pts(tr,br,far_br,far_tr)}"/>')
    # cortina iluminada, em vãos
    h0, h1 = 0.20, 0.80
    for i in range(bays):
        t0 = tmax * (1 - (1 - i / bays) ** 1.5) + 0.004
        t1 = tmax * (1 - (1 - (i + 0.9) / bays) ** 1.5)
        def wp(t, f):
            return to_vp((gr, lerp(base - wall, base, f)), t)
        op = random.uniform(.34, .78)
        svg.append(f'<polygon fill="#eabf74" fill-opacity="{op:.2f}" points="{pts(wp(t0,h0),wp(t1,h0),wp(t1,h1),wp(t0,h1))}"/>')
    # brilho difuso da cortina
    a, b = to_vp((gr, base - wall * .5), 0), to_vp((gr, base - wall * .5), tmax)
    svg.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#e3b96a" stroke-opacity=".20" stroke-width="{wall*.7:.0f}" filter="url(#softer)"/>')
    # empena
    svg.append(f'<polygon fill="url(#gable)" points="{pts(bl,br,tr,rd,tl)}"/>')
    svg.append(f'<polyline fill="none" stroke="#cdb78e" stroke-opacity=".5" stroke-width="2" points="{pts(tl,rd,tr)}"/>')
    # exaustores na empena
    n = 3
    r = (gr - gl) * 0.105
    cy = base - wall * 0.48
    for k in range(n):
        cx = lerp(gl, gr, (k + 1) / (n + 1))
        svg.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="#0a0c10" stroke="#59606a" stroke-width="1.6"/>')
        for a in range(0, 180, 45):
            dx, dy = r * .9 * math.cos(math.radians(a)), r * .9 * math.sin(math.radians(a))
            svg.append(f'<line x1="{cx-dx:.1f}" y1="{cy-dy:.1f}" x2="{cx+dx:.1f}" y2="{cy+dy:.1f}" stroke="#3a4048" stroke-width="1"/>')
    # porta/entrada de serviço
    return far_br

def silo(x, base, w, body, color="url(#steel)"):
    top = base - body
    legs = body * 0.20
    cone = body * 0.17
    b0 = base - legs
    s = [f'<g stroke="#1a1d22" stroke-width="{max(1.2,w*.05):.1f}">']
    for dx in (-.46, .46):
        s.append(f'<line x1="{x+dx*w:.1f}" y1="{b0-cone*.5:.1f}" x2="{x+dx*w:.1f}" y2="{base}"/>')
    s.append(f'<line x1="{x-.46*w:.1f}" y1="{base-legs*.4:.1f}" x2="{x+.46*w:.1f}" y2="{base-legs*.4:.1f}"/></g>')
    # cone inferior
    s.append(f'<polygon fill="#20242a" points="{pts((x-w/2,b0-cone),(x+w/2,b0-cone),(x+w*.08,b0),(x-w*.08,b0))}"/>')
    # corpo
    s.append(f'<rect x="{x-w/2:.1f}" y="{top+body*.12:.1f}" width="{w}" height="{b0-cone-top-body*.12:.1f}" fill="{color}"/>')
    # anéis
    y = top + body * .12
    while y < b0 - cone - 2:
        s.append(f'<line x1="{x-w/2:.1f}" y1="{y:.1f}" x2="{x+w/2:.1f}" y2="{y:.1f}" stroke="#14171b" stroke-opacity=".5" stroke-width="1"/>')
        y += body * .075
    # tampo cônico
    s.append(f'<polygon fill="#8f8a7d" points="{pts((x-w/2,top+body*.12),(x+w/2,top+body*.12),(x,top))}"/>')
    s.append(f'<polygon fill="#2b2f36" points="{pts((x-w/2,top+body*.12),(x,top+body*.12),(x,top))}" fill-opacity=".75"/>')
    svg.append("".join(s))

# aviário ao fundo
barn(432, 548, 472, 34, 26, 0.62, 16)
silo(566, 470, 18, 74)
silo(592, 470, 18, 74)

# aviário principal
barn(72, 340, 548, 76, 58, 0.635, 15)

# silos do aviário principal
silo(372, 552, 44, 190)
silo(430, 552, 44, 190)
# tubo de ração ligando silo ao aviário
svg.append(f'<path d="M372 524 L352 524 L340 500" fill="none" stroke="#6b6f76" stroke-width="3"/>')
svg.append(f'<path d="M430 524 L352 524" fill="none" stroke="#6b6f76" stroke-width="3"/>')

svg.append('</g>')
svg.append('<rect width="100%" height="100%" fill="url(#fade)"/>')
svg.append('<rect width="100%" height="100%" fill="url(#vign)"/>')
svg.append('<rect width="100%" height="100%" filter="url(#grain)"/>')
svg.append('</svg>')
Path(sys.argv[1] if len(sys.argv) > 1 else 'bg.svg').write_text("\n".join(svg))
print("ok")
