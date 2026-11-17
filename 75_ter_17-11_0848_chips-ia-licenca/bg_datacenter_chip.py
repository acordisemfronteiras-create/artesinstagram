import random, sys
from pathlib import Path
random.seed(17)
W, H = 1080, 1350
VX, VY = 540, 250          # ponto de fuga
FLOOR = 450                # linha do piso na borda da arte
def lerp(a,b,t): return a+(b-a)*t
def toward(x,y,t):         # move ponto (x,y) em direção ao ponto de fuga
    return lerp(x,VX,t), lerp(y,VY,t)

s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
<linearGradient id="bgg" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0e131b"/><stop offset="0.20" stop-color="#151c27"/>
 <stop offset="0.33" stop-color="#11161e"/><stop offset="0.42" stop-color="#0c0d10"/>
 <stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="core" cx="0.5" cy="0.185" r="0.32">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.30"/>
 <stop offset="0.5" stop-color="#c9a45c" stop-opacity="0.07"/>
 <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="rackL" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#151a22"/><stop offset="1" stop-color="#0b0e13"/></linearGradient>
<linearGradient id="rackR" x1="1" y1="0" x2="0" y2="0">
 <stop offset="0" stop-color="#151a22"/><stop offset="1" stop-color="#0b0e13"/></linearGradient>
<linearGradient id="die" x1="0" y1="0" x2="1" y2="1">
 <stop offset="0" stop-color="#232933"/><stop offset="0.5" stop-color="#151a21"/><stop offset="1" stop-color="#0d1015"/></linearGradient>
<linearGradient id="gold" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#e2c27f"/><stop offset="1" stop-color="#9c7a3c"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.25"/>
 <stop offset="0.12" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.27" stop-color="#0a0a0a" stop-opacity="0.04"/>
 <stop offset="0.36" stop-color="#0a0a0a" stop-opacity="0.75"/>
 <stop offset="0.42" stop-color="#0a0a0a" stop-opacity="1"/>
 <stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.25" r="0.8">
 <stop offset="0.5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.7"/></radialGradient>
<filter id="blur"><feGaussianBlur stdDeviation="2.2"/></filter>
<filter id="blur6"><feGaussianBlur stdDeviation="7"/></filter>
<filter id="grain" x="0" y="0" width="100%" height="100%">
 <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="5"/>
 <feColorMatrix type="saturate" values="0"/>
 <feComponentTransfer><feFuncA type="table" tableValues="0 0.07"/></feComponentTransfer></filter>
