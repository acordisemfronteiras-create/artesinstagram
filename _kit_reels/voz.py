"""Gera a narração e a linha do tempo de um Reels.

Uso:
    python3 _kit_reels/voz.py PASTA_DO_REELS [--alinhar]

Lê PASTA/roteiro.json e gera PASTA/narracao.wav + PASTA/timeline.json com:
  cenas     início/fim de cada cena
  legendas  início/fim de cada fala (texto da tela)
  cues      instante de cada {deixa} marcada dentro das falas (para sincronizar visual e som com a palavra)
  duracao

roteiro.json:
  "voz": {"motor": "kokoro", "nome": "pm_alex", "velocidade": 1.1}    (padrão do estilo v2)
         {"motor": "piper"}                                            (voz do piloto de 12/11: pt_BR-faber-medium)
  "ritmo": {"pausa_fala": 0.16, "pausa_cena": 0.35, "intro": 0.45, "final": 2.6}   (opcional)
  "cenas": [{"id": "...", "falas": [{"fala": "Esse quadradinho {voce} é você.", "legenda": "Esse quadradinho é você."}]}]

Em "fala", números por extenso. {nome} marca uma deixa no início da palavra seguinte.
--alinhar refina as deixas com reconhecimento de fala (faster-whisper, se instalado); sem ele, a deixa é
estimada pela posição proporcional na frase (erro típico < 0,2 s em frases curtas).
As vozes são baixadas uma vez para ~/voices.
"""
import json, re, subprocess, sys, wave
from pathlib import Path
import numpy as np

VOICES = Path.home() / "voices"
PIPER = "pt_BR-faber-medium"
PIPER_URL = "https://huggingface.co/rhasspy/piper-voices/resolve/main/pt/pt_BR/faber/medium/"
KOKORO_URL = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
RITMO = {"pausa_fala": 0.16, "pausa_cena": 0.35, "intro": 0.45, "final": 2.6}
RITMO_PIPER = {"pausa_fala": 0.28, "pausa_cena": 0.55, "intro": 0.6, "final": 1.6}
SR = 24000


def baixar(url, destino):
    if not destino.exists() or destino.stat().st_size == 0:
        destino.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["curl", "-sSL", "--fail", "-o", str(destino), url], check=True)
    return destino


class Kokoro:
    def __init__(self, nome, velocidade):
        from kokoro_onnx import Kokoro as K
        d = VOICES / "kokoro"
        self.k = K(str(baixar(KOKORO_URL + "kokoro-v1.0.onnx", d / "kokoro-v1.0.onnx")),
                   str(baixar(KOKORO_URL + "voices-v1.0.bin", d / "voices-v1.0.bin")))
        self.nome, self.vel = nome, velocidade

    def falar(self, texto):
        a, sr = self.k.create(texto, voice=self.nome, speed=self.vel, lang="pt-br")
        return reamostrar(np.asarray(a, dtype=np.float32), sr)


class Piper:
    def __init__(self, escala="0.9"):
        self.modelo = baixar(PIPER_URL + PIPER + ".onnx", VOICES / (PIPER + ".onnx"))
        baixar(PIPER_URL + PIPER + ".onnx.json", VOICES / (PIPER + ".onnx.json"))
        self.escala = escala

    def falar(self, texto):
        tmp = VOICES / "_tmp.wav"
        subprocess.run([sys.executable, "-m", "piper", "-m", str(self.modelo), "--length-scale", self.escala,
                        "-f", str(tmp)], input=texto.encode(), check=True, capture_output=True)
        with wave.open(str(tmp)) as w:
            a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
            sr = w.getframerate()
        tmp.unlink()
        return reamostrar(a, sr)


def reamostrar(a, sr):
    if sr == SR:
        return a
    n = int(len(a) * SR / sr)
    return np.interp(np.linspace(0, len(a) - 1, n), np.arange(len(a)), a).astype(np.float32)


def aparar(a, limiar=0.012, margem=0.03):
    """Tira o silêncio do começo e do fim (as pausas são controladas pelo ritmo)."""
    idx = np.where(np.abs(a) > limiar)[0]
    if len(idx) == 0:
        return a
    m = int(margem * SR)
    return a[max(0, idx[0] - m): min(len(a), idx[-1] + m)]


