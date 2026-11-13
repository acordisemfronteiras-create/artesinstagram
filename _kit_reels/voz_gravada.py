"""Usa a voz gravada pelo Tiago no lugar da voz sintética.

Uso:
    python3 _kit_reels/voz_gravada.py PASTA gravacao.m4a [--cortar 35.95-39.95,...] [--pausa-max 0.42] [--so-alinhar]

1. Edita: tira o silêncio do começo, corta os trechos de --cortar (segundos do arquivo original, para tirar
   regravações e tropeços) e encurta as pausas longas para --pausa-max (as curtas ficam como estão).
2. Limpa: passa-alta, redução de ruído leve, de-esser, equalização de presença, compressão e volume padrão.
3. Alinha: transcreve com faster-whisper (tempo por palavra), casa as palavras com as legendas do roteiro.json
   e grava PASTA/narracao.wav + PASTA/timeline.json no mesmo formato do voz.py. Assim a página e os efeitos
   (que usam L1, L2... e @deixas) acompanham a fala dele sem mexer em nada.
Confira a lista de deixas que o script imprime: deixa fora do lugar aparece como animação adiantada ou atrasada.
--so-alinhar pula a edição e a limpeza (usa PASTA/narracao.wav como está).
"""
import difflib, json, re, subprocess, sys, unicodedata
from pathlib import Path
import numpy as np
import soundfile as sf

SR = 24000
FINAL = 2.8   # segundos de silêncio no fim (cartão final)
LIMPEZA = ("highpass=f=75,lowpass=f=14000,afftdn=nr=10:nf=-45,deesser=i=0.4,"
           "equalizer=f=200:t=q:w=1:g=-1.5,equalizer=f=3500:t=q:w=1.2:g=2,"
           "acompressor=threshold=-20dB:ratio=2.5:attack=8:release=150:makeup=2,loudnorm=I=-16:TP=-1.5:LRA=7")


def norm(w):
    w = unicodedata.normalize("NFD", w.lower())
    w = "".join(c for c in w if unicodedata.category(c) != "Mn")
    return re.sub(r"[^\w,%]", "", w).strip(",")


NUM = set("zero um uma dois duas tres quatro cinco seis sete oito nove dez onze doze treze quatorze catorze quinze "
          "dezesseis dezessete dezoito dezenove vinte trinta quarenta cinquenta sessenta setenta oitenta noventa cem "
          "cento duzentos trezentos quatrocentos quinhentos seiscentos setecentos oitocentos novecentos mil milhao "
          "milhoes bilhao bilhoes virgula meio".split())


def agrupa_numeros(ws):
    """Junta um número por extenso ("cento e setenta e dois", "dois e meio por cento") num só token "#",
    e troca por "#" todo token com algarismo ("172", "2,5%"), para casar fala por extenso com legenda."""
    out, i = [], 0
    while i < len(ws):
        w = ws[i]
        if any(ch.isdigit() for ch in w):
            out.append("#"); i += 1; continue
        if w in NUM:
            j = i + 1
            liga = {"e", "virgula", "mil", "milhao", "milhoes", "bilhao", "bilhoes", "cem", "cento", "duzentos",
                    "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"}
            while j < len(ws) and ((ws[j] in NUM and (ws[j - 1] in liga or ws[j] in {"mil", "milhao", "milhoes",
                                    "bilhao", "bilhoes", "virgula"})) or (ws[j] == "e" and j + 1 < len(ws) and ws[j + 1] in NUM)
                                   or (ws[j] == "por" and j + 1 < len(ws) and ws[j + 1] == "cento") or
                                   (ws[j] == "cento" and ws[j - 1] == "por")):
                j += 1
            out.append(("#", i, j)); i = j; continue
        out.append(w); i += 1
    return out


