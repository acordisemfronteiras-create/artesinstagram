"""Fundo: painel de projeções (barras do PIB encolhendo, linha da inflação encostando no teto,
leque de incerteza) flutuando sobre uma fileira genérica de prédios de ministérios ao entardecer."""
import random, math
random.seed(2411)
W, H = 1080, 1350
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0e131b"/><stop offset="0.2" stop-color="#161b23"/>
 <stop offset="0.3" stop-color="#2c2518"/><stop offset="0.34" stop-color="#3a2e1a"/>
 <stop offset="0.38" stop-color="#0f0d0b"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="sun" cx="0.5" cy="0.31" r="0.42">
 <stop offset="0" stop-color="#e2bf78" stop-opacity="0.32"/><stop offset="0.5" stop-color="#c9a45c" stop-opacity="0.08"/>
 <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="panel" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0d1219" stop-opacity="0.88"/><stop offset="1" stop-color="#0a0d12" stop-opacity="0.72"/></linearGradient>
<linearGradient id="bar" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#e6c784"/><stop offset="1" stop-color="#8a6a32"/></linearGradient>
<linearGradient id="fan" x1="0" y1="0" x2="1" y2="0">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.05"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0.22"/></linearGradient>
<linearGradient id="bld" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#1d1a15"/><stop offset="1" stop-color="#0c0b0a"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.3"/><stop offset="0.09" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.29" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.345" stop-color="#0a0a0a" stop-opacity="0.85"/>
 <stop offset="0.37" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.22" r="0.75">
 <stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
<filter id="blur"><feGaussianBlur stdDeviation="3"/></filter>
<filter id="soft"><feGaussianBlur stdDeviation="1.2"/></filter>
<filter id="grain" x="0" y="0" width="100%" height="100%">
 <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="11"/>
 <feColorMatrix type="saturate" values="0"/>
 <feComponentTransfer><feFuncA type="table" tableValues="0 0.07"/></feComponentTransfer></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/>
