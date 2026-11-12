"""Fundo: corredor de supermercado em perspectiva à noite, gôndolas com produtos genéricos,
etiquetas de preço douradas penduradas e uma linha de inflação mensal no alto."""
import math, random, sys
from pathlib import Path

random.seed(1211)
W, H = 1080, 1350
HZ = 430          # chão/limite inferior da ilustração
VP = (540, 300)   # ponto de fuga

s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
s.append('''
<defs>
  <linearGradient id="bgc" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#10151c"/>
    <stop offset="0.22" stop-color="#171c23"/>
    <stop offset="0.33" stop-color="#14161a"/>
    <stop offset="0.5" stop-color="#0b0b0b"/>
    <stop offset="1" stop-color="#0a0a0a"/>
  </linearGradient>
  <radialGradient id="glowend" cx="0.5" cy="0.222" r="0.30">
    <stop offset="0" stop-color="#e2bd72" stop-opacity="0.30"/>
    <stop offset="0.35" stop-color="#c9a45c" stop-opacity="0.10"/>
    <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="shelfL" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#1b2028"/>
    <stop offset="1" stop-color="#11141a"/>
  </linearGradient>
  <linearGradient id="shelfR" x1="1" y1="0" x2="0" y2="0">
    <stop offset="0" stop-color="#1b2028"/>
    <stop offset="1" stop-color="#11141a"/>
  </linearGradient>
  <linearGradient id="floor" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#1c1a16"/>
    <stop offset="1" stop-color="#0a0a0a"/>
  </linearGradient>
  <linearGradient id="line" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#c9a45c" stop-opacity="0"/>
    <stop offset="0.3" stop-color="#c9a45c" stop-opacity="0.35"/>
    <stop offset="1" stop-color="#e2bd72" stop-opacity="0.9"/>
  </linearGradient>
  <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.45"/>
    <stop offset="0.12" stop-color="#0a0a0a" stop-opacity="0"/>
    <stop offset="0.25" stop-color="#0a0a0a" stop-opacity="0"/>
    <stop offset="0.31" stop-color="#0a0a0a" stop-opacity="0.75"/>
    <stop offset="0.355" stop-color="#0a0a0a" stop-opacity="1"/>
    <stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/>
  </linearGradient>
  <radialGradient id="vign" cx="0.5" cy="0.25" r="0.8">
    <stop offset="0.5" stop-color="#000" stop-opacity="0"/>
    <stop offset="1" stop-color="#000" stop-opacity="0.6"/>
  </radialGradient>
  <filter id="grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="7"/>
    <feColorMatrix type="saturate" values="0"/>
    <feComponentTransfer><feFuncA type="table" tableValues="0 0.07"/></feComponentTransfer>
  </filter>
  <filter id="glow"><feGaussianBlur stdDeviation="4"/></filter>
  <filter id="soft"><feGaussianBlur stdDeviation="1.2"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#bgc)"/>
''')

# Parede do fundo do corredor (retângulo central) com luz quente
BW, BH = 150, 150
bx0, by0 = VP[0] - BW / 2, VP[1] - BH * 0.62
s.append(f'<rect x="{bx0}" y="{by0}" width="{BW}" height="{BH}" fill="#1d1c1a"/>')
s.append('<rect width="100%" height="100%" fill="url(#glowend)"/>')

# Teto: luminárias lineares convergindo
CEIL = -40
def proj(xw, yw, t):
    """interpola de um ponto da borda (xw,yw) até o ponto de fuga por t (0=borda,1=fundo)"""
    return xw + (VP[0] - xw) * t, yw + (VP[1] - yw) * t
for k in range(7):
    t0 = 1 - 0.78 ** k * 0.95
    t1 = t0 + (1 - t0) * 0.09
    xa, ya = proj(540, CEIL, t0); xb2, yb2 = proj(540, CEIL, t1)
    w0 = 120 * (1 - t0); w1 = 120 * (1 - t1)
    s.append(f'<polygon points="{xa-w0:.1f},{ya:.1f} {xa+w0:.1f},{ya:.1f} {xb2+w1:.1f},{yb2:.1f} {xb2-w1:.1f},{yb2:.1f}" fill="#efe6d6" fill-opacity="{0.10+0.05*(6-k)/6:.2f}"/>')
    s.append(f'<polygon points="{xa-w0*1.6:.1f},{ya:.1f} {xa+w0*1.6:.1f},{ya:.1f} {xb2+w1*1.6:.1f},{yb2:.1f} {xb2-w1*1.6:.1f},{yb2:.1f}" fill="#e2bd72" fill-opacity="0.05" filter="url(#glow)"/>')

