"""Fundo: painel de votação (353 x 128 x 5) e mesa com projeto, caneta e selo de sanção."""
import random
random.seed(24)
W, H = 1080, 1350
s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#10151d"/><stop offset="0.22" stop-color="#171c24"/>
 <stop offset="0.33" stop-color="#2a2419"/><stop offset="0.42" stop-color="#0d0c0b"/>
 <stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="glow" cx="0.5" cy="0.15" r="0.45">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.16"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="board" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0c1017"/><stop offset="1" stop-color="#080a0e"/></linearGradient>
<linearGradient id="desk" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#2b2117"/><stop offset="0.5" stop-color="#1a140e"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<linearGradient id="paper" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#d9cfbd"/><stop offset="1" stop-color="#8a8172"/></linearGradient>
<linearGradient id="pen" x1="0" y1="0" x2="1" y2="1">
 <stop offset="0" stop-color="#1b1b1d"/><stop offset="0.5" stop-color="#34343a"/><stop offset="1" stop-color="#121214"/></linearGradient>
<linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
 <stop offset="0" stop-color="#e6c784"/><stop offset="0.5" stop-color="#c9a45c"/><stop offset="1" stop-color="#8a6a32"/></linearGradient>
<radialGradient id="seal" cx="0.4" cy="0.35" r="0.7">
 <stop offset="0" stop-color="#e2c07a"/><stop offset="0.6" stop-color="#b08a45"/><stop offset="1" stop-color="#6e5226"/></radialGradient>
<radialGradient id="lamp" cx="0.5" cy="0.5" r="0.5">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.22"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.35"/><stop offset="0.1" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.27" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.335" stop-color="#0a0a0a" stop-opacity="0.85"/>
 <stop offset="0.36" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.22" r="0.75">
 <stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
<filter id="blur"><feGaussianBlur stdDeviation="2.2"/></filter>
<filter id="grain" x="0" y="0" width="100%" height="100%">
 <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="5"/>
 <feColorMatrix type="saturate" values="0"/>
 <feComponentTransfer><feFuncA type="table" tableValues="0 0.07"/></feComponentTransfer></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/>
