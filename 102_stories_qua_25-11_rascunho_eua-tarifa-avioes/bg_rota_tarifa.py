"""Fundo Stories notícia: rota tracejada de exportação (sul -> norte) com um avião genérico
em perfil se aproximando de uma barreira alfandegária tracejada (proposta, ainda não em vigor)
e uma etiqueta dourada "10%" pendurada nela."""
import random, math
random.seed(2511)
W, H = 1080, 1920
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0e121a"/><stop offset="0.3" stop-color="#151a23"/>
 <stop offset="0.45" stop-color="#12100d"/><stop offset="0.52" stop-color="#0a0a0a"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="glow" cx="0.70" cy="0.33" r="0.36">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.18"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="fus" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#4a463e"/><stop offset="0.55" stop-color="#2a2822"/><stop offset="1" stop-color="#1a1915"/></linearGradient>
<linearGradient id="tagg" x1="0" y1="0" x2="1" y2="1">
 <stop offset="0" stop-color="#e2c47f"/><stop offset="1" stop-color="#b08d48"/></linearGradient>
<filter id="gl"><feGaussianBlur stdDeviation="14"/></filter>
<filter id="sh"><feGaussianBlur stdDeviation="8"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/><rect width="100%" height="100%" fill="url(#glow)"/>''')
for _ in range(55):
    x, y = random.uniform(0, W), random.uniform(60, 420)
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="1" fill="#d8d2c4" opacity="{random.uniform(0.1,0.35):.2f}"/>')

# --- rota tracejada: sai de baixo à esquerda e sobe em arco até a barreira à direita
P0, P1, P2 = (110, 770), (300, 450), (700, 560)
def bez(t):
    x = (1-t)**2*P0[0] + 2*(1-t)*t*P1[0] + t*t*P2[0]
    y = (1-t)**2*P0[1] + 2*(1-t)*t*P1[1] + t*t*P2[1]
    return x, y
s.append(f'<path d="M {P0[0]} {P0[1]} Q {P1[0]} {P1[1]} {P2[0]} {P2[1]}" fill="none" stroke="#8f8a82" stroke-width="2.5" stroke-dasharray="4 14" stroke-linecap="round" opacity="0.7"/>')
s.append(f'<circle cx="{P0[0]}" cy="{P0[1]}" r="9" fill="#0a0a0a" stroke="#a9a39a" stroke-width="2"/>')
s.append(f'<text x="{P0[0]+24}" y="{P0[1]+9}" font-family="Inter, sans-serif" font-size="24" letter-spacing="5" fill="#8f8a82">BRASIL</text>')

# --- avião genérico em perfil, sobre a rota (t≈0.62), inclinado na direção da curva
t = 0.60
ax, ay = bez(t)
dx = 2*(1-t)*(P1[0]-P0[0]) + 2*t*(P2[0]-P1[0])
dy = 2*(1-t)*(P1[1]-P0[1]) + 2*t*(P2[1]-P1[1])
ang = math.degrees(math.atan2(dy, dx))
plane = f'''<g transform="translate({ax:.1f},{ay-6:.1f}) rotate({ang:.1f}) scale(1.05)">
 <ellipse cx="0" cy="40" rx="150" ry="12" fill="#000" opacity="0.45" filter="url(#sh)"/>
 <path d="M -150 -6 C -120 -20, 90 -22, 128 -14 C 150 -9, 162 0, 160 6 C 156 14, 120 16, 90 16 L -140 14 C -152 12, -158 2, -150 -6 Z" fill="url(#fus)" stroke="#6a6252" stroke-width="1.5"/>
 <path d="M -130 -12 L -168 -78 L -146 -78 L -96 -16 Z" fill="#2e2b25" stroke="#6a6252" stroke-width="1.5"/>
 <path d="M -140 4 L -182 22 L -164 26 L -120 10 Z" fill="#2a2822" stroke="#5a5244" stroke-width="1.2"/>
 <path d="M -20 6 L -78 66 L -50 66 L 34 10 Z" fill="#34312a" stroke="#6a6252" stroke-width="1.5"/>
 <rect x="-62" y="16" width="40" height="15" rx="7" fill="#24221d" stroke="#5a5244" stroke-width="1.2"/>
 <path d="M 118 -12 C 136 -10, 148 -4, 152 2 L 128 2 Z" fill="#1a2230" opacity="0.9"/>'''
for i in range(9):
    plane += f'\n <rect x="{-96 + i*22}" y="-8" width="9" height="7" rx="2" fill="#c9a45c" opacity="0.5"/>'
plane += '\n</g>'
s.append(plane)

# --- barreira alfandegária tracejada (proposta) à direita
GX = 770
s.append(f'<line x1="{GX}" y1="420" x2="{GX}" y2="830" stroke="#c9a45c" stroke-width="3" stroke-dasharray="14 10" opacity="0.75"/>')
s.append(f'<line x1="{GX+90}" y1="420" x2="{GX+90}" y2="830" stroke="#c9a45c" stroke-width="3" stroke-dasharray="14 10" opacity="0.45"/>')
for yy in (470, 610, 750):
    s.append(f'<line x1="{GX}" y1="{yy}" x2="{GX+90}" y2="{yy}" stroke="#5a5244" stroke-width="2" stroke-dasharray="6 8"/>')
s.append(f'<text x="{GX+45}" y="405" text-anchor="middle" font-family="Inter, sans-serif" font-size="24" letter-spacing="5" fill="#8f8a82">EUA</text>')

# --- etiqueta dourada "10%" pendurada na barreira
TX, TY = GX + 45, 560
s.append(f'<line x1="{GX}" y1="500" x2="{TX-40}" y2="{TY-46}" stroke="#a9a39a" stroke-width="1.5"/>')
s.append(f'<line x1="{GX+90}" y1="500" x2="{TX+40}" y2="{TY-46}" stroke="#a9a39a" stroke-width="1.5"/>')
s.append(f'<circle cx="{TX}" cy="{TY+40}" r="90" fill="#c9a45c" opacity="0.25" filter="url(#gl)"/>')
s.append(f'<g transform="translate({TX},{TY}) rotate(4)">'
         '<path d="M -70 -40 L 70 -40 L 70 110 L 0 140 L -70 110 Z" fill="url(#tagg)" stroke="#f1dfae" stroke-width="1.5"/>'
         '<circle cx="0" cy="-16" r="9" fill="#0a0a0a" opacity="0.85"/>'
         '<text x="0" y="62" text-anchor="middle" font-family="Georgia, serif" font-size="54" font-weight="600" fill="#0a0a0a">10%</text>'
         '<text x="0" y="96" text-anchor="middle" font-family="Inter, sans-serif" font-size="15" letter-spacing="3" font-weight="600" fill="#2a2418">PROPOSTA</text>'
         '</g>')

# chão
s.append('<line x1="70" y1="858" x2="1010" y2="858" stroke="#2a2824" stroke-width="1.5"/>')
s.append('<rect y="858" width="1080" height="1062" fill="#0a0a0a"/>')
s.append('</svg>')
open(__file__.replace("bg_rota_tarifa.py", "bg.svg"), "w").write("\n".join(s))
