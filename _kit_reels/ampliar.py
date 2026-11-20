"""Amplia uma imagem 4x com Real-ESRGAN (xinntao/Real-ESRGAN, modelo RealESRGAN_x4plus, via spandrel), na CPU.

Uso (precisa de `bash _kit_reels/instalar.sh --ia`):
    ~/ia/bin/python _kit_reels/ampliar.py entrada.png saida.png [--escala-final 0.5]
Para imagens pequenas ou borradas que vão entrar num Reels ou post (foto do Tiago enviada por WhatsApp, print de
gráfico oficial). Imagem grande demora: ~1 s por 100x100 px na CPU; corte antes o que vai aparecer.
--escala-final reduz o resultado (ex.: 0.5 = 2x no fim, mais nítido que ampliar 2x direto).
"""
import sys
from pathlib import Path
import numpy as np
import torch
from PIL import Image
from spandrel import ModelLoader

PESOS = Path.home() / "ia/pesos/RealESRGAN_x4plus.pth"
ent, sai = sys.argv[1], sys.argv[2]
fim = float(sys.argv[sys.argv.index("--escala-final") + 1]) if "--escala-final" in sys.argv else 1.0
m = ModelLoader().load_from_file(str(PESOS)).eval()
im = Image.open(ent)
alfa = im.getchannel("A") if im.mode == "RGBA" else None
x = torch.from_numpy(np.asarray(im.convert("RGB")).astype("float32") / 255).permute(2, 0, 1)[None]
with torch.no_grad():
    y = m(x)[0].permute(1, 2, 0).clamp(0, 1).numpy()
out = Image.fromarray((y * 255).round().astype("uint8"))
if alfa is not None:
    out.putalpha(alfa.resize(out.size, Image.LANCZOS))
if fim != 1.0:
    out = out.resize((round(out.width * fim), round(out.height * fim)), Image.LANCZOS)
out.save(sai)
print(f"{im.size} -> {out.size}: {sai}")
