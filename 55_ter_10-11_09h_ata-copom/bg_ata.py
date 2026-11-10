import random, sys, math
from pathlib import Path
random.seed(11)
W, H = 1080, 1350
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#111821"/><stop offset="0.30" stop-color="#19212c"/>
 <stop offset="0.42" stop-color="#2a261f"/><stop offset="0.52" stop-color="#0d0c0b"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="lamp" cx="0.42" cy="0.22" r="0.55">
 <stop offset="0" stop-color="#e6c27a" stop-opacity="0.22"/><stop offset="1" stop-color="#e6c27a" stop-opacity="0"/></radialGradient>
<linearGradient id="paper" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#e9dfcb"/><stop offset="1" stop-color="#b9ad96"/></linearGradient>
<linearGradient id="paper2" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#c8bca5"/><stop offset="1" stop-color="#8e846f"/></linearGradient>
<linearGradient id="desk" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#2a1f15"/><stop offset="1" stop-color="#120d09"/></linearGradient>
<linearGradient id="pen" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#3a3f47"/><stop offset="0.45" stop-color="#14171b"/><stop offset="1" stop-color="#050607"/></linearGradient>
<linearGradient id="gold" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#f0d396"/><stop offset="0.5" stop-color="#c9a45c"/><stop offset="1" stop-color="#7a5f2c"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.30"/><stop offset="0.12" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.27" stop-color="#0a0a0a" stop-opacity="0.04"/><stop offset="0.36" stop-color="#0a0a0a" stop-opacity="0.70"/>
 <stop offset="0.43" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.28" r="0.8"><stop offset="0.5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.7"/></radialGradient>
<filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="5"/>
 <feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="table" tableValues="0 0.07"/></feComponentTransfer></filter>
<filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="14"/></filter>
<filter id="soft"><feGaussianBlur stdDeviation="1.2"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/>''')

# Window behind desk with distant BC-like tower silhouette (right)
s.append('<rect x="610" y="40" width="400" height="330" fill="#121a24" stroke="#2c3440" stroke-width="6"/>')
s.append('<line x1="810" y1="40" x2="810" y2="370" stroke="#2c3440" stroke-width="5"/><line x1="610" y1="205" x2="1010" y2="205" stroke="#2c3440" stroke-width="5"/>')
# tower in window
tx0, tx1, ty0, ty1 = 760, 880, 95, 370
s.append(f'<rect x="{tx0}" y="{ty0}" width="{tx1-tx0}" height="{ty1-ty0}" fill="#0b0f15"/>')
s.append(f'<rect x="{(tx0+tx1)/2-3}" y="{ty0+10}" width="6" height="{ty1-ty0}" fill="#05070a"/>')
for i in range(22):
    y = ty0 + 14 + i*11.5
    s.append(f'<line x1="{tx0}" y1="{y:.1f}" x2="{tx1}" y2="{y:.1f}" stroke="#8796a8" stroke-opacity="0.13"/>')
    for j in range(10):
        if random.random() < 0.08:
            x = tx0 + 4 + j*11.6 + (6 if j>=5 else 0)
            s.append(f'<rect x="{x:.1f}" y="{y+2:.1f}" width="8" height="7" fill="#e3b96a" fill-opacity="{random.uniform(.15,.4):.2f}"/>')
s.append('<polygon fill="#070a0e" points="610,370 610,330 650,330 650,318 700,318 700,340 740,340 740,370"/>')
s.append('<polygon fill="#070a0e" points="890,370 890,345 940,345 940,325 1010,325 1010,370"/>')
# window frame shadow re-draw
s.append('<rect x="610" y="40" width="400" height="330" fill="none" stroke="#2c3440" stroke-width="6"/>')
s.append('<rect width="100%" height="100%" fill="url(#lamp)"/>')

# Desk surface (perspective)
s.append('<polygon fill="url(#desk)" points="0,380 1080,380 1080,760 0,760"/>')
s.append('<line x1="0" y1="380" x2="1080" y2="380" stroke="#c9a45c" stroke-opacity="0.25" stroke-width="1.5"/>')
for k in range(9):
    y = 392 + k*k*5
    s.append(f'<line x1="0" y1="{y}" x2="1080" y2="{y+random.randint(-3,3)}" stroke="#4a3622" stroke-opacity="0.35"/>')

# Document stack: back sheet and front sheet, rotated
def sheet(cx, cy, w, h, rot, fill, shadow=True):
    out = []
    if shadow:
        out.append(f'<g transform="translate({cx+18},{cy+22}) rotate({rot})"><rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" fill="#000" opacity="0.6" filter="url(#shadow)"/></g>')
    out.append(f'<g transform="translate({cx},{cy}) rotate({rot})"><rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" fill="{fill}"/></g>')
    return out
s += sheet(400, 345, 390, 400, -10, 'url(#paper2)')
s += sheet(430, 335, 390, 400, -4, 'url(#paper)')

# Content on front sheet
g = ['<g transform="translate(430,335) rotate(-4)">']
w, h = 390, 400
x0, y0 = -w/2 + 40, -h/2 + 38
# seal/header
g.append(f'<circle cx="{x0+22}" cy="{y0+20}" r="20" fill="none" stroke="#7a5f2c" stroke-width="2.5"/>')
g.append(f'<circle cx="{x0+22}" cy="{y0+20}" r="12" fill="none" stroke="#7a5f2c" stroke-width="1.5"/>')
g.append(f'<rect x="{x0+56}" y="{y0+8}" width="170" height="10" rx="2" fill="#3b3329" opacity="0.85"/>')
g.append(f'<rect x="{x0+56}" y="{y0+26}" width="110" height="7" rx="2" fill="#6a5e4d" opacity="0.7"/>')
g.append(f'<line x1="{x0}" y1="{y0+58}" x2="{w/2-44}" y2="{y0+58}" stroke="#7a5f2c" stroke-width="1.5"/>')
# text paragraphs
yy = y0 + 80
for p in range(3):
    n = 3
    for i in range(n):
        ln = (w - 80) * (random.uniform(0.55, 0.85) if i == n-1 else random.uniform(0.92, 1.0))
        hl = (p == 1 and i == 1)
        if hl:
            g.append(f'<rect x="{x0-4}" y="{yy-4}" width="{ln+8}" height="15" fill="#c9a45c" opacity="0.55"/>')
        g.append(f'<rect x="{x0}" y="{yy}" width="{ln:.0f}" height="7" rx="2" fill="#4b4235" opacity="{0.9 if hl else 0.55}"/>')
        yy += 17
    yy += 14
# mini chart: target dashed line and projection curve above it
cx0, cy0, cw, ch = x0, yy + 2, w - 80, 78
g.append(f'<rect x="{cx0}" y="{cy0}" width="{cw}" height="{ch}" fill="#d9ceb7" opacity="0.55"/>')
for k in range(1, 4):
    g.append(f'<line x1="{cx0}" y1="{cy0+k*ch/4}" x2="{cx0+cw}" y2="{cy0+k*ch/4}" stroke="#8e846f" stroke-opacity="0.35"/>')
ty = cy0 + ch*0.78
g.append(f'<line x1="{cx0}" y1="{ty}" x2="{cx0+cw}" y2="{ty}" stroke="#2f5a46" stroke-width="2" stroke-dasharray="6 5"/>')
pts = []
for i in range(41):
    t = i/40
    yv = cy0 + ch*(0.40 - 0.18*math.sin(t*math.pi*0.9) + 0.30*t*t)
    pts.append((cx0 + 8 + t*(cw-16), yv))
g.append('<polyline fill="none" stroke="#9a7434" stroke-width="3.2" points="' + " ".join(f"{a:.1f},{b:.1f}" for a,b in pts) + '"/>')
for t in (0.0, 0.5, 1.0):
    a, b = pts[int(t*40)]
    g.append(f'<circle cx="{a:.1f}" cy="{b:.1f}" r="5" fill="#9a7434"/>')
g.append('</g>')
s += g

# Fountain pen lying diagonally across the right of the sheet
s.append('<g transform="translate(690,300) rotate(26)">')
s.append('<rect x="-10" y="18" width="330" height="26" rx="13" fill="#000" opacity="0.55" filter="url(#shadow)"/>')
s.append('<rect x="0" y="0" width="300" height="30" rx="15" fill="url(#pen)"/>')
s.append('<rect x="190" y="0" width="12" height="30" fill="url(#gold)"/>')
s.append('<rect x="206" y="0" width="4" height="30" fill="url(#gold)" opacity="0.8"/>')
s.append('<rect x="30" y="-3" width="140" height="6" rx="3" fill="url(#gold)"/>')
s.append('<polygon points="300,4 345,15 300,26" fill="url(#gold)"/>')
s.append('<line x1="302" y1="15" x2="344" y2="15" stroke="#5a4520" stroke-width="1.2"/>')
s.append('</g>')

# Stamp seal (wax-like, gold) near bottom-left of sheet
s.append('<g transform="translate(268,488) rotate(-12)" opacity="0.92">')
s.append('<circle r="46" fill="#000" opacity="0.5" filter="url(#shadow)"/>')
s.append('<circle r="42" fill="url(#gold)"/><circle r="33" fill="none" stroke="#6b5226" stroke-width="2"/>')
for k in range(24):
    a = k*math.pi/12
    s.append(f'<line x1="{36*math.cos(a):.1f}" y1="{36*math.sin(a):.1f}" x2="{40*math.cos(a):.1f}" y2="{40*math.sin(a):.1f}" stroke="#6b5226" stroke-width="1.5"/>')
s.append('<polygon points="0,-18 5,-6 18,-6 8,2 12,15 0,7 -12,15 -8,2 -18,-6 -5,-6" fill="#6b5226" opacity="0.8"/>')
s.append('</g>')

s.append('<rect width="100%" height="100%" fill="url(#fade)"/>')
s.append('<rect width="100%" height="100%" fill="url(#vign)"/>')
s.append('<rect width="100%" height="100%" filter="url(#grain)"/>')
s.append('</svg>')
Path(sys.argv[1]).write_text("\n".join(s)); print("ok")
