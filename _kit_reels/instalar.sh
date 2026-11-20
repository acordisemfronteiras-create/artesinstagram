#!/usr/bin/env bash
# Prepara a máquina para fazer Reels. A nuvem é apagada entre as rodadas, então rode no começo de cada uma.
#
#   bash _kit_reels/instalar.sh          # motor (voz, alinhamento, render) + yt-dlp + auto-editor  (~1 min)
#   bash _kit_reels/instalar.sh --ia     # + ambiente ~/ia: DeepFilterNet, Chatterbox, rembg, Real-ESRGAN, demucs  (~3 min, ~6 GB)
#   bash _kit_reels/instalar.sh --hf     # + CLI da HyperFrames (conferência: bash _kit_reels/conferir_hf.sh)
#   bash _kit_reels/instalar.sh --ref    # + clona as skills de referência (remotion-dev/skills, heygen-com/hyperframes) em ~/ref
# As opções se somam (ex.: --ia --hf). O que cada ferramenta faz e quando usar: _kit_reels/ferramentas.md
set -uo pipefail
PIP="pip install -q --break-system-packages"
echo "== motor =="
$PIP piper-tts kokoro-onnx soundfile faster-whisper playwright numpy pillow num2words yt-dlp auto-editor uv 2>&1 | grep -v -i "warning" | tail -2
python3 -c "import kokoro_onnx, faster_whisper, playwright, num2words; print('motor ok')"

for op in "$@"; do case "$op" in
--ia)
  echo "== ambiente ~/ia (separado: fixa torch 2.6 e numpy 1.26, que quebrariam o motor) =="
  [ -x ~/ia/bin/python ] || uv venv -q -p python3.11 ~/ia
  VIRTUAL_ENV=~/ia uv pip install -q chatterbox-tts deepfilternet demucs "rembg[cpu,cli]" filetype spandrel "setuptools<81"
  mkdir -p ~/.cache/DeepFilterNet ~/ia/pesos
  if [ ! -d ~/.cache/DeepFilterNet/DeepFilterNet3 ]; then   # o download automático do DeepFilterNet é barrado; o arquivo cru passa
    curl -sSL -o /tmp/DeepFilterNet3.zip https://raw.githubusercontent.com/Rikorose/DeepFilterNet/main/models/DeepFilterNet3.zip \
      && unzip -oq /tmp/DeepFilterNet3.zip -d ~/.cache/DeepFilterNet/ && rm -f /tmp/DeepFilterNet3.zip
  fi
  [ -s ~/ia/pesos/RealESRGAN_x4plus.pth ] || curl -sSL -o ~/ia/pesos/RealESRGAN_x4plus.pth \
      https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth
  ~/ia/bin/python -c "import df, rembg, spandrel, demucs; from chatterbox.mtl_tts import ChatterboxMultilingualTTS; print('ia ok')" 2>&1 | tail -1
  ls ~/.cache/DeepFilterNet/DeepFilterNet3 >/dev/null 2>&1 && echo "DeepFilterNet3 ok"
  echo "aviso: demucs instalado, mas os pesos vêm de dl.fbaipublicfiles.com, que a rede desta sessão não libera" ;;
--hf)
  echo "== HyperFrames CLI =="
  HYPERFRAMES_NO_TELEMETRY=1 npx -y hyperframes@0.9.72 --version ;;
--ref)
  echo "== skills de referência em ~/ref =="
  mkdir -p ~/ref
  for r in remotion-dev/skills heygen-com/hyperframes; do
    d=~/ref/$(echo $r | tr / _); [ -d "$d" ] || git clone -q --depth 1 https://github.com/$r.git "$d"; echo "$d"
  done ;;
esac; done
