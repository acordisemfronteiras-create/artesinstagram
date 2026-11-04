import random, sys
from pathlib import Path

random.seed(7)
W, H = 1080, 1350

# ---------- Banco Central tower illustration (SVG) ----------
def lerp(a, b, t):
    return a + (b - a) * t

# Tower geometry: low-angle frontal view, slight convergence toward the top
top_y, base_y = 62, 560
tl, tr = 392, 688          # top left / right x
bl, br = 346, 734          # bottom left / right x

def x_at(frac, y):
    """x position across facade (0..1) at height y."""
    t = (y - top_y) / (base_y - top_y)
    left = lerp(tl, bl, t)
    right = lerp(tr, br, t)
    return lerp(left, right, frac)

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
svg.append('''
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#121a26"/>
    <stop offset="0.38" stop-color="#1b2533"/>
    <stop offset="0.44" stop-color="#2a2a2c"/>
    <stop offset="0.50" stop-color="#3a2f22"/>
    <stop offset="0.60" stop-color="#0c0c0c"/>
    <stop offset="1" stop-color="#0a0a0a"/>
  </linearGradient>
  <linearGradient id="glass" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#0d1118"/>
    <stop offset="0.45" stop-color="#1a212b"/>
    <stop offset="1" stop-color="#0b0e13"/>
  </linearGradient>
  <linearGradient id="glassV" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#5a6a80" stop-opacity="0.22"/>
    <stop offset="0.5" stop-color="#000" stop-opacity="0"/>
    <stop offset="1" stop-color="#c9a45c" stop-opacity="0.10"/>
  </linearGradient>
  <radialGradient id="glow" cx="0.5" cy="0.36" r="0.5">
    <stop offset="0" stop-color="#c9a45c" stop-opacity="0.18"/>
    <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.35"/>
    <stop offset="0.14" stop-color="#0a0a0a" stop-opacity="0"/>
    <stop offset="0.30" stop-color="#0a0a0a" stop-opacity="0.05"/>
    <stop offset="0.40" stop-color="#0a0a0a" stop-opacity="0.72"/>
    <stop offset="0.47" stop-color="#0a0a0a" stop-opacity="1"/>
    <stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/>
  </linearGradient>
  <radialGradient id="vign" cx="0.5" cy="0.3" r="0.8">
    <stop offset="0.55" stop-color="#000" stop-opacity="0"/>
    <stop offset="1" stop-color="#000" stop-opacity="0.65"/>
  </radialGradient>
  <filter id="grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="3"/>
    <feColorMatrix type="saturate" values="0"/>
    <feComponentTransfer><feFuncA type="table" tableValues="0 0.07"/></feComponentTransfer>
  </filter>
  <filter id="soft"><feGaussianBlur stdDeviation="1.1"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/>
<rect width="100%" height="100%" fill="url(#glow)"/>
''')

# distant low skyline / trees silhouettes at horizon
pts = [(0, base_y)]
x = 0
while x < W:
    h = random.choice([8, 12, 18, 26, 14, 30, 10])
    w = random.randint(28, 70)
    pts += [(x, base_y - h), (x + w, base_y - h)]
    x += w
pts += [(W, base_y), (W, base_y+60), (0, base_y+60)]
svg.append('<polygon fill="#07090c" points="' + " ".join(f"{a},{b}" for a, b in pts) + '"/>')

# Tower body (two slabs + recessed center slot)
def facade_poly(f0, f1, y0=top_y, y1=base_y):
    return f"{x_at(f0,y0):.1f},{y0} {x_at(f1,y0):.1f},{y0} {x_at(f1,y1):.1f},{y1} {x_at(f0,y1):.1f},{y1}"

slot0, slot1 = 0.47, 0.53
svg.append(f'<polygon fill="url(#glass)" points="{facade_poly(0, slot0)}"/>')
svg.append(f'<polygon fill="url(#glass)" points="{facade_poly(slot1, 1)}"/>')
svg.append(f'<polygon fill="#050608" points="{facade_poly(slot0, slot1, top_y+26)}"/>')
svg.append(f'<polygon fill="url(#glassV)" points="{facade_poly(0, 1)}"/>')

# Crown band at top
svg.append(f'<polygon fill="#2a2f36" points="{x_at(-0.01,top_y-4):.1f},{top_y-4} {x_at(1.01,top_y-4):.1f},{top_y-4} {x_at(1.01,top_y+22):.1f},{top_y+22} {x_at(-0.01,top_y+22):.1f},{top_y+22}"/>')
svg.append(f'<line x1="{x_at(-0.01,top_y+22):.1f}" y1="{top_y+22}" x2="{x_at(1.01,top_y+22):.1f}" y2="{top_y+22}" stroke="#c9a45c" stroke-opacity="0.35" stroke-width="1.2"/>')

