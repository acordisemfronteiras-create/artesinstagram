import random, sys, math
from pathlib import Path
random.seed(11)
W, H = 1080, 1350
s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#14120f"/><stop offset="0.30" stop-color="#1d1915"/>
 <stop offset="0.42" stop-color="#2a2119"/><stop offset="0.50" stop-color="#120f0c"/>
 <stop offset="0.62" stop-color="#0a0a0a"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="glow" cx="0.5" cy="0.30" r="0.45">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.22"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="body" x1="0" y1="0" x2="1" y2="1">
 <stop offset="0" stop-color="#2b2c30"/><stop offset="0.55" stop-color="#17181b"/><stop offset="1" stop-color="#0c0c0e"/></linearGradient>
<linearGradient id="edge" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.55"/><stop offset="0.5" stop-color="#c9a45c" stop-opacity="0.10"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0.45"/></linearGradient>
<linearGradient id="screen" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#1e1a12"/><stop offset="1" stop-color="#0d0b08"/></linearGradient>
<radialGradient id="scrglow" cx="0.5" cy="0.45" r="0.6">
 <stop offset="0" stop-color="#e3b96a" stop-opacity="0.35"/><stop offset="1" stop-color="#e3b96a" stop-opacity="0"/></radialGradient>
<linearGradient id="c1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5a2a2c"/><stop offset="1" stop-color="#2a1416"/></linearGradient>
<linearGradient id="c2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#24443a"/><stop offset="1" stop-color="#11211c"/></linearGradient>
<linearGradient id="c3" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#26344d"/><stop offset="1" stop-color="#111827"/></linearGradient>
<linearGradient id="c4" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5b4a2a"/><stop offset="1" stop-color="#2a2214"/></linearGradient>
<linearGradient id="chip" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e6c784"/><stop offset="1" stop-color="#9c7a3a"/></linearGradient>
<linearGradient id="counter" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#2a2016"/><stop offset="0.25" stop-color="#16110c"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.35"/><stop offset="0.13" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.33" stop-color="#0a0a0a" stop-opacity="0.04"/><stop offset="0.41" stop-color="#0a0a0a" stop-opacity="0.75"/>
 <stop offset="0.47" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.3" r="0.8"><stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.65"/></radialGradient>
<filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="5"/>
 <feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="table" tableValues="0 0.07"/></feComponentTransfer></filter>