<rect width="100%" height="100%" fill="url(#glow)"/>''')

# Painel de votação: 486 pontos (353 sim, 128 não, 5 abstenções), 54 x 9
cols, rows = 54, 9
bx0, by0, step = 138, 150, 15
bw, bh = cols*step + 28, rows*step + 28
s.append(f'<rect x="{bx0-14}" y="{by0-14}" width="{bw}" height="{bh}" rx="6" fill="url(#board)" stroke="#2e2a22" stroke-width="2"/>')
s.append(f'<rect x="{bx0-22}" y="{by0-22}" width="{bw+16}" height="{bh+16}" rx="9" fill="none" stroke="#c9a45c" stroke-opacity="0.25" stroke-width="1.2"/>')
dots_glow, dots = [], []
for i in range(cols*rows):
    c, r = i % cols, i // cols
    # preenche por coluna para formar blocos verticais legíveis
    idx = c*rows + r
    x, y = bx0 + c*step + 7, by0 + r*step + 7
    if idx < 353:
        dots.append(f'<circle cx="{x}" cy="{y}" r="4.6" fill="#c9a45c" fill-opacity="{0.78+random.random()*0.22:.2f}"/>')
        dots_glow.append(f'<circle cx="{x}" cy="{y}" r="7" fill="#c9a45c" fill-opacity="0.25"/>')
    elif idx < 353+128:
        dots.append(f'<circle cx="{x}" cy="{y}" r="4.6" fill="#5b5650" fill-opacity="0.85"/>')
    else:
        dots.append(f'<circle cx="{x}" cy="{y}" r="4.2" fill="none" stroke="#8f8a82" stroke-width="1.3"/>')
s.append('<g filter="url(#blur)">' + ''.join(dots_glow) + '</g>')
s.append(''.join(dots))
# legenda discreta sob o painel (barras)
ly = by0 + bh - 2
s.append(f'<rect x="{bx0}" y="{ly}" width="{353/486*cols*step:.0f}" height="3" fill="#c9a45c" fill-opacity="0.8"/>')
s.append(f'<rect x="{bx0+353/486*cols*step+4:.0f}" y="{ly}" width="{128/486*cols*step-4:.0f}" height="3" fill="#5b5650"/>')

# Mesa
s.append('<rect x="0" y="318" width="1080" height="140" fill="url(#desk)"/>')
s.append('<line x1="0" y1="318" x2="1080" y2="318" stroke="#c9a45c" stroke-opacity="0.35" stroke-width="1.5"/>')
s.append('<ellipse cx="540" cy="360" rx="420" ry="70" fill="url(#lamp)"/>')
# veios da madeira
for k in range(14):
    y = 326 + k*9 + random.random()*3
    s.append(f'<path d="M0 {y:.1f} Q 270 {y+random.uniform(-3,3):.1f} 540 {y:.1f} T 1080 {y:.1f}" stroke="#3a2c1e" stroke-opacity="0.35" stroke-width="1" fill="none"/>')

# Documento em perspectiva
s.append('<polygon points="408,330 672,330 716,446 364,446" fill="#000" fill-opacity="0.45" transform="translate(8,6)"/>')
s.append('<polygon points="408,330 672,330 716,446 364,446" fill="url(#paper)"/>')
def xl(y): t=(y-330)/116; return 408+(364-408)*t
def xr(y): t=(y-330)/116; return 672+(716-672)*t
# título do documento (barras)
s.append(f'<line x1="{xl(342)+60:.0f}" y1="342" x2="{xr(342)-60:.0f}" y2="342" stroke="#3a342a" stroke-width="3"/>')
for j, y in enumerate([356, 366, 376, 386, 396, 406]):
    end = xr(y)-24 - (60 if j in (2,5) else random.randint(0,20))
    s.append(f'<line x1="{xl(y)+24:.0f}" y1="{y}" x2="{end:.0f}" y2="{y}" stroke="#5a5244" stroke-width="1.6" stroke-opacity="0.8"/>')
# linha de assinatura dourada
s.append(f'<line x1="{xl(428)+40:.0f}" y1="428" x2="{xl(428)+190:.0f}" y2="428" stroke="#8a6a32" stroke-width="1.8"/>')
# rubrica sugerida (traço abstrato)
s.append(f'<path d="M{xl(428)+48:.0f} 424 c 14 -14 22 -4 30 -10 s 14 6 24 -4 s 18 2 30 -6" stroke="#2b2418" stroke-width="1.8" fill="none"/>')

# Selo de sanção (cera dourada) no canto do documento
cx, cy = 650, 420
pts = []
import math
for a in range(0, 360, 15):
    rr = 26 + (3 if (a//15) % 2 == 0 else -1)
    pts.append(f'{cx+rr*math.cos(math.radians(a)):.1f},{cy+rr*0.62*math.sin(math.radians(a)):.1f}')
s.append(f'<polygon points="{" ".join(pts)}" fill="url(#seal)" stroke="#6e5226" stroke-width="1"/>')
s.append(f'<ellipse cx="{cx}" cy="{cy}" rx="16" ry="10" fill="none" stroke="#f0d9a0" stroke-opacity="0.7" stroke-width="1.4"/>')
s.append(f'<ellipse cx="{cx}" cy="{cy}" rx="9" ry="5.5" fill="none" stroke="#6e5226" stroke-width="1.2"/>')

# Caneta-tinteiro na diagonal
s.append('<g transform="translate(792,322) rotate(128) scale(0.8)">'
         '<rect x="0" y="-9" width="150" height="18" rx="9" fill="url(#pen)"/>'
         '<rect x="58" y="-9.5" width="8" height="19" fill="url(#gold)"/>'
         '<rect x="4" y="-3" width="40" height="3" rx="1.5" fill="url(#gold)"/>'
         '<polygon points="150,-8 186,0 150,8" fill="url(#gold)"/>'
         '<line x1="160" y1="0" x2="184" y2="0" stroke="#5a4520" stroke-width="1"/>'
         '</g>')
s.append('<ellipse cx="700" cy="410" rx="60" ry="8" fill="#000" fill-opacity="0.35" filter="url(#blur)"/>')

# poeira de luz
for _ in range(60):
    x, y = random.uniform(80, 1000), random.uniform(40, 300)
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(0.6,1.6):.1f}" fill="#e6c784" fill-opacity="{random.uniform(0.08,0.3):.2f}"/>')

s.append('<rect width="100%" height="100%" fill="url(#fade)"/>')
s.append('<rect width="100%" height="100%" fill="url(#vign)"/>')
s.append('<rect width="100%" height="100%" filter="url(#grain)"/>')
s.append('</svg>')
open('bg.svg', 'w').write('\n'.join(s))
print('ok')
