"""Fundo: mapa-múndi pontilhado centrado no Pacífico, à noite. Rota dourada e firme dos EUA
às Filipinas; rota tracejada e apagada do Brasil às Filipinas. Tema: Trump diz que as
Filipinas vão comprar 100% do agro dos EUA, citando o Brasil."""
import math, random
from global_land_mask import globe
random.seed(2111)
W, H = 1080, 1350
LON0, LON1 = 96.0, 332.0
LAT0, LAT1 = 52.0, -32.0
VY = 0.82  # compressão vertical estilizada
SC = W / (LON1 - LON0)
Y0 = 118
def xy(lat, lon):
    L = lon if lon >= LON0 else lon + 360
    return (L - LON0) * SC, Y0 + (LAT0 - lat) * SC * VY

s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0e141e"/><stop offset="0.25" stop-color="#121a25"/>
 <stop offset="0.36" stop-color="#0d1015"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
<radialGradient id="glowPH" cx="0.5" cy="0.5" r="0.5">
 <stop offset="0" stop-color="#e8c47a" stop-opacity="0.85"/><stop offset="0.3" stop-color="#c9a45c" stop-opacity="0.28"/>
 <stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<radialGradient id="glowSoft" cx="0.5" cy="0.5" r="0.5">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.22"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
<linearGradient id="arcUS" x1="1" y1="0" x2="0" y2="0">
 <stop offset="0" stop-color="#c9a45c" stop-opacity="0.35"/><stop offset="0.5" stop-color="#e3c07a" stop-opacity="0.95"/>
 <stop offset="1" stop-color="#f0d394" stop-opacity="1"/></linearGradient>
<filter id="blur" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="5"/></filter>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.55"/><stop offset="0.10" stop-color="#0a0a0a" stop-opacity="0"/>
 <stop offset="0.27" stop-color="#0a0a0a" stop-opacity="0.0"/><stop offset="0.35" stop-color="#0a0a0a" stop-opacity="0.7"/>
 <stop offset="0.41" stop-color="#0a0a0a" stop-opacity="1"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
<radialGradient id="vign" cx="0.5" cy="0.25" r="0.85">
 <stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
