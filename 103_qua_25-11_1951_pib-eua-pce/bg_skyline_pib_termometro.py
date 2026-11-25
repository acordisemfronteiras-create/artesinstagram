"""Fundo: skyline genérico à noite com gráfico de barras trimestral (PIB) no céu
e termômetro de inflação à direita. Tema: PIB e PCE dos EUA, 25/11/2026."""
import random
random.seed(1125)
W, H = 1080, 1350
HZ = 440  # horizonte
s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0d1420"/><stop offset="0.22" stop-color="#162030"/>
 <stop offset="0.31" stop-color="#2a2a2e"/><stop offset="0.335" stop-color="#3b2f20"/>
 <stop offset="0.40" stop-color="#0d0d0d"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="glow" cx="0.42" cy="0.30" r="0.45">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.20"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="bar" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#8a96a8" stop-opacity="0.55"/><stop offset="1" stop-color="#8a96a8" stop-opacity="0.08"/></linearGradient>
<linearGradient id="barG" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#e3c27e"/><stop offset="0.6" stop-color="#c9a45c" stop-opacity="0.75"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0.12"/></linearGradient>
<linearGradient id="tw" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#0b0e14"/><stop offset="0.5" stop-color="#151b25"/><stop offset="1" stop-color="#090b10"/></linearGradient>
<linearGradient id="merc" x1="0" y1="1" x2="0" y2="0">
 <stop offset="0" stop-color="#c9a45c"/><stop offset="1" stop-color="#e8c987"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.07"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></linearGradient>
