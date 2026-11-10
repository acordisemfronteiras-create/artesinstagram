"""Fundo: fachada neoclássica genérica (banco central americano) sob gráfico de inflação em alta."""
import random
from pathlib import Path
random.seed(11)
W, H = 1080, 1350
o = []
o.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
o.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0f1622"/><stop offset="0.30" stop-color="#18212e"/>
 <stop offset="0.40" stop-color="#2a2620"/><stop offset="0.44" stop-color="#33281b"/>
 <stop offset="0.52" stop-color="#0c0c0c"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<linearGradient id="marble" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#1c1d21"/><stop offset="0.5" stop-color="#2b2b2e"/><stop offset="1" stop-color="#18191c"/></linearGradient>
<linearGradient id="col" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#2e2e31"/><stop offset="0.35" stop-color="#4a4844"/><stop offset="0.6" stop-color="#3a3936"/><stop offset="1" stop-color="#1e1e20"/></linearGradient>
<linearGradient id="warm" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.55"/><stop offset="1" stop-color="#7a5a26" stop-opacity="0.25"/></linearGradient>
<linearGradient id="area" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.22"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></linearGradient>
<radialGradient id="glow" cx="0.5" cy="0.34" r="0.45">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.16"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.35"/><stop offset="0.12" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.31" stop-color="#0a0a0a" stop-opacity="0.04"/><stop offset="0.39" stop-color="#0a0a0a" stop-opacity="0.75"/>
 <stop offset="0.44" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.3" r="0.8">
 <stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
