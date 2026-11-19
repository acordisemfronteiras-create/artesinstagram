"""Fundo do post 19/11/2026 (noite): dólar fecha a R$ 5,93 mesmo com venda
à vista de US$ 1 bi das reservas pelo BC.
Ilustração: porta de cofre circular aberta (reservas) num salão de mármore,
com maços de cédulas genéricas saindo em luz dourada, e no alto uma escada de
seis degraus em alta (seis altas seguidas do dólar). Sem moedas reais."""
import math, random
from pathlib import Path

random.seed(1911)
W, H = 1080, 1350
HZ = 400
o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
o.append('''<defs>
<linearGradient id="wall" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#11151b"/><stop offset="0.2" stop-color="#1a1c20"/>
 <stop offset="0.31" stop-color="#231f19"/><stop offset="0.36" stop-color="#0d0d0d"/>
 <stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="vaultglow" cx="0.5" cy="0.5" r="0.5">
 <stop offset="0" stop-color="#f3d28c" stop-opacity="0.95"/><stop offset="0.35" stop-color="#d9a955" stop-opacity="0.55"/>
 <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="door" x1="0" y1="0" x2="1" y2="1">
 <stop offset="0" stop-color="#3a3530"/><stop offset="0.5" stop-color="#25221f"/><stop offset="1" stop-color="#151413"/></linearGradient>
<linearGradient id="doorEdge" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#5a4f40"/><stop offset="1" stop-color="#2a2622"/></linearGradient>
<linearGradient id="step" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#d8b46c"/><stop offset="1" stop-color="#7a6236"/></linearGradient>
<linearGradient id="note" x1="0" y1="0" x2="1" y2="1">
 <stop offset="0" stop-color="#cdbf97"/><stop offset="1" stop-color="#8f8463"/></linearGradient>
<linearGradient id="floor" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#2a241b"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0.33" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.41" stop-color="#0a0a0a" stop-opacity="0.85"/>
 <stop offset="0.47" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.28" r="0.8"><stop offset="0.5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
<filter id="soft"><feGaussianBlur stdDeviation="16"/></filter>
<filter id="blur2"><feGaussianBlur stdDeviation="2"/></filter>
</defs>''')
o.append(f'<rect width="{W}" height="{H}" fill="url(#wall)"/>')

