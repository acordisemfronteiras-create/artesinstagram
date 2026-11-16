"""Fundo: painel de câmbio estilo split-flap (casa de câmbio) com USD/BRL 5,78
suspenso sobre o skyline de um centro financeiro à noite."""
import random, sys
from pathlib import Path

random.seed(1611)
W, H = 1080, 1350
HZ = 430  # horizonte
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0f1622"/><stop offset="0.22" stop-color="#18202c"/>
 <stop offset="0.26" stop-color="#2b261f"/><stop offset="0.315" stop-color="#3b2d1d"/>
 <stop offset="0.36" stop-color="#0d0d0d"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<linearGradient id="flapT" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#23262b"/><stop offset="1" stop-color="#17191d"/></linearGradient>
<linearGradient id="flapB" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#131518"/><stop offset="1" stop-color="#0e0f12"/></linearGradient>
<linearGradient id="frame" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a2a2a"/><stop offset="1" stop-color="#121212"/></linearGradient>
<radialGradient id="glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#e0b468" stop-opacity="0.35"/><stop offset="1" stop-color="#e0b468" stop-opacity="0"/></radialGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0.36" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.43" stop-color="#0a0a0a" stop-opacity="0.85"/><stop offset="0.5" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.32" r="0.75"><stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.55"/></radialGradient>
<filter id="soft"><feGaussianBlur stdDeviation="14"/></filter>
<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="4"/><feColorMatrix values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0.05 0"/></filter>
</defs>''')
s.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
# estrelas
for _ in range(70):
    x, y = random.uniform(0, W), random.uniform(0, 300)
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(.5,1.3):.1f}" fill="#d8d2c4" fill-opacity="{random.uniform(.15,.55):.2f}"/>')

# skyline (silhuetas genéricas) apoiado no horizonte
def tower(x, w, h, col="#0e1218", lit=0.25):
    y = HZ - h
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{col}"/>')
    s.append(f'<line x1="{x}" y1="{y}" x2="{x+w}" y2="{y}" stroke="#c9a45c" stroke-opacity="0.18"/>')
    for wy in range(int(y) + 10, HZ - 8, 14):
        for wx in range(x + 6, x + w - 8, 12):
            if random.random() < lit:
                s.append(f'<rect x="{wx}" y="{wy}" width="5" height="7" fill="#e3b96a" fill-opacity="{random.uniform(.15,.6):.2f}"/>')
# fundo (mais claro, mais distante)
x = -10
while x < W:
    w = random.randint(40, 90); h = random.randint(70, 160)
    s.append(f'<rect x="{x}" y="{HZ-h}" width="{w}" height="{h}" fill="#141a22" fill-opacity="0.8"/>')
    x += w + random.randint(-6, 8)
# frente
for (x, w, h) in [(0,70,150),(78,58,210),(140,90,130),(236,64,250),(306,80,170),
                  (700,76,190),(782,60,260),(848,92,150),(946,62,220),(1012,80,140)]:
    tower(x, w, h)
# antena em uma torre
s.append(f'<line x1="268" y1="{HZ-250}" x2="268" y2="{HZ-292}" stroke="#3a3f47" stroke-width="2"/><circle cx="268" cy="{HZ-292}" r="3" fill="#e0574a" fill-opacity="0.8"/>')
s.append(f'<line x1="812" y1="{HZ-260}" x2="812" y2="{HZ-300}" stroke="#3a3f47" stroke-width="2"/><circle cx="812" cy="{HZ-300}" r="3" fill="#e0574a" fill-opacity="0.8"/>')

# painel split-flap suspenso
PX, PY, PW, PH = 250, 132, 580, 236
s.append(f'<ellipse cx="{PX+PW/2}" cy="{PY+PH/2+20}" rx="420" ry="190" fill="url(#glow)"/>')
for cx in (PX+PW/2-12, PX+PW/2+100):  # cabos
    s.append(f'<line x1="{cx}" y1="0" x2="{cx}" y2="{PY}" stroke="#4a4740" stroke-width="2"/>')
s.append(f'<rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" rx="10" fill="url(#frame)" stroke="#c9a45c" stroke-opacity="0.45" stroke-width="2"/>')
s.append(f'<rect x="{PX+12}" y="{PY+12}" width="{PW-24}" height="{PH-24}" rx="6" fill="#0b0c0e"/>')
# cabeçalho do painel
s.append(f'<text x="{PX+34}" y="{PY+46}" font-family="Inter,Arial,sans-serif" font-size="17" letter-spacing="5" fill="#c9a45c">USD</text>')
s.append(f'<path d="M{PX+88} {PY+40} h26 m-8 -6 l8 6 l-8 6" stroke="#c9a45c" stroke-width="2" fill="none"/>')
s.append(f'<text x="{PX+124}" y="{PY+46}" font-family="Inter,Arial,sans-serif" font-size="17" letter-spacing="5" fill="#c9a45c">BRL</text>')
s.append(f'<text x="{PX+PW-34}" y="{PY+46}" text-anchor="end" font-family="Inter,Arial,sans-serif" font-size="14" letter-spacing="4" fill="#8f8a82">VENDA · FECHAMENTO</text>')
s.append(f'<line x1="{PX+30}" y1="{PY+62}" x2="{PX+PW-30}" y2="{PY+62}" stroke="#2a2824"/>')
# flaps
chars = ["R$", "5", ",", "7", "8"]
fw = [118, 86, 44, 86, 86]
gap = 12
total = sum(fw) + gap * (len(fw) - 1)
fx = PX + (PW - total - 76) / 2
fy, fh = PY + 82, 128
for ch, w in zip(chars, fw):
    s.append(f'<rect x="{fx:.0f}" y="{fy}" width="{w}" height="{fh/2:.0f}" rx="5" fill="url(#flapT)"/>')
    s.append(f'<rect x="{fx:.0f}" y="{fy+fh/2:.0f}" width="{w}" height="{fh/2:.0f}" rx="5" fill="url(#flapB)"/>')
    col = "#e9c27a" if ch not in ("R$", ",") else "#d9cfbd"
    fs = 92 if ch != "R$" else 58
    s.append(f'<text x="{fx+w/2:.0f}" y="{fy+fh/2+ (32 if ch!="R$" else 20)}" text-anchor="middle" font-family="Fraunces,Georgia,serif" font-size="{fs}" fill="{col}">{ch}</text>')
    s.append(f'<rect x="{fx:.0f}" y="{fy+fh/2-1.5:.0f}" width="{w}" height="2" fill="#050506" fill-opacity="0.8"/>')
    for hx in (fx+6, fx+w-9):
        s.append(f'<rect x="{hx:.0f}" y="{fy+fh/2-5:.0f}" width="3" height="10" fill="#3a3a3a"/>')
    fx += w + gap
# seta de alta à direita
ax = fx + 14
s.append(f'<rect x="{ax-4}" y="{fy}" width="64" height="{fh}" rx="5" fill="#141210" stroke="#c9a45c" stroke-opacity="0.35"/>')
s.append(f'<path d="M{ax+28} {fy+30} l22 30 h-14 v40 h-16 v-40 h-14 z" fill="#c9a45c"/>')
# barra de lâmpadas embaixo do painel
for i in range(24):
    lx = PX + 40 + i * ((PW - 80) / 23)
    s.append(f'<circle cx="{lx:.0f}" cy="{PY+PH-8}" r="2.2" fill="#e3b96a" fill-opacity="{0.25 + 0.5*(i%3==0):.2f}"/>')

# linha do horizonte + reflexo
s.append(f'<rect x="0" y="{HZ}" width="{W}" height="{H-HZ}" fill="#0a0a0a"/>')
s.append(f'<rect x="0" y="{HZ}" width="{W}" height="40" fill="#08090b"/>')
s.append(f'<line x1="0" y1="{HZ}" x2="{W}" y2="{HZ}" stroke="#c9a45c" stroke-opacity="0.22"/>')
s.append(f'<ellipse cx="{W/2}" cy="{HZ+8}" rx="300" ry="14" fill="#e0b468" fill-opacity="0.10" filter="url(#soft)"/>')

s.append(f'<rect width="{W}" height="{H}" fill="url(#fade)"/>')
s.append(f'<rect width="{W}" height="{H}" fill="url(#vign)"/>')
s.append(f'<rect width="{W}" height="{H}" filter="url(#grain)"/>')
s.append('</svg>')
Path(sys.argv[1] if len(sys.argv) > 1 else 'bg.svg').write_text("\n".join(s))
print("ok")