<rect width="100%" height="100%" fill="url(#sun)"/>''')

# estrelas/poeira
for _ in range(70):
    x, y = random.uniform(40, 1040), random.uniform(120, 330)
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(0.5,1.4):.1f}" fill="#e6c784" fill-opacity="{random.uniform(0.06,0.25):.2f}"/>')

# Esplanada genérica: duas fileiras de blocos idênticos em perspectiva até um ponto de fuga
hz = 432
vpx = 540
s.append(f'<rect x="0" y="{hz}" width="1080" height="60" fill="#0c0b0a"/>')
def block(xc, h, w, shade):
    x = xc - w/2
    s.append(f'<rect x="{x:.1f}" y="{hz-h:.1f}" width="{w:.1f}" height="{h:.1f}" fill="url(#bld)" stroke="#2c271e" stroke-width="0.8"/>')
    # janelas: faixas horizontais
    nf = max(3, int(h/7))
    for k in range(1, nf):
        y = hz - h + k*h/nf
        op = 0.10 + 0.25*random.random() if random.random() < 0.55 else 0.04
        s.append(f'<line x1="{x+2:.1f}" y1="{y:.1f}" x2="{x+w-2:.1f}" y2="{y:.1f}" stroke="#c9a45c" stroke-opacity="{op*shade:.2f}" stroke-width="{max(0.6,h/90):.1f}"/>')
for side in (-1, 1):
    for i in range(9):
        t = i/9
        d = 470 - 410*(t**0.8)  # distância horizontal do centro
        xc = vpx + side*d
        h = 64 - 50*t
        w = 46 - 36*t
        block(xc, h, w, 1 - 0.5*t)
# cúpulas discretas ao fundo (genéricas) e eixo central
s.append(f'<path d="M{vpx-30} {hz} q 30 -20 60 0" fill="#15130f" stroke="#3a3226" stroke-width="1"/>')
s.append(f'<rect x="{vpx-4}" y="{hz-30}" width="3" height="30" fill="#1d1a15"/><rect x="{vpx+2}" y="{hz-30}" width="3" height="30" fill="#1d1a15"/>')
# reflexo da luz no gramado/espelho d'água
s.append(f'<ellipse cx="{vpx}" cy="{hz+16}" rx="300" ry="10" fill="#c9a45c" fill-opacity="0.10" filter="url(#blur)"/>')
for k in range(6):
    y = hz + 8 + k*7
    s.append(f'<line x1="{vpx-200+k*25}" y1="{y}" x2="{vpx+200-k*25}" y2="{y}" stroke="#c9a45c" stroke-opacity="{0.12-k*0.018:.3f}" stroke-width="1"/>')

# Painel de projeções flutuante
px, py, pw, ph = 170, 160, 740, 214
s.append(f'<rect x="{px-10}" y="{py-10}" width="{pw+20}" height="{ph+20}" rx="10" fill="none" stroke="#c9a45c" stroke-opacity="0.22" stroke-width="1.2"/>')
s.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="6" fill="url(#panel)" stroke="#2e2a22" stroke-width="1.5"/>')
# grade
for k in range(1, 6):
    y = py + k*ph/6
    s.append(f'<line x1="{px+20}" y1="{y:.1f}" x2="{px+pw-20}" y2="{y:.1f}" stroke="#8f8a82" stroke-opacity="0.12" stroke-width="1"/>')
for k in range(1, 8):
    x = px + k*pw/8
    s.append(f'<line x1="{x:.1f}" y1="{py+16}" x2="{x:.1f}" y2="{py+ph-16}" stroke="#8f8a82" stroke-opacity="0.06" stroke-width="1"/>')
base = py + ph - 30
s.append(f'<line x1="{px+24}" y1="{base}" x2="{px+pw-24}" y2="{base}" stroke="#8f8a82" stroke-opacity="0.45" stroke-width="1.2"/>')

# Barras do PIB (lado esquerdo): fantasma = projeção anterior, sólida = nova
sc = 60  # px por ponto percentual
bars = [(px+90, 2.0, 1.9), (px+190, 2.3, 1.8)]
for x, old, new in bars:
    s.append(f'<rect x="{x}" y="{base-old*sc:.1f}" width="56" height="{old*sc:.1f}" fill="none" stroke="#c9a45c" stroke-opacity="0.55" stroke-width="1.4" stroke-dasharray="5 4"/>')
    s.append(f'<rect x="{x+6}" y="{base-new*sc:.1f}" width="44" height="{new*sc:.1f}" fill="url(#bar)" fill-opacity="0.92"/>')
    # seta para baixo entre fantasma e sólida
    ya, yb = base-old*sc-2, base-new*sc-6
    s.append(f'<line x1="{x+68}" y1="{ya-6:.1f}" x2="{x+68}" y2="{yb+4:.1f}" stroke="#e6c784" stroke-width="1.6"/>')
    s.append(f'<polygon points="{x+63},{yb:.1f} {x+73},{yb:.1f} {x+68},{yb+8:.1f}" fill="#e6c784"/>')
s.append(f'<text x="{px+150}" y="{base+22}" font-family="Inter, sans-serif" font-size="13" letter-spacing="4" fill="#8f8a82" text-anchor="middle">PIB</text>')
# separador
s.append(f'<line x1="{px+320}" y1="{py+24}" x2="{px+320}" y2="{base}" stroke="#c9a45c" stroke-opacity="0.18" stroke-width="1"/>')

# Linha da inflação (lado direito) subindo até o teto, com leque de incerteza
x0, x1 = px+350, px+pw-40
isc = 42
def iy(v): return base - (v-2.0)*isc
teto = iy(4.5)
s.append(f'<line x1="{x0-6}" y1="{teto:.1f}" x2="{x1+10}" y2="{teto:.1f}" stroke="#d9b56a" stroke-opacity="0.8" stroke-width="1.4" stroke-dasharray="10 6"/>')
s.append(f'<text x="{x1+8}" y="{teto-9:.1f}" font-family="Inter, sans-serif" font-size="12" letter-spacing="3" fill="#c9a45c" fill-opacity="0.85" text-anchor="end">TETO</text>')
s.append(f'<line x1="{x0-6}" y1="{iy(3.0):.1f}" x2="{x1+10}" y2="{iy(3.0):.1f}" stroke="#8f8a82" stroke-opacity="0.3" stroke-width="1" stroke-dasharray="3 6"/>')
# trajetória anterior (fantasma) e nova
oldpts = [(x0, 4.6), (x0+90, 4.9), (x0+190, 4.3), (x0+300, 3.8)]
newpts = [(x0, 4.6), (x0+90, 5.0), (x0+190, 5.3), (x0+300, 4.5)]
def path(pts):
    return 'M' + ' L'.join(f'{x:.1f} {iy(v):.1f}' for x, v in pts)
# leque após o ponto atual
fx = x0+190
up = [(fx, 5.3), (x0+300, 5.6), (x1, 5.9)]
dn = [(fx, 5.3), (x0+300, 3.5), (x1, 3.0)]
fan = 'M' + ' L'.join(f'{x:.1f} {iy(v):.1f}' for x, v in up) + ' L' + ' L'.join(f'{x:.1f} {iy(v):.1f}' for x, v in reversed(dn)) + ' Z'
s.append(f'<path d="{fan}" fill="url(#fan)"/>')
up2 = [(fx, 5.3), (x0+300, 5.05), (x1, 5.2)]
dn2 = [(fx, 5.3), (x0+300, 4.0), (x1, 3.7)]
fan2 = 'M' + ' L'.join(f'{x:.1f} {iy(v):.1f}' for x, v in up2) + ' L' + ' L'.join(f'{x:.1f} {iy(v):.1f}' for x, v in reversed(dn2)) + ' Z'
s.append(f'<path d="{fan2}" fill="#c9a45c" fill-opacity="0.12"/>')
s.append(f'<path d="{path(oldpts)}" fill="none" stroke="#8f8a82" stroke-opacity="0.6" stroke-width="1.6" stroke-dasharray="5 5"/>')
s.append(f'<path d="{path(newpts)}" fill="none" stroke="#e6c784" stroke-width="5" stroke-opacity="0.25" filter="url(#soft)"/>')
s.append(f'<path d="{path(newpts)}" fill="none" stroke="#e6c784" stroke-width="2.4" stroke-linejoin="round"/>')
for x, v in newpts:
    s.append(f'<circle cx="{x:.1f}" cy="{iy(v):.1f}" r="4.5" fill="#0a0a0a" stroke="#e6c784" stroke-width="2"/>')
# ponto final no teto com halo
ex, ev = newpts[-1]
s.append(f'<circle cx="{ex:.1f}" cy="{iy(ev):.1f}" r="13" fill="#c9a45c" fill-opacity="0.25" filter="url(#blur)"/>')
s.append(f'<text x="{(x0+x1)/2:.0f}" y="{base+22}" font-family="Inter, sans-serif" font-size="13" letter-spacing="4" fill="#8f8a82" text-anchor="middle">IPCA</text>')
# ticks de ano discretos
for x in (x0, x0+90, x0+190, x0+300):
    s.append(f'<line x1="{x}" y1="{base}" x2="{x}" y2="{base+5}" stroke="#8f8a82" stroke-opacity="0.5"/>')

s.append('<rect width="100%" height="100%" fill="url(#fade)"/>')
s.append('<rect width="100%" height="100%" fill="url(#vign)"/>')
s.append('<rect width="100%" height="100%" filter="url(#grain)"/>')
s.append('</svg>')
open('bg.svg', 'w').write('\n'.join(s))
print('ok')
