"""Slides 2 a 5 do carrossel 'Trabuco na Fazenda' (1080x1350) no padrão @tiagoassessorxp.
A capa (slide 1) sai de ../_kit_noticias/render.py com bg.svg (bg_alvorada.py).
Uso: python3 carrossel_trabuco.py  -> slide_2.png ... slide_5.png
"""
import asyncio, html, shutil, tempfile
from pathlib import Path
HERE = Path(__file__).resolve().parent
KIT = HERE.parent / "_kit_noticias"
GOLD = "#c9a45c"

CSS = """
@font-face{font-family:"Fraunces";src:url(fonts/fraunces-latin-400-normal.woff2);font-weight:400}
@font-face{font-family:"Fraunces";src:url(fonts/fraunces-latin-500-normal.woff2);font-weight:500}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;background:#0a0a0a}
.art{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:"Inter",sans-serif;color:#efe6d6;
 background:radial-gradient(ellipse 900px 420px at 50% 0%,rgba(201,164,92,.13),rgba(201,164,92,0) 70%),#0a0a0a}
.top{position:absolute;left:100px;right:100px;top:80px;display:flex;justify-content:space-between;font-size:22px;letter-spacing:.32em;text-transform:uppercase}
.top .k{color:#c9a45c}.top .d{color:#a9a39a}
.vis{position:absolute;left:100px;top:140px}
.content{position:absolute;left:100px;right:100px;top:350px}
h2{font-family:"Fraunces",serif;font-weight:500;font-size:66px;line-height:1.06;color:#f1e8d8;letter-spacing:-.01em}
h2 em{font-style:normal;color:#c9a45c}
.lead{font-size:26px;line-height:1.45;color:#d4cdc2;margin-top:18px}
.rows{margin-top:30px;border-top:1px solid #2a2824}
.row{display:grid;grid-template-columns:220px 1fr;gap:28px;padding:26px 0 25px;border-bottom:1px solid #2a2824}
.row .w{font-family:"Fraunces",serif;font-size:32px;color:#c9a45c;line-height:1.15}
.row .w small{display:block;font-family:"Inter";font-size:16px;letter-spacing:.24em;color:#8f8a82;text-transform:uppercase;margin-top:6px}
.row .t{font-size:26px;line-height:1.42;color:#e4dccd}
.row .t b{color:#f1e8d8;font-weight:600}
.quote{margin-top:34px;padding:24px 28px;border-left:3px solid #c9a45c;background:rgba(201,164,92,.06);font-family:"Fraunces",serif;font-size:30px;line-height:1.38;color:#efe6d6}
.grid{display:grid;grid-template-columns:1fr 1fr;margin-top:28px;border-top:1px solid #2a2824}
.cell{padding:24px 0 22px;border-bottom:1px solid #2a2824}
.cell:nth-child(odd){padding-right:30px;border-right:1px solid #2a2824}
.cell:nth-child(even){padding-left:40px}
.lab{font-size:17px;letter-spacing:.3em;color:#8f8a82;text-transform:uppercase}
.val{font-family:"Fraunces",serif;font-size:46px;margin-top:10px;color:#f1e8d8}
.val .ar{color:#c9a45c;font-family:"Inter";font-size:32px;margin-right:6px}
.note{font-size:20px;color:#8f8a82;margin-top:4px}
.foot{position:absolute;left:100px;right:100px;bottom:62px;display:flex;justify-content:space-between;align-items:flex-end;border-top:1px solid #2a2824;padding-top:24px}
.name{font-family:"Fraunces",serif;font-size:36px;color:#f1e8d8}
.role{font-size:15px;letter-spacing:.24em;color:#8f8a82;text-transform:uppercase;margin-top:6px}
.right{text-align:right}.handle{font-family:"Fraunces",serif;font-size:31px;color:#c9a45c}
.src{font-size:16px;color:#8f8a82;margin-top:8px;letter-spacing:.04em}
"""

def svg(inner, h=160):
    return f'<svg class="vis" width="880" height="{h}" viewBox="0 0 880 {h}" xmlns="http://www.w3.org/2000/svg">{inner}</svg>'