# painéis de pedra na parede (juntas)
for y in range(40, HZ, 62):
    o.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#2a2723" stroke-opacity="0.45" stroke-width="1"/>')
    off = 0 if (y // 62) % 2 else 90
    for x in range(off, W, 180):
        o.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{min(y+62,HZ)}" stroke="#2a2723" stroke-opacity="0.35" stroke-width="1"/>')

# colunas laterais
for cx in (70, 1010):
    o.append(f'<rect x="{cx-34}" y="60" width="68" height="{HZ-60}" fill="#1b1a18" stroke="#3a342b" stroke-width="1.2"/>')
    for k in range(-2, 3):
        o.append(f'<line x1="{cx+k*11}" y1="78" x2="{cx+k*11}" y2="{HZ-12}" stroke="#2c2924" stroke-width="2"/>')
    o.append(f'<rect x="{cx-44}" y="52" width="88" height="16" fill="#2a2620"/>')
    o.append(f'<rect x="{cx-44}" y="{HZ-14}" width="88" height="14" fill="#2a2620"/>')

# cofre: abertura circular com brilho
VX, VY, VR = 700, 225, 128
o.append(f'<circle cx="{VX}" cy="{VY}" r="{VR*2.1}" fill="url(#vaultglow)" opacity="0.55" filter="url(#soft)"/>')
o.append(f'<circle cx="{VX}" cy="{VY}" r="{VR+22}" fill="#1c1a17" stroke="#4d4234" stroke-width="3"/>')
for a in range(0, 360, 15):
    r1, r2 = VR + 6, VR + 20
    x1, y1 = VX + r1*math.cos(math.radians(a)), VY + r1*math.sin(math.radians(a))
    x2, y2 = VX + r2*math.cos(math.radians(a)), VY + r2*math.sin(math.radians(a))
    o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#3b342b" stroke-width="2"/>')
o.append(f'<circle cx="{VX}" cy="{VY}" r="{VR}" fill="#f0cf8a"/>')
o.append(f'<circle cx="{VX}" cy="{VY}" r="{VR}" fill="url(#vaultglow)"/>')
# interior: prateleiras com maços
for i, yy in enumerate((VY-70, VY-10, VY+50)):
    half = math.sqrt(max(VR**2 - (yy-VY)**2, 0)) - 18
    o.append(f'<rect x="{VX-half:.0f}" y="{yy+30}" width="{2*half:.0f}" height="5" fill="#8a6c3a" opacity="0.7"/>')
    n = int(2*half // 44)
    for j in range(n):
        bx = VX - half + 6 + j*44
        o.append(f'<rect x="{bx:.0f}" y="{yy+8}" width="38" height="22" rx="2" fill="#b39a63" stroke="#7d6638" stroke-width="1.2" opacity="0.85"/>')
        o.append(f'<rect x="{bx+15:.0f}" y="{yy+8}" width="8" height="22" fill="#6e5a33" opacity="0.8"/>')

# porta aberta (elipse em perspectiva, à esquerda da abertura)
DX = VX - VR - 70
o.append(f'<ellipse cx="{DX+8}" cy="{VY}" rx="58" ry="{VR+20}" fill="url(#doorEdge)"/>')
o.append(f'<ellipse cx="{DX}" cy="{VY}" rx="54" ry="{VR+16}" fill="url(#door)" stroke="#5c5142" stroke-width="2"/>')
o.append(f'<ellipse cx="{DX}" cy="{VY}" rx="36" ry="{VR-20}" fill="none" stroke="#4a4136" stroke-width="2"/>')
for a in range(0, 360, 60):
    x2 = DX + 30*math.cos(math.radians(a))*0.6
    y2 = VY + (VR-30)*math.sin(math.radians(a))*0.6
    o.append(f'<line x1="{DX}" y1="{VY}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#6b5c46" stroke-width="5" stroke-linecap="round"/>')
o.append(f'<ellipse cx="{DX}" cy="{VY}" rx="10" ry="22" fill="#8a7556"/>')
# dobradiças
for dy in (-90, 90):
    o.append(f'<rect x="{VX-VR-30}" y="{VY+dy-14}" width="30" height="28" rx="4" fill="#3e372e" stroke="#5a4f40"/>')

# feixe de luz saindo do cofre até o chão
o.append(f'<polygon points="{VX-VR+30},{VY+60} {VX+VR-30},{VY+60} {VX+250},{HZ+40} {VX-250},{HZ+40}" fill="#e7c27a" opacity="0.10"/>')

# cédulas genéricas flutuando para fora do cofre (rumo à esquerda/acima)
notes = [(525, 160, -18), (490, 228, 12), (528, 300, -24), (585, 345, 16), (655, 365, 30),
         (775, 362, 8), (860, 318, -14), (885, 185, 20)]
for x, y, rot in notes:
    o.append(f'<g transform="translate({x} {y}) rotate({rot})" opacity="0.92">'
             f'<rect x="-34" y="-16" width="68" height="32" rx="2" fill="url(#note)" stroke="#6f6448" stroke-width="1"/>'
             f'<rect x="-28" y="-11" width="56" height="22" fill="none" stroke="#6f6448" stroke-width="0.8"/>'
             f'<circle cx="0" cy="0" r="7" fill="none" stroke="#6f6448" stroke-width="1"/></g>')

# escada de 6 degraus em alta (canto superior esquerdo)
SX, SB, SWd = 150, 318, 38
heights = [34, 52, 72, 94, 118, 146]
for i, hgt in enumerate(heights):
    x = SX + i*(SWd+8)
    o.append(f'<rect x="{x}" y="{SB-hgt}" width="{SWd}" height="{hgt}" fill="url(#step)" opacity="{0.45+i*0.09:.2f}"/>')
    o.append(f'<rect x="{x}" y="{SB-hgt}" width="{SWd}" height="3" fill="#f2d79c"/>')
# seta subindo
pts = [(SX + i*(SWd+8) + SWd/2, SB - h - 20) for i, h in enumerate(heights)]
path = " ".join(f"{'M' if i == 0 else 'L'}{x:.0f},{y:.0f}" for i, (x, y) in enumerate(pts))
o.append(f'<path d="{path}" fill="none" stroke="#f2d79c" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
ex, ey = pts[-1]
o.append(f'<polygon points="{ex+16},{ey-14} {ex-4},{ey-12} {ex+10},{ey+6}" fill="#f2d79c"/>')
for x, y in pts:
    o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="4" fill="#f2d79c"/>')
o.append(f'<line x1="{SX-10}" y1="{SB}" x2="{SX+6*(SWd+8)}" y2="{SB}" stroke="#5a4f40" stroke-width="2"/>')

# piso de mármore em perspectiva
o.append(f'<rect x="0" y="{HZ}" width="{W}" height="{H-HZ}" fill="url(#floor)"/>')
VPX = 540
for k in range(-12, 13):
    x2 = VPX + k*160
    o.append(f'<line x1="{VPX + k*14}" y1="{HZ}" x2="{x2}" y2="{HZ+260}" stroke="#4a3f2f" stroke-opacity="0.35" stroke-width="1"/>')
for j, yy in enumerate((HZ+14, HZ+34, HZ+62, HZ+100, HZ+150)):
    o.append(f'<line x1="0" y1="{yy}" x2="{W}" y2="{yy}" stroke="#4a3f2f" stroke-opacity="{0.35-j*0.05:.2f}" stroke-width="1"/>')
o.append(f'<line x1="0" y1="{HZ}" x2="{W}" y2="{HZ}" stroke="#6a5a40" stroke-opacity="0.6" stroke-width="1.5"/>')
# reflexo do cofre no piso
o.append(f'<ellipse cx="{VX}" cy="{HZ+30}" rx="230" ry="26" fill="#e7c27a" opacity="0.18" filter="url(#soft)"/>')

o.append(f'<rect width="{W}" height="{H}" fill="url(#fade)"/>')
o.append(f'<rect width="{W}" height="{H}" fill="url(#vign)"/>')
o.append('</svg>')
Path(__file__).with_name('bg.svg').write_text("\n".join(o))
print("ok")