<filter id="blur"><feGaussianBlur stdDeviation="6"/></filter>
</defs>''')
s.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
s.append(f'<rect width="{W}" height="{H}" fill="url(#glow)"/>')
# estrelas
for _ in range(70):
    x, y = random.uniform(0, W), random.uniform(150, 330)
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(.5,1.4):.1f}" fill="#d9d2c4" opacity="{random.uniform(.15,.5):.2f}"/>')

# grade do gráfico no céu
gx0, gx1, gbase = 150, 790, 395
for i, yy in enumerate(range(gbase, 170, -45)):
    s.append(f'<line x1="{gx0}" y1="{yy}" x2="{gx1}" y2="{yy}" stroke="#c9a45c" stroke-opacity="{0.10 if i else 0.25}" stroke-dasharray="{"" if i==0 else "3 7"}"/>')
# barras trimestrais (ilustrativas; a última, dourada, é a maior)
heights = [70, 40, 95, 60, 85, 190]
bw, gap = 64, 42
x = gx0 + 30
tops = []
for i, h in enumerate(heights):
    last = i == len(heights) - 1
    fill = "url(#barG)" if last else "url(#bar)"
    if last:
        s.append(f'<rect x="{x-10}" y="{gbase-h-10}" width="{bw+20}" height="{h+10}" fill="#c9a45c" opacity="0.25" filter="url(#blur)"/>')
        # contorno pontilhado da prévia (barra menor)
        s.append(f'<rect x="{x}" y="{gbase-150}" width="{bw}" height="2" fill="#efe6d6" opacity="0.55"/>')
    s.append(f'<rect x="{x}" y="{gbase-h}" width="{bw}" height="{h}" fill="{fill}"/>')
    s.append(f'<rect x="{x}" y="{gbase-h}" width="{bw}" height="3" fill="{"#f0d79c" if last else "#aab4c3"}" opacity="{1 if last else .6}"/>')
    tops.append((x + bw/2, gbase - h))
    x += bw + gap
# seta de revisão para cima sobre a última barra
cx, ty = tops[-1]
s.append(f'<path d="M{cx} {ty-58} l-16 22 h10 v22 h12 v-22 h10 z" fill="#e3c27e"/>')
# linha de tendência
pts = " ".join(f"{px:.0f},{py-18:.0f}" for px, py in tops)
s.append(f'<polyline points="{pts}" fill="none" stroke="#efe6d6" stroke-opacity="0.35" stroke-width="2"/>')
for px, py in tops:
    s.append(f'<circle cx="{px:.0f}" cy="{py-18:.0f}" r="4" fill="#efe6d6" opacity="0.5"/>')

# skyline genérico
def tower(x0, w, top, lit=0.25):
    out = [f'<rect x="{x0}" y="{top}" width="{w}" height="{HZ-top}" fill="url(#tw)"/>',
           f'<rect x="{x0}" y="{top}" width="{w}" height="2" fill="#c9a45c" opacity="0.25"/>']
    for wy in range(top + 10, HZ - 6, 12):
        for wx in range(x0 + 6, x0 + w - 6, 10):
            if random.random() < lit:
                c = "#e3c27e" if random.random() < .7 else "#9fb0c8"
                out.append(f'<rect x="{wx}" y="{wy}" width="4" height="5" fill="{c}" opacity="{random.uniform(.25,.75):.2f}"/>')
    return out
x = -10
while x < W:
    w = random.choice([46, 58, 70, 84, 96])
    top = random.randint(HZ - 120, HZ - 40)
    # torres mais altas nas pontas, mais baixas sob o gráfico
    if x < 120 or x > 960:
        top = random.randint(HZ - 200, HZ - 120)
    s += tower(x, w, top, lit=random.uniform(.12, .3))
    x += w + random.randint(2, 10)
# data center em primeiro plano (investimento em software)
dc_x, dc_w, dc_top = 600, 260, HZ - 46
s.append(f'<rect x="{dc_x}" y="{dc_top}" width="{dc_w}" height="46" fill="#0b0d12" stroke="#c9a45c" stroke-opacity="0.3"/>')
for i in range(12):
    lx = dc_x + 12 + i * 20
    s.append(f'<rect x="{lx}" y="{dc_top+10}" width="12" height="28" fill="#141922"/>')
    for k in range(4):
        if random.random() < .6:
            s.append(f'<circle cx="{lx+6}" cy="{dc_top+15+k*6}" r="1.4" fill="{"#c9a45c" if random.random()<.6 else "#7fb0d8"}"/>')
# termômetro (inflação) à direita
tx, ttop, tbot = 900, 140, 340
s.append(f'<rect x="{tx-22}" y="{ttop}" width="44" height="{tbot-ttop}" rx="22" fill="#10141b" stroke="#c9a45c" stroke-opacity="0.55" stroke-width="2"/>')
s.append(f'<circle cx="{tx}" cy="{tbot+18}" r="36" fill="#10141b" stroke="#c9a45c" stroke-opacity="0.55" stroke-width="2"/>')
s.append(f'<circle cx="{tx}" cy="{tbot+18}" r="26" fill="url(#merc)"/>')
mtop = 190
s.append(f'<rect x="{tx-10}" y="{mtop}" width="20" height="{tbot+10-mtop}" rx="10" fill="url(#merc)"/>')
s.append(f'<circle cx="{tx}" cy="{tbot+18}" r="44" fill="#c9a45c" opacity="0.18" filter="url(#blur)"/>')
for i, yy in enumerate(range(ttop+24, tbot-10, 22)):
    s.append(f'<line x1="{tx+28}" y1="{yy}" x2="{tx+(46 if i%2==0 else 38)}" y2="{yy}" stroke="#c9a45c" stroke-opacity="0.5" stroke-width="2"/>')
# marca da meta (linha tracejada baixa)
s.append(f'<line x1="{tx-60}" y1="300" x2="{tx+60}" y2="300" stroke="#efe6d6" stroke-opacity="0.35" stroke-dasharray="4 5"/>')

s.append('<rect x="{}" y="{}" width="{}" height="{}" fill="#0a0a0a" opacity="0"/>'.format(0,0,0,0))
# chão e reflexo
s.append(f'<rect x="0" y="{HZ}" width="{W}" height="2" fill="#c9a45c" opacity="0.35"/>')
s.append(f'<rect x="0" y="{HZ+2}" width="{W}" height="90" fill="url(#water)"/>')
for _ in range(40):
    x0 = random.uniform(0, W); y0 = random.uniform(HZ + 8, HZ + 80)
    s.append(f'<rect x="{x0:.0f}" y="{y0:.0f}" width="{random.uniform(8,40):.0f}" height="1.5" fill="#e3c27e" opacity="{random.uniform(.05,.25):.2f}"/>')
s.append(f'<rect x="0" y="{HZ-30}" width="{W}" height="{H-HZ+30}" fill="url(#fade)" opacity="0.55"/>')
s.append(f'<rect x="0" y="{HZ+90}" width="{W}" height="{H-HZ-90}" fill="#0a0a0a"/>')
s.append(f'<rect x="0" y="{HZ+40}" width="{W}" height="52" fill="url(#fade)"/>')
s.append('</svg>')
open("bg.svg", "w").write("\n".join(s))
print("bg.svg ok")
