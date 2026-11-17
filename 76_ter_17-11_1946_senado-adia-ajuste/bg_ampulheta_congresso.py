"""Fundo 1080x1350: ampulheta dourada (votação adiada) diante da silhueta
do Congresso ao anoitecer, com a linha do dólar subindo no céu."""
import random, sys, math
from pathlib import Path
random.seed(1711)
W, H = 1080, 1350
HZ = 425
o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
o.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0b1019"/><stop offset="0.17" stop-color="#121a26"/>
 <stop offset="0.26" stop-color="#262630"/><stop offset="0.305" stop-color="#4a3624"/>
 <stop offset="0.335" stop-color="#21190f"/><stop offset="0.40" stop-color="#0b0b0b"/>
 <stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="glow" cx="0.5" cy="0.22" r="0.36">
 <stop offset="0" stop-color="#e0b56a" stop-opacity="0.30"/><stop offset="0.45" stop-color="#c9a45c" stop-opacity="0.08"/>
 <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="glass" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#efe6d6" stop-opacity="0.05"/><stop offset="0.25" stop-color="#efe6d6" stop-opacity="0.22"/>
 <stop offset="0.5" stop-color="#efe6d6" stop-opacity="0.06"/><stop offset="1" stop-color="#efe6d6" stop-opacity="0.14"/></linearGradient>
<linearGradient id="sand" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#f0cf8a"/><stop offset="1" stop-color="#a8823e"/></linearGradient>
<linearGradient id="wood" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#3a2a16"/><stop offset="0.45" stop-color="#c9a45c"/><stop offset="0.6" stop-color="#8c6c34"/><stop offset="1" stop-color="#2a1d0f"/></linearGradient>
<linearGradient id="tower" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#161b23"/><stop offset="0.5" stop-color="#222833"/><stop offset="1" stop-color="#11151b"/></linearGradient>
<linearGradient id="line" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.05"/><stop offset="1" stop-color="#e3c27e" stop-opacity="0.75"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.35"/><stop offset="0.12" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.32" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.375" stop-color="#0a0a0a" stop-opacity="0.8"/>
 <stop offset="0.43" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.3" r="0.8">
 <stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="9"/>
 <feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="table" tableValues="0 0.07"/></feComponentTransfer></filter>
