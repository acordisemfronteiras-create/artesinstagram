"""Fundo: lavoura de soja ao entardecer, silos e linha de preço subindo no céu."""
import math, random, sys
from pathlib import Path

random.seed(11)
W, H = 1080, 1350
HZ = 478  # linha do horizonte

s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
s.append('''
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0f1621"/>
    <stop offset="0.20" stop-color="#18202b"/>
    <stop offset="0.30" stop-color="#2b2a2a"/>
    <stop offset="0.335" stop-color="#4a3721"/>
    <stop offset="0.36" stop-color="#1a140d"/>
    <stop offset="0.6" stop-color="#0b0b0b"/>
    <stop offset="1" stop-color="#0a0a0a"/>
  </linearGradient>
  <radialGradient id="sun" cx="0.30" cy="0.335" r="0.42">
    <stop offset="0" stop-color="#e2b466" stop-opacity="0.55"/>
    <stop offset="0.18" stop-color="#c9a45c" stop-opacity="0.22"/>
    <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="field" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#1d1a12"/>
    <stop offset="0.5" stop-color="#121109"/>
    <stop offset="1" stop-color="#0a0a0a"/>
  </linearGradient>
  <linearGradient id="bin" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#151a20"/>
    <stop offset="0.35" stop-color="#3a3f45"/>
    <stop offset="0.55" stop-color="#262b31"/>
    <stop offset="1" stop-color="#0c0f12"/>
  </linearGradient>
  <linearGradient id="line" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#c9a45c" stop-opacity="0"/>
    <stop offset="0.35" stop-color="#c9a45c" stop-opacity="0.35"/>
    <stop offset="1" stop-color="#e2bd72" stop-opacity="0.95"/>
  </linearGradient>
  <linearGradient id="area" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#c9a45c" stop-opacity="0.16"/>
    <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.35"/>
    <stop offset="0.13" stop-color="#0a0a0a" stop-opacity="0"/>
    <stop offset="0.34" stop-color="#0a0a0a" stop-opacity="0"/>
    <stop offset="0.41" stop-color="#0a0a0a" stop-opacity="0.75"/>
    <stop offset="0.47" stop-color="#0a0a0a" stop-opacity="1"/>
    <stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/>
  </linearGradient>
  <radialGradient id="vign" cx="0.5" cy="0.3" r="0.8">
    <stop offset="0.55" stop-color="#000" stop-opacity="0"/>
    <stop offset="1" stop-color="#000" stop-opacity="0.6"/>
  </radialGradient>
  <filter id="grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="5"/>
    <feColorMatrix type="saturate" values="0"/>
    <feComponentTransfer><feFuncA type="table" tableValues="0 0.07"/></feComponentTransfer>
  </filter>
  <filter id="blur"><feGaussianBlur stdDeviation="2.2"/></filter>
  <filter id="glow"><feGaussianBlur stdDeviation="4"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/>
<rect width="100%" height="100%" fill="url(#sun)"/>
''')

# Sol baixo, meio escondido no horizonte
s.append(f'<circle cx="324" cy="{HZ+4}" r="34" fill="#e7bd70" fill-opacity="0.55" filter="url(#blur)"/>')

# Grade discreta de cotação no céu + linha de preço subindo (o rali em Chicago)
for gy in (120, 180, 240, 300):
    s.append(f'<line x1="90" y1="{gy}" x2="990" y2="{gy}" stroke="#8796a8" stroke-opacity="0.07" stroke-dasharray="2 8"/>')
pts = []
x, y = 90, 236
while x < 870:
    pts.append((x, y))
    x += random.randint(22, 34)
    y += random.uniform(-9, 10)
    y = max(214, min(252, y))
# arrancada final (último pregão)
pts += [(900, 232), (928, 196), (954, 160), (982, 132)]
d = "M" + " L".join(f"{a:.0f},{b:.1f}" for a, b in pts)
s.append(f'<path d="{d} L982,310 L90,310 Z" fill="url(#area)"/>')
s.append(f'<path d="{d}" fill="none" stroke="url(#line)" stroke-width="2.6" stroke-linejoin="round"/>')
s.append('<circle cx="982" cy="132" r="11" fill="#e2bd72" fill-opacity="0.35" filter="url(#glow)"/>')
s.append('<circle cx="982" cy="132" r="5" fill="#e9c47a"/>')

