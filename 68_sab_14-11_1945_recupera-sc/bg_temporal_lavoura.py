"""Fundo: temporal sobre o interior de SC (coxilhas, silo, aviários), com luz dourada abrindo no horizonte."""
import random, math
random.seed(1411)
W, H = 1080, 1350
HZ = 420  # horizonte
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0d1117"/><stop offset="0.18" stop-color="#151b24"/>
 <stop offset="0.29" stop-color="#232326"/><stop offset="0.33" stop-color="#3a3024"/>
 <stop offset="0.40" stop-color="#0c0c0c"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="breach" cx="0.78" cy="0.29" r="0.42">
 <stop offset="0" stop-color="#e2c27e" stop-opacity="0.42"/><stop offset="0.35" stop-color="#c9a45c" stop-opacity="0.16"/>
 <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="cloud" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#1c222c"/><stop offset="1" stop-color="#0e1218"/></linearGradient>
<linearGradient id="hill1" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#1a1d1a"/><stop offset="1" stop-color="#0d0e0d"/></linearGradient>
<linearGradient id="hill2" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#131512"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.35"/><stop offset="0.12" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.28" stop-color="#0a0a0a" stop-opacity="0.04"/><stop offset="0.37" stop-color="#0a0a0a" stop-opacity="0.75"/>
 <stop offset="0.43" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.28" r="0.85">
 <stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