# --- vinhetas de topo ---
def vis_timeline():
    s = f'<line x1="20" y1="90" x2="860" y2="90" stroke="{GOLD}" stroke-opacity=".35" stroke-width="2"/>'
    pts = [(60, "SEG 23"), (320, "QUI 26 · DIA"), (570, "QUI 26 · TARDE"), (820, "QUI 26 · NOITE")]
    for i, (x, lab) in enumerate(pts):
        last = i == len(pts) - 1
        s += f'<circle cx="{x}" cy="90" r="{14 if last else 9}" fill="{"#f3dfa8" if last else "#0a0a0a"}" stroke="{GOLD}" stroke-width="2.5"/>'
        if last:
            s += f'<circle cx="{x}" cy="90" r="28" fill="{GOLD}" opacity=".18"/>'
        anc = "start" if i == 0 else ("end" if last else "middle")
        s += f'<text x="{x+ (-20 if i==0 else (24 if last else 0))}" y="140" text-anchor="{anc}" font-family="Inter" font-size="15" letter-spacing="3" fill="#8f8a82">{lab}</text>'
    s += f'<path d="M820 66 l0 -30 l26 9 l-26 9" fill="{GOLD}" opacity=".9"/>'
    return svg(s)

def vis_carreira():
    s = ''
    steps = [(1969, 22), (1992, 40), (2003, 58), (2009, 78), (2018, 96), (2027, 116)]
    for i, (yr, h) in enumerate(steps):
        x = 30 + i * 140
        gold = yr == 2027
        s += f'<rect x="{x}" y="{150-h}" width="110" height="{h}" fill="{GOLD if gold else "#2a2824"}" opacity="{1 if gold else .9}"/>'
        s += f'<text x="{x+55}" y="{150-h-12}" text-anchor="middle" font-family="Fraunces" font-size="24" fill="{"#f3dfa8" if gold else "#a9a39a"}">{yr}</text>'
    return svg(s, 160).replace("y=\"", "y=\"", 1)

def vis_mercado():
    import random
    random.seed(5)
    s = ''
    p = 120.0; pts = []
    for i in range(48):
        x = 20 + i * 17.5
        p += random.uniform(-6, 7) if i < 36 else -random.uniform(5, 10)
        p = max(18, min(140, p)); pts.append((x, p))
    d = "M" + " L".join(f"{x:.0f},{y:.0f}" for x, y in pts)
    s += f'<path d="{d}" fill="none" stroke="{GOLD}" stroke-width="3"/>'
    s += f'<circle cx="{pts[-1][0]:.0f}" cy="{pts[-1][1]:.0f}" r="7" fill="#f3dfa8"/>'
    q = 40.0; pts2 = []
    for i in range(48):
        x = 20 + i * 17.5
        q += random.uniform(-5, 6) if i < 36 else random.uniform(4, 8)
        q = max(20, min(150, q)); pts2.append((x, q))
    d2 = "M" + " L".join(f"{x:.0f},{y:.0f}" for x, y in pts2)
    s += f'<path d="{d2}" fill="none" stroke="#8f8a82" stroke-width="2" stroke-dasharray="6 5"/>'
    s += f'<text x="860" y="{pts[-1][1]-14:.0f}" text-anchor="end" font-family="Inter" font-size="15" letter-spacing="3" fill="{GOLD}">BOLSA</text>'
    s += f'<text x="860" y="{min(156,pts2[-1][1]+22):.0f}" text-anchor="end" font-family="Inter" font-size="15" letter-spacing="3" fill="#8f8a82">DÓLAR</text>'
    return svg(s)

def vis_balanca():
    s = f'<line x1="440" y1="10" x2="440" y2="150" stroke="{GOLD}" stroke-width="3"/>'
    s += f'<path d="M400 150 h80" stroke="{GOLD}" stroke-width="3"/>'
    s += f'<line x1="250" y1="44" x2="630" y2="24" stroke="{GOLD}" stroke-width="3"/>'
    s += f'<circle cx="440" cy="34" r="7" fill="#f3dfa8"/>'
    for cx, cy, lab, col in [(250, 44, "EXPECTATIVA", GOLD), (630, 24, "ENTREGA", "#a9a39a")]:
        s += f'<line x1="{cx}" y1="{cy}" x2="{cx-50}" y2="{cy+60}" stroke="{col}" stroke-opacity=".6"/><line x1="{cx}" y1="{cy}" x2="{cx+50}" y2="{cy+60}" stroke="{col}" stroke-opacity=".6"/>'
        s += f'<path d="M{cx-60} {cy+60} q60 34 120 0 z" fill="{col}" fill-opacity=".25" stroke="{col}"/>'
        s += f'<text x="{cx}" y="{cy+112}" text-anchor="middle" font-family="Inter" font-size="15" letter-spacing="3" fill="{col}">{lab}</text>'
    return svg(s)

def rows(items):
    return '<div class="rows">' + ''.join(
        f'<div class="row"><div class="w">{w}</div><div class="t">{t}</div></div>' for w, t in items) + '</div>'

def page(n, kicker, vis, body, src):
    return f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="art"><div class="top"><span class="k">{kicker}</span><span class="d">{n:02d} / 05</span></div>{vis}
