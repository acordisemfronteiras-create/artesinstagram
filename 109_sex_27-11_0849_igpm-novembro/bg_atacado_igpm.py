"""Fundo: pavilhão de atacado de hortifrúti (tipo central de abastecimento) sob um sol forte de El Niño,
com pilhas de caixotes de tomate e cebola, balança de plataforma, fileira de casas com chaves (aluguel)
ao fundo e, no céu, a linha do IGP-M mensal (genérica) desacelerando em patamar alto."""
import random, sys, math

random.seed(2711)
W, H = 1080, 1350
HZ = 450

s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
 <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#141210"/><stop offset="0.16" stop-color="#2a1f14"/>
  <stop offset="0.27" stop-color="#3a2a17"/><stop offset="0.32" stop-color="#1c1610"/>
  <stop offset="0.45" stop-color="#0b0b0b"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
 <radialGradient id="sun" cx="0.80" cy="0.16" r="0.55">
  <stop offset="0" stop-color="#e3b862" stop-opacity="0.45"/><stop offset="0.25" stop-color="#c9a45c" stop-opacity="0.16"/>
  <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
 <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.35"/><stop offset="0.10" stop-color="#0a0a0a" stop-opacity="0"/>
  <stop offset="0.27" stop-color="#0a0a0a" stop-opacity="0.05"/><stop offset="0.35" stop-color="#0a0a0a" stop-opacity="0.72"/>
  <stop offset="0.41" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
 <radialGradient id="vign" cx="0.5" cy="0.25" r="0.8">
  <stop offset="0.5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.7"/></radialGradient>
 <linearGradient id="roof" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#3a3126"/><stop offset="1" stop-color="#1a1612"/></linearGradient>
 <radialGradient id="lamp" cx="0.5" cy="0" r="1">
  <stop offset="0" stop-color="#e8c27a" stop-opacity="0.20"/><stop offset="1" stop-color="#e8c27a" stop-opacity="0"/></radialGradient>
