"""Fundo: globo pontilhado com rotas de exportação do Brasil para os EUA e o Golfo Pérsico."""
import math, random, sys
from pathlib import Path

random.seed(18)
W, H = 1080, 1350
CX, CY, R = 540, 370, 335
LON0, LAT0 = -24.0, -10.0

def proj(lon, lat, r=R):
    l, p = math.radians(lon - LON0), math.radians(lat)
    p0 = math.radians(LAT0)
    cosc = math.sin(p0) * math.sin(p) + math.cos(p0) * math.cos(p) * math.cos(l)
    x = r * math.cos(p) * math.sin(l)
    y = r * (math.cos(p0) * math.sin(p) - math.sin(p0) * math.cos(p) * math.cos(l))
    return CX + x, CY - y, cosc

LAND = {
 "sam": [(-80,10),(-75,11),(-62,11),(-52,5),(-50,0),(-44,-2),(-35,-5),(-35,-9),(-39,-15),(-41,-22),(-48,-26),(-53,-34),(-58,-38),(-65,-41),(-68,-50),(-70,-55),(-74,-50),(-73,-40),(-71,-30),(-70,-18),(-76,-14),(-81,-6),(-80,-1),(-78,2),(-77,7)],
 "nam": [(-168,66),(-160,70),(-140,70),(-120,72),(-95,72),(-80,68),(-62,60),(-55,52),(-66,45),(-70,42),(-76,38),(-76,35),(-81,31),(-80,25),(-82,27),(-84,30),(-90,30),(-97,27),(-97,22),(-92,18),(-87,21),(-88,16),(-83,10),(-79,9),(-85,11),(-92,14),(-105,20),(-110,24),(-112,30),(-117,33),(-121,36),(-124,40),(-124,46),(-128,51),(-135,57),(-150,60),(-160,58),(-165,62)],
 "grl": [(-55,60),(-45,60),(-20,70),(-20,80),(-60,82),(-72,78),(-55,68)],
 "afr": [(-17,21),(-17,15),(-15,11),(-8,5),(-2,5),(8,4),(9,0),(13,-5),(12,-17),(15,-27),(18,-34),(25,-34),(32,-28),(36,-20),(40,-15),(40,-10),(39,-4),(42,0),(51,11),(43,12),(39,17),(32,30),(25,32),(10,37),(-2,35),(-6,36),(-10,30),(-13,27)],
 "eur": [(-10,36),(-9,43),(-2,44),(-5,48),(2,51),(8,54),(9,57),(5,62),(15,69),(28,71),(40,67),(60,68),(60,45),(48,42),(40,41),(28,41),(24,38),(20,40),(13,45),(16,38),(10,44),(5,43),(-1,37)],
 "uk":  [(-6,50),(2,51),(0,53),(-3,56),(-5,58),(-6,55)],
 "ara": [(35,30),(48,30),(50,26),(52,24),(56,26),(60,22),(55,17),(45,13),(43,13),(39,20),(35,28)],
 "asi": [(60,45),(60,68),(80,73),(100,77),(140,72),(180,68),(180,60),(140,55),(130,42),(122,30),(120,22),(108,18),(105,10),(100,13),(98,8),(92,22),(88,22),(80,15),(77,8),(72,20),(66,25),(57,25),(48,30),(48,42)],
}

def inside(pt, poly):
    x, y = pt; c = False; n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % n]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            c = not c
    return c

s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
s.append('''<defs>
 <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#0e141d"/><stop offset="0.35" stop-color="#121a24"/>
  <stop offset="0.5" stop-color="#0c0d0f"/><stop offset="1" stop-color="#0a0a0a"/></linearGradient>
 <radialGradient id="sphere" cx="0.42" cy="0.32" r="0.75">
  <stop offset="0" stop-color="#1d2836"/><stop offset="0.6" stop-color="#111821"/><stop offset="1" stop-color="#07090c"/></radialGradient>
 <radialGradient id="halo" cx="0.5" cy="0.5" r="0.5">
  <stop offset="0.80" stop-color="#c9a45c" stop-opacity="0"/><stop offset="0.86" stop-color="#c9a45c" stop-opacity="0.16"/>
  <stop offset="0.93" stop-color="#5d7290" stop-opacity="0.08"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
 <radialGradient id="dot" cx="0.5" cy="0.5" r="0.5">
  <stop offset="0" stop-color="#ffd98f" stop-opacity="1"/><stop offset="0.35" stop-color="#e2b766" stop-opacity="0.55"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></radialGradient>
 <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5"/></filter>
 <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="4"/>
  <feColorMatrix values="0 0 0 0 0.5  0 0 0 0 0.5  0 0 0 0 0.5  0 0 0 0.05 0"/></filter>
 <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#0a0a0a" stop-opacity="0.8"/><stop offset="0.06" stop-color="#0a0a0a" stop-opacity="0.45"/><stop offset="0.13" stop-color="#0a0a0a" stop-opacity="0"/>
  <stop offset="0.30" stop-color="#0a0a0a" stop-opacity="0"/><stop offset="0.35" stop-color="#0a0a0a" stop-opacity="0.5"/>
  <stop offset="0.41" stop-color="#0a0a0a" stop-opacity="0.97"/><stop offset="1" stop-color="#0a0a0a" stop-opacity="1"/></linearGradient>
 <radialGradient id="vign" cx="0.5" cy="0.3" r="0.8">
  <stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
 <clipPath id="disc"><circle cx="CXV" cy="CYV" r="RV"/></clipPath>
</defs>'''.replace('CXV', str(CX)).replace('CYV', str(CY)).replace('RV', str(R)))
s.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
for _ in range(120):
    x, y = random.uniform(0, W), random.uniform(0, 560)
    if math.hypot(x - CX, y - CY) < R + 20:
        continue
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{random.uniform(0.5,1.5):.2f}" fill="#d9d2c4" fill-opacity="{random.uniform(0.15,0.55):.2f}"/>')