</defs>''')
s.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')

# gratícula sutil
for lat in range(-30, 61, 15):
    _, y = xy(lat, 120)
    op = 0.10 if lat == 0 else 0.05
    s.append(f'<line x1="0" y1="{y:.1f}" x2="{W}" y2="{y:.1f}" stroke="#8fa3bd" stroke-opacity="{op}" stroke-width="1"/>')
for lon in range(100, 330, 20):
    x, _ = xy(0, lon if lon <= 180 else lon - 360)
    s.append(f'<line x1="{x:.1f}" y1="0" x2="{x:.1f}" y2="520" stroke="#8fa3bd" stroke-opacity="0.04" stroke-width="1"/>')

# mapa pontilhado
STEP = 1.55
def region(lat, lon):
    if 4 <= lat <= 21 and 116 <= lon <= 128: return "ph"
    if 25 <= lat <= 49 and -125 <= lon <= -67: return "us"
    if -34 <= lat <= 5.5 and -74 <= lon <= -34:
        # aproxima o território brasileiro
        if lon > -60 or (lat > -12 and lon > -70): return "br"
    return None
lat = LAT0
while lat >= LAT1 - 2:
    L = LON0
    while L <= LON1:
        lon = L if L <= 180 else L - 360
        if globe.is_land(lat, lon):
            x, y = xy(lat, lon)
            r = region(lat, lon)
            if r == "ph":
                s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="#e8c47a" fill-opacity="0.95"/>')
            elif r == "us":
                s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.1" fill="#d8cdb8" fill-opacity="0.55"/>')
            elif r == "br":
                s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.1" fill="#9a8a6a" fill-opacity="0.45"/>')
            else:
                op = 0.20 + random.random() * 0.08
                s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.9" fill="#7f90a8" fill-opacity="{op:.2f}"/>')
        L += STEP
    lat -= STEP / VY

PH = xy(14.5, 121.0); US = xy(39.0, -98.0); BR = xy(-14.0, -50.0)

# brilho dos pontos
s.append(f'<circle cx="{PH[0]:.1f}" cy="{PH[1]:.1f}" r="90" fill="url(#glowPH)"/>')
s.append(f'<circle cx="{US[0]:.1f}" cy="{US[1]:.1f}" r="70" fill="url(#glowSoft)"/>')

def qpath(a, b, lift):
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2 - lift
    return f'M{a[0]:.1f},{a[1]:.1f} Q{mx:.1f},{my:.1f} {b[0]:.1f},{b[1]:.1f}'

# rota Brasil -> Filipinas: tracejada, apagada, interrompida no meio
br_path = qpath(BR, PH, -70)  # curva para baixo
s.append(f'<path d="{br_path}" fill="none" stroke="#8a7a5c" stroke-opacity="0.55" stroke-width="2" stroke-dasharray="3 9" stroke-linecap="round"/>')
# rota EUA -> Filipinas: firme e luminosa
us_path = qpath(US, PH, 70)
s.append(f'<path d="{us_path}" fill="none" stroke="#c9a45c" stroke-opacity="0.45" stroke-width="9" filter="url(#blur)"/>')
s.append(f'<path d="{us_path}" fill="none" stroke="url(#arcUS)" stroke-width="2.6" stroke-linecap="round"/>')
# pequenas setas ao longo da rota dos EUA
def qpt(a, b, lift, t):
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2 - lift
    x = (1-t)**2*a[0] + 2*(1-t)*t*mx + t*t*b[0]
    y = (1-t)**2*a[1] + 2*(1-t)*t*my + t*t*b[1]
    return x, y
for t in (0.3, 0.55, 0.8):
    p1 = qpt(US, PH, 70, t); p2 = qpt(US, PH, 70, t + 0.01)
    ang = math.degrees(math.atan2(p2[1]-p1[1], p2[0]-p1[0]))
    s.append(f'<g transform="translate({p1[0]:.1f},{p1[1]:.1f}) rotate({ang:.1f})"><path d="M-7,-5 L3,0 L-7,5" fill="none" stroke="#f0d394" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g>')

# marcos dos pontos
for (x, y), r, col in ((PH, 7, "#f0d394"), (US, 5, "#e8dcc4"), (BR, 5, "#a8966f")):
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r+9}" fill="none" stroke="{col}" stroke-opacity="0.35" stroke-width="1.2"/>')
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}"/>')
# "x" sutil no meio da rota do Brasil
mx, my = qpt(BR, PH, -70, 0.5)
s.append(f'<g transform="translate({mx:.1f},{my:.1f})" stroke="#a8966f" stroke-opacity="0.8" stroke-width="2" stroke-linecap="round"><line x1="-7" y1="-7" x2="7" y2="7"/><line x1="7" y1="-7" x2="-7" y2="7"/></g>')

# rótulos
def label(x, y, txt, col, anchor="start"):
    s.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="Inter, Helvetica, Arial, sans-serif" font-size="15" letter-spacing="4" fill="{col}" text-anchor="{anchor}">{txt}</text>')
label(PH[0] + 22, PH[1] + 34, "FILIPINAS", "#e8c47a")
label(US[0] + 18, US[1] + 30, "EUA", "#e8dcc4")
label(BR[0] - 20, BR[1] + 5, "BRASIL", "#b8a67f", "end")

s.append(f'<rect width="{W}" height="{H}" fill="url(#fade)"/>')
s.append(f'<rect width="{W}" height="{H}" fill="url(#vign)"/>')
s.append('</svg>')
open("bg.svg", "w").write("\n".join(s))
print("ok", PH, US, BR)
