"""Fundo: calendário de mesa da semana de 16 a 20/11 (agenda econômica)."""
import random
random.seed(15)
W, H = 1080, 1350
s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#11161e"/><stop offset="0.25" stop-color="#171d27"/>
 <stop offset="0.36" stop-color="#1d1a16"/><stop offset="0.45" stop-color="#0d0d0d"/>
 <stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="glow" cx="0.5" cy="0.2" r="0.55">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.16"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="board" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#1c1f25"/><stop offset="1" stop-color="#121418"/></linearGradient>
<linearGradient id="card" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#22262d"/><stop offset="1" stop-color="#171a1f"/></linearGradient>
<linearGradient id="cardHi" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#2e2819"/><stop offset="1" stop-color="#1a1710"/></linearGradient>
<linearGradient id="desk" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#2a2118"/><stop offset="1" stop-color="#0f0d0b"/></linearGradient>
<pattern id="hatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
 <line x1="0" y1="0" x2="0" y2="10" stroke="#3a3a3a" stroke-width="2"/></pattern>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.35"/><stop offset="0.10" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.335" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.375" stop-color="#0a0a0a" stop-opacity="0.75"/>
 <stop offset="0.43" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.3" r="0.8">
 <stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#000" flood-opacity="0.6"/></filter>
</defs>''')
s.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
s.append(f'<rect width="{W}" height="{H}" fill="url(#glow)"/>')
# faint wall grid
for x in range(0, W, 54):
    s.append(f'<line x1="{x}" y1="0" x2="{x}" y2="470" stroke="#ffffff" stroke-opacity="0.025"/>')
# desk surface
s.append('<path d="M0 452 L1080 452 L1080 560 L0 560 Z" fill="url(#desk)"/>')
s.append('<line x1="0" y1="452" x2="1080" y2="452" stroke="#c9a45c" stroke-opacity="0.25"/>')
# board
bx, by, bw, bh = 96, 162, 888, 282
s.append(f'<g filter="url(#sh)"><rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="14" fill="url(#board)" stroke="#2f333a"/></g>')
# binding rings
for i in range(14):
    x = bx + 46 + i * 61
    s.append(f'<rect x="{x-4}" y="{by-14}" width="8" height="30" rx="4" fill="#8f7a4e"/>')
    s.append(f'<circle cx="{x}" cy="{by+22}" r="5" fill="#0b0c0e"/>')
# header
s.append(f'<text x="{W/2}" y="{by+62}" text-anchor="middle" font-family="Georgia,serif" font-size="22" letter-spacing="9" fill="#c9a45c" fill-opacity="0.85">NOVEMBRO · 2026</text>')
s.append(f'<line x1="{bx+40}" y1="{by+80}" x2="{bx+bw-40}" y2="{by+80}" stroke="#c9a45c" stroke-opacity="0.3"/>')
days = [("SEG", "16"), ("TER", "17"), ("QUA", "18"), ("QUI", "19"), ("SEX", "20")]
cw, gap = 152, 18
x0 = (W - (5 * cw + 4 * gap)) / 2
cy0, ch = by + 92, 170

def icon(i, cx, cy, col):
    if i == 0:  # prévia do PIB: barras + linha
        out = []
        for k, h in enumerate([18, 26, 22, 34]):
            out.append(f'<rect x="{cx-30+k*16}" y="{cy+18-h}" width="10" height="{h}" fill="{col}" fill-opacity="0.55"/>')
        out.append(f'<polyline points="{cx-28},{cy+2} {cx-12},{cy-6} {cx+4},{cy-2} {cx+22},{cy-18}" fill="none" stroke="{col}" stroke-width="2.5"/>')
        return ''.join(out)
    if i == 1:  # martelo de votação
        return (f'<g transform="rotate(-35 {cx} {cy})"><rect x="{cx-22}" y="{cy-16}" width="44" height="18" rx="4" fill="{col}"/>'
                f'<rect x="{cx-3}" y="{cy+2}" width="6" height="30" fill="{col}"/></g>'
                f'<rect x="{cx-26}" y="{cy+22}" width="40" height="6" rx="2" fill="{col}" fill-opacity="0.6"/>')
    if i == 2:  # ata: documento
        o = f'<rect x="{cx-20}" y="{cy-24}" width="40" height="50" rx="3" fill="none" stroke="{col}" stroke-width="2.5"/>'
        for k in range(5):
            o += f'<line x1="{cx-12}" y1="{cy-14+k*9}" x2="{cx+12 - (8 if k==4 else 0)}" y2="{cy-14+k*9}" stroke="{col}" stroke-width="2"/>'
        return o
    if i == 3:  # moedas
        o = ''
        for k in range(4):
            o += f'<ellipse cx="{cx}" cy="{cy+16-k*9}" rx="22" ry="7" fill="#1a1c20" stroke="{col}" stroke-width="2"/>'
        return o
    # feriado: estrela
    import math
    pts = []
    for k in range(10):
        r = 18 if k % 2 == 0 else 8
        a = -math.pi/2 + k * math.pi/5
        pts.append(f'{cx+r*math.cos(a):.1f},{cy+r*math.sin(a):.1f}')
    return f'<polygon points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="2"/>'

for i, (d, n) in enumerate(days):
    x = x0 + i * (cw + gap)
    hi = (i == 1)
    hol = (i == 4)
    fill = 'url(#cardHi)' if hi else 'url(#card)'
    stroke = '#c9a45c' if hi else '#30343b'
    s.append(f'<rect x="{x}" y="{cy0}" width="{cw}" height="{ch}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="{2 if hi else 1}"/>')
    if hol:
        s.append(f'<rect x="{x}" y="{cy0}" width="{cw}" height="{ch}" rx="8" fill="url(#hatch)" fill-opacity="0.6"/>')
    tc = '#c9a45c' if hi else ('#6b6760' if hol else '#a9a39a')
    nc = '#e2c27f' if hi else ('#5c5852' if hol else '#e6dccb')
    s.append(f'<text x="{x+cw/2}" y="{cy0+30}" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="15" letter-spacing="5" fill="{tc}">{d}</text>')
    s.append(f'<text x="{x+cw/2}" y="{cy0+88}" text-anchor="middle" font-family="Georgia,serif" font-size="58" fill="{nc}">{n}</text>')
    s.append(icon(i, x + cw/2, cy0 + 132, '#c9a45c' if hi else ('#5c5852' if hol else '#8d877d')))
# gold ring around 17
x = x0 + 1 * (cw + gap)
s.append(f'<ellipse cx="{x+cw/2}" cy="{cy0+70}" rx="54" ry="33" fill="none" stroke="#c9a45c" stroke-width="2.5" stroke-opacity="0.85" transform="rotate(-6 {x+cw/2} {cy0+70})"/>')
s.append(f'<rect width="{W}" height="{H}" fill="url(#fade)"/>')
s.append(f'<rect width="{W}" height="{H}" fill="url(#vign)"/>')
s.append('</svg>')
open('bg.svg', 'w').write('\n'.join(s))
print('ok')