# Floors
floors = 21
fy0, fy1 = top_y + 30, base_y - 70
floor_h = (fy1 - fy0) / floors
for i in range(floors + 1):
    y = fy0 + i * floor_h
    for a, b in ((0, slot0), (slot1, 1)):
        svg.append(f'<line x1="{x_at(a,y):.1f}" y1="{y:.1f}" x2="{x_at(b,y):.1f}" y2="{y:.1f}" stroke="#8796a8" stroke-opacity="0.16" stroke-width="1.4"/>')

# Vertical mullions
cols = 13
for a, b in ((0, slot0), (slot1, 1)):
    for j in range(cols + 1):
        f = lerp(a, b, j / cols)
        svg.append(f'<line x1="{x_at(f,top_y+22):.1f}" y1="{top_y+22}" x2="{x_at(f,base_y-70):.1f}" y2="{base_y-70}" stroke="#9aa8b8" stroke-opacity="{0.10 if j%2 else 0.22}" stroke-width="{1.0 if j%2 else 1.8}"/>')

# Lit windows (warm), sparse
for i in range(floors):
    y = fy0 + i * floor_h
    for a, b in ((0, slot0), (slot1, 1)):
        for j in range(cols):
            if random.random() < 0.06:
                f0 = lerp(a, b, j / cols); f1 = lerp(a, b, (j + 1) / cols)
                op = random.uniform(0.10, 0.28)
                svg.append(f'<polygon fill="#e3b96a" fill-opacity="{op:.2f}" points="{x_at(f0,y+2):.1f},{y+2:.1f} {x_at(f1,y+2):.1f},{y+2:.1f} {x_at(f1,y+floor_h-2):.1f},{y+floor_h-2:.1f} {x_at(f0,y+floor_h-2):.1f},{y+floor_h-2:.1f}"/>')

# Pilotis (open ground level with columns)
py0, py1 = base_y - 70, base_y
svg.append(f'<polygon fill="#030405" points="{facade_poly(0.0, 1.0, py0, py1)}"/>')
svg.append(f'<polygon fill="#242a31" points="{facade_poly(-0.005, 1.005, py0-6, py0+4)}"/>')
for k in range(9):
    f = lerp(0.05, 0.95, k / 8)
    cx = x_at(f, py1)
    svg.append(f'<rect x="{cx-5:.1f}" y="{py0+4}" width="10" height="{py1-py0-4}" fill="#2b3139"/>')
# warm lobby light
svg.append(f'<rect x="{x_at(0.12,py1):.1f}" y="{py0+18}" width="{x_at(0.88,py1)-x_at(0.12,py1):.1f}" height="{py1-py0-18}" fill="#d9ad62" fill-opacity="0.16" filter="url(#soft)"/>')

# Low wide annex buildings on both sides
svg.append(f'<rect x="70" y="{base_y-46}" width="{bl-70-20}" height="46" fill="#0d1014"/>')
svg.append(f'<rect x="{br+20}" y="{base_y-46}" width="{W-70-br-20}" height="46" fill="#0d1014"/>')
for x0, x1 in ((70, bl - 20), (br + 20, W - 70)):
    svg.append(f'<line x1="{x0}" y1="{base_y-46}" x2="{x1}" y2="{base_y-46}" stroke="#c9a45c" stroke-opacity="0.25"/>')
    xx = x0 + 10
    while xx < x1 - 14:
        if random.random() < 0.35:
            svg.append(f'<rect x="{xx}" y="{base_y-34}" width="16" height="10" fill="#e3b96a" fill-opacity="{random.uniform(0.15,0.4):.2f}"/>')
        xx += 26

# Flagpoles on the left plaza
for k, fx in enumerate((150, 178, 206)):
    svg.append(f'<line x1="{fx}" y1="{base_y-150}" x2="{fx}" y2="{base_y}" stroke="#56606c" stroke-width="2"/>')
svg.append(f'<rect x="150" y="{base_y-150}" width="40" height="24" fill="#2f4a37" fill-opacity="0.85"/>')

# Plaza + reflecting pool with mirrored, faded tower
svg.append(f'<rect x="0" y="{base_y}" width="{W}" height="80" fill="#08090b"/>')
svg.append(f'<g opacity="0.22" transform="translate(0,{2*base_y}) scale(1,-1)">'
           f'<polygon fill="#1c2430" points="{facade_poly(0,1)}"/></g>')
svg.append(f'<line x1="0" y1="{base_y}" x2="{W}" y2="{base_y}" stroke="#c9a45c" stroke-opacity="0.18"/>')

svg.append('<rect width="100%" height="100%" fill="url(#fade)"/>')
svg.append('<rect width="100%" height="100%" fill="url(#vign)"/>')
svg.append('<rect width="100%" height="100%" filter="url(#grain)"/>')
svg.append('</svg>')
Path(sys.argv[1] if len(sys.argv)>1 else 'bg.svg').write_text("\n".join(svg))
print("ok")
