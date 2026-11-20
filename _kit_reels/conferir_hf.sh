#!/usr/bin/env bash
# Confere um Reels com a CLI da HyperFrames (heygen-com/hyperframes), sem mudar o nosso motor.
#
# Uso (da raiz do repositório):
#   bash _kit_reels/conferir_hf.sh PASTA            # check da página (tempo de leitura, tamanho, contraste, zona segura)
#   bash _kit_reels/conferir_hf.sh PASTA snapshot   # quadros + folha de contato da página (--at 3,12,30 por padrão)
#   bash _kit_reels/conferir_hf.sh PASTA video      # mede o reels.mp4: som (LUFS, pico, cortes de som) e trechos parados
#
# A HyperFrames só aceita projeto dela; o adaptador copia a página para uma pasta temporária, injeta a linha do tempo
# e liga o evento hf-seek ao nosso window.seek(t). Tudo roda local, sem login. NÃO use share, publish, reverse,
# templates, cloud, auth, billing nem "audio --quality best": exigem conta ou mandam arquivos para fora.
set -euo pipefail
PASTA=${1:?informe a pasta do Reels}; MODO=${2:-check}
RAIZ=$(cd "$(dirname "$0")/.." && pwd); if [ -d "$RAIZ/$PASTA" ]; then PASTA="$RAIZ/$PASTA"; else PASTA=$(cd "$PASTA" && pwd); fi
export HYPERFRAMES_NO_TELEMETRY=1
HF="npx -y hyperframes@0.9.72"

if [ "$MODO" = "video" ]; then
  V="$PASTA/reels.mp4"; [ -f "$V" ] || { echo "sem reels.mp4 em $PASTA"; exit 1; }
  T=$(mktemp -d); cp "$V" "$T/"; cd "$T"
  echo "== som (alvo: -16 a -14 LUFS, pico real <= -1 dBTP) =="
  $HF audio reels.mp4 --json 2>/dev/null | python3 -c "
import json,sys; it=json.load(sys.stdin)['items'][0]; l=it['loudness']
print(f\"{l['lufsIntegrated']} LUFS integrado · pico real {l['truePeakDb']} dBTP · duração {it['duration']:.1f} s\")
for w in it.get('warnings') or []: print('aviso:', w)" || true
  echo "== trechos parados (acima de 3 s merecem revisão) =="
  $HF measure events reels.mp4 --json 2>/dev/null | python3 -c "
import json,sys; d=json.load(sys.stdin)
hs=[e for e in d['events'] if e.get('type')=='hold' and e.get('seconds',0)>=2.5]
for e in sorted(hs,key=lambda e:-e['seconds'])[:8]: print(f\"{e['t']:6.2f}s  {e['seconds']:.2f}s sem mudança visível\")
print(d['holds'].get('count'),'trechos parados no total; o maior tem',d['holds'].get('longest_s'),'s')" || true
  exit 0
fi

T=$(mktemp -d)
mkdir -p "$T/kit" "$T/fonts"
cp "$RAIZ"/_kit_reels/{base.css,base.js,personas.js} "$T/kit/"
cp "$RAIZ"/_kit_noticias/fonts/*.woff2 "$T/fonts/" 2>/dev/null || true
sed -i 's#\.\./_kit_noticias/fonts/#../fonts/#g' "$T/kit/base.css"
python3 - "$PASTA" "$T" <<'EOF'
import json, sys
p, t = sys.argv[1:]
tl = open(f'{p}/timeline.json').read(); d = json.loads(tl)['duracao']
rot = json.load(open(f'{p}/roteiro.json'))
tl2 = json.loads(tl); tl2['kicker'] = rot.get('kicker', 'Entenda em 1 minuto'); tl2['sem_legenda'] = rot.get('legenda_na_tela', True) is False
h = open(f'{p}/pagina.html').read().replace('../_kit_reels/', 'kit/')
h = h.replace('<script src="kit/', '<script>window.TL=' + json.dumps(tl2, ensure_ascii=False) + ';</script><script src="kit/', 1)
h = h.replace('<div id="stage">', f'<div id="stage" data-composition-id="reels" data-no-timeline data-width="1080" data-height="1920" data-start="0" data-duration="{d}">', 1)
for alvo in ('id="world"', 'id="persp"', 'class="fila"'):   # desenho (moedas, quadradinhos): fora da checagem de texto
    h = h.replace(alvo, alvo + ' data-layout-ignore', 1)
h = h.replace('</body>', '<script>addEventListener("hf-seek",e=>window.seek&&window.seek(e.detail.time))</script></body>')
open(f'{t}/index.html', 'w').write(h)
EOF
cd "$T"
case "$MODO" in
  check)    $HF check --json --safe-zone reels --no-contrast > check.json || true
            python3 - check.json <<'EOF'
import json, sys
d = json.load(open(sys.argv[1]))
achados = []
def anda(x):
    if isinstance(x, dict):
        if 'code' in x and ('message' in x or 'severity' in x): achados.append(x)
        for v in x.values(): anda(v)
    elif isinstance(x, list):
        for v in x: anda(v)
anda(d)
ruido = {'film_silent', 'audio_none', 'outside_safe_zone'}   # o som entra no render.py; cabeçalho e legenda ficam fora da zona por desenho
for a in achados:
    if a.get('code') in ruido: continue
    print(f"- [{a.get('severity','')}] {a.get('code')}: {a.get('message','')[:220]}")
print(f"{len(achados)} achados ({sum(a.get('code') in ruido for a in achados)} de ruído esperado ocultos). JSON: {sys.argv[1]}")
EOF
            echo "pasta temporária: $T" ;;
  snapshot) $HF snapshot --at "${3:-3,12,30}" --no-end && echo "quadros em $T/.hyperframes/artifacts/snapshots/" ;;
  *)        $HF "${@:2}" ;;
esac
