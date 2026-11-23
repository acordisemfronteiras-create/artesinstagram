"""Fundo Focus 23/11: quatro mostradores (velocímetros) num painel de instrumentos,
um para cada projeção do boletim (IPCA, PIB, câmbio, Selic)."""
import math, random
random.seed(2311)
W, H = 1080, 1350
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#10151e"/><stop offset="0.2" stop-color="#19202b"/>
 <stop offset="0.30" stop-color="#262019"/><stop offset="0.34" stop-color="#0f0e0d"/>
 <stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="dial" cx="0.5" cy="0.5" r="0.5">
 <stop offset="0" stop-color="#1c2532"/><stop offset="0.85" stop-color="#121821"/><stop offset="1" stop-color="#0b0e13"/></radialGradient>
<radialGradient id="glow" cx="0.5" cy="0.28" r="0.55">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.12"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.3"/><stop offset="0.12" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.30" stop-color="#0a0a0a" stop-opacity="0.05"/><stop offset="0.37" stop-color="#0a0a0a" stop-opacity="0.85"/>
 <stop offset="0.41" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.28" r="0.8">
 <stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
<filter id="gl"><feGaussianBlur stdDeviation="4"/></filter>
</defs>
<rect width="100%" height="100%" fill="url(#sky)"/><rect width="100%" height="100%" fill="url(#glow)"/>''')
# painel de instrumentos (placa)
s.append('<rect x="40" y="150" width="1000" height="260" rx="22" fill="#0d1016" stroke="#2a2824" stroke-width="2"/>')
s.append('<rect x="52" y="162" width="976" height="236" rx="16" fill="none" stroke="#c9a45c" stroke-opacity="0.12"/>')
# parafusos
for (x, y) in [(64, 174), (1016, 174), (64, 386), (1016, 386)]:
    s.append(f'<circle cx="{x}" cy="{y}" r="5" fill="#1a1d22" stroke="#33363c"/>')
# 4 mostradores: ângulo da agulha (graus, 180=esq, 0=dir) e se subiu
dials = [(330, True), (210, False), (320, True), (300, True)]  # leitura simbólica: sobe/cai
R = 92
for i, (ang, up) in enumerate(dials):
    cx = 160 + i * 253; cy = 300
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{R+14}" fill="#0a0c10" stroke="#2a313c" stroke-width="2"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#dial)"/>')
    # arco de escala (semicírculo superior, 200° a 340°)
    a0, a1 = 200, 340
    for k in range(0, 29):
        a = math.radians(a0 + (a1 - a0) * k / 28)
        r1 = R - 10; r2 = R - (22 if k % 7 == 0 else 15)
        x1 = cx + r1 * math.cos(a); y1 = cy + r1 * math.sin(a)
        x2 = cx + r2 * math.cos(a); y2 = cy + r2 * math.sin(a)
        op = 0.85 if k % 7 == 0 else 0.4
        s.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#c9a45c" stroke-opacity="{op}" stroke-width="{2 if k%7==0 else 1.2}"/>')
    # faixa dourada no final da escala
    p = []
    for k in range(0, 21):
        a = math.radians(305 + 35 * k / 20)
        p.append(f"{cx + (R-6)*math.cos(a):.1f},{cy + (R-6)*math.sin(a):.1f}")
    s.append(f'<polyline points="{" ".join(p)}" fill="none" stroke="#c9a45c" stroke-opacity="0.35" stroke-width="4"/>')
    # rótulos simbólicos (barrinhas)
    s.append(f'<rect x="{cx-22}" y="{cy+22}" width="44" height="5" fill="#c9a45c" fill-opacity="0.6"/>')
    s.append(f'<rect x="{cx-14}" y="{cy+34}" width="28" height="3" fill="#8f8a82" fill-opacity="0.5"/>')
    # agulha
    a = math.radians(ang)
    nx = cx + (R - 24) * math.cos(a); ny = cy + (R - 24) * math.sin(a)
    col = "#e2c27e" if up else "#8f8a82"
    s.append(f'<line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="{col}" stroke-width="8" stroke-opacity="0.25" filter="url(#gl)"/>')
    s.append(f'<line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="{col}" stroke-width="3.2" stroke-linecap="round"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="#1a1d22" stroke="{col}" stroke-width="2"/>')
    # indicador de seta
    tri = f"{cx},{cy+52} {cx-7},{cy+64} {cx+7},{cy+64}" if up else f"{cx},{cy+64} {cx-7},{cy+52} {cx+7},{cy+52}"
    s.append(f'<polygon points="{tri}" fill="{col}" opacity="0.8" transform="translate(0,6)"/>')
    # brilho no vidro
    s.append(f'<path d="M{cx-R+18},{cy-30} A{R-10},{R-10} 0 0 1 {cx+20},{cy-R+12}" fill="none" stroke="#ffffff" stroke-opacity="0.06" stroke-width="10"/>')
# linha de luz sob o painel
s.append('<rect x="80" y="412" width="920" height="5" fill="#c9a45c" fill-opacity="0.12" filter="url(#gl)"/>')
s.append('<rect width="100%" height="100%" fill="url(#fade)"/><rect width="100%" height="100%" fill="url(#vign)"/></svg>')
open("bg.svg", "w").write("\n".join(s)); print("ok")
