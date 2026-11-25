"""Fundo: Esplanada dos Ministérios ao entardecer, em perspectiva central,
com blocos de ministérios convergindo para o Congresso ao longe.
Algumas janelas voltam a acender (liberação de recursos)."""
import random, sys
from pathlib import Path

random.seed(25)
W, H = 1080, 1350
HZ = 392          # linha do horizonte
CX = 540          # ponto de fuga
F = 720           # distância focal
CAM = 22          # altura da câmera (m)

def P(X, Y, Z):
    return (CX + X * F / Z, HZ + (CAM - Y) * F / Z)

def poly(pts, **kw):
    attrs = " ".join(f'{k.replace("_","-")}="{v}"' for k, v in kw.items())
    return '<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f'" {attrs}/>'

def line(a, b, **kw):
    attrs = " ".join(f'{k.replace("_","-")}="{v}"' for k, v in kw.items())
    return f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" {attrs}/>'

s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0d131d"/><stop offset="0.17" stop-color="#18202c"/>
 <stop offset="0.25" stop-color="#2c2a2a"/><stop offset="0.29" stop-color="#5a4127"/>
 <stop offset="0.31" stop-color="#3a2c1e"/><stop offset="0.5" stop-color="#0c0c0c"/>
 <stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="sun" cx="0.5" cy="0.29" r="0.42">
 <stop offset="0" stop-color="#e0b56a" stop-opacity="0.55"/>
 <stop offset="0.25" stop-color="#c9a45c" stop-opacity="0.18"/>
 <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="slabL" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#151b24"/><stop offset="1" stop-color="#232a33"/></linearGradient>
<linearGradient id="slabR" x1="1" y1="0" x2="0" y2="0">
 <stop offset="0" stop-color="#131921"/><stop offset="1" stop-color="#20272f"/></linearGradient>
<linearGradient id="lawn" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#2a2a22"/><stop offset="1" stop-color="#0d0f0c"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.35"/>
 <stop offset="0.12" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.31" stop-color="#0a0a0a" stop-opacity="0.04"/>
 <stop offset="0.39" stop-color="#0a0a0a" stop-opacity="0.75"/>
 <stop offset="0.45" stop-color="#0a0a0a" stop-opacity="1"/>
 <stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.28" r="0.8">
 <stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.65"/></radialGradient>
<filter id="grain" x="0" y="0" width="100%" height="100%">
 <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="5"/>
 <feColorMatrix type="saturate" values="0"/>
 <feComponentTransfer><feFuncA type="table" tableValues="0 0.07"/></feComponentTransfer></filter>