<div class="content">{body}</div>
<div class="foot"><div><div class="name">Tiago Acordi</div><div class="role">Assessor Alta Renda da XP Investimentos</div></div>
<div class="right"><div class="handle">@tiagoassessorxp</div><div class="src">Fonte: {html.escape(src)}</div></div></div></div></body></html>"""

SLIDES = {
2: page(2, "Como ele aceitou", vis_timeline(),
  '<h2>Do convite ao <em>sim</em> em três dias.</h2>' + rows([
   ('Seg. 23<small>Alvorada</small>', 'Lula faz o convite em conversa <b>fora da agenda oficial</b>. Trabuco pede tempo para ouvir a família, o banco e outros empresários.'),
   ('Qui. 26<small>Durante o dia</small>', 'O nome ganha força no mercado e a bolsa acelera ao longo do pregão.'),
   ('Qui. 26<small>Fim da tarde</small>', 'Nova reunião no Alvorada. Trabuco <b>aceita</b> e Lula chama os ministros da Fazenda e do Planejamento para iniciar a transição.'),
   ('Qui. 26<small>Noite</small>', 'Nota do governo: Trabuco “aceitou o convite (...) para comandar o Ministério da Fazenda a partir de 2027”.'),
  ]), "Planalto, Metrópoles, Folha"),
3: page(3, "Quem é Trabuco", vis_carreira(),
  '<h2>Mais de <em>50 anos</em> no mesmo banco.</h2>' + rows([
   ('75 anos<small>Perfil</small>', 'Nascido em Marília (SP), formado em <b>Filosofia pela USP</b>.'),
   ('1969<small>Início</small>', 'Entra aos 17 anos como escriturário em um dos maiores bancos privados do país.'),
   ('2009–2018<small>Comando</small>', 'Presidente executivo do banco. Desde 2018, <b>preside o conselho de administração</b>.'),
   ('2014<small>O primeiro não</small>', 'Recusou o convite de Dilma Rousseff para a Fazenda. A escolhida foi Joaquim Levy, que ficou cerca de 11 meses no cargo.'),
  ]), "SBT News, Jovem Pan, Metrópoles"),
4: page(4, "A reação do mercado", vis_mercado(),
  '<h2>O dia em que a bolsa subiu <em>6,07%</em>.</h2>'
  '<div class="grid">'
  '<div class="cell"><div class="lab">Ibovespa</div><div class="val"><span class="ar">↑</span>176.799</div><div class="note">maior alta desde o 1º turno</div></div>'
  '<div class="cell"><div class="lab">Dólar</div><div class="val"><span class="ar">↓</span>R$ 5,74</div><div class="note">4ª queda seguida</div></div>'
  '<div class="cell"><div class="lab">Juros futuros</div><div class="val"><span class="ar">↓</span>Em queda</div><div class="note">alívio na curva</div></div>'
  '<div class="cell"><div class="lab">IPCA-15 novembro</div><div class="val">0,22%</div><div class="note">abaixo do esperado</div></div></div>'
  '<div class="quote">Analistas citam um nome técnico e não político, a expectativa de condução mais previsível e de maior responsabilidade fiscal.</div>',
  "B3, IBGE, CNN Brasil, InfoMoney"),
5: page(5, "O que o mercado espera", vis_balanca(),
  '<h2>Agora, o nome precisa virar <em>entrega</em>.</h2>' + rows([
   ('Gastos<small>Na mesa</small>', 'Governo estuda uma PEC para conter as <b>despesas obrigatórias</b> a partir de 2027.'),
   ('Ajuste<small>Debate</small>', 'Parte dos economistas considera o ajuste aprovado pelo Congresso insuficiente para mudar a percepção de risco.'),
   ('Alerta<small>Analistas</small>', 'Nomes respeitados trazem alívio inicial. A melhora duradoura depende de medidas concretas e da equipe.'),
   ('Política<small>Base</small>', 'Há resistência no PT: o líder da bancada na Câmara, Pedro Uczai (SC), disse que o banqueiro não seria a melhor opção.'),
  ]), "InfoMoney, IstoÉ, Folha, SBT"),
}

async def shoot(paths):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        kw = {"executable_path": "/usr/bin/google-chrome"} if Path("/usr/bin/google-chrome").exists() else {}
        b = await p.chromium.launch(**kw)
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for src, out in paths:
            await pg.goto(src.as_uri()); await pg.wait_for_timeout(600)
            await pg.screenshot(path=str(out))
        await b.close()

with tempfile.TemporaryDirectory() as d:
    d = Path(d); shutil.copytree(KIT / "fonts", d / "fonts")
    jobs = []
    for n, h in SLIDES.items():
        f = d / f"s{n}.html"; f.write_text(h); jobs.append((f, HERE / f"slide_{n}.png"))
    asyncio.run(shoot(jobs))
print("ok")