</defs>
<rect width="100%" height="100%" fill="url(#bgg)"/>''')

# ---- teto: luminárias lineares convergindo
for k in range(7):
    t0 = k/7; t1 = t0 + 0.045
    for xo in (360, 720):
        x0,y0 = toward(xo, -10, t0); x1,y1 = toward(xo,-10,t1)
        s.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="#cfd8e3" stroke-opacity="{0.28-0.03*k:.2f}" stroke-width="{6-0.6*k:.1f}" stroke-linecap="round"/>')
# bandeja de cabos no teto
for side in (-1,1):
    xo = 540 + side*470
    x1,y1 = toward(xo, 40, 0.9)
    s.append(f'<line x1="{xo}" y1="40" x2="{x1:.1f}" y2="{y1:.1f}" stroke="#2b333f" stroke-width="3"/>')
    xo2 = 540 + side*300
    x2,y2 = toward(xo2, -20, 0.9)
    s.append(f'<line x1="{xo2}" y1="-20" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#202732" stroke-width="2"/>')

# ---- piso: placas elevadas
for i in range(-9,10):
    xo = 540 + i*120
    x1,y1 = toward(xo, FLOOR+40, 0.92)
    s.append(f'<line x1="{xo}" y1="{FLOOR+40}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="#7d8896" stroke-opacity="0.10"/>')
for t in (0.0,0.18,0.34,0.48,0.6,0.7,0.78,0.85):
    y = lerp(FLOOR+40, VY, t)
    s.append(f'<line x1="0" y1="{y:.1f}" x2="{W}" y2="{y:.1f}" stroke="#7d8896" stroke-opacity="{0.08:.2f}"/>')
# faixa de luz dourada no corredor
s.append(f'<polygon points="470,{FLOOR+40} 610,{FLOOR+40} {VX+6},{VY+8} {VX-6},{VY+8}" fill="#c9a45c" fill-opacity="0.07"/>')

# ---- fileiras de racks (esquerda e direita)
def rack_row(side):
    # face interna da fileira: do primeiro plano (x0) ao fundo
    xo_near = 540 + side*300           # borda interna próxima
    top_near, bot_near = 40, FLOOR+30
    n = 9
    ts = [0.0,0.15,0.28,0.39,0.49,0.57,0.64,0.70,0.75,0.79]
    for k in range(n):
        ta, tb = ts[k], ts[k+1]
        xa,ya_t = toward(xo_near, top_near, ta); _,ya_b = toward(xo_near, bot_near, ta)
        xb,yb_t = toward(xo_near, top_near, tb); _,yb_b = toward(xo_near, bot_near, tb)
        grad = "rackL" if side<0 else "rackR"
        s.append(f'<polygon points="{xa:.1f},{ya_t:.1f} {xb:.1f},{yb_t:.1f} {xb:.1f},{yb_b:.1f} {xa:.1f},{ya_b:.1f}" fill="url(#{grad})" stroke="#2e3743" stroke-width="1"/>')
        # porta perfurada: linhas horizontais (slots de servidores)
        units = 22
        for u in range(1,units):
            f = u/units
            yA = lerp(ya_t, ya_b, f); yB = lerp(yb_t, yb_b, f)
            s.append(f'<line x1="{xa:.1f}" y1="{yA:.1f}" x2="{xb:.1f}" y2="{yB:.1f}" stroke="#3a4552" stroke-opacity="0.35" stroke-width="0.8"/>')
            # LEDs
            if random.random() < 0.5:
                g = random.uniform(0.12,0.88)
                lx = lerp(xa,xb,g); ly = lerp(yA,yB,g) - 0.35*abs(yA-lerp(ya_t,ya_b,(u-1)/units))
                col = random.choice(["#e3b96a","#e3b96a","#7fd0c4","#cfd8e3"])
                r = max(0.8, 2.4*(1-ta*1.1))
                s.append(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="{r:.1f}" fill="{col}" fill-opacity="{random.uniform(0.35,0.95):.2f}"/>')
        # topo do rack
        s.append(f'<line x1="{xa:.1f}" y1="{ya_t:.1f}" x2="{xb:.1f}" y2="{yb_t:.1f}" stroke="#c9a45c" stroke-opacity="0.22" stroke-width="1.2"/>')
    # face frontal (lado de fora, voltada pra borda)
    xedge = 0 if side<0 else W
    s.append(f'<polygon points="{xo_near},{top_near} {xedge},{top_near-18} {xedge},{bot_near+22} {xo_near},{bot_near}" fill="#07090c"/>')
    # brilho de LEDs na face frontal
    for u in range(24):
        y = lerp(top_near+10, bot_near-10, u/24)
        if random.random()<0.55:
            x = lerp(xo_near, xedge, random.uniform(0.1,0.6))
            s.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{random.randint(10,40)}" height="2.2" fill="#e3b96a" fill-opacity="{random.uniform(0.15,0.5):.2f}"/>')
        if random.random()<0.25:
            x = lerp(xo_near, xedge, random.uniform(0.1,0.7))
            s.append(f'<circle cx="{x:.1f}" cy="{y+4:.1f}" r="2.4" fill="#7fd0c4" fill-opacity="0.6"/>')
    s.append(f'<line x1="{xo_near}" y1="{top_near}" x2="{xo_near}" y2="{bot_near}" stroke="#c9a45c" stroke-opacity="0.35" stroke-width="1.5"/>')
rack_row(-1); rack_row(1)

# ---- brilho central
s.append('<rect width="100%" height="100%" fill="url(#core)"/>')

# ---- chip flutuante com cadeado
cx, cy, half = 540, 236, 92
# traços de circuito saindo do chip
for side in (-1,1):
    for k in range(5):
        y = cy - 60 + k*30
        x0 = cx + side*(half+20)
        x1 = x0 + side*random.randint(40,70)
        y2 = y + random.choice([-24,-12,12,24])
        x2 = x1 + side*random.randint(30,60)
        s.append(f'<polyline points="{x0},{y} {x1},{y} {x2},{y2}" fill="none" stroke="#c9a45c" stroke-opacity="0.45" stroke-width="1.6"/>')
        s.append(f'<circle cx="{x2}" cy="{y2}" r="3.2" fill="none" stroke="#c9a45c" stroke-opacity="0.7" stroke-width="1.4"/>')
s.append(f'<rect x="{cx-half-6}" y="{cy-half-6}" width="{2*half+12}" height="{2*half+12}" rx="10" fill="#c9a45c" fill-opacity="0.18" filter="url(#blur6)"/>')
# pinos
for k in range(12):
    p = cx-half+12 + k*((2*half-24)/11)
    s.append(f'<rect x="{p-3:.1f}" y="{cy-half-20}" width="6" height="20" fill="url(#gold)"/>')
    s.append(f'<rect x="{p-3:.1f}" y="{cy+half}" width="6" height="20" fill="url(#gold)"/>')
    q = cy-half+12 + k*((2*half-24)/11)
    s.append(f'<rect x="{cx-half-20}" y="{q-3:.1f}" width="20" height="6" fill="url(#gold)"/>')
    s.append(f'<rect x="{cx+half}" y="{q-3:.1f}" width="20" height="6" fill="url(#gold)"/>')
s.append(f'<rect x="{cx-half}" y="{cy-half}" width="{2*half}" height="{2*half}" rx="8" fill="url(#die)" stroke="#c9a45c" stroke-width="2"/>')
s.append(f'<rect x="{cx-half+14}" y="{cy-half+14}" width="{2*half-28}" height="{2*half-28}" rx="4" fill="none" stroke="#c9a45c" stroke-opacity="0.35" stroke-width="1"/>')
# grade interna do die
for k in range(1,8):
    g = cx-half+14 + k*((2*half-28)/8)
    s.append(f'<line x1="{g:.1f}" y1="{cy-half+14}" x2="{g:.1f}" y2="{cy+half-14}" stroke="#8796a8" stroke-opacity="0.10"/>')
    s.append(f'<line x1="{cx-half+14}" y1="{g:.1f}" x2="{cx+half-14}" y2="{g:.1f}" stroke="#8796a8" stroke-opacity="0.10"/>')
s.append(f'<circle cx="{cx-half+26}" cy="{cy-half+26}" r="4" fill="#c9a45c" fill-opacity="0.7"/>')
# cadeado
lx, ly = cx, cy+8
s.append(f'<path d="M{lx-24},{ly-12} v-18 a24,24 0 0 1 48,0 v18" fill="none" stroke="url(#gold)" stroke-width="9" stroke-linecap="round"/>')
s.append(f'<rect x="{lx-36}" y="{ly-14}" width="72" height="56" rx="7" fill="url(#gold)"/>')
s.append(f'<rect x="{lx-36}" y="{ly-14}" width="72" height="8" rx="4" fill="#f0d79c" fill-opacity="0.55"/>')
s.append(f'<circle cx="{lx}" cy="{ly+8}" r="7" fill="#151a21"/>')
s.append(f'<rect x="{lx-3}" y="{ly+10}" width="6" height="16" rx="2" fill="#151a21"/>')

# ---- partículas
for _ in range(60):
    x = random.uniform(80,1000); y = random.uniform(20,420)
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{random.uniform(0.6,1.6):.1f}" fill="#e3c88e" fill-opacity="{random.uniform(0.08,0.35):.2f}"/>')

s.append('<rect width="100%" height="100%" fill="url(#fade)"/>')
s.append('<rect width="100%" height="100%" fill="url(#vign)"/>')
s.append('<rect width="100%" height="100%" filter="url(#grain)"/>')
s.append('</svg>')
Path(sys.argv[1] if len(sys.argv)>1 else 'bg.svg').write_text("\n".join(s))
print("ok")
