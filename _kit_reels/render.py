"""Renderiza um Reels (1080x1920, 30 fps) a partir de PASTA/pagina.html + timeline.json + narracao.wav.

Uso:
    python3 _kit_reels/render.py PASTA [--quadros 3.0,12.5,...]   # só tira prints desses instantes
    python3 _kit_reels/render.py PASTA                              # vídeo completo -> PASTA/reels.mp4

A trilha instrumental é sintetizada aqui (pad suave, sem direitos autorais) e mixada baixa sob a voz.
"""
import json, subprocess, sys, wave
from pathlib import Path
import numpy as np

FPS, W, H = 30, 1080, 1920


def chrome_kw():
    return {"executable_path": "/usr/bin/google-chrome"} if Path("/usr/bin/google-chrome").exists() else {}


def abrir(p, pasta, tl):
    b = p.chromium.launch(**chrome_kw())
    pg = b.new_page(viewport={"width": W, "height": H})
    pg.add_init_script(f"window.TL = {json.dumps(tl, ensure_ascii=False)};")
    pg.goto((pasta / "pagina.html").resolve().as_uri())
    pg.wait_for_function("window.__ready === true")
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(300)
    return b, pg


def trilha(dur, rate, out):
    """Pad ambiente em Ré menor (i–VI–III–VII), 72 bpm, com pulso discreto."""
    t = np.arange(int(dur * rate)) / rate
    acordes = [[146.83, 174.61, 220.0], [116.54, 146.83, 174.61], [174.61, 220.0, 261.63], [130.81, 164.81, 196.0]]
    seg = 60 / 72 * 4  # um compasso
    y = np.zeros_like(t)
    for i, a in enumerate(acordes * int(dur // (seg * 4) + 2)):
        ini = i * seg
        m = (t >= ini - 0.6) & (t < ini + seg + 0.6)
        if not m.any(): continue
        tt = t[m] - ini
        env = np.clip((tt + 0.6) / 0.9, 0, 1) * np.clip((seg + 0.6 - tt) / 0.9, 0, 1)
        for f in a:
            for det in (0.997, 1.003):
                y[m] += env * np.sin(2 * np.pi * f * det * t[m]) * 0.06
        y[m] += env * np.sin(2 * np.pi * a[0] / 2 * t[m]) * 0.08  # baixo
    beat = 60 / 72
    ph = (t % beat) / beat
    y += np.sin(2 * np.pi * 55 * t) * np.exp(-ph * 9) * 0.10  # pulso grave
    fade = np.clip(t / 1.5, 0, 1) * np.clip((dur - t) / 2.0, 0, 1)
    y *= fade
    y = y / (np.abs(y).max() + 1e-9) * 0.5
    with wave.open(str(out), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate)
        w.writeframes((y * 32767).astype(np.int16).tobytes())


def main():
    pasta = Path(sys.argv[1])
    tl = json.loads((pasta / "timeline.json").read_text())
    rot = json.loads((pasta / "roteiro.json").read_text())
    tl["kicker"] = rot.get("kicker", "Entenda em 1 minuto")
    from playwright.sync_api import sync_playwright
    if "--quadros" in sys.argv:
        ts = [float(x) for x in sys.argv[sys.argv.index("--quadros") + 1].split(",")]
        with sync_playwright() as p:
            b, pg = abrir(p, pasta, tl)
            for t in ts:
                pg.evaluate(f"window.seek({t})")
                pg.screenshot(path=str(pasta / f"_quadro_{t:05.1f}.jpg"), type="jpeg", quality=85)
            b.close()
        print("quadros ok"); return
    dur = tl["duracao"]
    n = int(np.ceil(dur * FPS))
    mudo = pasta / "_mudo.tmp.mp4"
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg",
                           "-i", "-", "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p",
                           "-r", str(FPS), str(mudo)], stdin=subprocess.PIPE)
    with sync_playwright() as p:
        b, pg = abrir(p, pasta, tl)
        for i in range(n):
            pg.evaluate(f"window.seek({i / FPS})")
            ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
            if i % 300 == 0: print(f"quadro {i}/{n}", flush=True)
        b.close()
    ff.stdin.close()
    assert ff.wait() == 0, "ffmpeg (vídeo) falhou"
    with wave.open(str(pasta / "narracao.wav")) as w:
        rate = w.getframerate()
    trilha(dur, rate, pasta / "_trilha.wav")
    final_tmp = pasta / "_reels.tmp.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(mudo), "-i", str(pasta / "narracao.wav"),
                    "-i", str(pasta / "_trilha.wav"), "-filter_complex",
                    "[1:a]highpass=f=70,acompressor=threshold=-18dB:ratio=3:attack=5:release=120,volume=1.6[v];"
                    "[2:a]volume=0.16[m];[v][m]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95,"
                    "aresample=48000[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ac", "2",
                    "-movflags", "+faststart", "-shortest", str(final_tmp)], check=True)
    final_tmp.rename(pasta / "reels.mp4")
    mudo.unlink(); (pasta / "_trilha.wav").unlink()
    print(pasta / "reels.mp4")


if __name__ == "__main__":
    main()