<filter id="soft"><feGaussianBlur stdDeviation="6"/></filter>
<filter id="blur"><feGaussianBlur stdDeviation="2"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/>
<rect width="100%" height="100%" fill="url(#glow)"/>''')
for _ in range(80):
    x, y = random.uniform(0, W), random.uniform(120, 300)
    o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.choice([0.6,0.8,1.1])}" fill="#efe6d6" opacity="{random.uniform(.12,.45):.2f}"/>')

# grade fina + linha do dólar subindo (à direita)
for gy in range(170, HZ - 40, 34):
    o.append(f'<line x1="640" y1="{gy}" x2="1020" y2="{gy}" stroke="#efe6d6" stroke-opacity="0.04"/>')
pts, x, y = [], 640, 330
while x <= 1010:
    pts.append((x, y)); x += 18; y -= random.uniform(-6, 10)
o.append('<polyline points="' + " ".join(f"{a:.0f},{b:.0f}" for a, b in pts) + '" fill="none" stroke="url(#line)" stroke-width="3"/>')
lx, ly = pts[-1]
o.append(f'<circle cx="{lx:.0f}" cy="{ly:.0f}" r="6" fill="#e3c27e"/><circle cx="{lx:.0f}" cy="{ly:.0f}" r="14" fill="#e3c27e" opacity="0.18"/>')

# silhueta do Congresso no horizonte (à esquerda, pequena)
p = [(0, HZ)]
x = 0
while x < W:
    h = random.choice([3, 6, 9, 5]); w = random.randint(40, 90)
    p += [(x, HZ - h), (x + w, HZ - h)]; x += w
p += [(W, HZ), (W, HZ + 40), (0, HZ + 40)]
o.append('<polygon fill="#0d0e11" points="' + " ".join(f"{a},{b}" for a, b in p) + '"/>')
o.append(f'<rect x="60" y="{HZ-20}" width="380" height="20" fill="#1b1f26"/>')
o.append(f'<line x1="60" y1="{HZ-20}" x2="440" y2="{HZ-20}" stroke="#c9a45c" stroke-opacity="0.4"/>')
o.append(f'<path d="M110,{HZ-20} A46,30 0 0 1 202,{HZ-20} Z" fill="#3a3f48"/>')
o.append(f'<path d="M300,{HZ-62} A60,32 0 0 0 420,{HZ-62} Z" fill="#3a3f48"/>')
o.append(f'<ellipse cx="360" cy="{HZ-62}" rx="60" ry="5" fill="#1a1d22" stroke="#efe6d6" stroke-opacity="0.3"/>')
o.append(f'<rect x="352" y="{HZ-36}" width="16" height="16" fill="#1a1d22"/>')
for tx in (230, 262):
    o.append(f'<rect x="{tx}" y="{HZ-175}" width="26" height="155" fill="url(#tower)"/>')
    for yy in range(HZ - 168, HZ - 26, 9):
        for k in range(2):
            op = random.choice([0.05, 0.1, 0.2, 0.5])
            o.append(f'<rect x="{tx+4+k*10}" y="{yy}" width="7" height="4" fill="#d9b46a" opacity="{op}"/>')
o.append(f'<rect x="256" y="{HZ-110}" width="6" height="12" fill="#262b33"/>')

# ampulheta (centro)
cx, top, bot, hw = 540, 150, 400, 92
neck = (top + bot) / 2
o.append(f'<ellipse cx="{cx}" cy="{(top+bot)/2}" rx="170" ry="150" fill="#c9a45c" opacity="0.10" filter="url(#soft)"/>')
# vidro
glass = (f'M{cx-hw},{top+16} C{cx-hw},{neck-60} {cx-10},{neck-20} {cx-8},{neck} '
         f'C{cx-10},{neck+20} {cx-hw},{neck+60} {cx-hw},{bot-16} L{cx+hw},{bot-16} '
         f'C{cx+hw},{neck+60} {cx+10},{neck+20} {cx+8},{neck} C{cx+10},{neck-20} {cx+hw},{neck-60} {cx+hw},{top+16} Z')
o.append(f'<path d="{glass}" fill="#0f1218" opacity="0.85"/>')
# areia de cima (pouca, ainda escorrendo)
o.append(f'<path d="M{cx-58},{neck-58} C{cx-30},{neck-48} {cx+30},{neck-48} {cx+58},{neck-58} C{cx+40},{neck-30} {cx+12},{neck-12} {cx},{neck-4} C{cx-12},{neck-12} {cx-40},{neck-30} {cx-58},{neck-58} Z" fill="url(#sand)"/>')
# fio de areia
o.append(f'<line x1="{cx}" y1="{neck}" x2="{cx}" y2="{bot-62}" stroke="#f0cf8a" stroke-width="2.4"/>')
# monte de baixo
o.append(f'<path d="M{cx-hw+6},{bot-17} C{cx-60},{bot-40} {cx-24},{bot-64} {cx},{bot-66} C{cx+24},{bot-64} {cx+60},{bot-40} {cx+hw-6},{bot-17} Z" fill="url(#sand)"/>')
o.append(f'<path d="{glass}" fill="url(#glass)" stroke="#efe6d6" stroke-opacity="0.45" stroke-width="2"/>')
o.append(f'<path d="M{cx-hw+16},{top+30} C{cx-hw+16},{neck-70} {cx-40},{neck-40} {cx-26},{neck-18}" fill="none" stroke="#fff" stroke-opacity="0.25" stroke-width="3"/>')
# armação
for yy in (top, bot - 16):
    o.append(f'<rect x="{cx-hw-26}" y="{yy}" width="{2*hw+52}" height="16" rx="3" fill="url(#wood)"/>')
for px in (cx - hw - 16, cx + hw + 10):
    o.append(f'<rect x="{px}" y="{top+16}" width="6" height="{bot-top-32}" fill="url(#wood)"/>')
o.append(f'<rect x="{cx-hw-26}" y="{top}" width="{2*hw+52}" height="3" fill="#f0cf8a" opacity="0.5"/>')

# reflexo no chão
o.append(f'<rect x="{cx-hw-26}" y="{HZ+6}" width="{2*hw+52}" height="60" fill="#c9a45c" opacity="0.06" filter="url(#blur)"/>')
for i in range(18):
    y = HZ + 10 + i * 5
    x1 = random.uniform(60, 900); L = random.uniform(40, 200)
    o.append(f'<line x1="{x1:.0f}" y1="{y}" x2="{x1+L:.0f}" y2="{y}" stroke="#c9a45c" stroke-opacity="{random.uniform(.04,.14):.2f}"/>')

o.append('<rect width="100%" height="100%" fill="url(#fade)"/>')
o.append('<rect width="100%" height="100%" fill="url(#vign)"/>')
o.append('<rect width="100%" height="100%" filter="url(#grain)"/>')
o.append('</svg>')
Path(sys.argv[1] if len(sys.argv) > 1 else "bg.svg").write_text("\n".join(o))
