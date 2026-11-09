import asyncio, sys
from pathlib import Path
from playwright.async_api import async_playwright
OUT = Path(sys.argv[1])
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1080px;background:#131417;font-family:'Liberation Sans',Arial,sans-serif;color:#f1ede4;position:relative;overflow:hidden}
.top{position:absolute;left:92px;top:92px;font-size:24px;font-weight:700;letter-spacing:.2em;color:#8e8e90;text-transform:uppercase}
.rule{position:absolute;left:92px;width:84px;height:5px;background:#c9a646}
.h{position:absolute;left:92px;font-family:'Liberation Serif','Times New Roman',serif;font-weight:400;color:#f1ede4}
.p{position:absolute;left:92px;color:#8e8e90;font-size:34px;line-height:1.32}
.foot{position:absolute;left:92px;right:92px;top:957px;border-top:1px solid #27282c;display:flex;justify-content:space-between;padding-top:50px;font-size:22px;letter-spacing:.12em;color:#8e8e90;white-space:nowrap}
.foot b{color:#c9a646;letter-spacing:.2em}
.grid{position:absolute;left:92px;top:170px;width:894px;height:524px;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:262px 262px;border:1px solid #2a2b30}
.cell{border:1px solid #2a2b30;padding:26px 34px}
.t{font-size:23px;font-weight:700;letter-spacing:.2em;color:#c9a646}.t span{font-weight:400;color:#8e8e90;letter-spacing:.14em;margin-left:10px}
.sub{font-size:20px;color:#8e8e90;margin-top:6px}
.vals{display:flex;gap:56px;margin-top:38px}
.sub+.vals{margin-top:18px}
.y{font-size:23px;letter-spacing:.16em;color:#8e8e90}
.v{font-family:'Liberation Serif',serif;font-size:66px;line-height:1.05;color:#f1ede4}
.a{font-size:25px;color:#c9a646;margin-top:8px;height:30px}
.leg{position:absolute;left:92px;top:830px;font-size:24px;color:#8e8e90}.leg i{font-style:normal;color:#c9a646}
"""
def foot(n, extra=""):
    return f'<div class="foot"><span>@tiagoassessorxp{extra}</span><b>0{n} / 03</b></div>'
def cell(title, unit, sub, a, b):
    s = f'<div class="sub">{sub}</div>' if sub else ''
    def col(y, v, ar):
        return f'<div><div class="y">{y}</div><div class="v">{v}</div><div class="a">{ar}</div></div>'
    return f'<div class="cell"><div class="t">{title}<span>{unit}</span></div>{s}<div class="vals">{col("2026",*a)}{col("2027",*b)}</div></div>'
UP,DN,EQ="▲","▼","="
s1 = f'''<div class="top">LEITURA DA SEMANA</div><div class="rule" style="top:358px"></div>
<div class="h" style="top:405px;font-size:92px;line-height:1.03;width:760px">O que o mercado projeta para a economia.</div>
<div class="p" style="top:726px;font-size:36px;line-height:1.37">Boletim Focus, Banco Central do Brasil.<br>Edição de 06/11/2026.</div>{foot(1)}'''
s2 = f'''<div class="top">FOCUS · 06/11/2026</div><div class="grid">
{cell("IPCA","(%)","",("5,22",EQ),("4,90",UP))}
{cell("PIB","(var. %)","",("1,75",DN),("1,15",DN))}
{cell("CÂMBIO","(R$/US$)","fim de período",("5,35",UP),("5,40",EQ))}
{cell("SELIC","(% a.a.)","meta fim de período",("13,75",UP),("12,50",EQ))}</div>
<div class="leg"><i>▲</i> alta &nbsp;&nbsp; <i>▼</i> queda &nbsp;&nbsp; <i>=</i> estável &nbsp;&nbsp; em relação à semana anterior</div>{foot(2)}'''
s3 = f'''<div class="top">LEITURA PARA O OESTE</div><div class="rule" style="top:298px"></div>
<div class="h" style="top:350px;font-size:70px;line-height:1.1;width:900px">Inflação de 2027 sobe.<br>Crescimento perde força.</div>
<div class="p" style="top:572px;width:880px">O IPCA esperado para 2027 subiu para 4,90%, o PIB de 2026 recuou para 1,75% e a Selic projetada para o fim de 2026 passou a 13,75%. Para quem empreende e produz no Oeste catarinense, o cenário sugere custo do dinheiro elevado por mais tempo.</div>{foot(3, "&nbsp;&nbsp;·&nbsp;&nbsp;Assessor Alta Renda da XP Investimentos")}'''
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page(viewport={"width":1080,"height":1080})
        for i, s in enumerate((s1,s2,s3),1):
            await pg.set_content(f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body>{s}</body></html>")
            await pg.wait_for_timeout(200)
            await pg.screenshot(path=str(OUT/f"slide-0{i}.png"))
        await b.close()
asyncio.run(main())