<filter id="blur6"><feGaussianBlur stdDeviation="6"/></filter>
<filter id="blur2"><feGaussianBlur stdDeviation="2"/></filter>
<filter id="glowf"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>''')
s.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
s.append(f'<rect width="{W}" height="{HZ+60}" fill="url(#breach)"/>')

# raios de sol saindo da abertura nas nuvens (direita)
s.append('<g filter="url(#blur6)">')
cx, cy = 840, 300
for a in range(-150, -20, 9):
    r = math.radians(a + random.uniform(-2, 2))
    L = random.uniform(260, 420); w = random.uniform(5, 14)
    x2, y2 = cx + L*math.cos(r), cy + L*math.sin(r)*0.55 + 120
    s.append(f'<line x1="{cx}" y1="{cy}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#c9a45c" stroke-opacity="{random.uniform(.03,.07):.3f}" stroke-width="{w:.0f}"/>')
s.append('</g>')

# massas de nuvem de tempestade (esquerda/centro, pesadas)
def cloudbank(y0, n, x0, x1, rmin, rmax, op, col="url(#cloud)"):
    out = []
    for i in range(n):
        x = random.uniform(x0, x1); y = y0 + random.uniform(-30, 30)
        rx = random.uniform(rmin, rmax); ry = rx*random.uniform(.35, .55)
        out.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{rx:.0f}" ry="{ry:.0f}" fill="{col}" opacity="{op}"/>')
    return out
s.append('<g filter="url(#blur6)">')
s += cloudbank(40, 14, -80, 900, 120, 230, .95)
s += cloudbank(140, 12, -80, 700, 100, 200, .9)
s += cloudbank(220, 8, -60, 560, 80, 160, .85)
s.append('</g>')
# borda iluminada das nuvens perto da abertura
s.append('<g filter="url(#blur6)">')
for i in range(5):
    x = random.uniform(600, 800); y = random.uniform(150, 260)
    s.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{random.uniform(60,110):.0f}" ry="{random.uniform(14,26):.0f}" fill="#c9a45c" fill-opacity=".06"/>')
s.append('</g>')

# cortina de chuva (esquerda)
for i in range(260):
    x = random.uniform(-40, 640); y = random.uniform(150, HZ)
    L = random.uniform(22, 60)
    s.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x-L*0.32:.0f}" y2="{y+L:.0f}" stroke="#8fa0b4" stroke-opacity="{random.uniform(.08,.22):.2f}" stroke-width="1.2"/>')

# raio dourado ao longe
pts = [(250, 120), (232, 190), (258, 196), (226, 275), (250, 280), (214, 372)]
d = "M" + " L".join(f"{x},{y}" for x, y in pts)
s.append(f'<path d="{d}" fill="none" stroke="#e8cf92" stroke-width="3.2" stroke-linejoin="bevel" filter="url(#glowf)" opacity=".9"/>')
s.append(f'<path d="M232,190 L205,228 L214,232 L196,262" fill="none" stroke="#e8cf92" stroke-width="1.6" opacity=".55" filter="url(#glowf)"/>')

# coxilhas ao fundo
def hill(base, amp, seed, fill, op=1):
    random.seed(seed)
    ph = random.uniform(0, 6)
    pts = []
    for x in range(-20, W+41, 20):
        y = base - amp*(0.6*math.sin(x/170+ph) + 0.4*math.sin(x/73+ph*2))
        pts.append(f"{x},{y:.1f}")
    return f'<polygon points="-20,{H} {" ".join(pts)} {W+40},{H}" fill="{fill}" opacity="{op}"/>'
s.append(hill(HZ-38, 14, 3, "#1d1f22", .9))
s.append(hill(HZ-14, 18, 9, "url(#hill1)"))

# lavoura em linhas (curvas de nível) na encosta da frente
random.seed(77)
for k in range(9):
    y = HZ - 4 + k*7
    s.append(f'<path d="M{-20},{y+6} Q{300},{y-10} {560},{y+2} T{1100},{y-4}" fill="none" stroke="#3a3a2c" stroke-opacity="{.45-k*.03:.2f}" stroke-width="1.4"/>')

# aviários (galpões longos) no meio
def barn(x, y, w, h, roof):
    g = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#121315"/>',
         f'<polygon points="{x-6},{y} {x+w/2},{y-roof} {x+w+6},{y}" fill="#1b1d21"/>',
         f'<line x1="{x-6}" y1="{y}" x2="{x+w+6}" y2="{y}" stroke="#c9a45c" stroke-opacity=".25" stroke-width="1"/>']
    for i in range(int(w//22)):
        g.append(f'<rect x="{x+8+i*22}" y="{y+h*0.35:.0f}" width="12" height="3" fill="#c9a45c" opacity="{random.choice([.0,.15,.35,.5])}"/>')
    return g
s += barn(520, 388, 230, 18, 10)
s += barn(560, 410, 260, 20, 11)
# telhas soltas sobre o galpão da frente (vento)
for i in range(9):
    x = random.uniform(600, 900); y = random.uniform(330, 395)
    a = random.uniform(-40, 40)
    s.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="10" height="5" fill="#2a2c30" transform="rotate({a:.0f} {x:.0f} {y:.0f})" opacity=".8"/>')

# silo e casa à esquerda
sx = 330
s.append(f'<rect x="{sx}" y="300" width="58" height="110" fill="#16181b"/>')
s.append(f'<path d="M{sx},300 Q{sx+29},270 {sx+58},300 Z" fill="#1f2226"/>')
for i in range(6):
    s.append(f'<line x1="{sx}" y1="{312+i*16}" x2="{sx+58}" y2="{312+i*16}" stroke="#2c3036" stroke-width="1.2"/>')
s.append(f'<line x1="{sx+29}" y1="268" x2="{sx+29}" y2="300" stroke="#c9a45c" stroke-opacity=".35"/>')
s.append(f'<rect x="{sx+66}" y="330" width="44" height="80" fill="#131518"/>')
s.append(f'<path d="M{sx+66},330 L{sx+88},312 L{sx+110},330 Z" fill="#1d2024"/>')
s.append(f'<rect x="{sx+72}" y="372" width="14" height="38" fill="#0d0e10"/>')
# casa com janela acesa
s.append('<rect x="190" y="382" width="70" height="34" fill="#141619"/>')
s.append('<polygon points="184,382 225,360 266,382" fill="#1e2125"/>')
s.append('<rect x="206" y="392" width="12" height="10" fill="#e2c27e" opacity=".8"/>')
s.append('<rect x="232" y="392" width="12" height="10" fill="#e2c27e" opacity=".45"/>')
# araucárias
def arauc(x, base, h):
    g = [f'<line x1="{x}" y1="{base}" x2="{x}" y2="{base-h}" stroke="#101113" stroke-width="4"/>']
    for k in range(4):
        y = base - h + k*h*0.12
        wdt = 26 + k*10
        g.append(f'<path d="M{x-wdt},{y+10} Q{x},{y-14} {x+wdt},{y+10}" fill="#101113"/>')
    return g
for x, b, h in [(60, 410, 120), (120, 406, 95), (960, 404, 110), (1015, 410, 86), (455, 402, 70)]:
    s += arauc(x, b, h)
# cerca
for i in range(30):
    x = 20 + i*36
    s.append(f'<line x1="{x}" y1="430" x2="{x}" y2="446" stroke="#1d1f22" stroke-width="3"/>')
s.append('<line x1="0" y1="436" x2="1080" y2="434" stroke="#1d1f22" stroke-width="1.5"/>')
# primeiro plano escuro
s.append(hill(HZ+40, 6, 21, "url(#hill2)"))
s.append(f'<rect width="{W}" height="{H}" fill="url(#fade)"/>')
s.append(f'<rect width="{W}" height="{H}" fill="url(#vign)"/>')
s.append(f'<rect y="{H-700}" width="{W}" height="700" fill="#0a0a0a"/>')
s.append('</svg>')
open("bg.svg", "w").write("\n".join(s))