<filter id="blur"><feGaussianBlur stdDeviation="6"/></filter>
</defs>''')
o.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
o.append(f'<rect width="{W}" height="{H}" fill="url(#glow)"/>')
# estrelas discretas
for _ in range(70):
    x, y = random.uniform(0, W), random.uniform(0, 300)
    o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(.5,1.3):.1f}" fill="#d8cfbf" opacity="{random.uniform(.15,.5):.2f}"/>')
# grade de gráfico no céu
for gy in range(140, 520, 60):
    o.append(f'<line x1="60" y1="{gy}" x2="1020" y2="{gy}" stroke="#c9a45c" stroke-opacity="0.07" stroke-width="1"/>')
for gx in range(60, 1030, 80):
    o.append(f'<line x1="{gx}" y1="120" x2="{gx}" y2="520" stroke="#c9a45c" stroke-opacity="0.05" stroke-width="1"/>')
# linha de inflação subindo (mensal)
pts = [(60,430),(140,418),(220,425),(300,402),(380,408),(460,380),(540,388),(620,350),(700,330),(780,300),(860,262),(940,226),(1010,196)]
d = "M" + " L".join(f"{x},{y}" for x, y in pts)
area = d + f" L1010,520 L60,520 Z"
o.append(f'<path d="{area}" fill="url(#area)"/>')
o.append(f'<path d="{d}" fill="none" stroke="#c9a45c" stroke-width="10" stroke-opacity="0.25" filter="url(#blur)"/>')
o.append(f'<path d="{d}" fill="none" stroke="#c9a45c" stroke-width="3.2" stroke-linejoin="round"/>')
for x, y in pts[:-1]:
    o.append(f'<circle cx="{x}" cy="{y}" r="4" fill="#0f1622" stroke="#c9a45c" stroke-width="2"/>')
x, y = pts[-1]
o.append(f'<circle cx="{x}" cy="{y}" r="16" fill="#c9a45c" opacity="0.18"/><circle cx="{x}" cy="{y}" r="7" fill="#e3c27f"/>')
# barras de câmbio discretas no rodapé do gráfico (volume)
for i, gx in enumerate(range(70, 1010, 26)):
    hgt = 8 + (i * 7919 % 23) + i * 0.6
    o.append(f'<rect x="{gx}" y="{520-hgt:.0f}" width="14" height="{hgt:.0f}" fill="#c9a45c" opacity="0.08"/>')
# ---- edifício neoclássico ----
o.append('<g transform="translate(0,-40)">')
L, R = 250, 830
o.append(f'<rect x="0" y="540" width="{W}" height="40" fill="#0d0d0e"/>')
# alas laterais baixas
o.append('<rect x="40" y="430" width="230" height="115" fill="#151517"/><rect x="810" y="430" width="230" height="115" fill="#151517"/>')
for bx in (60, 830):
    for j in range(5):
        for k in range(2):
            lit = random.random() < 0.35
            o.append(f'<rect x="{bx+12+j*40}" y="{448+k*46}" width="18" height="28" fill="{"#b88f4a" if lit else "#1f2024"}" opacity="{0.75 if lit else 1}"/>')
# frontão
o.append(f'<polygon points="{L-20},350 {(L+R)/2},268 {R+20},350" fill="#232326" stroke="#3d3b37" stroke-width="2"/>')
o.append(f'<polygon points="{L+30},343 {(L+R)/2},287 {R-30},343" fill="none" stroke="#c9a45c" stroke-opacity="0.35" stroke-width="1.5"/>')
# entablamento
o.append(f'<rect x="{L-24}" y="350" width="{R-L+48}" height="40" fill="url(#marble)" stroke="#3d3b37" stroke-width="1.5"/>')
o.append(f'<line x1="{L-24}" y1="372" x2="{R+24}" y2="372" stroke="#46433e" stroke-width="1"/>')
for gx in range(L-10, R+20, 22):
    o.append(f'<rect x="{gx}" y="376" width="8" height="10" fill="#141416"/>')
# interior iluminado atrás das colunas
o.append(f'<rect x="{L}" y="390" width="{R-L}" height="140" fill="#100f0e"/>')
n = 8
gap = (R - L) / (n - 1)
for i in range(n - 1):
    cx = L + gap * i + gap / 2
    o.append(f'<rect x="{cx-22:.0f}" y="420" width="44" height="96" fill="url(#warm)"/>')
    o.append(f'<line x1="{cx:.0f}" y1="420" x2="{cx:.0f}" y2="516" stroke="#0f0e0c" stroke-width="2"/>')
    o.append(f'<line x1="{cx-22:.0f}" y1="452" x2="{cx+22:.0f}" y2="452" stroke="#0f0e0c" stroke-width="2"/>')
# colunas
for i in range(n):
    cx = L + gap * i
    o.append(f'<rect x="{cx-17:.0f}" y="392" width="34" height="138" fill="url(#col)"/>')
    for f in (-9, -3, 3, 9):
        o.append(f'<line x1="{cx+f:.0f}" y1="398" x2="{cx+f:.0f}" y2="526" stroke="#151516" stroke-opacity="0.45" stroke-width="1.2"/>')
    o.append(f'<rect x="{cx-23:.0f}" y="388" width="46" height="8" fill="#4a4844"/>')
    o.append(f'<rect x="{cx-22:.0f}" y="526" width="44" height="8" fill="#3a3936"/>')
# escadaria
for s in range(4):
    o.append(f'<rect x="{L-40-s*14}" y="{534+s*6}" width="{R-L+80+s*28}" height="6" fill="{["#2c2b29","#252422","#1e1d1c","#171716"][s]}"/>')
# reflexo dourado no topo do frontão
o.append(f'<circle cx="{(L+R)/2}" cy="268" r="3" fill="#e3c27f"/>')
# mastros sem bandeira
for fx in (180, 900):
    o.append(f'<line x1="{fx}" y1="300" x2="{fx}" y2="430" stroke="#5a5650" stroke-width="2"/>')
o.append('</g>')
o.append(f'<rect width="{W}" height="{H}" fill="url(#fade)"/>')
o.append(f'<rect width="{W}" height="{H}" fill="url(#vign)"/>')
o.append('</svg>')
Path(__file__).with_name("bg.svg").write_text("\n".join(o))
print("ok")