def separar_deixas(fala):
    """'Esse quadradinho {voce} é você.' -> ('Esse quadradinho é você.', [('voce', fração_de_letras)])"""
    limpo, deixas, pos = "", [], 0
    for parte in re.split(r"(\{\w+\})", fala):
        if re.fullmatch(r"\{\w+\}", parte):
            deixas.append((parte[1:-1], len(re.sub(r"\W", "", limpo))))
        else:
            limpo += parte
    limpo = re.sub(r"\s+", " ", limpo).strip()
    limpo = re.sub(r"\s+([,.;:!?])", r"\1", limpo)
    total = max(1, len(re.sub(r"\W", "", limpo)))
    return limpo, [(n, c / total) for n, c in deixas]


def alinhador():
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("aviso: faster-whisper não instalado; deixas estimadas por proporção")
        return None
    m = WhisperModel("small", device="cpu", compute_type="int8")

    def alinhar(audio, frac):
        a16 = np.interp(np.linspace(0, len(audio) - 1, int(len(audio) * 16000 / SR)), np.arange(len(audio)), audio)
        segs, _ = m.transcribe(a16.astype(np.float32), language="pt", word_timestamps=True)
        ws = [w for s in segs for w in s.words]
        if not ws:
            return None
        letras = np.cumsum([0] + [len(re.sub(r"\W", "", w.word)) for w in ws])
        alvo = frac * letras[-1]
        i = int(np.argmin(np.abs(letras[:-1] - alvo)))   # palavra cujo início está mais perto da fração
        return float(ws[i].start)
    return alinhar


def main(pasta, alinhar=False):
    pasta = Path(pasta)
    rot = json.loads((pasta / "roteiro.json").read_text())
    cfg = rot.get("voz", {"motor": "piper"})
    if cfg.get("motor", "kokoro") == "kokoro":
        voz = Kokoro(cfg.get("nome", "pm_alex"), cfg.get("velocidade", 1.1)); ritmo = dict(RITMO)
    else:
        voz = Piper(); ritmo = dict(RITMO_PIPER)
    ritmo.update(rot.get("ritmo", {}))
    al = alinhador() if alinhar else None

    partes, t = [], 0.0
    def silencio(seg):
        nonlocal t
        partes.append(np.zeros(int(SR * seg), dtype=np.float32)); t += seg
    tl = {"cenas": [], "legendas": [], "cues": {}}
    n_cenas = len(rot["cenas"])
    silencio(ritmo["intro"])
    for ci, cena in enumerate(rot["cenas"]):
        cena_ini = 0.0 if ci == 0 else t - ritmo["pausa_cena"] / 2
        for fi, f in enumerate(cena["falas"]):
            texto, deixas = separar_deixas(f["fala"])
            a = aparar(voz.falar(texto))
            dur = len(a) / SR
            for nome, frac in deixas:
                if nome in tl["cues"]:
                    raise SystemExit(f"deixa repetida: {nome}")
                rel = frac * dur
                if al and 0 < frac < 1:
                    r = al(a, frac)
                    if r is not None and abs(r - rel) < 1.2:
                        rel = r
                tl["cues"][nome] = round(t + rel, 3)
            tl["legendas"].append({"cena": cena["id"], "ini": round(t, 3), "fim": round(t + dur, 3),
                                   "texto": f.get("legenda", texto)})
            partes.append(a); t += dur
            if fi < len(cena["falas"]) - 1:
                silencio(f.get("pausa", ritmo["pausa_fala"]))
        silencio(ritmo["pausa_cena"] if ci < n_cenas - 1 else ritmo["final"])
        fim = t - (ritmo["pausa_cena"] / 2 if ci < n_cenas - 1 else 0)
        tl["cenas"].append({"id": cena["id"], "ini": round(cena_ini, 3), "fim": round(fim, 3)})
    tl["duracao"] = round(t, 3)
    audio = np.concatenate(partes)
    audio = audio / (np.abs(audio).max() + 1e-9) * 0.9
    with wave.open(str(pasta / "narracao.wav"), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((audio * 32767).astype(np.int16).tobytes())
    (pasta / "timeline.json").write_text(json.dumps(tl, ensure_ascii=False, indent=1))
    palavras = sum(len(separar_deixas(f["fala"])[0].split()) for c in rot["cenas"] for f in c["falas"])
    print(f"duração {t:.1f}s · {palavras} palavras · {len(tl['cenas'])} cenas · {len(tl['cues'])} deixas")


if __name__ == "__main__":
    main(sys.argv[1], "--alinhar" in sys.argv)
