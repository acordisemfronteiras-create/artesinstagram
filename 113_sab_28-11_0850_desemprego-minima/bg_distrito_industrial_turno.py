"""Fundo: distrito industrial ao amanhecer, troca de turno (PNAD: ocupação recorde)."""
import random
random.seed(28)
W, H = 1080, 1350
HZ = 440  # horizonte
s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0f1622"/><stop offset="0.20" stop-color="#18202d"/>
 <stop offset="0.29" stop-color="#2b2a2b"/><stop offset="0.33" stop-color="#4a3824"/>
 <stop offset="0.36" stop-color="#1a1612"/><stop offset="0.5" stop-color="#0b0b0b"/>
 <stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="sun" cx="0.70" cy="0.325" r="0.42">
 <stop offset="0" stop-color="#e2b86a" stop-opacity="0.38"/>
 <stop offset="0.35" stop-color="#c9a45c" stop-opacity="0.12"/>
 <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="steam" x1="0" y1="1" x2="0" y2="0">
 <stop offset="0" stop-color="#b9b1a3" stop-opacity="0.14"/>
 <stop offset="1" stop-color="#b9b1a3" stop-opacity="0"/></linearGradient>
<linearGradient id="road" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#15130f"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.35"/>
 <stop offset="0.12" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.31" stop-color="#0a0a0a" stop-opacity="0.04"/>
 <stop offset="0.375" stop-color="#0a0a0a" stop-opacity="0.75"/>
 <stop offset="0.42" stop-color="#0a0a0a" stop-opacity="1"/>
 <stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.28" r="0.85">
 <stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
<filter id="blur"><feGaussianBlur stdDeviation="6"/></filter>
<filter id="soft"><feGaussianBlur stdDeviation="1.2"/></filter>
<filter id="grain" x="0" y="0" width="100%" height="100%">
 <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="5"/>
 <feColorMatrix type="saturate" values="0"/>
 <feComponentTransfer><feFuncA type="table" tableValues="0 0.07"/></feComponentTransfer></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/>
