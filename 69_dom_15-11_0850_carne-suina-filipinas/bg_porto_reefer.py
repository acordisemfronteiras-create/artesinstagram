"""Fundo: porto à noite, navio com contêineres refrigerados parado diante de uma cancela fechada,
costa tropical (palmeiras) ao fundo. Tema: restrição das Filipinas à carne suína brasileira."""
import random
random.seed(1511)
W, H = 1080, 1350
HZ = 420  # horizonte do mar
s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0f1622"/><stop offset="0.22" stop-color="#18212e"/>
 <stop offset="0.30" stop-color="#2b2a2a"/><stop offset="0.335" stop-color="#4a3a24"/>
 <stop offset="0.36" stop-color="#14161a"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="sun" cx="0.78" cy="0.31" r="0.35">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.30"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="sea" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#1a1d22"/><stop offset="0.5" stop-color="#101215"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<linearGradient id="hull" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#23262b"/><stop offset="1" stop-color="#121417"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.30"/><stop offset="0.12" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.33" stop-color="#0a0a0a" stop-opacity="0.05"/><stop offset="0.40" stop-color="#0a0a0a" stop-opacity="0.75"/>
 <stop offset="0.45" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.3" r="0.8">
 <stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
<radialGradient id="lamp" cx="0.5" cy="0.5" r="0.5">
 <stop offset="0" stop-color="#e8c47a" stop-opacity="0.9"/><stop offset="0.25" stop-color="#c9a45c" stop-opacity="0.35"/>
 <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