def editar(orig, cortes, pausa_max, sr):
    h = int(0.01 * sr); n = len(orig) // h
    db = np.array([20 * np.log10(np.sqrt(np.mean(orig[i * h:(i + 1) * h] ** 2)) + 1e-9) for i in range(n)])
    voz = db > -50
    i = 0
    while i < n:                                  # fecha buracos curtos (< 120 ms) dentro das palavras
        if not voz[i]:
            j = i
            while j < n and not voz[j]: j += 1
            if 0 < i and j < n and j - i < 12: voz[i:j] = True
            i = j
        else: i += 1
    blocos, i = [], 0
    while i < n:
        if voz[i]:
            j = i
            while j < n and voz[j]: j += 1
            blocos.append((i * .01, j * .01)); i = j
        else: i += 1
    blocos = [b for b in blocos if not any(b[0] < c1 and b[1] > c0 for c0, c1 in cortes)]
    M, out, fim_ant = 0.04, [np.zeros(int(0.35 * sr))], None
    for s, e in blocos:
        s0, e0 = max(0, s - M), min(len(orig) / sr, e + M)
        if fim_ant is not None:
            gap = s0 - fim_ant
            if gap > pausa_max: out.append(np.zeros(int(pausa_max * sr)))
            elif gap > 0: out.append(orig[int(fim_ant * sr):int(s0 * sr)])
            else: s0 = fim_ant
        seg = orig[int(s0 * sr):int(e0 * sr)].copy()
        f = min(int(0.008 * sr), len(seg) // 2)
        seg[:f] *= np.linspace(0, 1, f); seg[-f:] *= np.linspace(1, 0, f)
        out.append(seg); fim_ant = e0
    return np.concatenate(out)


def transcrever(a, sr, dica):
    from faster_whisper import WhisperModel
    a16 = np.interp(np.linspace(0, len(a) - 1, int(len(a) * 16000 / sr)), np.arange(len(a)), a).astype(np.float32)
    m = WhisperModel("small", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(a16, language="pt", word_timestamps=True, initial_prompt=dica)
    ws = []
    for s in segs:
        for w in s.words:
            t = norm(w.word)
            if t in ("r", "", "$"): continue
            if ws and (w.word.strip().startswith((",", "%")) or (t.startswith(",") and ws[-1][0][-1:].isdigit())):
                ws[-1] = (ws[-1][0] + t, ws[-1][1], w.end); continue     # "5" ",65" -> "5,65"
            ws.append((t, w.start, w.end))
    return ws


def onsets(a, sr):
    h = int(0.01 * sr)
    db = np.array([20 * np.log10(np.sqrt(np.mean(a[i * h:(i + 1) * h] ** 2)) + 1e-9) for i in range(len(a) // h)])
    return db > -45


def main():
    pasta = Path(sys.argv[1]); arq = sys.argv[2]
    arg = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
    cortes = [tuple(map(float, c.split("-"))) for c in arg("--cortar", "").split(",") if c]
    rot = json.loads((pasta / "roteiro.json").read_text())
    if "--so-alinhar" not in sys.argv:
        tmp = pasta / "_orig.wav"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", arq, "-ac", "1", "-ar", "48000", str(tmp)], check=True)
        orig, sr = sf.read(tmp)
        sf.write(pasta / "_editado.wav", editar(orig, cortes, float(arg("--pausa-max", 0.42)), sr), sr)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(pasta / "_editado.wav"), "-af", LIMPEZA,
                        "-ar", str(SR), "-ac", "1", str(pasta / "narracao.wav")], check=True)
        tmp.unlink(); (pasta / "_editado.wav").unlink()
    a, sr = sf.read(pasta / "narracao.wav")
    falas = [(c["id"], f) for c in rot["cenas"] for f in c["falas"]]
    dica = " ".join(f.get("legenda", "") for _, f in falas)[:400]
    ws = transcrever(a, sr, dica)

    # tokens das legendas, com a fala de origem
    leg = []
    for k, (_, f) in enumerate(falas):
        for w in f["legenda"].split():
            t = norm(w)
            if t and t != "r": leg.append((t, k))
    sm = difflib.SequenceMatcher(None, [t for t, _ in leg], [t for t, _, _ in ws], autojunk=False)
    mapa = {}
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            for d in range(i2 - i1): mapa[i1 + d] = j1 + d
        elif op == "replace":
            for d in range(i2 - i1): mapa[i1 + d] = min(j2 - 1, j1 + round(d * (j2 - j1) / (i2 - i1)))
    vivo = onsets(a, sr)

    def ajusta_ini(t):    # encosta no começo real da voz (até 0,35 s antes ou depois)
        i = int(t * 100)
        for d in range(0, 36):
            for k in (i - d, i + d):
                if 0 < k < len(vivo) and vivo[k] and not vivo[k - 1]: return k / 100
        return t

    tl = {"cenas": [], "legendas": [], "cues": {}}
    for k, (cid, f) in enumerate(falas):
        idx = [i for i, (_, kk) in enumerate(leg) if kk == k]
        js = [mapa[i] for i in idx if i in mapa]
        if not js: raise SystemExit(f"fala sem correspondência no áudio: {f['legenda']}")
        ini, fim = ajusta_ini(ws[min(js)][1]), ws[max(js)][2]
        tl["legendas"].append({"cena": cid, "ini": round(ini, 3), "fim": round(fim, 3), "texto": f["legenda"]})
        # deixas: posição da palavra na fala (por extenso) -> token da legenda -> palavra no áudio
        partes = re.split(r"(\{\w+\})", f["fala"])
        fw, deixas = [], []
        for p in partes:
            if re.fullmatch(r"\{\w+\}", p): deixas.append((p[1:-1], len(fw)))
            else: fw += [norm(x) for x in p.split() if norm(x)]
        grupos = agrupa_numeros(fw)            # cada item: palavra ou ("#", ini, fim) em fw
        pos_g = []                             # posição em fw -> posição em grupos
        for gi_, g in enumerate(grupos):
            n_ = (g[2] - g[1]) if isinstance(g, tuple) else 1
            pos_g += [gi_] * n_
        fg = [g[0] if isinstance(g, tuple) else g for g in grupos]
        lt = ["#" if any(ch.isdigit() for ch in leg[i][0]) else leg[i][0] for i in idx]
        sm2 = difflib.SequenceMatcher(None, fg, lt, autojunk=False)
        for nome, pos in deixas:
            pg = pos_g[pos] if pos < len(pos_g) else len(fg) - 1
            jl = len(lt) - 1
            for op, i1, i2, j1, j2 in sm2.get_opcodes():
                if i1 <= pg < max(i2, i1 + 1):
                    jl = j1 + (pg - i1 if op == "equal" else round((pg - i1) * (j2 - j1) / max(1, i2 - i1)))
                    break
            jl = max(0, min(len(lt) - 1, jl))
            gi = idx[jl]
            t = ws[mapa[gi]][1] if (gi in mapa and jl > 0) else ini
            tl["cues"][nome] = round(float(max(ini, t)), 3)
    ids = [c["id"] for c in rot["cenas"]]
    dur = round(tl["legendas"][-1]["fim"] + FINAL, 3)
    for n, cid in enumerate(ids):
        ls = [l for l in tl["legendas"] if l["cena"] == cid]
        if n == 0: c0 = 0.0
        else:
            ant = [l for l in tl["legendas"] if l["cena"] == ids[n - 1]][-1]
            c0 = round((ant["fim"] + ls[0]["ini"]) / 2, 3)
        tl["cenas"].append({"id": cid, "ini": c0, "fim": None})
    for n, c in enumerate(tl["cenas"]):
        c["fim"] = tl["cenas"][n + 1]["ini"] if n + 1 < len(tl["cenas"]) else dur
    tl["duracao"] = dur
    a = np.concatenate([a, np.zeros(int((dur - len(a) / sr) * sr) + 1)])[: int(dur * sr)]
    sf.write(pasta / "narracao.wav", a.astype(np.float32), sr, subtype="PCM_16")
    (pasta / "timeline.json").write_text(json.dumps(tl, ensure_ascii=False, indent=1))
    print("transcrição:", " ".join(t for t, _, _ in ws))
    for l in tl["legendas"]: print(f"{l['ini']:6.2f}-{l['fim']:6.2f}  {l['texto']}")
    print("deixas:", tl["cues"]); print(f"duração {dur:.1f}s")


if __name__ == "__main__":
    main()
