"""Fundo: sala de análise com quatro painéis (inflação, atividade, câmbio, juros)
para o post do Boletim Focus. Ilustração própria, sem marcas."""
import random, sys
random.seed(1311)
W, H = 1080, 1350
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0e141d"/><stop offset="0.22" stop-color="#171f2b"/>
 <stop offset="0.31" stop-color="#241f1b"/><stop offset="0.34" stop-color="#0f0e0d"/>
 <stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="glow" cx="0.5" cy="0.2" r="0.55">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.16"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="panel" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#1b2431"/><stop offset="1" stop-color="#10151d"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.35"/><stop offset="0.12" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.31" stop-color="#0a0a0a" stop-opacity="0.1"/><stop offset="0.40" stop-color="#0a0a0a" stop-opacity="0.85"/>
 <stop offset="0.45" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.28" r="0.8">
 <stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
<filter id="grain" x="0" y="0" width="100%" height="100%">
 <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="8"/><feColorMatrix type="saturate" values="0"/>
 <feComponentTransfer><feFuncA type="table" tableValues="0 0.07"/></feComponentTransfer></filter>
<filter id="gl"><feGaussianBlur stdDeviation="3"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/><rect width="100%" height="100%" fill="url(#glow)"/>''')

# skyline distante (janela)
x = 0
while x < W:
    w = random.randint(30, 70); h = random.randint(30, 120)
    s.append(f'<rect x="{x}" y="{330-h}" width="{w}" height="{h+40}" fill="#10151c" opacity="0.8"/>')
    for wy in range(330 - h + 8, 330, 12):
        for wx in range(x + 5, x + w - 5, 10):
            if random.random() < 0.08:
                s.append(f'<rect x="{wx}" y="{wy}" width="3" height="5" fill="#c9a45c" fill-opacity="0.4"/>')
    x += w + random.randint(0, 6)

# quatro painéis
px0, pw, gap, py, ph = 100, 200, 26, 150, 210
kinds = ['line_up', 'bars', 'line_fx', 'steps']
for i, k in enumerate(kinds):
    x0 = px0 + i * (pw + gap)
    s.append(f'<rect x="{x0-6}" y="{py-6}" width="{pw+12}" height="{ph+12}" rx="4" fill="#0b0e13" stroke="#2a313c" stroke-width="1.5"/>')
    s.append(f'<rect x="{x0}" y="{py}" width="{pw}" height="{ph}" fill="url(#panel)"/>')
    for gy in range(py + 40, py + ph, 40):
        s.append(f'<line x1="{x0+8}" y1="{gy}" x2="{x0+pw-8}" y2="{gy}" stroke="#c9a45c" stroke-opacity="0.07"/>')
    s.append(f'<rect x="{x0+14}" y="{py+14}" width="46" height="5" fill="#c9a45c" fill-opacity="0.7"/>')
    s.append(f'<rect x="{x0+14}" y="{py+26}" width="26" height="3" fill="#8f8a82" fill-opacity="0.5"/>')
    bx0, bx1, by0, by1 = x0 + 16, x0 + pw - 16, py + 60, py + ph - 22
    n = 9
    if k == 'bars':
        vs = [0.55, 0.7, 0.6, 0.8, 0.72, 0.62, 0.5, 0.58, 0.46]
        bw = (bx1 - bx0) / n
        for j, v in enumerate(vs):
            hh = (by1 - by0) * v
            s.append(f'<rect x="{bx0 + j*bw + 3:.1f}" y="{by1-hh:.1f}" width="{bw-6:.1f}" height="{hh:.1f}" fill="#c9a45c" fill-opacity="{0.25 + 0.5*(j==n-1):.2f}"/>')
        continue
    if k == 'steps':
        lv = [0.2, 0.2, 0.55, 0.55, 0.55, 0.9, 0.9, 0.9, 0.9]
        pts = [(bx0 + (bx1-bx0)*j/(n-1), by1 - (by1-by0)*v) for j, v in enumerate(lv)]
        d = f'M{pts[0][0]:.1f},{pts[0][1]:.1f}'
        for (xa, ya), (xb, yb) in zip(pts, pts[1:]):
            d += f' L{xb:.1f},{ya:.1f} L{xb:.1f},{yb:.1f}'
    else:
        vs = {'line_up': [0.3, 0.4, 0.38, 0.5, 0.6, 0.55, 0.7, 0.66, 0.78],
              'line_fx': [0.6, 0.5, 0.58, 0.45, 0.52, 0.4, 0.5, 0.44, 0.36]}[k]
        pts = [(bx0 + (bx1-bx0)*j/(n-1), by1 - (by1-by0)*v) for j, v in enumerate(vs)]
        d = 'M' + ' L'.join(f'{a:.1f},{b:.1f}' for a, b in pts)
    s.append(f'<path d="{d}" fill="none" stroke="#c9a45c" stroke-width="6" stroke-opacity="0.22" filter="url(#gl)"/>')
    s.append(f'<path d="{d}" fill="none" stroke="#c9a45c" stroke-width="2.2" stroke-linejoin="round"/>')
    ex, ey = pts[-1]
    s.append(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="4.5" fill="#0f1620" stroke="#e2c47f" stroke-width="2"/>')

# luz difusa dos painéis na mesa
s.append('<rect x="80" y="372" width="920" height="6" fill="#c9a45c" fill-opacity="0.10" filter="url(#gl)"/>')
# mesa longa em perspectiva
s.append('<path d="M0,392 L1080,392 L1080,470 L0,470 Z" fill="#0e0e0f"/>')
s.append('<line x1="0" y1="392" x2="1080" y2="392" stroke="#2a2824" stroke-width="2"/>')
# monitores/laptops de mesa (silhuetas) e abajures
for lx in [150, 360, 580, 800, 930]:
    s.append(f'<path d="M{lx},392 L{lx+10},366 L{lx+70},366 L{lx+80},392 Z" fill="#12151a" stroke="#262b33"/>')
    s.append(f'<rect x="{lx+14}" y="370" width="52" height="18" fill="#c9a45c" fill-opacity="0.16"/>')
for lx in [265, 690]:
    s.append(f'<line x1="{lx}" y1="392" x2="{lx}" y2="350" stroke="#2a2f37" stroke-width="3"/><circle cx="{lx}" cy="346" r="7" fill="#c9a45c" fill-opacity="0.8"/>')
    s.append(f'<circle cx="{lx}" cy="346" r="26" fill="#c9a45c" fill-opacity="0.10" filter="url(#gl)"/>')
s.append('<rect width="100%" height="100%" fill="url(#fade)"/><rect width="100%" height="100%" fill="url(#vign)"/><rect width="100%" height="100%" filter="url(#grain)"/></svg>')
open(sys.argv[1] if len(sys.argv) > 1 else 'bg.svg', 'w').write('\n'.join(s))