</defs>''')
s.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
s.append(f'<rect width="{W}" height="{H}" fill="url(#sun)"/>')
# estrelas
for _ in range(90):
    x, y = random.uniform(0, W), random.uniform(0, 300)
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(.5,1.4):.1f}" fill="#d8d2c4" opacity="{random.uniform(.15,.55):.2f}"/>')
# costa distante com palmeiras (direita)
s.append(f'<path d="M640 {HZ} Q700 {HZ-26} 780 {HZ-30} T940 {HZ-22} T1080 {HZ-34} L1080 {HZ} Z" fill="#14171b"/>')
def palm(x, y, h, lean):
    tx, ty = x + lean, y - h
    out = [f'<path d="M{x} {y} Q{x+lean*0.3} {y-h*0.6} {tx} {ty}" stroke="#0f1114" stroke-width="5" fill="none"/>']
    for ang, ln in [(-160, 46), (-130, 52), (-95, 40), (-60, 50), (-25, 46), (10, 38), (-180, 34)]:
        import math
        a = math.radians(ang)
        ex, ey = tx + ln*math.cos(a), ty + ln*math.sin(a) * 0.55 + 18
        cx, cy = tx + ln*0.5*math.cos(a), ty - 14
        out.append(f'<path d="M{tx} {ty} Q{cx:.0f} {cy:.0f} {ex:.0f} {ey:.0f}" stroke="#0f1114" stroke-width="4" fill="none" stroke-linecap="round"/>')
    return "".join(out)
for x, h, l in [(820, 70, 10), (860, 92, -8), (905, 64, 12), (985, 84, -6), (1035, 70, 8)]:
    s.append(palm(x, HZ-24, h, l))
# mar
s.append(f'<rect x="0" y="{HZ}" width="{W}" height="{H-HZ}" fill="url(#sea)"/>')
# reflexo dourado no mar
for i in range(26):
    y = HZ + 6 + i*7
    w = random.uniform(30, 120) * (1 - i/34)
    x = 840 + random.uniform(-60, 60)
    s.append(f'<rect x="{x-w/2:.0f}" y="{y}" width="{w:.0f}" height="1.6" fill="#c9a45c" opacity="{0.35*(1-i/26):.2f}"/>')
# guindastes do cais (esquerda)
def crane(x, base, h, boom):
    g = [f'<g stroke="#2a2d32" stroke-width="5" fill="none">',
         f'<path d="M{x} {base} L{x} {base-h} M{x+46} {base} L{x+46} {base-h}"/>',
         f'<path d="M{x-30} {base-h} L{x+boom} {base-h}" stroke-width="7"/>',
         f'<path d="M{x} {base-h+40} L{x+46} {base-h+90} M{x+46} {base-h+40} L{x} {base-h+90}" stroke-width="3"/>',
         f'<path d="M{x+23} {base-h-50} L{x-30} {base-h} M{x+23} {base-h-50} L{x+boom} {base-h}" stroke-width="2.5"/>',
         '</g>',
         f'<rect x="{x+boom*0.62}" y="{base-h+2}" width="22" height="16" fill="#2a2d32"/>',
         f'<line x1="{x+boom*0.62+11}" y1="{base-h+18}" x2="{x+boom*0.62+11}" y2="{base-h+70}" stroke="#3a3d42" stroke-width="1.5"/>',
         f'<circle cx="{x+23}" cy="{base-h-50}" r="3.5" fill="#c9a45c"/>']
    return "".join(g)
s.append(crane(70, 412, 190, 280))
s.append(crane(250, 412, 165, 240))
# cais
s.append(f'<rect x="0" y="404" width="560" height="22" fill="#16181c"/>')
s.append(f'<rect x="0" y="402" width="560" height="3" fill="#3a3326"/>')
# navio porta-contêineres (atracado, parado)
hx0, hx1, deck = 150, 760, 386
s.append(f'<path d="M{hx0} {deck} L{hx1} {deck} L{hx1-30} {deck+46} L{hx0+18} {deck+46} Z" fill="url(#hull)"/>')
s.append(f'<rect x="{hx0}" y="{deck+8}" width="{hx1-hx0-8}" height="3" fill="#c9a45c" opacity="0.35"/>')
# superestrutura
s.append(f'<rect x="{hx1-120}" y="{deck-112}" width="66" height="112" fill="#1d2025"/>')
s.append(f'<rect x="{hx1-128}" y="{deck-120}" width="82" height="10" fill="#26292e"/>')
for r in range(4):
    for c in range(4):
        on = random.random() < .45
        s.append(f'<rect x="{hx1-114+c*15}" y="{deck-100+r*24}" width="9" height="8" fill="{"#c9a45c" if on else "#2c3036"}" opacity="{.85 if on else 1}"/>')
# contêineres refrigerados (reefers), pilhas
cw, ch = 34, 22
cols = ["#2d3238", "#353a40", "#2a2e33", "#3b3a36", "#30353b"]
for col in range(13):
    x = hx0 + 20 + col*(cw+2)
    tiers = random.choice([3, 4, 4, 5, 5, 5])
    for t in range(tiers):
        y = deck - (t+1)*(ch+1)
        fc = random.choice(cols)
        s.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" fill="{fc}"/>')
        for k in range(1, 4):
            s.append(f'<line x1="{x+k*cw/4:.1f}" y1="{y+2}" x2="{x+k*cw/4:.1f}" y2="{y+ch-2}" stroke="#1a1d21" stroke-width="1"/>')
        # unidade de refrigeração (painel com luz)
        s.append(f'<rect x="{x+3}" y="{y+5}" width="8" height="10" fill="#1b1e22"/>')
        if random.random() < .5:
            s.append(f'<circle cx="{x+7}" cy="{y+10}" r="1.6" fill="#c9a45c" opacity=".9"/>')
# floco (símbolo de refrigeração) em um contêiner de destaque
fx, fy = hx0 + 20 + 6*(cw+2) + cw/2, deck - ch/2 - 1
for a in (0, 60, 120):
    import math
    r = math.radians(a)
    s.append(f'<line x1="{fx-7*math.cos(r):.1f}" y1="{fy-7*math.sin(r):.1f}" x2="{fx+7*math.cos(r):.1f}" y2="{fy+7*math.sin(r):.1f}" stroke="#c9a45c" stroke-width="1.6"/>')
# reflexo do navio
s.append(f'<rect x="{hx0+18}" y="{deck+46}" width="{hx1-hx0-48}" height="40" fill="#1a1c20" opacity=".45"/>')
# cancela fechada em primeiro plano (direita), com lâmpada dourada
px, py = 900, 452
s.append(f'<rect x="{px}" y="{py-90}" width="34" height="96" fill="#1c1f23" stroke="#2c2f34"/>')
s.append(f'<rect x="{px-6}" y="{py+4}" width="46" height="10" fill="#15171a"/>')
s.append(f'<circle cx="{px+17}" cy="{py-104}" r="70" fill="url(#lamp)"/>')
s.append(f'<rect x="{px+9}" y="{py-112}" width="16" height="14" rx="3" fill="#e2bd72"/>')
# braço da cancela (listras)
bx0, bx1, by = 470, px+10, py-58
s.append(f'<rect x="{bx0}" y="{by}" width="{bx1-bx0}" height="13" fill="#d9d2c3"/>')
seg = 30
x = bx0
i = 0
while x < bx1:
    if i % 2 == 0:
        s.append(f'<polygon points="{x},{by} {min(x+seg,bx1)},{by} {min(x+seg-8,bx1)},{by+13} {x-8 if x>bx0 else x},{by+13}" fill="#c9a45c"/>')
    x += seg; i += 1
s.append(f'<rect x="{bx0}" y="{by+13}" width="{bx1-bx0}" height="2" fill="#000" opacity=".4"/>')
s.append(f'<rect x="{bx0-4}" y="{by-2}" width="8" height="17" fill="#2a2d32"/>')
# píer em primeiro plano
s.append(f'<path d="M420 {py+14} L1080 {py+14} L1080 {py+40} L380 {py+40} Z" fill="#121418"/>')
for k in range(9):
    xx = 440 + k*72
    s.append(f'<rect x="{xx}" y="{py+14}" width="4" height="26" fill="#1c1f23"/>')
s.append(f'<rect width="{W}" height="{H}" fill="url(#fade)"/>')
s.append(f'<rect width="{W}" height="{H}" fill="url(#vign)"/>')
s.append('</svg>')
open('bg.svg', 'w').write("\n".join(s))
print('bg.svg ok')
