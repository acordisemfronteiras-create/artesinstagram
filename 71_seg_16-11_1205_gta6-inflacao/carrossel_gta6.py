"""Carrossel 'GTA 6 x inflação' (7 slides, 1080x1350) no padrão @tiagoassessorxp.
Ilustrações originais em SVG (sem capas, logos ou marcas reais).
Uso: python3 carrossel_gta6.py  -> gera slide_1.png ... slide_7.png
"""
import asyncio, random, math, shutil, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
KIT = HERE.parent / "_kit_noticias"
GOLD, INK, MUTE, LINE = "#c9a45c", "#f1e8d8", "#8f8a82", "#2a2824"

# ---------- dados verificados ----------
IPCA = {2013:[.35,.57,.54,.92],2014:[.55,.69,.92,.67,.46,.40,.01,.25,.57,.42,.51,.78],
2015:[1.24,1.22,1.32,.71,.74,.79,.62,.22,.54,.82,1.01,.96],2016:[1.27,.90,.43,.61,.78,.35,.52,.44,.08,.26,.18,.30],
2017:[.38,.33,.25,.14,.31,-.23,.24,.19,.16,.42,.28,.44],2018:[.29,.32,.09,.22,.40,1.26,.33,-.09,.48,.45,-.21,.15],
2019:[.32,.43,.75,.57,.13,.01,.19,.11,-.04,.10,.51,1.15],2020:[.21,.25,.07,-.31,-.38,.26,.36,.24,.64,.86,.89,1.35],
2021:[.25,.86,.93,.31,.83,.53,.96,.87,1.16,1.25,.95,.73],2022:[.54,1.01,1.62,1.06,.47,.67,-.68,-.36,-.29,.59,.41,.62],
2023:[.53,.84,.71,.61,.23,-.08,.12,.23,.26,.24,.28,.56],2024:[.42,.83,.16,.38,.46,.21,.38,-.02,.44,.56,.39,.52],
2025:[.16,1.31,.56,.43,.26,.24,.26,-.11,.48,.09,.18,.33],2026:[.33,.70,.88,.67,.58,.16,.07,-.32,.82,.14]}
idx = [1.0]
for y in IPCA:
    for v in IPCA[y]:
        idx.append(idx[-1] * (1 + v / 100))
F = idx[-1]                      # 2,0684 -> +106,8%
V13, STD, ULT = 199.0, 449.90, 549.90
CORR = V13 * F                   # 411,60
HOJE = V13 / F                   # 96,21
def brl(x): return f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
def pct(x): return f"{x*100:.1f}".replace(".", ",") + "%"
print("IPCA acumulado", pct(F-1), "corrigido", brl(CORR), "hoje", brl(HOJE),
      "std", pct(STD/CORR-1), "ult", pct(ULT/CORR-1), "nominal", pct(STD/V13-1), "perda", pct(1-HOJE/V13))

# ---------- peças de ilustração ----------
def frame(inner, h=470):
    return f'<svg class="vis" viewBox="0 0 880 {h}" width="880" height="{h}" xmlns="http://www.w3.org/2000/svg">{inner}</svg>'

DEFS = f'''<defs>
<linearGradient id="gold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e2c27f"/><stop offset="1" stop-color="#9c7d3e"/></linearGradient>
<linearGradient id="grey" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a4740"/><stop offset="1" stop-color="#2b2925"/></linearGradient>
<linearGradient id="case" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1d2026"/><stop offset="1" stop-color="#121418"/></linearGradient>
<radialGradient id="halo" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{GOLD}" stop-opacity=".22"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></radialGradient>
<filter id="sh" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="16" stdDeviation="16" flood-color="#000" flood-opacity=".7"/></filter>
</defs>'''