# Chão do corredor
FL, FR = -260, 1340
s.append(f'<polygon points="{FL},{HZ+260} {FR},{HZ+260} {VP[0]+BW/2},{by0+BH} {VP[0]-BW/2},{by0+BH}" fill="url(#floor)"/>')
# reflexo da luz no piso
s.append(f'<polygon points="470,{HZ+80} 610,{HZ+80} {VP[0]+12},{by0+BH} {VP[0]-12},{by0+BH}" fill="#e2bd72" fill-opacity="0.05"/>')
for k in range(1, 9):
    t = 1 - 0.72 ** k
    y = (HZ + 260) + ((by0 + BH) - (HZ + 260)) * t
    xl = FL + ((VP[0] - BW / 2) - FL) * t; xr = FR + ((VP[0] + BW / 2) - FR) * t
    s.append(f'<line x1="{xl:.1f}" y1="{y:.1f}" x2="{xr:.1f}" y2="{y:.1f}" stroke="#c9a45c" stroke-opacity="0.05"/>')

# Gôndolas: lado esquerdo e direito em perspectiva
PAL = ["#3a2f22", "#2b3440", "#4a3b26", "#283028", "#3b2a2a", "#33302a", "#24303a", "#40362a"]
def gondola(side):
    # borda externa (perto do observador) e interna (fundo)
    xo = -10 if side < 0 else W + 10
    xi = VP[0] - BW / 2 if side < 0 else VP[0] + BW / 2
    yo_top, yo_bot = 40, HZ + 5
    yi_top, yi_bot = by0 + 12, by0 + BH
    s.append(f'<polygon points="{xo},{yo_top} {xi},{yi_top} {xi},{yi_bot} {xo},{yo_bot}" fill="url(#{"shelfL" if side<0 else "shelfR"})"/>')
    n_shelf = 5
    for j in range(n_shelf + 1):
        f = j / n_shelf
        ya = yo_top + (yo_bot - yo_top) * f
        yb = yi_top + (yi_bot - yi_top) * f
        # prateleira (borda frontal clara)
        s.append(f'<line x1="{xo}" y1="{ya:.1f}" x2="{xi}" y2="{yb:.1f}" stroke="#55606c" stroke-opacity="0.55" stroke-width="{3 if j<n_shelf else 2}"/>')
        if j == n_shelf:
            break
        f2 = (j + 1) / n_shelf
        ya2 = yo_top + (yo_bot - yo_top) * f2
        yb2 = yi_top + (yi_bot - yi_top) * f2
        # produtos ao longo da prateleira (do perto para o longe)
        t = 0.0
        while t < 0.97:
            wdt = random.uniform(0.022, 0.05) * (1 - t * 0.6)
            t2 = min(t + wdt, 0.985)
            # interpolação não-linear para profundidade
            def P(tt, fy):
                tt_ = 1 - (1 - tt) ** 2.2
                x = xo + (xi - xo) * tt_
                ytop = (yo_top + (yo_bot - yo_top) * fy) + ((yi_top + (yi_bot - yi_top) * fy) - (yo_top + (yo_bot - yo_top) * fy)) * tt_
                return x, ytop
            xa_, ya_top = P(t, j / n_shelf); xb_, yb_top = P(t2, j / n_shelf)
            _, ya_bot = P(t, f2); _, yb_bot = P(t2, f2)
            hfrac = random.uniform(0.45, 0.88)
            ta = ya_bot - (ya_bot - ya_top) * hfrac
            tb = yb_bot - (yb_bot - yb_top) * hfrac
            col = random.choice(PAL)
            s.append(f'<polygon points="{xa_:.1f},{ta:.1f} {xb_:.1f},{tb:.1f} {xb_:.1f},{yb_bot-1:.1f} {xa_:.1f},{ya_bot-1:.1f}" fill="{col}" fill-opacity="0.95" stroke="#0a0a0a" stroke-opacity="0.6" stroke-width="0.8"/>')
            # rótulo discreto
            if abs(xb_ - xa_) > 6:
                ma = ta + (ya_bot - ta) * 0.45; mb = tb + (yb_bot - tb) * 0.45
                s.append(f'<line x1="{xa_:.1f}" y1="{ma:.1f}" x2="{xb_:.1f}" y2="{mb:.1f}" stroke="#efe6d6" stroke-opacity="0.10" stroke-width="{max(1, abs(ya_bot-ta)*0.12):.1f}"/>')
            t = t2 + 0.004
        # etiquetas de preço na borda da prateleira (poucas, douradas)
        for tt in (0.08, 0.30, 0.55):
            tt_ = 1 - (1 - tt) ** 2.2
            x = xo + (xi - xo) * tt_
            yfront = ya2 + (yb2 - ya2) * tt_
            sc = 1 - tt_ * 0.88
            w, h = 46 * sc, 20 * sc
            xx = x if side < 0 else x - w
            s.append(f'<rect x="{xx:.1f}" y="{yfront-h*0.2:.1f}" width="{w:.1f}" height="{h:.1f}" fill="#c9a45c" fill-opacity="{0.55 + 0.25*sc:.2f}"/>')
            s.append(f'<line x1="{xx+w*0.15:.1f}" y1="{yfront+h*0.35:.1f}" x2="{xx+w*0.7:.1f}" y2="{yfront+h*0.35:.1f}" stroke="#0a0a0a" stroke-opacity="0.7" stroke-width="{max(1,3*sc):.1f}"/>')
    # coluna da gôndola (perto)
    s.append(f'<line x1="{xo + (40 if side<0 else -40)}" y1="{yo_top}" x2="{xo + (40 if side<0 else -40)}" y2="{yo_bot+10}" stroke="#0d1014" stroke-width="10"/>')

