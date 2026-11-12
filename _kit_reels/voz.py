"""Gera a narração (voz fixa pt_BR-faber-medium, Piper) e a linha do tempo de um Reels.

Uso:
    python3 _kit_reels/voz.py PASTA_DO_REELS

Lê PASTA/roteiro.json, gera PASTA/narracao.wav e PASTA/timeline.json
(início/fim de cada cena e de cada legenda, em segundos).
A voz é baixada uma vez para ~/voices (Hugging Face, rhasspy/piper-voices).
"""
import json, subprocess, sys, wave
from pathlib import Path

VOZ = "pt_BR-faber-medium"          # voz masculina brasileira: sempre a mesma
LENGTH_SCALE = "0.9"               # ritmo levemente mais ágil que o padrão
BASE = "https://huggingface.co/rhasspy/piper-voices/resolve/main/pt/pt_BR/faber/medium/"
GAP_FALA, GAP_CENA, INTRO, OUTRO = 0.28, 0.55, 0.6, 1.6


def garantir_voz():
    d = Path.home() / "voices"; d.mkdir(exist_ok=True)
    for f in (f"{VOZ}.onnx", f"{VOZ}.onnx.json"):
        p = d / f
        if not p.exists() or p.stat().st_size == 0:
            subprocess.run(["curl", "-sSL", "-o", str(p), BASE + f], check=True)
    return d / f"{VOZ}.onnx"


def main(pasta):
    pasta = Path(pasta)
    rot = json.loads((pasta / "roteiro.json").read_text())
    modelo = garantir_voz()
    tmp = pasta / "_tts"; tmp.mkdir(exist_ok=True)
    rate = None
    frames = bytearray()
    t = 0.0
    def silencio(seg):
        nonlocal t
        frames.extend(b"\x00\x00" * int(rate * seg)); t += seg
    timeline = {"cenas": [], "legendas": []}
    k = 0
    for ci, cena in enumerate(rot["cenas"]):
        for fi, f in enumerate(cena["falas"]):
            wav = tmp / f"{k:02d}.wav"; k += 1
            subprocess.run([sys.executable, "-m", "piper", "-m", str(modelo), "--length-scale", LENGTH_SCALE,
                            "-f", str(wav)], input=f["fala"].encode(), check=True, capture_output=True)
            with wave.open(str(wav)) as w:
                if rate is None:
                    rate = w.getframerate(); silencio(INTRO)
                data = w.readframes(w.getnframes())
            if fi == 0:
                cena_ini = max(0.0, t - (INTRO if ci == 0 else GAP_CENA / 2))
            ini = t
            frames.extend(data); t += len(data) / 2 / rate
            timeline["legendas"].append({"cena": cena["id"], "ini": round(ini, 3), "fim": round(t, 3), "texto": f["legenda"]})
            if fi < len(cena["falas"]) - 1:
                silencio(GAP_FALA)
        silencio(GAP_CENA if ci < len(rot["cenas"]) - 1 else OUTRO)
        fim = t - (GAP_CENA / 2 if ci < len(rot["cenas"]) - 1 else 0)
        timeline["cenas"].append({"id": cena["id"], "ini": round(0 if ci == 0 else cena_ini, 3), "fim": round(fim, 3)})
    # cenas contíguas
    for a, b in zip(timeline["cenas"], timeline["cenas"][1:]):
        b["ini"] = a["fim"]
    timeline["duracao"] = round(t, 3)
    with wave.open(str(pasta / "narracao.wav"), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate); w.writeframes(bytes(frames))
    (pasta / "timeline.json").write_text(json.dumps(timeline, ensure_ascii=False, indent=1))
    for p in tmp.iterdir(): p.unlink()
    tmp.rmdir()
    print(f"duração {t:.1f}s, {len(timeline['cenas'])} cenas")


if __name__ == "__main__":
    main(sys.argv[1])