def game_case(x, y, w, h, year, accent, dim=False):
    op = .55 if dim else 1
    random.seed(year)
    lines = ''.join(f'<line x1="{x+18}" y1="{y+40+i*14}" x2="{x+w-18}" y2="{y+40+i*14}" stroke="{accent}" stroke-opacity=".07"/>' for i in range(int((h-60)/14)))
    # padrão abstrato de losangos na capa
    shapes = ''
    for i in range(7):
        cx, cy, r = x + random.uniform(.2,.8)*w, y + random.uniform(.18,.55)*h, random.uniform(14, 40)
        shapes += f'<polygon points="{cx},{cy-r} {cx+r},{cy} {cx},{cy+r} {cx-r},{cy}" fill="none" stroke="{accent}" stroke-opacity=".35" stroke-width="1.5"/>'
    return f'''<g opacity="{op}" filter="url(#sh)">
<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="url(#case)" stroke="#3a3d44" stroke-width="2"/>
<rect x="{x}" y="{y}" width="{w}" height="26" rx="12" fill="{accent}" fill-opacity=".85"/>
<rect x="{x}" y="{y+14}" width="{w}" height="12" fill="{accent}" fill-opacity=".85"/>
{lines}{shapes}
<text x="{x+w/2}" y="{y+h*.80}" text-anchor="middle" font-family="Fraunces" font-size="{w*.30:.0f}" fill="{accent}">{year}</text>
<line x1="{x+30}" y1="{y+h*.86}" x2="{x+w-30}" y2="{y+h*.86}" stroke="{accent}" stroke-opacity=".5"/>
</g>'''

def price_tag(x, y, text, accent, rot):
    return f'''<g transform="rotate({rot} {x} {y})">
<line x1="{x}" y1="{y-40}" x2="{x}" y2="{y}" stroke="{accent}" stroke-width="1.5" stroke-opacity=".7"/>
<path d="M{x-70} {y} h140 l0 52 h-140 z" fill="#0f0f10" stroke="{accent}" stroke-width="2"/>
<circle cx="{x}" cy="{y+10}" r="4" fill="{accent}"/>
<text x="{x}" y="{y+41}" text-anchor="middle" font-family="Fraunces" font-size="26" fill="{accent}">{text}</text></g>'''

def vis_capa():
    s = DEFS + '<ellipse cx="560" cy="230" rx="330" ry="230" fill="url(#halo)"/>'
    s += game_case(150, 90, 230, 300, "2013", "#8f8a82", dim=True)
    s += game_case(470, 40, 270, 352, "2026", GOLD)
    s += f'<path d="M398 250 C430 230 440 220 456 210" fill="none" stroke="{GOLD}" stroke-width="2" stroke-dasharray="5 6"/>'
    s += f'<polygon points="456,210 444,208 450,220" fill="{GOLD}"/>'
    s += price_tag(265, 420, "R$ 199", "#a9a39a", -4)
    s += price_tag(605, 420, "R$ 449,90", GOLD, 3)
    # controle estilizado
    s += f'''<g transform="translate(790 330) rotate(-14)" opacity=".85"><path d="M-55 -20 h110 a35 35 0 0 1 30 50 l-14 22 a20 20 0 0 1 -32 -2 l-12 -16 h-46 l-12 16 a20 20 0 0 1 -32 2 l-14 -22 a35 35 0 0 1 30 -50z" fill="#16181c" stroke="#3a3d44" stroke-width="2"/>
<circle cx="-40" cy="5" r="7" fill="none" stroke="{GOLD}" stroke-width="2"/><circle cx="38" cy="0" r="4" fill="{GOLD}"/><circle cx="50" cy="10" r="4" fill="{GOLD}" fill-opacity=".6"/></g>'''
    return frame(s, 500)

def bars(items, h=470, maxv=None, base=420, bw=150):
    """items: (label, value, valuetext, style)"""
    maxv = maxv or max(v for _, v, _, _ in items)
    n = len(items); gap = (880 - n*bw) / (n+1)
    s = DEFS + f'<line x1="20" y1="{base}" x2="860" y2="{base}" stroke="#3a3833"/>'
    for i, (lab, v, vt, st) in enumerate(items):
        x = gap + i*(bw+gap); hh = (base-80) * v / maxv; y = base - hh
        fill = {"gold": "url(#gold)", "grey": "url(#grey)", "line": "none"}[st]
        stroke = f'stroke="{GOLD}" stroke-width="2" stroke-dasharray="8 6"' if st == "line" else ''
        s += f'<rect x="{x}" y="{y}" width="{bw}" height="{hh}" rx="4" fill="{fill}" {stroke}/>'
        col = GOLD if st != "grey" else "#d4cdc2"
        s += f'<text x="{x+bw/2}" y="{y-18}" text-anchor="middle" font-family="Fraunces" font-size="34" fill="{col}">{vt}</text>'
        for k, part in enumerate(lab.split("|")):
            s += f'<text x="{x+bw/2}" y="{base+34+k*24}" text-anchor="middle" font-family="Inter" font-size="19" fill="{MUTE}" letter-spacing="1">{part}</text>'
    return frame(s, h + 20)

