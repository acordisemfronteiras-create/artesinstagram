"""Fundo: hemiciclo de 513 cadeiras, com as 257 da maioria absoluta acesas em dourado.
Uso: python3 bg_hemiciclo_quorum.py bg.svg
"""
import math, random, sys
from pathlib import Path

random.seed(22)
W, H = 1080, 1350
CX, CY = 540, 462          # centro do hemiciclo (linha do piso)
R_IN, R_OUT = 116, 312
ROWS = 12
TOTAL, MAIOR = 513, 257

svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
svg.append('''
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#10161f"/>
    <stop offset="0.22" stop-color="#151c27"/>
    <stop offset="0.33" stop-color="#1c1d22"/>
    <stop offset="0.40" stop-color="#21190f"/>
    <stop offset="0.50" stop-color="#0c0c0c"/>
    <stop offset="1" stop-color="#0a0a0a"/>
  </linearGradient>
  <radialGradient id="glow" cx="0.5" cy="0.33" r="0.42">
    <stop offset="0" stop-color="#c9a45c" stop-opacity="0.20"/>
    <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="seatG" cx="0.4" cy="0.35" r="0.7">
    <stop offset="0" stop-color="#f0cf86"/>
    <stop offset="1" stop-color="#b48a3e"/>
  </radialGradient>
  <filter id="bloom" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3.2"/></filter>
  <filter id="soft"><feGaussianBlur stdDeviation="1.4"/></filter>
  <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.30"/>
    <stop offset="0.12" stop-color="#0a0a0a" stop-opacity="0"/>
    <stop offset="0.33" stop-color="#0a0a0a" stop-opacity="0"/>
    <stop offset="0.40" stop-color="#0a0a0a" stop-opacity="0.75"/>
    <stop offset="0.46" stop-color="#0a0a0a" stop-opacity="1"/>
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
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/>
<rect width="100%" height="100%" fill="url(#glow)"/>
''')

# arquitetura ao fundo: parede curva com painéis verticais (sem marcas)
for i in range(46):
    a = math.pi * (i / 45)
    x = CX - math.cos(a) * 470
    op = 0.05 + 0.06 * math.sin(a)
    svg.append(f'<line x1="{x:.1f}" y1="60" x2="{x:.1f}" y2="{CY-10}" stroke="#8a96a6" stroke-opacity="{op:.3f}" stroke-width="2"/>')
# arcos de anéis concêntricos (teto)
for k in range(5):
    r = 520 + k * 60
    svg.append(f'<path d="M {CX-r} {CY+80} A {r} {r*0.62:.1f} 0 0 1 {CX+r} {CY+80}" fill="none" '
               f'stroke="#c9a45c" stroke-opacity="{0.05 + 0.02*k:.2f}" stroke-width="1.2"/>')

# distribuição de cadeiras por fileira, proporcional ao raio
radii = [R_IN + (R_OUT - R_IN) * i / (ROWS - 1) for i in range(ROWS)]
tot_r = sum(radii)
counts = [round(TOTAL * r / tot_r) for r in radii]
counts[-1] += TOTAL - sum(counts)
seats = []
for r, n in zip(radii, counts):
    for j in range(n):
        a = math.pi * (j + 0.5) / n          # 0 = esquerda, pi = direita
        seats.append((a, r))
seats.sort(key=lambda s: (s[0], -s[1]))     # ordena da esquerda para a direita
seat_r = 5.0

# tribuna/mesa no centro do piso
svg.append(f'<path d="M {CX-R_IN+30} {CY} A {R_IN-30} {R_IN-30} 0 0 1 {CX+R_IN-30} {CY} Z" fill="#0f1116"/>')
svg.append(f'<rect x="{CX-70}" y="{CY-34}" width="140" height="22" rx="3" fill="#1b1d22" stroke="#c9a45c" stroke-opacity="0.35"/>')
svg.append(f'<rect x="{CX-56}" y="{CY-30}" width="112" height="3" fill="#c9a45c" fill-opacity="0.35"/>')

# fileiras (degraus) sob as cadeiras
for r in radii:
    svg.append(f'<path d="M {CX-r-9:.1f} {CY} A {r+9:.1f} {r+9:.1f} 0 0 1 {CX+r+9:.1f} {CY}" fill="none" stroke="#2a2a2e" stroke-opacity="0.55" stroke-width="1"/>')

lit, dim = [], []
for idx, (a, r) in enumerate(seats):
    x = CX - math.cos(a) * r
    y = CY - math.sin(a) * r
    (lit if idx < MAIOR else dim).append((x, y))

# brilho por baixo das cadeiras acesas
svg.append('<g filter="url(#bloom)" opacity="0.55">')
for x, y in lit:
    svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{seat_r+1.5}" fill="#c9a45c"/>')
svg.append('</g>')
for x, y in lit:
    svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{seat_r}" fill="url(#seatG)"/>')
for x, y in dim:
    svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{seat_r}" fill="#2c2f36" stroke="#4a4f59" stroke-opacity="0.6" stroke-width="0.8"/>')

# linha da maioria (eixo central), tracejada
svg.append(f'<line x1="{CX}" y1="{CY-R_OUT-16}" x2="{CX}" y2="{CY-R_IN+20}" stroke="#e8c983" stroke-opacity="0.75" stroke-width="1.6" stroke-dasharray="5 6"/>')
svg.append(f'<circle cx="{CX}" cy="{CY-R_OUT-20}" r="4" fill="#e8c983"/>')

# piso
svg.append(f'<rect x="0" y="{CY+2}" width="{W}" height="90" fill="#08090b"/>')
svg.append(f'<line x1="0" y1="{CY+2}" x2="{W}" y2="{CY+2}" stroke="#c9a45c" stroke-opacity="0.22"/>')
# reflexo suave do hemiciclo
svg.append(f'<g opacity="0.12" filter="url(#soft)" transform="translate(0,{2*CY+4}) scale(1,-1)">')
for x, y in lit[::2]:
    svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{seat_r}" fill="#c9a45c"/>')
svg.append('</g>')

svg.append('<rect width="100%" height="100%" fill="url(#fade)"/>')
svg.append('<rect width="100%" height="100%" fill="url(#vign)"/>')
svg.append('<rect width="100%" height="100%" filter="url(#grain)"/>')
svg.append('</svg>')
Path(sys.argv[1] if len(sys.argv) > 1 else "bg.svg").write_text("\n".join(svg))
print("ok", len(lit), len(dim))
