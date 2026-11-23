"""Renderiza um Stories de notícia (1080x1920) no padrão @tiagoassessorxp.

Uso:
    python3 render_story.py spec.json bg.svg saida.png

spec.json:
{
  "kicker": "Câmbio · Agora",
  "date": "23.11.2026",
  "tag": "Urgente",                         # opcional
  "headline_html": "Dólar encosta em <em>R$ 6</em>.",   # <em> = dourado; até 3 linhas
  "sub": "Moeda sobe 0,86% e chega a R$ 5,986 na manhã desta segunda...",  # até 3 linhas
  "cells": [                                 # 2 ou 4 células
    {"label": "Dólar às 9h08", "value": "R$ 5,986", "arrow": "↑", "note": "alta de 0,86%"}
  ],
  "source": "IstoÉ Dinheiro, BPMoney"
}

bg.svg: ilustração 1080x1920. A ilustração fica entre y≈380 e y≈900; de ~y=960 para baixo,
o fundo precisa terminar em #0a0a0a (o texto fica ali, ancorado de baixo para cima).
Zonas seguras do Stories: nada importante acima de y=230 nem abaixo de y=1745.
"""
import asyncio, html, json, shutil, sys, tempfile
from pathlib import Path

KIT = Path(__file__).resolve().parent
FONTS = KIT.parent / "_kit_noticias" / "fonts"

CSS = """
@font-face{font-family:"Fraunces";src:url(fonts/fraunces-latin-400-normal.woff2);font-weight:400}
@font-face{font-family:"Fraunces";src:url(fonts/fraunces-latin-500-normal.woff2);font-weight:500}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;background:#0a0a0a}
.a{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:"Inter",sans-serif;color:#efe6d6}
.bg{position:absolute;inset:0;width:1080px;height:1920px}
.top{position:absolute;left:96px;right:96px;top:250px;display:flex;justify-content:space-between;font-size:24px;letter-spacing:.32em;text-transform:uppercase}
.top .k{color:#c9a45c}.top .d{color:#a9a39a}
.tag{position:absolute;left:96px;top:310px;border:1.5px solid #c9a45c;color:#c9a45c;background:rgba(10,10,10,.55);font-size:20px;font-weight:600;letter-spacing:.3em;padding:9px 16px 8px 20px;text-transform:uppercase}
.c{position:absolute;left:96px;right:96px;bottom:325px}
h1{font-family:"Fraunces";font-weight:500;font-size:92px;line-height:1.04;color:#f1e8d8}
h1 em{font-style:normal;color:#c9a45c}
.sub{font-size:31px;line-height:1.45;color:#d4cdc2;margin-top:24px}
.grid{display:grid;grid-template-columns:1fr 1fr;margin-top:36px;border-top:1px solid #2a2824}
.cell{padding:20px 0 18px;border-bottom:1px solid #2a2824}
.cell:nth-child(odd){padding-right:26px;border-right:1px solid #2a2824}.cell:nth-child(even){padding-left:34px}
.lab{font-size:18px;letter-spacing:.28em;color:#8f8a82;text-transform:uppercase}
.val{font-family:"Fraunces";font-size:46px;margin-top:8px;color:#f1e8d8}.val .ar{color:#c9a45c;font-family:"Inter";font-size:36px;margin-right:6px}
.note{font-size:21px;color:#8f8a82;margin-top:4px}
.foot{position:absolute;left:96px;right:96px;bottom:175px;display:flex;justify-content:space-between;align-items:flex-end;border-top:1px solid #2a2824;padding-top:24px}
.name{font-family:"Fraunces";font-size:36px}.role{white-space:nowrap;font-size:15px;letter-spacing:.2em;color:#8f8a82;text-transform:uppercase;margin-top:6px}
.h{font-family:"Fraunces";font-size:32px;color:#c9a45c;text-align:right}.src{font-size:16px;color:#8f8a82;margin-top:8px;text-align:right}
"""

def build_html(spec):
    e = html.escape
    cells = ""
    for c in spec.get("cells", []):
        ar = f'<span class="ar">{e(c["arrow"])}</span>' if c.get("arrow") else ""
        cells += (f'<div class="cell"><div class="lab">{e(c["label"])}</div>'
                  f'<div class="val">{ar}{e(c["value"])}</div><div class="note">{e(c.get("note",""))}</div></div>')
    grid = f'<div class="grid">{cells}</div>' if cells else ""
    tag = f'<span class="tag">{e(spec["tag"])}</span>' if spec.get("tag") else ""
    return f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="a"><img class="bg" src="bg.svg">
<div class="top"><span class="k">{e(spec['kicker'])}</span><span class="d">{e(spec['date'])}</span></div>{tag}
<div class="c"><h1>{spec['headline_html']}</h1><p class="sub">{e(spec.get('sub',''))}</p>{grid}</div>
<div class="foot"><div><div class="name">Tiago Acordi</div><div class="role">Assessor Alta Renda da XP Investimentos</div></div>
<div><div class="h">@tiagoassessorxp</div><div class="src">Fonte: {e(spec['source'])}</div></div></div>
</div></body></html>"""

async def shoot(page, out):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        kw = {"executable_path": "/usr/bin/google-chrome"} if Path("/usr/bin/google-chrome").exists() else {}
        b = await p.chromium.launch(**kw)
        pg = await b.new_page(viewport={"width": 1080, "height": 1920})
        await pg.goto(page.as_uri())
        await pg.evaluate("document.fonts.ready")
        await pg.wait_for_timeout(500)
        await pg.screenshot(path=str(out))
        await b.close()

def main():
    spec_p, bg_p, out_p = map(Path, sys.argv[1:4])
    spec = json.loads(spec_p.read_text())
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        shutil.copytree(FONTS, td / "fonts")
        shutil.copy(bg_p, td / "bg.svg")
        (td / "story.html").write_text(build_html(spec))
        asyncio.run(shoot(td / "story.html", out_p.resolve()))
    print(out_p.resolve())

if __name__ == "__main__":
    main()
