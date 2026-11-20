"""Trabalhador da voz Chatterbox (resemble-ai/chatterbox, modelo multilíngue, roda local na CPU).

Roda no ambiente separado ~/ia (criado por `bash _kit_reels/instalar.sh --ia`), porque o Chatterbox fixa versões de
torch e numpy que quebrariam o motor principal. O voz.py abre este processo uma vez e manda uma fala por linha:
    {"texto": "...", "saida": "/caminho.wav"}  ->  responde "ok" (ou "erro: ...")
Configuração no roteiro.json:
    "voz": {"motor": "chatterbox", "referencia": "caminho/para/amostra.wav", "exagero": 0.5, "cfg": 0.5}
"referencia" clona o timbre de uma gravação (10 a 20 s de fala limpa). Só use a voz de quem autorizou por escrito,
e, se for a voz do Tiago clonada, o post vai com "aiGenerated": true (voz realista feita por IA).
Velocidade na CPU: ~10x o tempo real (1 min de narração ≈ 10 min).
"""
import json, sys
import torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

cfg = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {}
m = ChatterboxMultilingualTTS.from_pretrained(device="cpu")
print("pronto", flush=True)
for linha in sys.stdin:
    try:
        p = json.loads(linha)
        kw = {"language_id": "pt", "exaggeration": cfg.get("exagero", 0.5), "cfg_weight": cfg.get("cfg", 0.5)}
        if cfg.get("referencia"):
            kw["audio_prompt_path"] = cfg["referencia"]
        wav = m.generate(p["texto"], **kw)
        ta.save(p["saida"], wav, m.sr)
        print("ok", flush=True)
    except Exception as e:
        print("erro:", str(e).replace("\n", " "), flush=True)