def vis_nominal():
    return bars([("GTA V|set/2013", V13, "R$ 199", "grey"), ("GTA 6 Standard|nov/2026", STD, "R$ 449,90", "gold")], bw=180)

def vis_ipca():
    W0, W1, T, B = 70, 830, 60, 400
    n = len(idx) - 1
    pts = [(W0 + (W1-W0)*i/n, B - (B-T)*(v-1)/(F-1)) for i, v in enumerate(idx)]
    path = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    area = f"{W0},{B} " + path + f" {W1},{B}"
    s = DEFS + '''<linearGradient id="ar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c9a45c" stop-opacity=".30"/><stop offset="1" stop-color="#c9a45c" stop-opacity="0"/></linearGradient>'''
    for k in range(5):
        y = B - (B-T)*k/4
        s += f'<line x1="{W0}" y1="{y}" x2="{W1}" y2="{y}" stroke="#ffffff" stroke-opacity=".05"/>'
    s += f'<polygon points="{area}" fill="url(#ar)"/><polyline points="{path}" fill="none" stroke="{GOLD}" stroke-width="3.5" stroke-linejoin="round"/>'
    x0, y0 = pts[0]; x1, y1 = pts[-1]
    s += f'<circle cx="{x0}" cy="{y0}" r="7" fill="#d4cdc2"/><circle cx="{x1}" cy="{y1}" r="9" fill="{GOLD}"/><circle cx="{x1}" cy="{y1}" r="18" fill="{GOLD}" fill-opacity=".2"/>'
    s += f'<text x="{x0-6}" y="{y0-48}" font-family="Fraunces" font-size="32" fill="#d4cdc2">R$ 199</text>'
    s += f'<text x="{x1-14}" y="{y1-26}" text-anchor="end" font-family="Fraunces" font-size="40" fill="{GOLD}">{brl(CORR)}</text>'
    for i, yr in enumerate(range(2014, 2027, 2)):
        m = (yr - 2013) * 12 - 8
        x = W0 + (W1-W0)*m/n
        s += f'<text x="{x}" y="{B+34}" text-anchor="middle" font-family="Inter" font-size="18" fill="{MUTE}">{yr}</text>'
    return frame(s, 450)

def vis_comp():
    return bars([("GTA V corrigido|pelo IPCA", CORR, brl(CORR), "line"), ("GTA 6|Standard", STD, "R$ 449,90", "gold"),
                 ("GTA 6|Ultimate", ULT, "R$ 549,90", "grey")], bw=160)

def vis_nota():
    random.seed(3)
    x, y, w, h = 110, 90, 560, 280
    s = DEFS + f'<ellipse cx="440" cy="230" rx="380" ry="220" fill="url(#halo)"/>'
    clip = f'<clipPath id="cl"><rect x="{x}" y="{y}" width="{w*.55}" height="{h}"/></clipPath>'
    guil = ''.join(f'<ellipse cx="{x+150}" cy="{y+h/2}" rx="{40+i*9}" ry="{20+i*6}" fill="none" stroke="{GOLD}" stroke-opacity=".18"/>' for i in range(14))
    note = f'''<g clip-path="url(#cl)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#1b1a17" stroke="{GOLD}" stroke-width="2"/>{guil}
<rect x="{x+20}" y="{y+20}" width="{w-40}" height="{h-40}" rx="6" fill="none" stroke="{GOLD}" stroke-opacity=".35"/>
<text x="{x+44}" y="{y+h-52}" font-family="Fraunces" font-size="92" fill="{GOLD}">R$</text>
<text x="{x+44}" y="{y+70}" font-family="Inter" font-size="16" letter-spacing="6" fill="{GOLD}" fill-opacity=".7">DINHEIRO PARADO</text></g>'''
    s += clip + note
    # partículas se desfazendo
    for _ in range(900):
        t = random.random()
        px = x + w*.55 + t**.8 * (w*.75) + random.uniform(-12, 12)
        py = y + random.uniform(0, h) + random.uniform(-40, 40) * t - 30*t
        r = max(.6, 3.2*(1-t) * random.random() + .6)
        s += f'<rect x="{px:.1f}" y="{py:.1f}" width="{r:.1f}" height="{r:.1f}" fill="{GOLD}" fill-opacity="{max(.08, .9*(1-t)):.2f}"/>'
    return frame(s, 430)