gondola(-1)
gondola(1)

# Etiquetas de preço grandes penduradas do teto (primeiro plano), cada uma um pouco maior
def hang_tag(x, ytop, L, w, h, ang, op):
    s.append(f'<line x1="{x}" y1="-5" x2="{x}" y2="{ytop}" stroke="#8f8a82" stroke-opacity="0.35" stroke-width="1.2"/>')
    s.append(f'<g transform="rotate({ang} {x} {ytop})">')
    s.append(f'<path d="M{x-w/2},{ytop+h*0.22} L{x},{ytop} L{x+w/2},{ytop+h*0.22} L{x+w/2},{ytop+h} L{x-w/2},{ytop+h} Z" fill="#c9a45c" fill-opacity="{op}"/>')
    s.append(f'<circle cx="{x}" cy="{ytop+h*0.17}" r="{w*0.06:.1f}" fill="#0a0a0a" fill-opacity="0.8"/>')
    s.append(f'<line x1="{x-w*0.3}" y1="{ytop+h*0.5}" x2="{x+w*0.3}" y2="{ytop+h*0.5}" stroke="#0a0a0a" stroke-opacity="0.55" stroke-width="{h*0.1:.1f}"/>')
    s.append(f'<line x1="{x-w*0.3}" y1="{ytop+h*0.72}" x2="{x+w*0.12}" y2="{ytop+h*0.72}" stroke="#0a0a0a" stroke-opacity="0.35" stroke-width="{h*0.06:.1f}"/>')
    s.append('</g>')

# Linha de inflação mensal no alto (subida gradual), atrás das etiquetas
pts = []
x, y = 250, 228
for i in range(12):
    pts.append((x, y))
    x += 52
    y += random.uniform(-14, 6)
pts[-1] = (pts[-1][0], 150)
d = "M" + " L".join(f"{a:.0f},{b:.1f}" for a, b in pts)
s.append(f'<path d="{d}" fill="none" stroke="url(#line)" stroke-width="2.4" stroke-linejoin="round" stroke-dasharray="none"/>')
for a, b in pts[:-1]:
    s.append(f'<circle cx="{a}" cy="{b:.1f}" r="2.6" fill="#c9a45c" fill-opacity="0.45"/>')
ex, ey = pts[-1]
s.append(f'<circle cx="{ex}" cy="{ey}" r="12" fill="#e2bd72" fill-opacity="0.35" filter="url(#glow)"/>')
s.append(f'<circle cx="{ex}" cy="{ey}" r="5" fill="#e9c47a"/>')

hang_tag(150, 150, 0, 74, 104, -8, 0.85)
hang_tag(930, 170, 0, 66, 94, 7, 0.75)

s.append('<rect width="100%" height="100%" fill="url(#fade)"/>')
s.append('<rect width="100%" height="100%" fill="url(#vign)"/>')
s.append('<rect width="100%" height="100%" filter="url(#grain)"/>')
s.append('</svg>')
Path(sys.argv[1] if len(sys.argv) > 1 else 'bg.svg').write_text("\n".join(s))
print("ok")
