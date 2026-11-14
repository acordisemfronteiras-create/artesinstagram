"""Fundo: parque industrial ao amanhecer com um grande conjunto de engrenagens
(o 'motor do crescimento' sendo trocado). Gera bg.svg 1080x1350."""
import math, random, sys
from pathlib import Path

random.seed(14)
W, H = 1080, 1350
HZ = 430  # horizonte

def gear(cx, cy, r, teeth, depth, stroke, op, fill="none", sw=2.0, hub=True, rot=0):
    pts = []
    n = teeth * 4
    for i in range(n):
        a = 2 * math.pi * i / n + math.radians(rot)
        k = i % 4
        rr = r + depth if k in (1, 2) else r
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    s = [f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{fill}" stroke="{stroke}" stroke-opacity="{op}" stroke-width="{sw}" stroke-linejoin="round"/>']
    if hub:
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r*0.62:.1f}" fill="none" stroke="{stroke}" stroke-opacity="{op*0.6:.2f}" stroke-width="{sw*0.7:.1f}"/>')
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r*0.2:.1f}" fill="#0b0b0c" stroke="{stroke}" stroke-opacity="{op:.2f}" stroke-width="{sw:.1f}"/>')
        for j in range(6):
            a = math.radians(rot + j * 60 + 30)
            x1, y1 = cx + r*0.2*math.cos(a), cy + r*0.2*math.sin(a)
            x2, y2 = cx + r*0.62*math.cos(a), cy + r*0.62*math.sin(a)
            s.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-opacity="{op*0.55:.2f}" stroke-width="{sw*1.6:.1f}"/>')
    return "\n".join(s)

svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
svg.append('''<defs>
 <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#0f141d"/><stop offset="0.22" stop-color="#18202b"/>
  <stop offset="0.30" stop-color="#2b2a2a"/><stop offset="0.33" stop-color="#4a3a24"/>
  <stop offset="0.36" stop-color="#151311"/><stop offset="1" stop-color="#0a0a0a"/>
 </linearGradient>
 <radialGradient id="sun" cx="0.5" cy="0.32" r="0.42">
  <stop offset="0" stop-color="#e2b866" stop-opacity="0.30"/><stop offset="0.5" stop-color="#c9a45c" stop-opacity="0.08"/>
  <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/>
 </radialGradient>
 <linearGradient id="gearfill" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#2a241a"/><stop offset="1" stop-color="#121010"/>
 </linearGradient>
 <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.30"/><stop offset="0.12" stop-color="#0a0a0a" stop-opacity="0"/>
  <stop offset="0.29" stop-color="#0a0a0a" stop-opacity="0.05"/><stop offset="0.36" stop-color="#0a0a0a" stop-opacity="0.75"/>
  <stop offset="0.41" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/>
 </linearGradient>
 <radialGradient id="vign" cx="0.5" cy="0.28" r="0.8">
  <stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.65"/>
 </radialGradient>
 <filter id="grain" x="0" y="0" width="100%" height="100%">
  <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="5"/>
  <feColorMatrix type="saturate" values="0"/>
  <feComponentTransfer><feFuncA type="table" tableValues="0 0.07"/></feComponentTransfer>
 </filter>
 <filter id="blur"><feGaussianBlur stdDeviation="2"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/>
<rect width="100%" height="100%" fill="url(#sun)"/>''')

# faint stars
for _ in range(60):
    x, y = random.uniform(0, W), random.uniform(0, 260)
    svg.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(0.6,1.4):.1f}" fill="#efe6d6" fill-opacity="{random.uniform(0.15,0.5):.2f}"/>')

# rising sun disc behind gears
svg.append(f'<circle cx="540" cy="{HZ-8}" r="70" fill="#e0b565" fill-opacity="0.22" filter="url(#blur)"/>')

# Big gear assembly (center), partially above horizon
gc = "#c9a45c"
svg.append('<g>')
svg.append(gear(540, 300, 118, 18, 20, gc, 0.85, fill="url(#gearfill)", sw=2.4, rot=4))
svg.append(gear(712, 214, 66, 11, 15, gc, 0.70, fill="url(#gearfill)", sw=2.0, rot=12))
svg.append(gear(392, 196, 52, 9, 13, gc, 0.60, fill="url(#gearfill)", sw=1.8, rot=20))
svg.append(gear(808, 330, 40, 8, 11, gc, 0.45, fill="url(#gearfill)", sw=1.6, rot=7))
svg.append('</g>')
# motion arcs
for (cx, cy, r, a0, a1) in ((540, 300, 165, 200, 250), (712, 214, 100, -60, -10), (392, 196, 84, 120, 170)):
    x0, y0 = cx + r*math.cos(math.radians(a0)), cy + r*math.sin(math.radians(a0))
    x1, y1 = cx + r*math.cos(math.radians(a1)), cy + r*math.sin(math.radians(a1))
    svg.append(f'<path d="M{x0:.1f},{y0:.1f} A{r},{r} 0 0 1 {x1:.1f},{y1:.1f}" fill="none" stroke="#c9a45c" stroke-opacity="0.35" stroke-width="1.5" stroke-dasharray="4 7"/>')

# Industrial skyline: sawtooth sheds, chimneys, crane, silo/tanks
sil = "#08090b"
# back layer (bluish)
pts = [(0, HZ)]
x = 0
while x < W:
    h = random.choice([14, 22, 30, 18, 40, 26]); w = random.randint(40, 90)
    pts += [(x, HZ - h), (x + w, HZ - h)]; x += w
pts += [(W, HZ), (W, HZ + 40), (0, HZ + 40)]
svg.append('<polygon fill="#11151b" points="' + " ".join(f"{a},{b}" for a, b in pts) + '"/>')

