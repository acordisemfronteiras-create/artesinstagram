# Ferramentas de edição (pedido do Tiago em 20/11/2026)

O Tiago mandou 13 repositórios para "ficar mais profissional nas edições". A nuvem onde a rotina roda é apagada a cada
rodada, então "instalar" aqui quer dizer: o `instalar.sh` põe de volta em ~1 a 3 minutos, e o motor já sabe usar.
Testado em 20/11/2026 nesta máquina (Linux, 2 CPUs, sem placa de vídeo).

| # | Ferramenta | Status na nuvem | Como usamos |
|---|---|---|---|
| 01 | yt-dlp | instalado (`instalar.sh`) | Baixar um vídeo de referência que o Tiago mandar por link, só para estudo (o vídeo não entra no repositório). **A rede desta sessão bloqueia YouTube, Instagram e TikTok**; até liberar, ele precisa anexar o arquivo |
| 02 | LosslessCut | não roda aqui | Programa de desktop (janela). Para cortes rápidos, o mesmo resultado sai do `ffmpeg -c copy`, que já temos |
| 03 | auto-editor | instalado | Tira silêncios de uma gravação: `auto-editor gravacao.wav --edit audio:threshold=0.02 --margin 0.1s -o cortado.wav --no-open`. O `voz_gravada.py` já encurta pausas com mais controle (pausa máxima); use o auto-editor em vídeo bruto do Tiago falando para a câmera |
| 04 | faster-whisper | já usávamos | Alinhamento das deixas (`voz.py --alinhar`, agora convertendo números) e conferência da narração |
| 05 | remotion skills | estudado | Regras de tempo, transição, legenda, desfoque e silêncio resumidas em `_skill_reels_motion/edicao_profissional.md`. O código é React e não entra no motor |
| 06 | chatterbox | instalado (`--ia`) | Voz multilíngue local, mais natural que o Kokoro e capaz de **clonar um timbre** a partir de 10 a 20 s de gravação. Motor `"chatterbox"` no `voz.py`. ~10x o tempo real na CPU (1 min de narração ≈ 10 min). **Trocar a voz é decisão do Tiago**; clonar a voz dele só com autorização por escrito, e aí o post vai com `aiGenerated: true` |
| 07 | DeepFilterNet | instalado (`--ia`) | Já ligado no `voz_gravada.py`: tira o ruído de fundo da voz gravada pelo Tiago antes da equalização (`--sem-ia` volta ao filtro do ffmpeg). No teste, o piso de ruído entre as palavras foi de −40 dB para silêncio |
| 08 | demucs | instalado, sem pesos | Separaria voz e música (estudar a trilha de uma referência, limpar gravação com música ao fundo). Os pesos vêm de dl.fbaipublicfiles.com, que a rede desta sessão bloqueia |
| 09 | rembg | instalado (`--ia`) | Recorta o fundo de uma foto (do Tiago, de um objeto) para usar como figura no motion: `~/ia/bin/rembg i foto.jpg recorte.png`. Sem pessoas ou marcas reais de terceiros |
| 10 | Real-ESRGAN | instalado (`--ia`, via spandrel) | Amplia 4x imagem pequena ou borrada: `~/ia/bin/python _kit_reels/ampliar.py entrada.png saida.png` |
| 11 | davinci-resolve-mcp | não roda aqui | Controla o DaVinci Resolve instalado no computador do Tiago. Só funcionaria com o computador conectado e o Resolve instalado nele |
| 12 | OpenCut | não roda aqui | Editor visual (tipo CapCut) para uma pessoa usar na tela. Não ajuda a rotina automática; o Tiago pode usar no computador dele |
| 13 | hyperframes | instalado (`--hf`) e estudado | Mesmo princípio do nosso motor (HTML que vira MP4). Usamos a CLI para **conferir**: `bash _kit_reels/conferir_hf.sh PASTA` acha texto que some antes de dar tempo de ler, letra pequena e contraste; `... PASTA video` mede volume, pico e trechos parados. Regras de acabamento em `edicao_profissional.md` |

## Ordem de uso numa rodada

1. `bash _kit_reels/instalar.sh` (sempre). `--ia` só quando for usar voz gravada, Chatterbox, recorte ou ampliação. `--hf` para conferir.
2. Roteiro, voz e página como no `SKILL.md`.
3. Antes de filmar: quadros (`render.py --quadros`) **e** `bash _kit_reels/conferir_hf.sh PASTA`. Corrija os `line_unread`
   (texto que precisa ficar mais tempo) e `text_below_floor` que forem de leitura (o rodapé legal pode ficar pequeno).
4. Depois de filmar: `bash _kit_reels/conferir_hf.sh PASTA video`. Alvo: −16 a −14 LUFS, pico real ≤ −1 dBTP, nenhum trecho
   parado acima de ~3 s sem motivo.

## Cuidados

- O ambiente `~/ia` é separado de propósito: Chatterbox e DeepFilterNet fixam torch 2.6 e numpy 1.26, e instalar no
  Python principal derruba o Kokoro e o whisper. Nunca rode `pip install deepfilternet` fora dele.
- Ocupa ~6 GB. Não rode Chatterbox ao mesmo tempo que outro processo pesado (a máquina tem 7 GB de RAM; no teste, rodar
  junto com a instalação derrubou o processo).
- Para liberar YouTube/Instagram (yt-dlp) ou os pesos do demucs, o Tiago precisa liberar esses domínios nas
  configurações de rede do Claude (Configurações > Capacidades).
