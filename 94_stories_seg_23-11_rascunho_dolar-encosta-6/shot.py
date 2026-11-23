import asyncio
from playwright.async_api import async_playwright
async def m():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page(viewport={"width":1080,"height":1920})
        import pathlib; await pg.goto("file://"+str(pathlib.Path("story.html").resolve()))
        await pg.wait_for_timeout(800)
        await pg.screenshot(path="saida.png"); await b.close()
asyncio.run(m())