# Linha de árvores bem ao longe
tp = [(0, HZ)]
x = 0
while x < W:
    h = random.choice([3, 5, 7, 9, 6, 11, 4])
    w = random.randint(14, 40)
    tp += [(x, HZ - h), (x + w, HZ - h - random.randint(0, 3))]
    x += w
tp += [(W, HZ), (W, HZ + 4), (0, HZ + 4)]
s.append('<polygon fill="#0c0d0d" points="' + " ".join(f"{a},{b}" for a, b in tp) + '"/>')

# Complexo de silos (à direita)
def bin_(cx, w, h, base):
    top = base - h
    r = w / 2
    s.append(f'<rect x="{cx-r:.1f}" y="{top:.1f}" width="{w}" height="{h}" fill="url(#bin)"/>')
    for k in range(1, int(h // 9)):
        yy = top + k * 9
        s.append(f'<line x1="{cx-r:.1f}" y1="{yy:.1f}" x2="{cx+r:.1f}" y2="{yy:.1f}" stroke="#000" stroke-opacity="0.28" stroke-width="1"/>')
    s.append(f'<polygon fill="#2c3137" points="{cx-r-2:.1f},{top:.1f} {cx+r+2:.1f},{top:.1f} {cx:.1f},{top-w*0.34:.1f}"/>')
    s.append(f'<line x1="{cx:.1f}" y1="{top-w*0.34:.1f}" x2="{cx+r+2:.1f}" y2="{top:.1f}" stroke="#c9a45c" stroke-opacity="0.35" stroke-width="1.2"/>')
    s.append(f'<rect x="{cx-4:.1f}" y="{top-w*0.34-6:.1f}" width="8" height="6" fill="#3a3f45"/>')

base = HZ + 6
bin_(735, 70, 112, base)
bin_(812, 70, 112, base)
bin_(889, 70, 112, base)
bin_(660, 52, 78, base)
bin_(958, 52, 78, base)
# elevador / torre de carga
s.append(f'<rect x="842" y="{base-212}" width="26" height="212" fill="#1a1f25"/>')
s.append(f'<polygon fill="#262b31" points="836,{base-212} 874,{base-212} 870,{base-232} 840,{base-232}"/>')
s.append(f'<line x1="855" y1="{base-200}" x2="742" y2="{base-155}" stroke="#2f343a" stroke-width="4"/>')
s.append(f'<line x1="855" y1="{base-200}" x2="900" y2="{base-155}" stroke="#2f343a" stroke-width="4"/>')
s.append(f'<line x1="855" y1="{base-190}" x2="960" y2="{base-110}" stroke="#2f343a" stroke-width="3"/>')
for k in range(6):
    s.append(f'<rect x="850" y="{base-200+k*30}" width="10" height="5" fill="#e3b96a" fill-opacity="{random.uniform(0.25,0.55):.2f}"/>')
s.append(f'<rect x="604" y="{base-28}" width="44" height="28" fill="#12161a"/>')
s.append(f'<rect x="612" y="{base-20}" width="12" height="8" fill="#e3b96a" fill-opacity="0.45"/>')

# Lavoura em perspectiva (fileiras convergindo para o ponto de fuga)
FY0, FY1 = HZ + 4, 700
s.append(f'<rect x="0" y="{FY0}" width="{W}" height="{FY1-FY0}" fill="url(#field)"/>')
VP = (430, HZ - 6)
for i in range(-34, 35):
    xb = 540 + i * 64
    op = 0.10 + 0.16 * (1 - abs(i) / 34)
    s.append(f'<line x1="{VP[0]+(xb-VP[0])*0.012:.1f}" y1="{FY0}" x2="{xb}" y2="{FY1}" stroke="#c9a45c" stroke-opacity="{op*0.5:.2f}" stroke-width="1"/>')
    # fileira de plantas: pontos ao longo da linha
    for t in [0.08 * k for k in range(1, 13)]:
        t2 = t * t
        px = VP[0] + (xb - VP[0]) * (0.012 + 0.988 * t2)
        py = FY0 + (FY1 - FY0) * t2
        if -40 < px < W + 40 and py < 640:
            r = 0.6 + 4.8 * t2
            s.append(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="{r*1.5:.1f}" ry="{r:.1f}" fill="#2a2a19" fill-opacity="0.9"/>')

# Plantas de soja em primeiro plano (cantos), com vagens
def leaf(cx, cy, ang, L, col, op):
    a = math.radians(ang)
    tx, ty = cx + L * math.cos(a), cy + L * math.sin(a)
    nx, ny = -math.sin(a) * L * 0.38, math.cos(a) * L * 0.38
    mx, my = (cx + tx) / 2, (cy + ty) / 2
    s.append(f'<path d="M{cx:.1f},{cy:.1f} Q{mx+nx:.1f},{my+ny:.1f} {tx:.1f},{ty:.1f} Q{mx-nx:.1f},{my-ny:.1f} {cx:.1f},{cy:.1f} Z" fill="{col}" fill-opacity="{op}"/>')
    s.append(f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{tx:.1f}" y2="{ty:.1f}" stroke="#c9a45c" stroke-opacity="{op*0.25:.2f}" stroke-width="0.8"/>')

def plant(x0, y0, h, flip, scale=1.0):
    sgn = -1 if flip else 1
    stem_top = (x0 + sgn * 18 * scale, y0 - h)
    s.append(f'<path d="M{x0},{y0} Q{x0+sgn*4*scale:.1f},{y0-h*0.5:.1f} {stem_top[0]:.1f},{stem_top[1]:.1f}" stroke="#2b2c1c" stroke-width="{4*scale:.1f}" fill="none"/>')
    for k in range(5):
        t = 0.25 + 0.17 * k
        bx = x0 + sgn * 18 * scale * t * t
        by = y0 - h * t
        side = 1 if k % 2 else -1
        px, py = bx + side * 34 * scale, by - 22 * scale
        s.append(f'<line x1="{bx:.1f}" y1="{by:.1f}" x2="{px:.1f}" y2="{py:.1f}" stroke="#2b2c1c" stroke-width="{2.2*scale:.1f}"/>')
        base_ang = -90 + side * 40
        for da in (-55, 0, 55):
            leaf(px, py, base_ang + da, 46 * scale, "#1f2416", 0.95)
        # vagens penduradas no nó
        for p in range(2):
            vx = bx + side * (6 + p * 7) * scale
            vy = by + 4 * scale
            s.append(f'<path d="M{vx:.1f},{vy:.1f} q{side*4*scale:.1f},{14*scale:.1f} {side*1*scale:.1f},{26*scale:.1f}" stroke="#6b5a34" stroke-width="{5*scale:.1f}" stroke-linecap="round" fill="none" stroke-opacity="0.85"/>')
            s.append(f'<path d="M{vx:.1f},{vy:.1f} q{side*4*scale:.1f},{14*scale:.1f} {side*1*scale:.1f},{26*scale:.1f}" stroke="#c9a45c" stroke-width="{1.2*scale:.1f}" stroke-linecap="round" fill="none" stroke-opacity="0.45"/>')
    for da in (-60, 0, 60):
        leaf(stem_top[0], stem_top[1], -90 + da, 50 * scale, "#232a18", 0.95)

plant(30, 610, 170, False, 0.85)
plant(1050, 610, 175, True, 0.85)

s.append('<rect width="100%" height="100%" fill="url(#fade)"/>')
s.append('<rect width="100%" height="100%" fill="url(#vign)"/>')
s.append('<rect width="100%" height="100%" filter="url(#grain)"/>')
s.append('</svg>')
Path(sys.argv[1] if len(sys.argv) > 1 else 'bg.svg').write_text("\n".join(s))
print("ok")
