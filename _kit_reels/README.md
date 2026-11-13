# Kit de Reels — @tiagoassessorxp

Reels de ~60 s em motion, a cada 2 dias, sobre um tema do mercado financeiro que esteja em alta
(conceito explicado, assunto viral, notícia da semana com contexto). Piloto aprovado para teste em 12/11/2026.

**Aprovação:** todo Reels precisa do OK do Tiago antes de ir ao ar. Fluxo: gerar o vídeo, subir no HubPost
como **rascunho** (create_post sem scheduledAt, kind REEL), mandar vídeo + legenda para ele e esperar.
Só agendar/publicar (edit_post com scheduledAt) depois que ele aprovar por escrito.
No pedido de aprovação, mandar sempre a **legenda completa, exatamente como vai ao ar, já com as hashtags** (pedido do Tiago em 12/11/2026).

## Estilo
- 1080x1920, 30 fps, ~55–65 s. Paleta escura + dourado (#c9a45c), Fraunces + Inter (mesma dos posts).
- Narração com **voz fixa**: Piper `pt_BR-faber-medium` (masculina, brasileira), `length_scale 0.9`. Não trocar a voz.
- Trilha instrumental sintetizada no render.py (sem direitos autorais), baixa sob a voz.
- Legendas palavra a palavra na zona segura (y≈1300–1520); números em dourado.
- Personas genéricas (`personas.js`: executivo, investidor, empresario, produtor, assessor) e ícones; nada de pessoas,
  logos ou marcas reais. Estrutura sugerida: gancho com número → 2–4 "peças" explicando o mecanismo com personas →
  "na prática" (investidor, empresa, produtor rural) → resumo / próximo evento → CTA com nome, "Assessor Alta Renda da
  XP Investimentos", @tiagoassessorxp e o aviso "Conteúdo informativo. Não é recomendação de investimento."
- Compliance igual aos posts: descrever efeitos, nunca recomendar compra/venda/resgate, nem citar produto ou emissor,
  nem projetar rentabilidade. Política: só fatos. Todo número com 2 fontes independentes ou fonte primária.

## Como gerar
1. Pasta `NN_reels_dia_dd-mm_rascunho_tema/` (renomear para o horário de publicação depois da aprovação, se quiser).
2. `roteiro.json`: `{"titulo", "kicker", "cenas":[{"id", "falas":[{"fala": texto para a voz (números por extenso),
   "legenda": texto da tela}]}]}`. Mire em 140–160 palavras faladas.
3. `python3 _kit_reels/voz.py PASTA` → `narracao.wav` + `timeline.json` (ajuste o texto se passar de ~65 s).
4. `pagina.html`: uma `<div class="scene" id="...">` por cena (mesmos ids do roteiro), com `../_kit_reels/base.css`,
   `personas.js` e `base.js`. Animações declarativas: `data-in` (fade-up, down, fade, pop, left, right, grow-y, grow-x,
   draw, tilt, zoom), `data-at` ("1.2" após o início da cena ou "L2+0.3" = 2ª legenda da cena), `data-dur`, `data-out`,
   `data-float` (use em elemento interno, não no mesmo de `data-in`), `data-count`/`data-from`/`data-dec`/`data-pre`/`data-suf`.
   Veja `61_reels_qui_12-11_rascunho_dolar-fiscal/pagina.html` como exemplo.
5. Prévia: `python3 _kit_reels/render.py PASTA --quadros 4,12,20,...` e conferir os JPGs (sobreposição, cortes, números).
6. Vídeo: `python3 _kit_reels/render.py PASTA` → `PASTA/reels.mp4` (~4 min). Apagar `_quadro_*`, manter roteiro, página,
   timeline, legenda.txt e reels.mp4 (narracao.wav pode ser apagado).
7. Registrar em `_kit_reels/historico.md`.