def vis_gaveta():
    return bars([("R$ 199 em|2013", V13, "R$ 199", "grey"), ("o que compram|hoje", HOJE, "R$ 96,21", "gold")], bw=180)

def vis_patrimonio():
    def icon_casa(cx, cy):
        return (f'<path d="M{cx-60} {cy} L{cx} {cy-55} L{cx+60} {cy}" fill="none" stroke="{GOLD}" stroke-width="3"/>'
                f'<rect x="{cx-45}" y="{cy}" width="90" height="70" fill="none" stroke="{GOLD}" stroke-width="3"/>'
                f'<rect x="{cx-14}" y="{cy+28}" width="28" height="42" fill="none" stroke="{GOLD}" stroke-width="2"/>')
    def icon_predio(cx, cy):
        o = f'<rect x="{cx-40}" y="{cy-60}" width="80" height="130" fill="none" stroke="{GOLD}" stroke-width="3"/>'
        for r in range(5):
            for c in range(3):
                o += f'<rect x="{cx-28+c*22}" y="{cy-48+r*22}" width="12" height="12" fill="{GOLD}" fill-opacity="{.25 + .5*((r+c)%2)}"/>'
        return o
    def icon_silo(cx, cy):
        return (f'<path d="M{cx-35} {cy-30} Q{cx-35} {cy-70} {cx} {cy-70} Q{cx+35} {cy-70} {cx+35} {cy-30} V{cy+70} H{cx-35} Z" fill="none" stroke="{GOLD}" stroke-width="3"/>'
                + ''.join(f'<line x1="{cx-35}" y1="{cy-20+k*20}" x2="{cx+35}" y2="{cy-20+k*20}" stroke="{GOLD}" stroke-opacity=".4"/>' for k in range(5))
                + f'<rect x="{cx+45}" y="{cy-10}" width="40" height="80" fill="none" stroke="{GOLD}" stroke-width="2" stroke-opacity=".6"/>')
    s = DEFS + f'<ellipse cx="440" cy="200" rx="400" ry="200" fill="url(#halo)"/>'
    labels = ["FAMÍLIA", "EMPRESA", "AGRO"]
    for i, (fn, lab) in enumerate(zip([icon_casa, icon_predio, icon_silo], labels)):
        cx = 150 + i*290
        s += f'<circle cx="{cx}" cy="185" r="125" fill="#121212" stroke="#2f2c27"/>'
        s += fn(cx, 180)
        s += f'<text x="{cx}" y="360" text-anchor="middle" font-family="Inter" font-size="19" letter-spacing="6" fill="{MUTE}">{lab}</text>'
    return frame(s, 390)

# ---------- slides ----------
SLIDES = [
 dict(vis=vis_capa(), top=150, h1='O GTA 6 chega às lojas por <em>R$&nbsp;449,90</em>.',
      sub='Em 2013, o GTA V saiu no Brasil por R$ 199. O jogo ficou mesmo mais caro, ou foi o dinheiro que mudou?', src='Exame, O Tempo, Estado de Minas'),
 dict(vis=vis_nominal(), top=170, h1='Na etiqueta, a alta é de <em>126%</em>.',
      sub='É a conta que quase todo mundo faz. Só que comparar preços de anos diferentes sem descontar a inflação distorce o resultado.', src='Exame, Estado de Minas'),
 dict(vis=vis_ipca(), top=170, h1='Desde 2013, o IPCA acumulou <em>106,8%</em>.',
      sub=f'Corrigidos pela inflação de setembro de 2013 a outubro de 2026, os R$ 199 da época equivalem a {brl(CORR)} hoje.', src='IBGE (IPCA), cálculo próprio'),
 dict(vis=vis_comp(), top=170, h1='Em termos reais, o Standard custa só <em>9,3%</em> a mais.',
      sub=f'A edição Ultimate, de R$ 549,90, fica 33,6% acima do GTA V corrigido.', src='IBGE, Exame, O Tempo'),
 dict(vis=vis_nota(), top=190, h1='O jogo quase não encareceu. <em>O real</em> é que perdeu valor.',
      sub='A inflação não aparece em fatura nenhuma, mas trabalha todos os meses contra o dinheiro que fica parado.', src=''),
 dict(vis=vis_gaveta(), top=170, h1='R$ 199 parados compram hoje o que <em>R$&nbsp;96</em> compravam em 2013.',
      sub='Mais da metade do poder de compra (51,7%) ficou pelo caminho, sem aparecer em extrato nenhum.', src='IBGE (IPCA), cálculo próprio'),
 dict(vis=vis_patrimonio(), top=190, h1='No patrimônio, a conta é <em>a mesma</em>.',
      sub='Reserva da família, caixa da empresa ou receita da safra: o que importa é quanto sobra depois da inflação. Fale comigo pelo link da bio.', src=''),
]