<filter id="soft"><feGaussianBlur stdDeviation="1.4"/></filter>
<filter id="glow"><feGaussianBlur stdDeviation="3"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/>
<rect width="100%" height="100%" fill="url(#sun)"/>''')

# estrelas discretas
for _ in range(70):
    x, y = random.uniform(0, W), random.uniform(0, 250)
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(.5,1.3):.1f}" fill="#efe6d6" fill-opacity="{random.uniform(.12,.45):.2f}"/>')

# chão (gramado central + vias)
s.append(f'<rect x="0" y="{HZ}" width="{W}" height="{H-HZ}" fill="url(#lawn)"/>')

s.append(f'<line x1="0" y1="{HZ}" x2="{W}" y2="{HZ}" stroke="#c9a45c" stroke-opacity="0.22"/>')
# Congresso ao longe (silhueta genérica: torres gêmeas + duas cúpulas)
ZC = 1150
def box(x0, x1, y0, y1, z, fill):
    a, b = P(x0, y1, z), P(x1, y0, z)
    return f'<rect x="{a[0]:.1f}" y="{a[1]:.1f}" width="{b[0]-a[0]:.1f}" height="{b[1]-a[1]:.1f}" fill="{fill}"/>'
s.append(box(-120, 120, 0, 12, ZC, "#0b0d10"))              # plataforma
s.append(box(-12, -2, 0, 110, ZC, "#0b0d10"))               # torres
s.append(box(2, 12, 0, 110, ZC, "#0b0d10"))
s.append(box(-12, 12, 60, 63, ZC, "#0b0d10"))               # passarela
lx, ly = P(-70, 12, ZC); rx, ry = P(70, 12, ZC); k = F / ZC
s.append(f'<path d="M{lx-24*k*1.0:.1f},{ly:.1f} A{24*k*1.0:.1f},{14*k:.1f} 0 0 1 {lx+24*k:.1f},{ly:.1f} Z" fill="#0b0d10"/>')   # cúpula
s.append(f'<path d="M{rx-30*k:.1f},{ry - 16*k:.1f} L{rx+30*k:.1f},{ry-16*k:.1f} L{rx+18*k:.1f},{ry:.1f} L{rx-18*k:.1f},{ry:.1f} Z" fill="#0b0d10"/>')  # cuia invertida
# luz quente nas torres
for i in range(6):
    yy = P(0, 15 + i*15, ZC)[1]
    s.append(f'<rect x="{P(-11,0,ZC)[0]:.1f}" y="{yy:.1f}" width="{4:.1f}" height="1.2" fill="#e3b96a" fill-opacity="0.5"/>')

# Blocos dos ministérios: dois lados, do mais distante para o mais próximo
XIN, DEPTH, GAP, HB, WB = 95, 72, 34, 42, 18   # face interna, comprimento, vão, altura, largura
blocks = []
z = 70
while z < 1300:
    blocks.append(z); z += DEPTH + GAP
for z1 in reversed(blocks):
    z2 = z1 + DEPTH
    for side in (-1, 1):
        xi = side * XIN; xo = side * (XIN + WB)
        # face interna (voltada para o gramado)
        face = [P(xi, 0, z1), P(xi, HB, z1), P(xi, HB, z2), P(xi, 0, z2)]
        s.append(poly(face, fill="url(#slabL)" if side < 0 else "url(#slabR)"))
        # face frontal (voltada para o observador)
        front = [P(xi, 0, z1), P(xi, HB, z1), P(xo, HB, z1), P(xo, 0, z1)]
        s.append(poly(front, fill="#0e1218"))
        # cobertura (linha dourada)
        s.append(line(P(xi, HB, z1), P(xi, HB, z2), stroke="#c9a45c", stroke_opacity="0.35", stroke_width="1.2"))
        s.append(line(P(xi, HB, z1), P(xo, HB, z1), stroke="#c9a45c", stroke_opacity="0.22", stroke_width="1"))
        # andares e montantes
        floors, cols = 10, 14
        for f in range(1, floors):
            y = 4 + f * (HB - 6) / floors
            s.append(line(P(xi, y, z1), P(xi, y, z2), stroke="#8796a8", stroke_opacity="0.13", stroke_width="1"))
        if z1 < 600:
            for c in range(1, cols):
                zz = z1 + c * DEPTH / cols
                s.append(line(P(xi, 4, zz), P(xi, HB, zz), stroke="#9aa8b8", stroke_opacity="0.08", stroke_width="1"))
        # janelas acesas
        for f in range(floors - 1):
            ya, yb = 4 + f * (HB - 6) / floors + 0.8, 4 + (f + 1) * (HB - 6) / floors - 0.8
            for c in range(cols):
                if random.random() < 0.16:
                    za, zb = z1 + c * DEPTH / cols + 0.6, z1 + (c + 1) * DEPTH / cols - 0.6
                    op = random.uniform(0.18, 0.55)
                    s.append(poly([P(xi, ya, za), P(xi, yb, za), P(xi, yb, zb), P(xi, ya, zb)],
                                  fill="#e3b96a", fill_opacity=f"{op:.2f}"))
        # pilotis escuros
        s.append(poly([P(xi, 0, z1), P(xi, 4, z1), P(xi, 4, z2), P(xi, 0, z2)], fill="#06070a"))

# vias laterais com rastros de faróis convergindo
for side in (-1, 1):
    for lane, col in ((70, "#e8dcc4"), (82, "#c9673e")):
        x = side * lane
        a, b = P(x, 0, 65), P(x, 0, 1400)
        s.append(line(a, b, stroke=col, stroke_opacity="0.30", stroke_width="1.6", filter="url(#soft)"))
        for _ in range(16):
            zz = random.uniform(70, 1200)
            px, py = P(x, 0.5, zz)
            r = max(0.6, 2.2 * 90 / zz)
            s.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r:.1f}" fill="{col}" fill-opacity="0.75"/>')
# espelho d'água / eixo central dourado
s.append(line(P(0, 0, 65), P(0, 0, 1400), stroke="#c9a45c", stroke_opacity="0.18", stroke_width="2"))
# brilho no ponto de fuga
s.append(f'<ellipse cx="{CX}" cy="{HZ-4}" rx="120" ry="18" fill="#e0b56a" fill-opacity="0.18" filter="url(#glow)"/>')

s.append('<rect width="100%" height="100%" fill="url(#fade)"/>')
s.append('<rect width="100%" height="100%" fill="url(#vign)"/>')
s.append('<rect width="100%" height="100%" filter="url(#grain)"/>')
s.append('</svg>')
Path(sys.argv[1] if len(sys.argv) > 1 else "bg.svg").write_text("\n".join(s))
print("ok")