<rect width="100%" height="100%" fill="url(#sun)"/>''')

# estrelas tênues no alto
for _ in range(40):
    x, y = random.uniform(0, W), random.uniform(10, 200)
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(.5,1.2):.1f}" fill="#d9d2c4" opacity="{random.uniform(.15,.45):.2f}"/>')

# cidade distante (camada 1) com janelas acesas
x = 0
while x < W:
    w = random.randint(18, 46); h = random.randint(20, 95)
    if 560 < x < 900: h = random.randint(10, 40)
    s.append(f'<rect x="{x}" y="{HZ-60-h}" width="{w}" height="{h+60}" fill="#191b20"/>')
    for wy in range(HZ-60-h+6, HZ-62, 9):
        for wx in range(x+4, x+w-4, 7):
            if random.random() < .22:
                s.append(f'<rect x="{wx}" y="{wy}" width="3" height="4" fill="#c9a45c" opacity="{random.uniform(.25,.6):.2f}"/>')
    x += w + random.randint(2, 8)

# chaminés com vapor
for cx, ch, cw in [(250, 205, 22), (292, 170, 18), (840, 190, 20)]:
    top = HZ - 40 - ch
    s.append(f'<path d="M{cx-cw/2} {HZ-40} L{cx-cw/2+3} {top} L{cx+cw/2-3} {top} L{cx+cw/2} {HZ-40} Z" fill="#14161a"/>')
    for k in range(3):
        yy = top + 18 + k*30
        s.append(f'<rect x="{cx-cw/2+2}" y="{yy}" width="{cw-4}" height="4" fill="#3a3024" opacity=".9"/>')
    s.append(f'<circle cx="{cx}" cy="{top-6}" r="3" fill="#e0b25e" opacity=".9"/>')
    s.append(f'<g filter="url(#blur)"><ellipse cx="{cx+28}" cy="{top-50}" rx="{cw+26}" ry="40" fill="url(#steam)"/>'
             f'<ellipse cx="{cx+70}" cy="{top-100}" rx="{cw+40}" ry="46" fill="url(#steam)" opacity=".7"/></g>')

# caixa d'água
tx = 120
s.append(f'<g fill="#121418"><rect x="{tx-3}" y="{HZ-150}" width="6" height="110"/><rect x="{tx+57}" y="{HZ-150}" width="6" height="110"/>'
         f'<path d="M{tx-3} {HZ-110} L{tx+63} {HZ-60} M{tx+63} {HZ-110} L{tx-3} {HZ-60}" stroke="#121418" stroke-width="3"/>'
         f'<rect x="{tx-12}" y="{HZ-200}" width="84" height="54" rx="4"/><path d="M{tx-16} {HZ-200} L{tx+30} {HZ-225} L{tx+76} {HZ-200} Z"/></g>')

# galpões com telhado shed (dente de serra)
def galpao(x0, x1, base, h, teeth, fill="#101215", lit=.55):
    tw = (x1 - x0) / teeth
    d = f'M{x0} {base} L{x0} {base-h}'
    for i in range(teeth):
        a = x0 + i*tw
        d += f' L{a+tw*0.78:.1f} {base-h-34} L{a+tw*0.78:.1f} {base-h} L{a+tw:.1f} {base-h}'
    d += f' L{x1} {base} Z'
    s.append(f'<path d="{d}" fill="{fill}"/>')
    for i in range(teeth):  # claraboias acesas do shed
        a = x0 + i*tw
        s.append(f'<path d="M{a+tw*0.78-2:.1f} {base-h-30} L{a+tw*0.78-2:.1f} {base-h-2} L{a+tw*0.78-12:.1f} {base-h-2} Z" fill="#c9a45c" opacity="{lit*random.uniform(.5,1):.2f}"/>')
    # janelas em faixa
    for wx in range(int(x0)+12, int(x1)-20, 26):
        on = random.random() < .75
        s.append(f'<rect x="{wx}" y="{base-h+18}" width="16" height="22" fill="{"#d6ad62" if on else "#1d1f24"}" opacity="{random.uniform(.55,.95) if on else 1:.2f}"/>')

galpao(330, 760, HZ-6, 70, 8, "#121418")
galpao(-10, 300, HZ+4, 52, 5, "#0f1013", .45)
galpao(780, 1090, HZ+2, 60, 5, "#0f1013", .5)

# portões de doca iluminados no galpão central
for i, dx in enumerate(range(380, 740, 72)):
    s.append(f'<rect x="{dx}" y="{HZ-30}" width="40" height="24" fill="#e1b465" opacity=".85"/>')
    s.append(f'<rect x="{dx-6}" y="{HZ-34}" width="52" height="4" fill="#0c0d10"/>')
    s.append(f'<ellipse cx="{dx+20}" cy="{HZ-4}" rx="42" ry="7" fill="#c9a45c" opacity=".18" filter="url(#blur)"/>')

# guindaste/torre de pátio
s.append(f'<g stroke="#15171b" stroke-width="5" fill="none"><path d="M960 {HZ-58} L960 {HZ-250} L1080 {HZ-250}"/>'
         f'<path d="M960 {HZ-250} L900 {HZ-250}"/><path d="M960 {HZ-290} L1060 {HZ-250} M960 {HZ-290} L905 {HZ-250} M960 {HZ-290} L960 {HZ-250}" stroke-width="2"/></g>'
         f'<rect x="896" y="{HZ-244}" width="18" height="14" fill="#15171b"/><line x1="1040" y1="{HZ-250}" x2="1040" y2="{HZ-150}" stroke="#2a2620" stroke-width="1.5"/>'
         f'<circle cx="960" cy="{HZ-294}" r="3" fill="#d8573f" opacity=".9"/>')

# solo e via com faróis (troca de turno)
s.append(f'<rect x="0" y="{HZ+4}" width="{W}" height="160" fill="url(#road)"/>')
s.append(f'<path d="M0 {HZ+22} L{W} {HZ+16}" stroke="#2a2519" stroke-width="2"/>')
for _ in range(16):
    x = random.uniform(20, W-20); y = HZ + 14 + random.uniform(-2, 8)
    s.append(f'<g filter="url(#soft)"><circle cx="{x:.0f}" cy="{y:.0f}" r="2.4" fill="#f2d79a"/><circle cx="{x+7:.0f}" cy="{y:.0f}" r="2.4" fill="#f2d79a"/></g>')
    s.append(f'<ellipse cx="{x+4:.0f}" cy="{y:.0f}" rx="24" ry="5" fill="#c9a45c" opacity=".16" filter="url(#blur)"/>')
# postes
for px in range(40, W, 150):
    s.append(f'<line x1="{px}" y1="{HZ+20}" x2="{px}" y2="{HZ-48}" stroke="#16181c" stroke-width="3"/>'
             f'<line x1="{px}" y1="{HZ-48}" x2="{px+16}" y2="{HZ-52}" stroke="#16181c" stroke-width="3"/>'
             f'<circle cx="{px+16}" cy="{HZ-50}" r="9" fill="#e7bd6b" opacity=".22" filter="url(#blur)"/>'
             f'<circle cx="{px+16}" cy="{HZ-50}" r="2" fill="#f0d08a"/>')

s.append('<rect width="100%" height="100%" fill="url(#fade)"/>')
s.append('<rect width="100%" height="100%" fill="url(#vign)"/>')
s.append('<rect width="100%" height="100%" filter="url(#grain)"/>')
s.append('</svg>')
open('bg.svg', 'w').write('\n'.join(s))
print('bg.svg ok')