<filter id="blur8"><feGaussianBlur stdDeviation="8"/></filter>
<filter id="blur3"><feGaussianBlur stdDeviation="3"/></filter>
<filter id="shadow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="14"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/>
<rect width="100%" height="100%" fill="url(#glow)"/>''')

# warm bokeh lights of a restaurant in the background
for _ in range(34):
    x = random.uniform(20, 1060); y = random.uniform(40, 420)
    r = random.uniform(10, 38)
    op = random.uniform(0.05, 0.16)
    col = random.choice(["#e3b96a", "#c9a45c", "#d98f4e", "#f0d49a"])
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.0f}" fill="{col}" fill-opacity="{op:.2f}" filter="url(#blur8)"/>')
# pendant lamps
for lx, ly in ((170, 150), (910, 130)):
    s.append(f'<line x1="{lx}" y1="0" x2="{lx}" y2="{ly-28}" stroke="#3a332a" stroke-width="2"/>')
    s.append(f'<path d="M{lx-46},{ly} Q{lx},{ly-62} {lx+46},{ly} Z" fill="#1b1814" stroke="#c9a45c" stroke-opacity="0.35"/>')
    s.append(f'<ellipse cx="{lx}" cy="{ly+4}" rx="36" ry="9" fill="#f0d49a" fill-opacity="0.55" filter="url(#blur3)"/>')
    s.append(f'<path d="M{lx-40},{ly+4} L{lx-150},{ly+330} L{lx+150},{ly+330} L{lx+40},{ly+4} Z" fill="#e3b96a" fill-opacity="0.035"/>')

# counter top
cy0 = 468
s.append(f'<rect x="0" y="{cy0}" width="{W}" height="{H-cy0}" fill="url(#counter)"/>')
s.append(f'<line x1="0" y1="{cy0}" x2="{W}" y2="{cy0}" stroke="#c9a45c" stroke-opacity="0.30" stroke-width="1.5"/>')

# plates with cutlery on the counter sides (perspective ellipses)
def plate(cx, cy, rx):
    ry = rx * 0.26
    s.append(f'<ellipse cx="{cx}" cy="{cy+8}" rx="{rx*1.02:.0f}" ry="{ry:.0f}" fill="#000" fill-opacity="0.55" filter="url(#blur3)"/>')
    s.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry:.0f}" fill="#2c2924" stroke="#8f8a82" stroke-opacity="0.35"/>')
    s.append(f'<ellipse cx="{cx}" cy="{cy+2}" rx="{rx*0.66:.0f}" ry="{ry*0.62:.0f}" fill="#211e1a" stroke="#c9a45c" stroke-opacity="0.18"/>')
    # fork (left) and knife (right)
    fx = cx - rx - 26; kx = cx + rx + 26
    s.append(f'<path d="M{fx-34},{cy+6} L{fx+30},{cy-4}" stroke="#9a948a" stroke-opacity="0.55" stroke-width="4" stroke-linecap="round"/>')
    for d in (-6, 0, 6):
        s.append(f'<path d="M{fx+30},{cy-4+d*0.2} L{fx+52},{cy-7+d}" stroke="#9a948a" stroke-opacity="0.5" stroke-width="2"/>')
    s.append(f'<path d="M{kx+34},{cy+6} L{kx-26},{cy-4}" stroke="#9a948a" stroke-opacity="0.55" stroke-width="4" stroke-linecap="round"/>')
    s.append(f'<path d="M{kx-26},{cy-4} L{kx-56},{cy-8} L{kx-30},{cy-1} Z" fill="#9a948a" fill-opacity="0.5"/>')
plate(150, 512, 80)
plate(930, 512, 80)

# glass on right
s.append('<path d="M800,440 L808,494 L842,494 L850,440 Z" fill="#c9a45c" fill-opacity="0.06" stroke="#d4cdc2" stroke-opacity="0.25"/>')
s.append('<path d="M805,466 L810,494 L840,494 L845,466 Z" fill="#e3b96a" fill-opacity="0.14"/>')

s.append('<g transform="translate(540,150) scale(0.80) translate(-540,-130)">')
# credit-like benefit cards fanned behind terminal (no brands, no text)
def card(cx, cy, ang, grad, wave=False):
    w, h = 270, 170
    s.append(f'<g transform="translate({cx},{cy}) rotate({ang})">')
    s.append(f'<rect x="{-w/2+10}" y="{-h/2+16}" width="{w}" height="{h}" rx="16" fill="#000" fill-opacity="0.6" filter="url(#shadow)"/>')
    s.append(f'<rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="16" fill="url(#{grad})" stroke="#c9a45c" stroke-opacity="0.35"/>')
    s.append(f'<rect x="{-w/2+26}" y="{-h/2+50}" width="44" height="34" rx="6" fill="url(#chip)" fill-opacity="0.9"/>')
    s.append(f'<path d="M{-w/2+26},{-h/2+67} h44 M{-w/2+48},{-h/2+50} v34" stroke="#6b5226" stroke-width="1.2"/>')
    # contactless symbol
    for i, r in enumerate((10, 18, 26)):
        s.append(f'<path d="M{-w/2+96+r*0.3},{-h/2+67-r} A{r},{r} 0 0 1 {-w/2+96+r*0.3},{-h/2+67+r}" fill="none" stroke="#efe6d6" stroke-opacity="0.45" stroke-width="2.4"/>')
    for i in range(4):
        s.append(f'<rect x="{-w/2+26+i*52}" y="{h/2-44}" width="40" height="7" rx="3" fill="#efe6d6" fill-opacity="0.22"/>')
    # small fork-knife mark (generic meal symbol)
    mx, my = w/2-40, -h/2+36
    s.append(f'<path d="M{mx-8},{my-12} v24 M{mx-12},{my-12} v8 M{mx-4},{my-12} v8 M{mx-12},{my-4} h8" stroke="#c9a45c" stroke-opacity="0.8" stroke-width="2" fill="none"/>')
    s.append(f'<path d="M{mx+8},{my-12} q6,6 0,14 v10" stroke="#c9a45c" stroke-opacity="0.8" stroke-width="2" fill="none"/>')
    s.append('</g>')
card(300, 300, -18, "c1")
card(330, 405, -6, "c3")
card(780, 300, 16, "c2")
card(752, 405, 5, "c4")

# connection arcs from cards to terminal (interoperability)
for (x0, y0) in ((420, 270), (440, 400), (660, 270), (640, 400)):
    mx = (x0 + 540) / 2
    s.append(f'<path d="M{x0},{y0} Q{mx},{y0-70} 540,{205}" fill="none" stroke="#c9a45c" stroke-opacity="0.45" stroke-width="1.6" stroke-dasharray="4 7"/>')
    s.append(f'<circle cx="{x0}" cy="{y0}" r="4" fill="#c9a45c" fill-opacity="0.8"/>')

# POS terminal (center)
tx, ty, tw, th = 430, 130, 220, 400
s.append(f'<ellipse cx="540" cy="{ty+th+6}" rx="150" ry="20" fill="#000" fill-opacity="0.8" filter="url(#blur8)"/>')
s.append(f'<rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="34" fill="url(#body)" stroke="url(#edge)" stroke-width="2"/>')
# paper slot top
s.append(f'<rect x="{tx+40}" y="{ty-6}" width="{tw-80}" height="12" rx="5" fill="#0a0a0a" stroke="#c9a45c" stroke-opacity="0.25"/>')
# screen
sx, sy, sw, sh = tx+22, ty+28, tw-44, 150
s.append(f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="12" fill="url(#screen)" stroke="#c9a45c" stroke-opacity="0.45"/>')
s.append(f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="12" fill="url(#scrglow)"/>')
ccx, ccy = sx + sw/2, sy + 66
s.append(f'<circle cx="{ccx}" cy="{ccy}" r="34" fill="none" stroke="#c9a45c" stroke-width="3"/>')
s.append(f'<path d="M{ccx-15},{ccy+1} L{ccx-4},{ccy+12} L{ccx+17},{ccy-12}" fill="none" stroke="#e3b96a" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>')
s.append(f'<rect x="{ccx-50}" y="{sy+118}" width="100" height="6" rx="3" fill="#c9a45c" fill-opacity="0.45"/>')
# contactless reader mark on body
for r in (9, 16, 23):
    s.append(f'<path d="M{ccx-6+r*0.3},{ty+200-r} A{r},{r} 0 0 1 {ccx-6+r*0.3},{ty+200+r}" fill="none" stroke="#c9a45c" stroke-opacity="0.55" stroke-width="2"/>')
# keypad
kx0, ky0 = tx+36, ty+236
for r in range(4):
    for c in range(3):
        x = kx0 + c*52; y = ky0 + r*36
        fill = "#2a2b2f"
        st = "#8f8a82"
        if r == 3 and c == 2: fill = "#3a3324"; st = "#c9a45c"
        s.append(f'<rect x="{x}" y="{y}" width="40" height="26" rx="7" fill="{fill}" stroke="{st}" stroke-opacity="0.35"/>')
        s.append(f'<circle cx="{x+20}" cy="{y+13}" r="2.6" fill="#d4cdc2" fill-opacity="0.45"/>')
# highlight sheen
s.append(f'<path d="M{tx+16},{ty+40} Q{tx+20},{ty+16} {tx+50},{ty+12}" fill="none" stroke="#ffffff" stroke-opacity="0.18" stroke-width="3"/>')

s.append('</g>')
s.append('<rect width="100%" height="100%" fill="url(#fade)"/>')
s.append('<rect width="100%" height="100%" fill="url(#vign)"/>')
s.append('<rect width="100%" height="100%" filter="url(#grain)"/>')
s.append('</svg>')
Path(sys.argv[1] if len(sys.argv) > 1 else 'bg.svg').write_text("\n".join(s))
print("ok")
