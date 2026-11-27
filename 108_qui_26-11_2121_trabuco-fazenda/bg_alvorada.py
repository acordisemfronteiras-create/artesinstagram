"""Capa: colunata de palácio modernista em Brasília ao entardecer, espelho d'água e céu do Planalto (sem pessoas, sem marcas)."""
import random
random.seed(1126)
W, H = 1080, 1350
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0d121b"/><stop offset="0.16" stop-color="#1a2232"/>
 <stop offset="0.26" stop-color="#3b3226"/><stop offset="0.31" stop-color="#5a4426"/><stop offset="0.36" stop-color="#1a1610"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="sun" cx="0.5" cy="0.30" r="0.38">
 <stop offset="0" stop-color="#e6c27a" stop-opacity="0.45"/><stop offset="0.4" stop-color="#c9a45c" stop-opacity="0.14"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="slab" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9d2c2"/><stop offset="1" stop-color="#8f897c"/></linearGradient>
<linearGradient id="col" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ece4d2"/><stop offset="0.6" stop-color="#bdb5a3"/><stop offset="1" stop-color="#7d776b"/></linearGradient>
<linearGradient id="glass" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a2a26"/><stop offset="0.5" stop-color="#4a3a22"/><stop offset="1" stop-color="#14120e"/></linearGradient>
<linearGradient id="water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2b2418"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.3"/><stop offset="0.1" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.30" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.36" stop-color="#0a0a0a" stop-opacity="0.7"/>
 <stop offset="0.40" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<filter id="blur"><feGaussianBlur stdDeviation="2.2"/></filter>
<filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="9"/>
 <feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="table" tableValues="0 0.06"/></feComponentTransfer></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/><rect width="100%" height="100%" fill="url(#sun)"/>''')
for _ in range(40):
    s.append(f'<circle cx="{random.uniform(0,W):.0f}" cy="{random.uniform(20,170):.0f}" r="0.9" fill="#e8e0cc" opacity="{random.uniform(.1,.35):.2f}"/>')
# thin cloud streaks
for y, x, w in [(250, 80, 380), (272, 620, 340), (300, 180, 260)]:
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="3" rx="1.5" fill="#e6c27a" opacity="0.18"/>')
# palace: roof slab, glass box, curved colonnade
ROOF, BASE = 236, 396
s.append(f'<rect x="60" y="{ROOF-14}" width="960" height="16" fill="url(#slab)"/>')
s.append(f'<rect x="60" y="{ROOF+2}" width="960" height="4" fill="#5e594f"/>')
s.append(f'<rect x="150" y="{ROOF+6}" width="780" height="{BASE-ROOF-14}" fill="url(#glass)"/>')
for gx in range(150, 931, 26):
    s.append(f'<line x1="{gx}" y1="{ROOF+6}" x2="{gx}" y2="{BASE-8}" stroke="#c9a45c" stroke-opacity="0.12"/>')
s.append(f'<line x1="150" y1="{(ROOF+BASE)//2}" x2="930" y2="{(ROOF+BASE)//2}" stroke="#c9a45c" stroke-opacity="0.18"/>')
# warm interior lights
for _ in range(14):
    x = random.randint(160, 900); y = random.randint(ROOF + 20, BASE - 40)
    s.append(f'<rect x="{x}" y="{y}" width="{random.randint(10,24)}" height="{random.randint(6,14)}" fill="#f1d79a" opacity="{random.uniform(.15,.4):.2f}"/>')
# floor slab
s.append(f'<rect x="60" y="{BASE-8}" width="960" height="10" fill="url(#slab)" opacity="0.9"/>')
# columns: inverted-arch shape touching roof and floor at points
def column(cx, w=92):
    top, bot = ROOF + 2, BASE - 8
    mid = (top + bot) / 2
    hw = w / 2
    d = (f"M{cx-hw},{top} Q{cx},{top+40} {cx+hw},{top} "
         f"L{cx+6},{mid} L{cx+hw},{bot} Q{cx},{bot-40} {cx-hw},{bot} L{cx-6},{mid} Z")
    return f'<path d="{d}" fill="url(#col)"/><path d="{d}" fill="none" stroke="#5e594f" stroke-opacity="0.5"/>'
for cx in range(110, 1000, 108):
    s.append(column(cx))
# ground & reflecting pool
s.append(f'<rect x="0" y="{BASE+2}" width="{W}" height="10" fill="#1d1a14"/>')
s.append(f'<rect x="0" y="{BASE+12}" width="{W}" height="110" fill="url(#water)"/>')
refl = [f'<g transform="translate(0 {2*(BASE+12)}) scale(1 -1)" opacity="0.28" filter="url(#blur)">']
for cx in range(110, 1000, 108):
    refl.append(column(cx))
refl.append(f'<rect x="60" y="{ROOF-14}" width="960" height="16" fill="#bdb5a3"/></g>')
s += refl
for y in range(BASE + 22, BASE + 110, 12):
    s.append(f'<line x1="{random.randint(0,200)}" y1="{y}" x2="{random.randint(800,1080)}" y2="{y}" stroke="#e6c27a" stroke-opacity="0.07"/>')
s.append('<rect width="100%" height="100%" fill="url(#fade)"/><rect width="100%" height="100%" filter="url(#grain)"/></svg>')
open("bg.svg", "w").write("\n".join(s))
