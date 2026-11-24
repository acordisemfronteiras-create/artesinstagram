"""Fundo Stories notícia: folhas de uma proposta (PEC) à esquerda e régua de câmbio à direita,
com o marcador dourado descendo de R$ 6,00 até perto de R$ 5,80 (queda de 2% no dia)."""
import random
random.seed(2411)
W, H = 1080, 1920
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0f131b"/><stop offset="0.3" stop-color="#161b24"/>
 <stop offset="0.45" stop-color="#13110e"/><stop offset="0.52" stop-color="#0a0a0a"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="glow" cx="0.72" cy="0.40" r="0.38">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.20"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="paper" x1="0" y1="0" x2="1" y2="1">
 <stop offset="0" stop-color="#2a2722"/><stop offset="1" stop-color="#16150f"/></linearGradient>
<linearGradient id="trail" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0"/><stop offset="1" stop-color="#e9cf8f" stop-opacity="0.9"/></linearGradient>
<filter id="gl"><feGaussianBlur stdDeviation="12"/></filter>
<filter id="sh"><feGaussianBlur stdDeviation="10"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/><rect width="100%" height="100%" fill="url(#glow)"/>''')
for _ in range(50):
    x, y = random.uniform(0, W), random.uniform(60, 400)
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="1" fill="#d8d2c4" opacity="{random.uniform(0.1,0.35):.2f}"/>')

# --- folhas da proposta (esquerda), levemente giradas
def sheet(x, y, rot, op, lines=True, seal=False):
    g = [f'<g transform="translate({x},{y}) rotate({rot})" opacity="{op}">',
         '<rect x="8" y="14" width="330" height="430" rx="6" fill="#000" opacity="0.5" filter="url(#sh)"/>',
         '<rect width="330" height="430" rx="6" fill="url(#paper)" stroke="#4a4234" stroke-width="1.5"/>']
    if lines:
        g.append('<rect x="34" y="40" width="150" height="10" rx="3" fill="#c9a45c" opacity="0.75"/>')
        g.append('<rect x="34" y="62" width="96" height="6" rx="3" fill="#8f8a82" opacity="0.5"/>')
        yy = 104
        for i in range(11):
            w = random.choice([262, 250, 238, 262, 200, 255]) if i % 4 != 3 else 140
            g.append(f'<rect x="34" y="{yy}" width="{w}" height="5" rx="2.5" fill="#a9a39a" opacity="0.28"/>')
            yy += 24
    if seal:
        g.append('<circle cx="262" cy="372" r="34" fill="none" stroke="#c9a45c" stroke-width="2" opacity="0.8"/>')
        g.append('<circle cx="262" cy="372" r="25" fill="none" stroke="#c9a45c" stroke-width="1" opacity="0.6"/>')
        g.append('<text x="262" y="379" text-anchor="middle" font-family="Inter, sans-serif" font-size="17" font-weight="600" letter-spacing="2" fill="#e2c47f">PEC</text>')
    g.append('</g>')
    return "".join(g)
s.append(sheet(70, 415, -9, 0.45, lines=False))
s.append(sheet(95, 400, -4, 0.7))
s.append(sheet(125, 385, 2, 1.0, seal=True))

# --- régua de câmbio (direita)
RX = 760
TOP, BOT = 400, 815           # 6,00 em TOP; 5,78 em BOT
def ypos(v): return TOP + (6.00 - v) / 0.22 * (BOT - TOP)
s.append(f'<line x1="{RX}" y1="{TOP-30}" x2="{RX}" y2="{BOT+10}" stroke="#3a362e" stroke-width="2"/>')
v = 6.00
while v >= 5.779:
    y = ypos(v)
    major = abs((v * 100) % 5) < 0.01 or abs((v*100) % 5 - 5) < 0.01
    L = 34 if major else 16
    s.append(f'<line x1="{RX}" y1="{y:.1f}" x2="{RX+L}" y2="{y:.1f}" stroke="#5a5244" stroke-width="{2 if major else 1.2}"/>')
    v = round(v - 0.01, 2)
for lab in (6.00, 5.90, 5.80):
    y = ypos(lab)
    col = "#c9a45c" if lab == 6.00 else "#8f8a82"
    s.append(f'<text x="{RX+50}" y="{y+10:.1f}" font-family="Inter, sans-serif" font-size="28" letter-spacing="3" fill="{col}">R$ ' + f'{lab:.2f}'.replace(".", ",") + '</text>')
# linha tracejada no R$ 6
y6 = ypos(6.00)
s.append(f'<line x1="430" y1="{y6}" x2="{RX-10}" y2="{y6}" stroke="#c9a45c" stroke-width="2" stroke-dasharray="12 10" opacity="0.55"/>')
# rastro e marcador perto de 5,80
ym = ypos(5.805)
s.append(f'<rect x="{RX-9}" y="{y6}" width="18" height="{ym-y6:.1f}" rx="9" fill="url(#trail)" opacity="0.55"/>')
s.append(f'<circle cx="{RX}" cy="{y6}" r="10" fill="none" stroke="#c9a45c" stroke-width="2" opacity="0.6"/>')
s.append(f'<circle cx="{RX}" cy="{ym:.1f}" r="34" fill="#c9a45c" opacity="0.35" filter="url(#gl)"/>')
s.append(f'<circle cx="{RX}" cy="{ym:.1f}" r="15" fill="#f1dfae"/>')
# seta de queda curva entre folhas e régua
s.append(f'<path d="M 560 {y6+40} C 640 {y6+90}, 680 {ym-120}, {RX-40} {ym-20}" fill="none" stroke="#c9a45c" stroke-width="3" opacity="0.75" stroke-linecap="round"/>')
s.append(f'<path d="M {RX-62} {ym-40} L {RX-36} {ym-17} L {RX-70} {ym-8}" fill="none" stroke="#c9a45c" stroke-width="3" opacity="0.75" stroke-linecap="round" stroke-linejoin="round"/>')
s.append(f'<text x="{RX-120}" y="{(y6+ym)/2+8:.0f}" font-family="Inter, sans-serif" font-size="30" font-weight="600" letter-spacing="2" fill="#e2c47f" text-anchor="end">−2%</text>')
# chão
s.append('<line x1="70" y1="858" x2="1010" y2="858" stroke="#2a2824" stroke-width="1.5"/>')
s.append('<rect y="858" width="1080" height="1062" fill="#0a0a0a"/>')
s.append('</svg>')
open(__file__.replace("bg_regua_queda.py", "bg.svg"), "w").write("\n".join(s))
