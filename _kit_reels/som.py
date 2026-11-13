"""Som dos Reels: trilha de fundo e efeitos sonoros, tudo sintetizado aqui (sem direitos autorais).

Efeitos (campo "sfx" do roteiro.json): [{"em": "@deixa-0.15" | "12.4", "tipo": "whoosh", "ganho": 1.0}, ...]
  riser     subida de tensão (1,2 s) que termina no instante "em"  -> abertura, antes de um número forte
  impacto   batida grave                                           -> número grande entra, revelação
  whoosh    passagem de ar                                         -> movimento de câmera, troca de bloco
  pop       estalo curto e agudo                                   -> elemento aparece, contador termina
  tique     clique seco                                            -> detalhe pequeno
  contagem  sequência de tiques acelerando (0,9 s)                 -> contador subindo
  varredura tiques densos com filtro subindo (1,1 s)               -> onda de quadradinhos mudando de cor
  brilho    arpejo agudo com cauda                                 -> destaque positivo, conclusão
  bip       bipe limpo                                             -> "presta atenção"
"""
import numpy as np

SR = 48000
rng = np.random.default_rng(7)


def _t(d):
    return np.arange(int(SR * d)) / SR


def _ruido(n):
    return rng.standard_normal(n)


def _passa_faixa(x, f0, f1, q=2.0):
    """Filtro de estado variável com frequência de corte variando de f0 a f1 ao longo do som."""
    n = len(x); f = np.geomspace(f0, f1, n)
    lo = bd = 0.0; y = np.empty(n)
    for i in range(n):
        k = 2 * np.sin(np.pi * min(f[i], SR / 6.5) / SR)
        hi = x[i] - lo - bd / q
        bd += k * hi; lo += k * bd
        y[i] = bd
    return y


def whoosh(d=0.55):
    t = _t(d); env = np.sin(np.pi * t / d) ** 2
    return _passa_faixa(_ruido(len(t)), 300, 3800, 1.4) * env * 0.5


def riser(d=1.2):
    t = _t(d); env = (t / d) ** 2.2
    r = _passa_faixa(_ruido(len(t)), 250, 7000, 2.5) * 0.35
    f = np.geomspace(180, 900, len(t)); s = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.18
    return (r + s) * env


def impacto(d=0.8):
    t = _t(d); f = 38 + 70 * np.exp(-t * 22)
    corpo = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 5.5)
    estalo = _ruido(len(t)) * np.exp(-t * 90) * 0.25
    return (corpo + estalo) * 0.9


def pop(d=0.14, f0=620):
    t = _t(d); f = f0 * (1 + 0.6 * np.exp(-t * 45))
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 34) * 0.55


def tique(d=0.04):
    t = _t(d)
    return (np.sin(2 * np.pi * 2400 * t) + 0.5 * _ruido(len(t))) * np.exp(-t * 160) * 0.3


def contagem(d=0.9, n=14):
    y = np.zeros(int(SR * d) + int(SR * 0.05)); k = tique()
    for p in (np.linspace(0, 1, n) ** 0.7) * d:
        i = int(p * SR); y[i:i + len(k)] += k * 0.8
    return y


def varredura(d=1.1, n=34):
    y = np.zeros(int(SR * d) + int(SR * 0.06))
    for j, p in enumerate(np.linspace(0, 1, n) * d):
        k = pop(0.05, 500 + 30 * j) * 0.35
        i = int(p * SR); y[i:i + len(k)] += k
    return y


def brilho(d=1.3):
    t = _t(d); y = np.zeros(len(t))
    for j, f in enumerate([1174.66, 1396.91, 1760.0, 2349.32]):   # ré menor, agudo
        a = int(j * 0.07 * SR); tt = t[: len(t) - a]
        y[a:] += np.sin(2 * np.pi * f * tt) * np.exp(-tt * 4.2) * 0.16
    return y


def bip(d=0.16):
    t = _t(d); env = np.minimum(1, t / 0.008) * np.minimum(1, (d - t) / 0.03)
    return np.sin(2 * np.pi * 1318.5 * t) * env * 0.3


EFEITOS = {"whoosh": whoosh, "riser": riser, "impacto": impacto, "pop": pop, "tique": tique,
           "contagem": contagem, "varredura": varredura, "brilho": brilho, "bip": bip}
TERMINA_NO_INSTANTE = {"riser"}          # o som acaba em "em" (os outros começam em "em")
CENTRA_NO_INSTANTE = {"whoosh"}          # o meio do som fica em "em"


def instante(em, tl):
    """"@deixa", "@deixa+0.3", "@deixa-0.2" ou segundos ("12.4")."""
    import re
    m = re.fullmatch(r"@(\w+)([+-][\d.]+)?", str(em))
    if m:
        if m.group(1) not in tl["cues"]:
            raise SystemExit(f"sfx: deixa inexistente: {m.group(1)}")
        return tl["cues"][m.group(1)] + float(m.group(2) or 0)
    return float(em)


def faixa_sfx(lista, tl):
    y = np.zeros(int(SR * (tl["duracao"] + 1)))
    for e in lista:
        s = EFEITOS[e["tipo"]]() * e.get("ganho", 1.0)
        t0 = instante(e["em"], tl)
        if e["tipo"] in TERMINA_NO_INSTANTE: t0 -= len(s) / SR
        if e["tipo"] in CENTRA_NO_INSTANTE: t0 -= len(s) / SR / 2
        i = max(0, int(t0 * SR)); s = s[: max(0, len(y) - i)]
        y[i:i + len(s)] += s
    return y[: int(SR * tl["duracao"])]


def trilha(dur, bpm=84):
    """Pad em ré menor (i–VI–III–VII) com pulso e arpejo discretos; entra e sai em fade."""
    t = _t(dur); y = np.zeros(len(t))
    acordes = [[146.83, 174.61, 220.0], [116.54, 146.83, 174.61], [174.61, 220.0, 261.63], [130.81, 164.81, 196.0]]
    tempo = 60 / bpm; comp = tempo * 4
    for i in range(int(dur / comp) + 2):
        a = acordes[i % 4]; ini = i * comp
        m = (t >= ini - 0.5) & (t < ini + comp + 0.5)
        if not m.any(): continue
        tt = t[m] - ini
        env = np.clip((tt + 0.5) / 0.8, 0, 1) * np.clip((comp + 0.5 - tt) / 0.8, 0, 1)
        for f in a:
            for det in (0.997, 1.003):
                y[m] += env * np.sin(2 * np.pi * f * det * t[m]) * 0.055
        y[m] += env * np.sin(2 * np.pi * a[0] / 2 * t[m]) * 0.08
        for j in range(8):                                   # arpejo em colcheias
            n0 = ini + j * tempo / 2; f = a[j % 3] * 2
            mm = (t >= n0) & (t < n0 + 0.35)
            y[mm] += np.sin(2 * np.pi * f * (t[mm] - n0)) * np.exp(-(t[mm] - n0) * 11) * 0.035
    fase = (t % tempo) / tempo
    y += np.sin(2 * np.pi * 52 * t) * np.exp(-fase * 10) * 0.11
    y *= np.clip(t / 1.2, 0, 1) * np.clip((dur - t) / 1.8, 0, 1)
    return y / (np.abs(y).max() + 1e-9) * 0.5


def salvar(y, caminho):
    import wave
    y = np.clip(y, -1, 1)
    with wave.open(str(caminho), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((y * 32767).astype(np.int16).tobytes())