# esfera e halo
s.append(f'<circle cx="{CX}" cy="{CY}" r="{R*1.16:.0f}" fill="url(#halo)"/>')
s.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="url(#sphere)"/>')

# grade de latitude/longitude
g = ['<g clip-path="url(#disc)" fill="none" stroke="#7c8ba0" stroke-width="1">']
def polyline(pts, op):
    segs, cur = [], []
    for lon, lat in pts:
        x, y, c = proj(lon, lat)
        if c > 0: cur.append(f"{x:.1f},{y:.1f}")
        elif cur: segs.append(cur); cur = []
    if cur: segs.append(cur)
    for sg in segs:
        if len(sg) > 1:
            g.append(f'<polyline points="{" ".join(sg)}" stroke-opacity="{op}"/>')
for lat in range(-75, 90, 15):
    polyline([(lon, lat) for lon in range(-180, 181, 3)], 0.12 if lat else 0.22)
for lon in range(-180, 180, 15):
    polyline([(lon, lat) for lat in range(-90, 91, 3)], 0.12)
g.append('</g>')
s += g

# continentes em pontos
step = 1.9
lat = -60.0
while lat <= 80:
    lon = -180.0
    while lon < 180:
        for name, poly in LAND.items():
            if inside((lon, lat), poly):
                x, y, c = proj(lon, lat)
                if c > 0.02:
                    br = name == "sam"
                    op = (0.30 + 0.55 * c) * (1.0 if br else 0.75)
                    col = "#d8b46c" if br else "#a7b0bc"
                    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{1.5 + 1.1*c:.2f}" fill="{col}" fill-opacity="{op:.2f}"/>')
                break
        lon += step
    lat += step

# borda iluminada da esfera
s.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="#c9a45c" stroke-opacity="0.35" stroke-width="1.5"/>')

# rotas (arcos de grande círculo elevados)
def slerp(a, b, t):
    def v(lon, lat):
        lo, la = math.radians(lon), math.radians(lat)
        return (math.cos(la)*math.cos(lo), math.cos(la)*math.sin(lo), math.sin(la))
    p, q = v(*a), v(*b)
    d = math.acos(sum(i*j for i, j in zip(p, q)))
    k1, k2 = math.sin((1-t)*d)/math.sin(d), math.sin(t*d)/math.sin(d)
    x, y, z = (k1*i + k2*j for i, j in zip(p, q))
    return math.degrees(math.atan2(y, x)), math.degrees(math.asin(z))

origin = (-49.0, -20.0)    # Sul/Sudeste do Brasil
dests = [(-82.0, 33.0), (51.5, 25.5)]   # costa leste dos EUA, Golfo Pérsico
for dest, lift in ((dests[0], 0.13), (dests[1], 0.20)):
    pts = []
    for i in range(61):
        t = i / 60
        lon, lat = slerp(origin, dest, t)
        h = 1 + lift * math.sin(math.pi * t)
        x, y, c = proj(lon, lat, R * h)
        pts.append(f"{x:.1f},{y:.1f}")
    d = " ".join(pts)
    s.append(f'<polyline points="{d}" fill="none" stroke="#c9a45c" stroke-width="7" stroke-opacity="0.22" filter="url(#glow)"/>')
    s.append(f'<polyline points="{d}" fill="none" stroke="#e3be76" stroke-width="2.2" stroke-opacity="0.9" stroke-dasharray="10 7" stroke-linecap="round"/>')
    x, y, _ = proj(*dest)
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="22" fill="url(#dot)"/>')
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="#ffe2a8"/>')
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="none" stroke="#e3be76" stroke-opacity="0.6"/>')
x, y, _ = proj(*origin)
s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="34" fill="url(#dot)"/>')
s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="#fff0cc"/>')
s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="15" fill="none" stroke="#e3be76" stroke-opacity="0.7"/>')

s.append(f'<rect width="{W}" height="{H}" fill="url(#fade)"/>')
s.append(f'<rect width="{W}" height="{H}" fill="url(#vign)"/>')
s.append(f'<rect width="{W}" height="{H}" filter="url(#grain)"/>')
s.append('</svg>')
Path(sys.argv[1] if len(sys.argv) > 1 else "bg.svg").write_text("\n".join(s))
print("ok", proj(*origin)[:2], [proj(*d)[:2] for d in dests])