CSS = f"""
@font-face{{font-family:"Fraunces";src:url(fonts/fraunces-latin-400-normal.woff2);font-weight:400}}
@font-face{{font-family:"Fraunces";src:url(fonts/fraunces-latin-500-normal.woff2);font-weight:500}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;background:#0a0a0a}}
.art{{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:"Inter",sans-serif;color:{INK};
 background:radial-gradient(ellipse 900px 600px at 50% 18%, #1a1d24 0%, #111317 45%, #0a0a0a 75%)}}
.grain{{position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(255,255,255,.018) 0 1px,transparent 1px 54px)}}
.top{{position:absolute;left:100px;right:100px;top:80px;display:flex;justify-content:space-between;font-size:22px;letter-spacing:.32em;text-transform:uppercase}}
.top .k{{color:{GOLD}}}.top .d{{color:#a9a39a}}
.vis{{position:absolute;left:100px}}
.content{{position:absolute;left:100px;right:100px;bottom:200px}}
h1{{font-family:"Fraunces",serif;font-weight:500;font-size:74px;line-height:1.06;letter-spacing:-.01em;color:{INK}}}
h1 em{{font-style:normal;color:{GOLD}}}
.sub{{font-size:28px;line-height:1.45;color:#d4cdc2;margin-top:22px;max-width:860px}}
.foot{{position:absolute;left:100px;right:100px;bottom:62px;display:flex;justify-content:space-between;align-items:flex-end;border-top:1px solid {LINE};padding-top:24px}}
.name{{font-family:"Fraunces",serif;font-size:36px;color:{INK}}}
.role{{font-size:15px;letter-spacing:.24em;color:{MUTE};text-transform:uppercase;margin-top:6px}}
.right{{text-align:right}}.handle{{font-family:"Fraunces",serif;font-size:31px;color:{GOLD}}}
.src{{font-size:16px;color:{MUTE};margin-top:8px;letter-spacing:.04em}}
"""

def page(i, sl):
    n = len(SLIDES)
    right = "16.11.2026" if i == 0 else f"{i+1:02d} / {n:02d}"
    src = f'<div class="src">Fonte: {sl["src"]}</div>' if sl["src"] else '<div class="src">&nbsp;</div>'
    vis = sl["vis"].replace('<svg class="vis"', f'<svg class="vis" style="top:{sl["top"]}px"', 1)
    return f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="art"><div class="grain"></div>
<div class="top"><span class="k">Inflação · Poder de compra</span><span class="d">{right}</span></div>
{vis}
<div class="content"><h1>{sl['h1']}</h1><p class="sub">{sl['sub']}</p></div>
<div class="foot"><div><div class="name">Tiago Acordi</div><div class="role">Assessor Alta Renda da XP Investimentos</div></div>
<div class="right"><div class="handle">@tiagoassessorxp</div>{src}</div></div>
</div></body></html>"""

async def main():
    from playwright.async_api import async_playwright
    with tempfile.TemporaryDirectory() as d:
        d = Path(d); shutil.copytree(KIT / "fonts", d / "fonts")
        async with async_playwright() as p:
            kw = {"executable_path": "/usr/bin/google-chrome"} if Path("/usr/bin/google-chrome").exists() else {}
            b = await p.chromium.launch(**kw)
            pg = await b.new_page(viewport={"width": 1080, "height": 1350})
            for i, sl in enumerate(SLIDES):
                f = d / f"s{i}.html"; f.write_text(page(i, sl))
                await pg.goto(f.as_uri()); await pg.wait_for_timeout(500)
                # checa se o texto invade a ilustração
                vb = await pg.evaluate("(()=>{const v=document.querySelector('.vis').getBoundingClientRect();const c=document.querySelector('.content').getBoundingClientRect();return [v.bottom,c.top]})()")
                print(f"slide {i+1}: vis_bottom={vb[0]:.0f} content_top={vb[1]:.0f}", "OVERLAP" if vb[0] > vb[1] - 10 else "ok")
                await pg.screenshot(path=str(HERE / f"slide_{i+1}.png"))
            await b.close()

if __name__ == "__main__":
    asyncio.run(main())
