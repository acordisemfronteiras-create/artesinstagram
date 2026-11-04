"""Renderiza um post de notícia (1080x1350) no padrão @tiagoassessorxp.

Uso:
    python3 render.py spec.json bg.svg saida.png

spec.json:
{
  "kicker": "Juros no Brasil · Copom",
  "date": "04.11.2026",
  "tag": "Urgente",                      # opcional ("" ou ausente = sem selo)
  "headline_html": "BC mantém a Selic em <em>13,75%</em> ao ano.",   # <em> = dourado
  "sub": "Pausa nos cortes na primeira reunião do Copom após a reeleição de Lula.",
  "cells": [                             # 2 ou 4 células
    {"label": "Taxa Selic", "value": "13,75%", "note": "ao ano"},
    {"label": "Decisão de hoje", "value": "Manutenção", "arrow": "→", "note": "votação unânime"}
  ],
  "source": "Banco Central, InfoMoney"
}

bg.svg: ilustração de fundo 1080x1350 desenhada para o tema da notícia.
A metade de baixo precisa terminar em #0a0a0a (o texto fica ali).
"""
import asyncio, html, json, shutil, sys, tempfile
from pathlib import Path

KIT = Path(__file__).resolve().parent

CSS = """
@font-face{font-family:"Fraunces";src:url(fonts/fraunces-latin-400-normal.woff2);font-weight:400}
@font-face{font-family:"Fraunces";src:url(fonts/fraunces-latin-500-normal.woff2);font-weight:500}
@font-face{font-family:"Fraunces";src:url(fonts/fraunces-latin-400-italic.woff2);font-weight:400;font-style:italic}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;background:#0a0a0a}
.art{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:"Inter",sans-serif;color:#efe6d6}
.bg{position:absolute;inset:0;width:1080px;height:1350px}
.top{position:absolute;left:100px;right:100px;top:80px;display:flex;justify-content:space-between;font-size:22px;letter-spacing:.32em;text-transform:uppercase}
.top .k{color:#c9a45c}.top .d{color:#a9a39a}
.content{position:absolute;left:100px;right:100px;bottom:186px}
.tag{display:inline-block;border:1.5px solid #c9a45c;color:#c9a45c;background:rgba(10,10,10,.55);font-size:19px;font-weight:600;letter-spacing:.3em;padding:9px 16px 8px 20px;text-transform:uppercase;margin-bottom:22px}
h1{font-family:"Fraunces",serif;font-weight:500;font-size:82px;line-height:1.04;letter-spacing:-.01em;color:#f1e8d8}
h1 em{font-style:normal;color:#c9a45c}
.sub{font-size:28px;line-height:1.45;color:#d4cdc2;margin-top:20px;max-width:820px}
.grid{display:grid;grid-template-columns:1fr 1fr;margin-top:30px;border-top:1px solid #2a2824}
.cell{padding:18px 0 16px;border-bottom:1px solid #2a2824}
.cell:nth-child(odd){padding-right:30px;border-right:1px solid #2a2824}
.cell:nth-child(even){padding-left:40px}
.lab{font-size:17px;letter-spacing:.3em;color:#8f8a82;text-transform:uppercase}
.val{font-family:"Fraunces",serif;font-size:40px;margin-top:8px;color:#f1e8d8}
.val .ar{color:#c9a45c;font-family:"Inter";font-size:32px;margin-right:6px}
.note{font-size:20px;color:#8f8a82;margin-top:4px}
.foot{position:absolute;left:100px;right:100px;bottom:62px;display:flex;justify-content:space-between;align-items:flex-end;border-top:1px solid #2a2824;padding-top:24px}
.name{font-family:"Fraunces",serif;font-size:36px;color:#f1e8d8}
.role{font-size:15px;letter-spacing:.24em;color:#8f8a82;text-transform:uppercase;margin-top:6px}
.right{text-align:right}.handle{font-family:"Fraunces",serif;font-size:31px;color:#c9a45c}
.src{font-size:16px;color:#8f8a82;margin-top:8px;letter-spacing:.04em}
"""

def build_html(spec):
    e = html.escape
    cells = ""
    for c in spec.get("cells", []):
        arrow = f'<span class="ar">{e(c["arrow"])}</span>' if c.get("arrow") else ""
        cells += (f'<div class="cell"><div class="lab">{e(c["label"])}</div>'
                  f'<div class="val">{arrow}{e(c["value"])}</div>'
                  f'<div class="note">{e(c.get("note",""))}</div></div>')
    tag = f'<span class="tag">{e(spec["tag"])}</span><br>' if spec.get("tag") else ""
    grid = f'<div class="grid">{cells}</div>' if cells else ""
    return f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="art"><img class="bg" src="bg.svg">
<div class="top"><span class="k">{e(spec['kicker'])}</span><span class="d">{e(spec['date'])}</span></div>
<div class="content">{tag}<h1>{spec['headline_html']}</h1><p class="sub">{e(spec.get('sub',''))}</p>{grid}</div>
<div class="foot"><div><div class="name">Tiago Acordi</div><div class="role">Assessor Alta Renda da XP Investimentos</div></div>
<div class="right"><div class="handle">@tiagoassessorxp</div><div class="src">Fonte: {e(spec['source'])}</div></div></div>
</div></body></html>"""

async def shoot(page_path, out):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        kw = {}
        if Path("/usr/bin/google-chrome").exists():
            kw["executable_path"] = "/usr/bin/google-chrome"
        b = await p.chromium.launch(**kw)
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        await pg.goto(page_path.as_uri())
        await pg.wait_for_timeout(800)
        await pg.screenshot(path=str(out))
        await b.close()

def main():
    spec_p, bg_p, out_p = map(Path, sys.argv[1:4])
    spec = json.loads(spec_p.read_text())
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        shutil.copytree(KIT / "fonts", d / "fonts")
        shutil.copy(bg_p, d / "bg.svg")
        (d / "post.html").write_text(build_html(spec))
        out_p = out_p.resolve()
        asyncio.run(shoot(d / "post.html", out_p))
    print(out_p)

if __name__ == "__main__":
    main()
