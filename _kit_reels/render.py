"""Renderiza um Reels (1080x1920, 30 fps) a partir de PASTA/pagina.html + timeline.json + narracao.wav.

Uso:
    python3 _kit_reels/render.py PASTA --quadros 3.0,12.5,...   # só tira prints desses instantes (conferência)
    python3 _kit_reels/render.py PASTA                           # vídeo completo -> PASTA/reels.mp4
    python3 _kit_reels/render.py PASTA --so-audio                # refaz só o som sobre o reels.mp4 existente

O vídeo é filmado em 2 partes em paralelo (uma por CPU) e unido sem recodificar. O som (som.py) junta a
narração, a trilha sintetizada e os efeitos do campo "sfx" do roteiro.json, e sai normalizado em -14 LUFS.
"""
import json, subprocess, sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import som

FPS, W, H = 30, 1080, 1920
PARTES = 2
ENC = ["-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", str(FPS)]


def carregar(pasta):
    tl = json.loads((pasta / "timeline.json").read_text())
    rot = json.loads((pasta / "roteiro.json").read_text())
    tl["kicker"] = rot.get("kicker", "Entenda em 1 minuto")
    return tl, rot


def abrir(p, pasta, tl):
    kw = {"executable_path": "/usr/bin/google-chrome"} if Path("/usr/bin/google-chrome").exists() else {}
    b = p.chromium.launch(**kw)
    pg = b.new_page(viewport={"width": W, "height": H})
    erros = []
    pg.on("pageerror", lambda e: erros.append(str(e)))
    pg.add_init_script(f"window.TL = {json.dumps(tl, ensure_ascii=False)};")
    pg.goto((pasta / "pagina.html").resolve().as_uri())
    pg.wait_for_timeout(400)
    if erros:
        raise SystemExit("erro na página: " + " | ".join(erros))
    pg.wait_for_function("window.__ready === true", timeout=10000)
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(300)
    return b, pg


def filmar(pasta, i0, i1, saida):
    from playwright.sync_api import sync_playwright
    tl, _ = carregar(pasta)
    tmp = saida.with_name(saida.stem + ".tmp.mp4")
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS),
                           "-c:v", "mjpeg", "-i", "-", *ENC, str(tmp)], stdin=subprocess.PIPE)
    with sync_playwright() as p:
        b, pg = abrir(p, pasta, tl)
        for i in range(i0, i1):
            pg.evaluate(f"window.seek({i / FPS})")
            ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
            if (i - i0) % 300 == 0:
                print(f"quadro {i}/{i1}", flush=True)
        b.close()
    ff.stdin.close()
    if ff.wait() != 0:
        raise SystemExit("ffmpeg (vídeo) falhou")
    tmp.rename(saida)


def audio(pasta, video, tl, rot):
    dur = tl["duracao"]
    som.salvar(som.trilha(dur, rot.get("bpm", 84)), pasta / "_trilha.wav")
    som.salvar(np.clip(som.faixa_sfx(rot.get("sfx", []), tl) * 0.8, -1, 1), pasta / "_sfx.wav")
    g = rot.get("mix", {})
    final_tmp = pasta / "_reels.tmp.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(video), "-i", str(pasta / "narracao.wav"),
                    "-i", str(pasta / "_trilha.wav"), "-i", str(pasta / "_sfx.wav"), "-filter_complex",
                    "[1:a]aresample=48000,highpass=f=70,acompressor=threshold=-18dB:ratio=3:attack=5:release=120,"
                    f"volume={g.get('voz', 1.6)}[v];[2:a]volume={g.get('trilha', 0.14)}[m];"
                    f"[3:a]volume={g.get('sfx', 0.5)}[s];"
                    "[v][m][s]amix=inputs=3:duration=first:normalize=0,alimiter=limit=0.95,"
                    "loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ac", "2",
                    "-movflags", "+faststart", "-t", f"{dur:.3f}", str(final_tmp)], check=True)
    final_tmp.rename(pasta / "reels.mp4")
    (pasta / "_trilha.wav").unlink(); (pasta / "_sfx.wav").unlink()


def main():
    pasta = Path(sys.argv[1])
    tl, rot = carregar(pasta)
    if "--parte" in sys.argv:                       # uso interno: filma um trecho
        k = sys.argv.index("--parte")
        filmar(pasta, int(sys.argv[k + 1]), int(sys.argv[k + 2]), Path(sys.argv[k + 3])); return
    if "--quadros" in sys.argv:
        from playwright.sync_api import sync_playwright
        ts = [float(x) for x in sys.argv[sys.argv.index("--quadros") + 1].split(",")]
        with sync_playwright() as p:
            b, pg = abrir(p, pasta, tl)
            for t in ts:
                pg.evaluate(f"window.seek({t})")
                pg.screenshot(path=str(pasta / f"_quadro_{t:05.1f}.jpg"), type="jpeg", quality=85)
            b.close()
        print("quadros ok"); return
    if "--so-audio" in sys.argv:
        velho = pasta / "_video_antigo.mp4"
        (pasta / "reels.mp4").rename(velho)
        audio(pasta, velho, tl, rot); velho.unlink()
        print(pasta / "reels.mp4"); return
    n = int(np.ceil(tl["duracao"] * FPS))
    cortes = [round(n * k / PARTES) for k in range(PARTES + 1)]
    partes = [pasta / f"_parte{k}.mp4" for k in range(PARTES)]
    procs = [subprocess.Popen([sys.executable, __file__, str(pasta), "--parte", str(cortes[k]), str(cortes[k + 1]),
                               str(partes[k])]) for k in range(PARTES)]
    if any(p.wait() != 0 for p in procs):
        raise SystemExit("falha ao filmar")
    lista = pasta / "_lista.txt"
    lista.write_text("".join(f"file '{p.name}'\n" for p in partes))
    mudo = pasta / "_mudo.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lista),
                    "-c", "copy", str(mudo)], check=True)
    audio(pasta, mudo, tl, rot)
    for f in partes + [lista, mudo]:
        f.unlink()
    print(pasta / "reels.mp4")


if __name__ == "__main__":
    main()