# sawtooth factory left
def sawtooth(x0, n, w, h, base):
    p = [(x0, base)]
    for i in range(n):
        xa = x0 + i * w
        p += [(xa, base - h * 0.55), (xa + w * 0.75, base - h), (xa + w * 0.75, base - h * 0.55)]
    p += [(x0 + n * w, base - h * 0.55), (x0 + n * w, base)]
    return '<polygon fill="%s" points="%s"/>' % (sil, " ".join(f"{a:.0f},{b:.0f}" for a, b in p))
svg.append(sawtooth(30, 5, 58, 70, HZ + 6))
svg.append(sawtooth(760, 4, 62, 64, HZ + 6))
# skylight glints on sawtooth
for x0, n, w, h in ((30, 5, 58, 70), (760, 4, 62, 64)):
    for i in range(n):
        xa = x0 + i * w + w * 0.75
        svg.append(f'<line x1="{xa:.0f}" y1="{HZ+6-h:.0f}" x2="{xa:.0f}" y2="{HZ+6-h*0.55:.0f}" stroke="#e3b96a" stroke-opacity="0.45" stroke-width="2"/>')
# lit windows along factory walls
for x0, x1 in ((40, 315), (770, 1000)):
    xx = x0
    while xx < x1:
        if random.random() < 0.5:
            svg.append(f'<rect x="{xx}" y="{HZ-24}" width="14" height="9" fill="#e3b96a" fill-opacity="{random.uniform(0.2,0.55):.2f}"/>')
        xx += 24

# chimneys with smoke
for cx, top in ((250, HZ - 150), (290, HZ - 120), (930, HZ - 140)):
    svg.append(f'<polygon fill="{sil}" points="{cx-9},{HZ} {cx-6},{top} {cx+6},{top} {cx+9},{HZ}"/>')
    svg.append(f'<rect x="{cx-7}" y="{top+10}" width="14" height="3" fill="#c9a45c" fill-opacity="0.35"/>')
    for k in range(5):
        svg.append(f'<circle cx="{cx + k*14 + 6}" cy="{top - 14 - k*16}" r="{9 + k*5}" fill="#9aa2ad" fill-opacity="{0.08 - k*0.012:.3f}"/>')

# tanks / silos right-center
for cx, r, h in ((640, 26, 52), (690, 26, 52), (740, 20, 40)):
    svg.append(f'<rect x="{cx-r}" y="{HZ-h}" width="{2*r}" height="{h}" fill="{sil}"/>')
    svg.append(f'<ellipse cx="{cx}" cy="{HZ-h}" rx="{r}" ry="6" fill="#14171c" stroke="#c9a45c" stroke-opacity="0.25"/>')

# tower crane left-center
cx = 120
svg.append(f'<line x1="{cx}" y1="{HZ}" x2="{cx}" y2="{HZ-190}" stroke="{sil}" stroke-width="9"/>')
for yy in range(HZ - 185, HZ, 16):
    svg.append(f'<line x1="{cx-4}" y1="{yy}" x2="{cx+4}" y2="{yy+16}" stroke="#2a2e35" stroke-width="1.2"/>')
svg.append(f'<line x1="{cx-60}" y1="{HZ-188}" x2="{cx+150}" y2="{HZ-188}" stroke="{sil}" stroke-width="6"/>')
svg.append(f'<line x1="{cx}" y1="{HZ-215}" x2="{cx+150}" y2="{HZ-188}" stroke="#2a2e35" stroke-width="1.5"/>')
svg.append(f'<line x1="{cx}" y1="{HZ-215}" x2="{cx-60}" y2="{HZ-188}" stroke="#2a2e35" stroke-width="1.5"/>')
svg.append(f'<line x1="{cx}" y1="{HZ-215}" x2="{cx}" y2="{HZ-188}" stroke="{sil}" stroke-width="4"/>')
svg.append(f'<rect x="{cx-62}" y="{HZ-186}" width="22" height="14" fill="{sil}"/>')
svg.append(f'<line x1="{cx+118}" y1="{HZ-188}" x2="{cx+118}" y2="{HZ-120}" stroke="#3a3f47" stroke-width="1.2"/>')
svg.append(f'<rect x="{cx+108}" y="{HZ-120}" width="20" height="12" fill="#c9a45c" fill-opacity="0.55"/>')
svg.append(f'<circle cx="{cx+150}" cy="{HZ-188}" r="3" fill="#e3b96a"/>')

# conveyor across foreground with crates
svg.append(f'<rect x="0" y="{HZ+4}" width="{W}" height="70" fill="#08090b"/>')
svg.append(f'<line x1="60" y1="{HZ+26}" x2="1020" y2="{HZ+26}" stroke="#c9a45c" stroke-opacity="0.30" stroke-width="2"/>')
for xx in range(70, 1020, 34):
    svg.append(f'<circle cx="{xx}" cy="{HZ+31}" r="4" fill="none" stroke="#c9a45c" stroke-opacity="0.18"/>')
for xx in (150, 330, 610, 860):
    svg.append(f'<rect x="{xx}" y="{HZ+4}" width="34" height="20" fill="#16181c" stroke="#c9a45c" stroke-opacity="0.35"/>')
svg.append(f'<line x1="0" y1="{HZ+4}" x2="{W}" y2="{HZ+4}" stroke="#c9a45c" stroke-opacity="0.18"/>')

svg.append('<rect width="100%" height="100%" fill="url(#fade)"/>')
svg.append('<rect width="100%" height="100%" fill="url(#vign)"/>')
svg.append('<rect width="100%" height="100%" filter="url(#grain)"/>')
svg.append('</svg>')
Path(sys.argv[1] if len(sys.argv) > 1 else 'bg.svg').write_text("\n".join(svg))
print("ok")
