"""Fundo do post 12/11/2026 (noite): dólar dispara a R$ 5,65.
Ilustração: painel de câmbio com candles em alta no céu e um leque de cédulas
genéricas (sem desenho de moeda real) sobre uma mesa, com brilho dourado."""
import math, random
from pathlib import Path

random.seed(1211)
W, H = 1080, 1350
o = []
o.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
o.append('''
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0f1620"/>
    <stop offset="0.22" stop-color="#16202c"/>
    <stop offset="0.33" stop-color="#2a261f"/>
    <stop offset="0.42" stop-color="#16120d"/>
    <stop offset="0.55" stop-color="#0b0b0b"/>
    <stop offset="1" stop-color="#0a0a0a"/>
  </linearGradient>
  <radialGradient id="glow" cx="0.5" cy="0.27" r="0.45">
    <stop offset="0" stop-color="#c9a45c" stop-opacity="0.22"/>
    <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="note" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#2b3a2e"/>
    <stop offset="0.5" stop-color="#1f2b22"/>
    <stop offset="1" stop-color="#141c16"/>
  </linearGradient>
  <linearGradient id="noteHi" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#c9a45c" stop-opacity="0.18"/>
    <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="table" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#1a1611"/>
    <stop offset="1" stop-color="#0a0a0a"/>
  </linearGradient>
  <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0a0a0a" stop-opacity="0"/>
    <stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/>
  </linearGradient>
  <linearGradient id="line" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#c9a45c" stop-opacity="0.25"/>
    <stop offset="1" stop-color="#e6c88a" stop-opacity="1"/>
  </linearGradient>
  <filter id="soft"><feGaussianBlur stdDeviation="6"/></filter>
</defs>
<rect width="1080" height="1350" fill="url(#sky)"/>
<rect width="1080" height="1350" fill="url(#glow)"/>
''')

# estrelas discretas
for _ in range(60):
    x, y = random.uniform(0, W), random.uniform(0, 210)
    o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(.6,1.5):.1f}" fill="#efe6d6" opacity="{random.uniform(.12,.4):.2f}"/>')

# ---- painel de câmbio (telão) ----
px, py, pw, ph = 150, 150, 780, 230
o.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="6" fill="#0c1016" stroke="#3a3428" stroke-width="2" opacity="0.92"/>')
o.append(f'<rect x="{px+8}" y="{py+8}" width="{pw-16}" height="{ph-16}" rx="3" fill="none" stroke="#c9a45c" stroke-opacity="0.18"/>')
# grade
for i in range(1, 5):
    y = py + i * ph / 5
    o.append(f'<line x1="{px+16}" y1="{y:.0f}" x2="{px+pw-16}" y2="{y:.0f}" stroke="#c9a45c" stroke-opacity="0.08"/>')
for i in range(1, 12):
    x = px + i * pw / 12
    o.append(f'<line x1="{x:.0f}" y1="{py+14}" x2="{x:.0f}" y2="{py+ph-14}" stroke="#c9a45c" stroke-opacity="0.05"/>')
# candles em alta, com disparada no final
n = 22
vals = []
v = 0.62
for i in range(n):
    drift = -0.004 if i < 14 else (-0.02 if i < 19 else -0.07)
    v += drift + random.uniform(-0.02, 0.018)
    vals.append(v)
vals[-1] = 0.12
vals[-2] = min(vals[-2], 0.24)
cw = (pw - 80) / n
prev = 0.64
pts = []
for i, val in enumerate(vals):
    cx = px + 40 + i * cw + cw / 2
    o_, c_ = prev, val
    top = min(o_, c_) - random.uniform(0.01, 0.04)
    bot = max(o_, c_) + random.uniform(0.01, 0.04)
    up = c_ < o_
    col = "#c9a45c" if up else "#6b6357"
    yy = lambda f: py + 20 + f * (ph - 40)
    o.append(f'<line x1="{cx:.1f}" y1="{yy(top):.1f}" x2="{cx:.1f}" y2="{yy(bot):.1f}" stroke="{col}" stroke-width="1.6" opacity="0.8"/>')
    y1, y2 = yy(min(o_, c_)), yy(max(o_, c_))
    o.append(f'<rect x="{cx-cw*0.3:.1f}" y="{y1:.1f}" width="{cw*0.6:.1f}" height="{max(y2-y1,2):.1f}" fill="{col}" opacity="{0.95 if up else 0.55}"/>')
    pts.append((cx, yy(c_)))
    prev = val
path = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
o.append(f'<path d="{path}" fill="none" stroke="url(#line)" stroke-width="2.4" opacity="0.7"/>')
lx, ly = pts[-1]
o.append(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="16" fill="#c9a45c" opacity="0.35" filter="url(#soft)"/>')
o.append(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="5" fill="#f0d79c"/>')
# etiqueta genérica no painel
o.append(f'<text x="{px+28}" y="{py+40}" font-family="Inter, sans-serif" font-size="17" letter-spacing="4" fill="#c9a45c" opacity="0.65">USD / BRL</text>')
o.append(f'<text x="{px+28}" y="{py+64}" font-family="Inter, sans-serif" font-size="14" letter-spacing="3" fill="#a9a39a" opacity="0.45">FECHAMENTO DO DIA</text>')
# suportes do painel
for sx in (px + 120, px + pw - 120):
    o.append(f'<rect x="{sx-4}" y="{py+ph}" width="8" height="70" fill="#1a1712"/>')

# ---- mesa ----
o.append('<path d="M0,450 L1080,450 L1080,700 L0,700 Z" fill="url(#table)"/>')
o.append('<line x1="0" y1="450" x2="1080" y2="450" stroke="#c9a45c" stroke-opacity="0.25" stroke-width="1.5"/>')

# ---- leque de cédulas genéricas ----
def note(cx, cy, ang, scale=1.0, op=1.0, lift=95):
    w, h = 300 * scale, 132 * scale
    g = [f'<g transform="translate({cx:.1f},{cy:.1f}) rotate({ang:.1f}) translate(0,{-lift}) rotate(-90)" opacity="{op:.2f}">']
    g.append(f'<rect x="{-w/2:.1f}" y="{-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" rx="5" fill="url(#note)" stroke="#c9a45c" stroke-opacity="0.45" stroke-width="1.4"/>')
    g.append(f'<rect x="{-w/2+10:.1f}" y="{-h/2+10:.1f}" width="{w-20:.1f}" height="{h-20:.1f}" rx="3" fill="none" stroke="#c9a45c" stroke-opacity="0.25"/>')
    g.append(f'<rect x="{-w/2:.1f}" y="{-h/2:.1f}" width="{w:.1f}" height="{h/2:.1f}" rx="5" fill="url(#noteHi)"/>')
    # medalhão central com símbolo genérico
    g.append(f'<circle cx="0" cy="0" r="{36*scale:.1f}" fill="none" stroke="#c9a45c" stroke-opacity="0.5" stroke-width="1.4"/>')
    g.append(f'<circle cx="0" cy="0" r="{28*scale:.1f}" fill="none" stroke="#c9a45c" stroke-opacity="0.25"/>')
    g.append(f'<text x="0" y="{13*scale:.1f}" text-anchor="middle" font-family="Fraunces, Georgia, serif" font-size="{38*scale:.0f}" fill="#c9a45c" opacity="0.8">$</text>')
    # guilhoché
    for k in range(5):
        yk = -h/2 + 24*scale + k*7*scale
        g.append(f'<path d="M{-w/2+22*scale:.1f},{yk:.1f} q{12*scale:.1f},-6 {24*scale:.1f},0 t{24*scale:.1f},0 t{24*scale:.1f},0" fill="none" stroke="#c9a45c" stroke-opacity="0.18"/>')
    for sgn in (-1, 1):
        g.append(f'<text x="{sgn*(w/2-34*scale):.1f}" y="{h/2-20*scale:.1f}" text-anchor="middle" font-family="Fraunces, Georgia, serif" font-size="{24*scale:.0f}" fill="#c9a45c" opacity="0.55">100</text>')
    g.append('</g>')
    return "".join(g)

# sombra
o.append('<ellipse cx="540" cy="470" rx="220" ry="26" fill="#000" opacity="0.6" filter="url(#soft)"/>')
angles = [-48, -32, -16, 0, 16, 32, 48]
for a in angles:
    o.append(note(540, 470, a, 0.72, 0.98))
# pilha de moedas estilizadas nas laterais
for (bx, n_) in ((190, 6), (250, 4), (850, 5), (900, 3)):
    for k in range(n_):
        y = 440 - k * 9
        o.append(f'<ellipse cx="{bx}" cy="{y+4}" rx="30" ry="9" fill="#5a4626"/>')
        o.append(f'<ellipse cx="{bx}" cy="{y}" rx="30" ry="9" fill="#8f7240" stroke="#c9a45c" stroke-opacity="0.6"/>')

# esmaecimento para o preto na metade de baixo
o.append('<rect x="0" y="420" width="1080" height="300" fill="url(#fade)"/>')
o.append('<rect x="0" y="700" width="1080" height="650" fill="#0a0a0a"/>')
o.append('</svg>')

Path(__file__).with_name("bg.svg").write_text("\n".join(o))
print("bg.svg ok")