</defs>''')
s.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
s.append(f'<rect width="{W}" height="700" fill="url(#sun)"/>')

# sol com raios (El Niño)
sx, sy = 860, 215
for i in range(28):
    a = i * math.pi * 2 / 28
    r1, r2 = 62, 62 + (34 if i % 2 == 0 else 18)
    s.append(f'<line x1="{sx+r1*math.cos(a):.1f}" y1="{sy+r1*math.sin(a):.1f}" x2="{sx+r2*math.cos(a):.1f}" '
             f'y2="{sy+r2*math.sin(a):.1f}" stroke="#c9a45c" stroke-width="2" opacity="0.45" stroke-linecap="round"/>')
s.append(f'<circle cx="{sx}" cy="{sy}" r="50" fill="#d9b36a" opacity="0.85"/>')
s.append(f'<circle cx="{sx}" cy="{sy}" r="50" fill="none" stroke="#f0d79a" stroke-width="2" opacity="0.6"/>')
# ondas de calor
for k in range(3):
    y = 255 + k * 16
    d = f"M{sx-120},{y} " + " ".join(f"q 15,{-6 if j%2==0 else 6} 30,0" for j in range(8))
    s.append(f'<path d="{d}" fill="none" stroke="#c9a45c" stroke-width="1.4" opacity="{0.28-k*0.07:.2f}"/>')

# linha genérica do índice mensal (barras + linha), sem valores
bx0, base = 120, 205
bars = [24, 41, 15, 67, 28, 13, 8, 11, 52, 46, 41]
for i, h in enumerate(bars):
    x = bx0 + i * 44
    op = 0.55 if i == len(bars) - 1 else 0.22
    s.append(f'<rect x="{x}" y="{base-h}" width="26" height="{h}" fill="#c9a45c" opacity="{op}"/>')
s.append(f'<line x1="{bx0-10}" y1="{base}" x2="{bx0+len(bars)*44-6}" y2="{base}" stroke="#c9a45c" stroke-width="1" opacity="0.4"/>')
pts = [(bx0 + i * 44 + 13, base - h - 14) for i, h in enumerate(bars)]
d = "M" + " L".join(f"{x},{y}" for x, y in pts)
s.append(f'<path d="{d}" fill="none" stroke="#e0bd78" stroke-width="2.5" opacity="0.8" stroke-linejoin="round"/>')
lx, ly = pts[-1]
s.append(f'<circle cx="{lx}" cy="{ly}" r="6" fill="#e0bd78"/><circle cx="{lx}" cy="{ly}" r="14" fill="#c9a45c" opacity="0.2"/>')

# casas ao fundo (aluguel)
x = -20
while x < W + 20:
    w = random.randint(70, 110); h = random.randint(30, 55)
    top = HZ - 150 - h
    s.append(f'<rect x="{x}" y="{top}" width="{w}" height="{h+40}" fill="#15130f"/>')
    s.append(f'<polygon points="{x-6},{top} {x+w/2},{top-34} {x+w+6},{top}" fill="#1b1813"/>')
    for wx in (x + 14, x + w - 30):
        if random.random() < .5:
            s.append(f'<rect x="{wx}" y="{top+16}" width="16" height="18" fill="#c9a45c" opacity="{random.uniform(.25,.55):.2f}"/>')
    x += w + random.randint(6, 18)


# pavilhão de atacado (telhado em arcos)
px0, px1, ptop = 60, 1020, HZ - 190
# chão e fundo escuro sob o telhado
s.append(f'<rect x="0" y="{ptop+40}" width="{W}" height="{H}" fill="#110f0d"/>')
s.append(f'<rect x="0" y="{HZ-14}" width="{W}" height="3" fill="#2b241b"/>')
nar = 4
aw = (px1 - px0) / nar
for i in range(nar):
    ax = px0 + i * aw
    s.append(f'<path d="M{ax},{ptop+40} Q{ax+aw/2},{ptop-30} {ax+aw},{ptop+40} Z" fill="url(#roof)" stroke="#5a4a33" stroke-width="1.5"/>')
    for j in range(1, 6):
        t = j / 6
        xx = ax + aw * t
        yy = (1 - t) ** 2 * (ptop + 40) + 2 * (1 - t) * t * (ptop - 30) + t ** 2 * (ptop + 40)
        s.append(f'<line x1="{xx:.1f}" y1="{yy:.1f}" x2="{xx:.1f}" y2="{ptop+40}" stroke="#4a3d2b" stroke-width="1" opacity="0.7"/>')
s.append(f'<rect x="{px0-10}" y="{ptop+38}" width="{px1-px0+20}" height="10" fill="#2b241b"/>')
# colunas
for i in range(nar + 1):
    cx = px0 + i * aw
    s.append(f'<rect x="{cx-5}" y="{ptop+48}" width="10" height="{HZ-ptop-60}" fill="#241e17"/>')
# luminárias
for i in range(nar):
    cx = px0 + i * aw + aw / 2
    s.append(f'<line x1="{cx}" y1="{ptop+48}" x2="{cx}" y2="{ptop+70}" stroke="#3a3126" stroke-width="2"/>')
    s.append(f'<path d="M{cx-14},{ptop+80} L{cx-7},{ptop+70} L{cx+7},{ptop+70} L{cx+14},{ptop+80} Z" fill="#c9a45c" opacity="0.8"/>')
    s.append(f'<polygon points="{cx-14},{ptop+80} {cx+14},{ptop+80} {cx+90},{HZ-12} {cx-90},{HZ-12}" fill="url(#lamp)"/>')

# caixotes
def caixote(x, y, w, h, fruta, rnd):
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#5a4329" stroke="#2d2216" stroke-width="1.5"/>')
    for k in range(1, 3):
        s.append(f'<line x1="{x}" y1="{y+h*k/3:.1f}" x2="{x+w}" y2="{y+h*k/3:.1f}" stroke="#3a2b1b" stroke-width="1.5"/>')
    n = int(w / 13)
    for k in range(n):
        fx = x + 8 + k * (w - 16) / max(n - 1, 1)
        fy = y - 3 + rnd.uniform(-2, 2)
        if fruta == "tomate":
            s.append(f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="7" fill="#9c3a2a"/><circle cx="{fx-2:.1f}" cy="{fy-2:.1f}" r="2" fill="#d77a5e" opacity="0.7"/>')
            s.append(f'<path d="M{fx-3:.1f},{fy-6:.1f} l3,2 l3,-2" stroke="#4d6b33" stroke-width="1.5" fill="none"/>')
        else:
            s.append(f'<ellipse cx="{fx:.1f}" cy="{fy:.1f}" rx="7" ry="6.5" fill="#b8874a"/><path d="M{fx:.1f},{fy-6:.1f} l0,-5" stroke="#d6b07a" stroke-width="1.5"/>')
            s.append(f'<path d="M{fx-4:.1f},{fy+1:.1f} q4,-6 8,0" stroke="#8a6234" stroke-width="1" fill="none"/>')

rnd = random.Random(7)
groundy = HZ - 10
stacks = [(95, "tomate", 4), (225, "cebola", 3), (355, "tomate", 2), (640, "cebola", 2), (770, "tomate", 3), (900, "cebola", 4)]
for sx0, fr, nlev in stacks:
    for lv in range(nlev):
        for c in range(2):
            caixote(sx0 + c * 58 + (lv % 2) * 4, groundy - (lv + 1) * 34, 54, 32, fr if lv == nlev - 1 else ("tomate" if fr == "tomate" else "cebola"), rnd)

# balança de plataforma no centro
bx = 540
s.append(f'<rect x="{bx-70}" y="{groundy-14}" width="140" height="14" fill="#2c2620" stroke="#5a4a33"/>')
s.append(f'<rect x="{bx-6}" y="{groundy-110}" width="12" height="96" fill="#2c2620"/>')
s.append(f'<circle cx="{bx}" cy="{groundy-128}" r="30" fill="#1a1712" stroke="#c9a45c" stroke-width="2.5"/>')
for i in range(9):
    a = math.pi * (1.15 + 0.7 * i / 8)
    s.append(f'<line x1="{bx+22*math.cos(a):.1f}" y1="{groundy-128+22*math.sin(a):.1f}" x2="{bx+27*math.cos(a):.1f}" y2="{groundy-128+27*math.sin(a):.1f}" stroke="#c9a45c" stroke-width="1.5"/>')
s.append(f'<line x1="{bx}" y1="{groundy-128}" x2="{bx+18}" y2="{groundy-144}" stroke="#e0bd78" stroke-width="2.5" stroke-linecap="round"/>')
caixote(bx - 46, groundy - 48, 44, 32, "tomate", rnd)
caixote(bx + 2, groundy - 48, 44, 32, "cebola", rnd)

# chave (aluguel) pendurada na coluna central
kx, ky = px0 + 2 * aw + 22, ptop + 120
s.append(f'<line x1="{kx-22}" y1="{ky-26}" x2="{kx}" y2="{ky-10}" stroke="#8f7a52" stroke-width="1.5"/>')
s.append(f'<circle cx="{kx}" cy="{ky}" r="11" fill="none" stroke="#c9a45c" stroke-width="3"/>')
s.append(f'<path d="M{kx},{ky+11} l0,34 m0,-10 l8,0 m-8,-8 l6,0" stroke="#c9a45c" stroke-width="3" fill="none"/>')

s.append(f'<rect width="{W}" height="{H}" fill="url(#fade)"/>')
s.append(f'<rect width="{W}" height="{H}" fill="url(#vign)"/>')
s.append(f'<rect x="0" y="560" width="{W}" height="{H-560}" fill="#0a0a0a"/>')
s.append('</svg>')
open(sys.argv[1] if len(sys.argv) > 1 else "bg.svg", "w").write("\n".join(s))
