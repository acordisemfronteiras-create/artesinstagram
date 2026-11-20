# Edição profissional: o que tiramos da HyperFrames e da Remotion

Duas bibliotecas de skills foram estudadas em 20/11/2026 para deixar os Reels com cara e som mais profissionais.
**Não trocamos de motor.** O nosso (`pagina.html` + `base.js` + `som.py` + `render.py`) continua sendo o caminho;
as duas servem de referência de acabamento e, no caso da HyperFrames, de ferramenta de conferência opcional.

- **HyperFrames (HeyGen)**: renderiza HTML em MP4 buscando quadro a quadro, como o nosso `render.py`. As skills trazem
  números medidos em filmes de lançamento (easing, tempos de leitura, transições, som) e uma CLI que mede vídeo e página.
  Clone de consulta: `~/ref/heygen-com_hyperframes` (abaixo, `HF:` = `~/ref/heygen-com_hyperframes/skills/`).
- **Remotion skills**: vídeo em React. O código não serve para nós, mas as regras de tempo, transição, desfoque de
  movimento e detecção de silêncio se traduzem. Clone: `~/ref/remotion-dev_skills/skills` (abaixo, `RM:`).

Para consultar os originais: `bash _kit_reels/instalar.sh --ref` (clona os dois em `~/ref`). O que importa está resumido aqui.

## Regras que adotamos

### Legenda da fala (`#cap`) e texto cinético (`.cin`)
- Cada `legenda` do roteiro com 3 a 5 palavras por batida de conversa (2 a 3 em trecho de energia alta). Frase maior que
  duas linhas no `#cap` vira duas falas no roteiro, quebrando em fim de frase ou pausa de 150 ms ou mais. (HF:hyperframes/references/captions.md)
- Uma legenda na tela por vez; ela entra até o início da primeira palavra e sai depois do fim da última, com saída curta
  (~0,12 s) e sumiço total no fim. O `caption()` do `base.js` já segue isso; não empilhar legendas. (HF:hyperframes/references/captions.md)
- No `.cin`, anime a palavra ou o bloco, não os dois ao mesmo tempo: as opacidades se multiplicam e parece um "pop". (HF:hyperframes/references/captions.md)
- Entrada por palavra que parece profissional: blur 6 px para 0 e opacidade 0 para 1 em ~0,13 s, palavras a 60–120 ms
  uma da outra, sem deslocamento (o `.cin` usa 26 px de subida; tente sem). (HF:hyperframes/references/motion.md)
- Texto longo demais: corte palavras, nunca diminua a fonte. Nada para ler abaixo de 28 px; em vertical, ~5 palavras por linha numa afirmação. (HF:hyperframes/references/types/vertical.md)
- Container de legenda com largura total e `text-align`, nunca `left:50%` + `translateX(-50%)` (corta nas bordas);
  `overflow: visible` para palavras com escala ou brilho. (HF:hyperframes/references/captions.md)
- Alinhamento com whisper (`voz.py --alinhar`, `voz_gravada.py`): case palavra transcrita com palavra da fala pela
  **posição**, não pelo texto (palavra repetida pega o tempo errado), e descarte palavras que começam dentro do silêncio
  final (o whisper inventa texto ali). Transcrição com mais de 20% de lixo = refazer com modelo maior. (HF:hyperframes/references/captions.md)
- Corte de silêncio na voz gravada: meça `input_thresh` com `loudnorm=print_format=json` e use esse valor como `noise`
  do `silencedetect` (d=0,5 s); silêncios separados por menos de 0,2 s no início ou no fim contam como um só. (RM:remotion-markup/silence-detection.md)

### Zonas seguras e primeiro quadro
- Área livre comum a TikTok, Reels e Shorts em 1080×1920: y 288–1248, x 120–888. Só Reels (guia de anúncios da Meta,
  conservador): topo 14% (y≥269), base 65% (y≤1248), laterais 6%. Número, fonte e frase-chave ficam dentro dela. (HF:hyperframes/references/types/vertical.md; código em `packages/core/src/safeAreas.ts`)
- Nosso cabeçalho (y≈120–205) e a legenda (y≈1330–1470) ficam fora dessa área por desenho aprovado; o `check` avisa
  `outside_safe_zone`. Mantemos, mas nada essencial além da legenda vai abaixo de y=1248.
- O quadro 0 é a capa e o gancho: nunca preto, nunca só logo; o primeiro número ou frase já visível em até 0,3 s. (HF:hyperframes/references/types/vertical.md; HF:hyperframes/references/story.md §3)

### Tempo e easing (`data-in`, `data-out`, `onSeek`)
- Easing por papel: chegada com cauda longa (`cubic-bezier(.16,1,.3,1)`), câmera em `ease()` (entra e sai suave),
  saída acelerando (`cubic-bezier(.32,0,.67,0)`, equivalente ao `power3.in`). A mesma curva em tudo é o sinal de "vídeo gerado"; hoje o `base.js`
  usa uma só (`E`). (HF:hyperframes/references/motion.md; RM:remotion-markup/timing.md)
- Saída 40–50% mais curta que a entrada e num movimento só (nunca desliza, para e sai). (HF:hyperframes/references/motion.md)
- Sobreposição: o próximo elemento começa quando o anterior está 30–50% feito. Itens de lista a 40–80 ms entre si. (HF:hyperframes/references/motion.md)
- Tempo de leitura: bloco de texto fica ≥ 0,5 s + 0,3 s por palavra (1–2 palavras: 0,4 s); a última frase do vídeo,
  ≥ 2 s. Na prática: `data-out` ≥ `data-at` + esse tempo. O `check` mede isso (`line_unread`). (HF:hyperframes/references/motion.md; HF:hyperframes/references/story.md §6)
- Título pousado fica parado; o movimento passa para o próximo elemento, a câmera ou o fundo. `data-float` só em
  desenho/persona, nunca em número ou título. (HF:hyperframes/references/motion.md)
- Contador (`data-count`): 1,2–1,6 s e depois parado; `font-variant-numeric: tabular-nums` para os dígitos não tremerem. (HF:hyperframes/references/types/data.md)
- Mola: amortecimento 0,7–0,85 parece premium; posição e tamanho podem passar do ponto, opacidade e cor nunca. Sem quique em interface. (HF:hyperframes/references/motion.md)
- Zoom de câmera no `onSeek`: interpole a escala em log (`s = Math.exp(lerp(ln s0, ln s1, ease(k)))`); escala linear
  parece frear quanto maior fica. (RM:remotion-markup/timing.md, "perceptual-scale")
- Tudo é função de `t`: nada de `Date.now()`, timer, `Math.random()` sem semente (use mulberry32 com semente fixa), e
  nada de medir layout (`getBoundingClientRect`) dentro do `onSeek`; meça uma vez no setup, depois de `document.fonts.ready`. (HF:hyperframes/references/runtimes.md; RM:remotion-markup/3d.md; RM:remotion-markup/measuring-text.md)
- Ritmo vertical: uma batida nova a cada 2–4 s; segurar 0,3–0,75 s antes da revelação, que roda em velocidade normal. (HF:hyperframes/references/types/vertical.md; HF:hyperframes/references/motion.md)
- Se o Tiago disser "rápido demais": desacelere só zooms e panorâmicas para 0,7× da velocidade, nada mais. (HF:hyperframes/references/motion.md)

### Transições entre blocos e cenas
- Use 3 a 5 tipos de transição por vídeo, cada uma causada por algo na tela; no máximo um terço das trocas como corte seco. (HF:hyperframes/references/motion.md)
- Repertório que cabe no nosso motor (bloco = `data-out` + `data-in`; cena = `onSeek`):
  - **troca com blur no mesmo palco**: sai com opacidade→0 e blur ~8 px em 0,13–0,2 s, o novo entra com blur→0 em 0,13 s;
  - **objeto vira o mundo**: um elemento cresce além da tela em ~0,65 s (in-out) e o que está em volta desfoca ~15 px e some em 0,3 s;
  - **inundação de cor**: o objeto principal fica e o fundo muda de cor em ~0,4 s (in-out);
  - **chicote**: borrão de 0,13–0,3 s; o que chega pousa desfocado e fica nítido em ~0,13 s;
  - **dip**: escurecer o quadro ~40% por 3 quadros antes de um corte seco, para o corte parecer intencional. (HF:hyperframes/references/motion.md)
- Corte no quadro mais rápido do movimento, com mesma direção e velocidade dos dois lados (`power3.in` sai, `power3.out` entra). (HF:hyperframes/references/motion.md)
- Nossas cenas têm duração fixada pela narração, então efeito sobre a troca de cena é **sobreposição** (não encurta a
  linha do tempo), centrada no `fim` da cena, 20–30 quadros. (RM:remotion-markup/transitions.md)
- Uma explicação cresce: comece do desenho mais simples e acrescente uma parte por batida, quando a voz a nomeia (`@deixa`),
  na metade final da cena; rótulo em cima da parte, sem legenda de cores. (HF:hyperframes/references/types/explainer.md; HF:hyperframes/references/film.md)

### Desfoque de movimento, luz e textura
- Movimento rápido (0,3–0,6 s) leva blur no próprio easing, com pico no quadro mais rápido: 6–12 px em texto, 15–20 px
  na tela inteira, só horizontal se o movimento é horizontal (SVG `feGaussianBlur stdDeviation="X 0"`). No `onSeek`,
  blur proporcional à velocidade do quadro. (HF:hyperframes/references/motion.md)
- Referência de obturador: 180° = metade de um quadro (1/60 s a 30 fps). Desfoque "de verdade" por média de subquadros
  multiplica o custo do render; só em trecho curto, se um dia valer. (RM:remotion-markup/motion-blur.md)
- Vazamento de luz: sobreposição na troca de cena que acende na primeira metade e recolhe na segunda, padrão por
  semente; o tom padrão (amarelo-laranja) casa com o nosso dourado. Faça como gradiente radial animado por `t`, uma ou
  duas vezes por vídeo, em momentos que importam. (RM:remotion-markup/light-leaks.md)
- Atmosfera com 15–25% de opacidade; acento a 5% some na compressão. Gradiente linear de tela inteira em fundo escuro
  faz faixas no H.264: prefira radial, cor sólida + brilho local, e confira os véus (`#veu-topo`) no MP4. (HF:hyperframes/references/look.md)
- Brilho, partículas, lens flare e "vazio escuro com coisas pequenas flutuando" são os padrões de vídeo gerado: só quando
  a peça pede, e nunca como enfeite fixo. (HF:hyperframes/references/spec.md, "BANNED by default")

### Tipografia e destaque
- Título com 4–9% da altura (77–173 px), uma ou duas linhas; linhas calmas com 2,5–4% (48–77 px) contra a palavra
  herói que ocupa 60–90% da largura. Uma palavra destacada na cor de acento, e ela carrega o sentido (`<em>`, `.gold`). (HF:hyperframes/references/motion.md)
- Contraste AA: 4,5:1 texto normal, 3:1 texto grande (24 px+, ou 19 px+ negrito). O cinza das palavras ainda não
  faladas do `#cap` (`#5f5a52`) dá 2,77:1; o `check` sugere `rgb(101,96,88)` (`#656058`), que mantém o efeito e passa. (HF:hyperframes-cli/references/lint-validate-inspect.md)
- Marca-texto, sublinhado, círculo ou risco desenhados com progresso preso ao tempo destacam um número sem trocar de
  tela; no nosso motor é `data-in="draw"` num SVG por cima da palavra. (RM:remotion-markup/text-highlights.md)
- O texto grande não repete a frase falada palavra por palavra (a legenda de baixo já faz isso); ele resume em 2–6 palavras. (HF:hyperframes/references/story.md §6)
- Evitar: tudo entrando com `fade-up`, três cartões em fila, grade de KPIs, texto que se mexe enquanto é lido. (HF:hyperframes/references/spec.md; HF:hyperframes/references/types/explainer.md)

### Som (`"sfx"` do roteiro, `som.py`)
- Todo efeito tem causa na tela: `whoosh` em troca de cena ou cartão grande em movimento rápido; `pop` em número ou
  selo pousando; `tique` em texto chegando linha a linha; `riser` + `impacto` **uma vez** no vídeo, no clímax. (HF:hyperframes/references/sound.md)
- O pico do efeito cai **um quadro depois** da imagem (luz chega antes do som). Como o pico do arquivo vem depois do
  início, ajuste o `em`: `"@deixa - pico + 0.033"`; meça o pico de cada tipo com `hyperframes audio` (abaixo). (HF:hyperframes/references/sound.md)
- Som repetido igual em toda troca é o sinal mais comum de amadorismo: varie 2–3 versões (duração, filtro) do mesmo efeito. (HF:hyperframes/references/sound.md)
- Efeito 3–6 dB acima da trilha; trilha com energia toda abaixo de 150 Hz some no alto-falante do celular. Trilha sob voz em ~0,14 de volume. (HF:hyperframes/references/sound.md)
- Trilha entra na parte mais forte (sem intro fraca), fade-in ~0,4 s, termina em fim de compasso com fade ~1,5 s sob o cartão final. (HF:hyperframes/references/film.md)
- Loudness do `reels.mp4`: −16 a −14 LUFS integrado, pico real ≤ −1 dBTP, sem clipping. (HF:hyperframes/references/sound.md)
- Com trilha de BPM conhecido: quadros por batida = 30×60/BPM, calculado pelo índice da batida (não somando); troca de layout no compasso. (HF:hyperframes/references/motion.md)

### Conferência (passo 7 do SKILL.md)
- Descreva cada quadro de conferência em uma frase, como um estranho; objeto que precisa de explicação ("essas bolas são
  as reservas") é defeito grave. Com as palavras cobertas, as imagens ainda contam a história? (HF:hyperframes/references/review.md)
- Anote cada problema como `t=4,2s · onde · problema → mudança exata · o que fica`, em P0 (quebra leitura ou está errado),
  P1 (enfraquece) e P2 (polimento). Corrija P0, depois os P1 que valem; texto, depois tempo, depois detalhe. Nada de nota de 0 a 10. (HF:hyperframes/references/review.md)
- Veja os quadros com 360 px de largura (tamanho de celular): toda linha feita para ler precisa ser legível. Vídeo
  carregado demais: tire um terço do movimento e fique com o que guia o olho. (HF:hyperframes/references/review.md)
- Som: medido, não ouvido. Diga isso ao Tiago na entrega. (HF:hyperframes/references/review.md §4)

## Ferramentas da HyperFrames que usamos na conferência

Testado em 20/11/2026 com `npx -y hyperframes@latest` (v0.9.72) no Reels 84, sempre fora do repositório e com
`export HYPERFRAMES_NO_TELEMETRY=1` (desliga a contagem de uso). Todas rodam localmente, sem login.

**No vídeo pronto** (copie o `reels.mp4` para uma pasta temporária e rode de lá; elas escrevem `.hyperframes/` na pasta atual):
- `npx -y hyperframes@latest audio reels.mp4 --json` (5 s): loudness (84: −14,8 LUFS, pico real −4,1 dBTP, 0 clipping),
  silêncios, onsets (233) e `moments.peak`. Também serve num efeito isolado do `som.py` para achar o pico e acertar o `em`.
- `npx -y hyperframes@latest measure probe reels.mp4 --json`: 1080×1920, 30 fps, 56,667 s, 1700 quadros, áudio sim, sem VFR.
- `npx -y hyperframes@latest measure events reels.mp4 --json` (13 s): trocas e "holds" (trechos sem mudança visível).
  No 84: 26 holds, maior 4,33 s em t=20,3 e outro de 3,03 s em t=37,5; acima de 3 s é trecho morto a revisar.
  Com `--map --start 0 --end 20` agrupa mudanças de imagem com os onsets do som (`windows`): bom para ver se o SFX bate com o que aparece.
- `npx -y hyperframes@latest measure cuts reels.mp4 --json`: cortes secos. No 84, zero (as cenas se fundem), como esperado.

**Na página** (`check`, `snapshot`, `lint` só aceitam projeto HyperFrames; a `pagina.html` crua dá erro de
`data-composition-id` e de caminho `../`). Um adaptador temporário resolve, porque a HyperFrames aceita o evento `hf-seek`.
Rode da raiz do repositório:

O adaptador virou script: `bash _kit_reels/conferir_hf.sh PASTA` (check), `... PASTA snapshot` e `... PASTA video`
(mede o `reels.mp4`). Ele copia a página para uma pasta temporária e liga o `hf-seek` ao nosso `window.seek(t)`.

- `npx -y hyperframes@latest check --json --safe-zone reels` (45 s; `--no-contrast` para ir mais rápido): o mais útil.
  No 84 achou `line_unread` reais ("nem tudo aqui é dólar." 1,07 s, precisava ~2 s; "o colchão do país em moeda forte"
  1,83 s; aviso final 3,55 s), `text_below_floor` ("Au" das moedas com 15 px), contraste do cinza da legenda e
  `outside_safe_zone` no cabeçalho e na legenda. Ruído esperado: `film_silent`/`audio_none` (o som entra no `render.py`)
  e `text_not_painted`/`text_occluded` nas moedas 3D; marque desenho com `data-layout-ignore` no adaptador para limpar.
- `npx -y hyperframes@latest snapshot --at 3,12,30 --no-end` (8 s): PNGs + folha de contato em `.hyperframes/artifacts/snapshots/`.
  Conferido: bate com o render.
- `npx -y hyperframes@latest snapshot --review`: folha de batidas e folha "celular" (360 px). Com uma cena só, espalha 5 batidas.

**Não usar** (login, plano pago ou envio de dados para fora): `share`, `publish`, `cloud`, `lambda`, `cloudrun`,
`reverse` (Pro, sobe o vídeo), `templates pull` / style-sampling (Pro), `media-use resolve|generate` (catálogo e
créditos HeyGen), `auth`, `billing`, `usage`, `feedback`, `events` (telemetria das skills) e `audio --quality best`
(sobe o áudio para a HeyGen e pode cobrar). `npx` ainda consulta o npm para baixar e checar versão.

## O que não adotamos e por quê
- **Migrar para HyperFrames ou Remotion.** Nosso motor já é determinístico e aprovado; GSAP/React, subcomposições,
  Studio e o app desktop não acrescentam nada que o Tiago veja.
- **Mídia HeyGen** (vozes, avatar, catálogo de música, imagens geradas) e **templates de estilo**: pago, externo, e a
  regra aqui é trilha e efeitos sintetizados, voz fixa.
- **"Sem tons sintetizados"** (HF:hyperframes/references/sound.md): não dá, nosso som é todo sintetizado por direito
  autoral. Ficamos com o espírito: `bip` e `brilho` com parcimônia, nada de "ding" em toda batida.
- **Legenda acima de y=1248** como a HF pede: o layout com legenda em y≈1330–1470 foi aprovado; reavaliar só se o Tiago
  ou um teste no app mostrar a legenda coberta.
- **Efeitos da Remotion** (`remotion.media/*.wav`, sons de meme): remotos, de terceiros e com tom de meme.
- **Pacotes Remotion** (`@remotion/effects`, `rough-notation`, `motion-blur`, `three`, `captions`): só em React e com
  licença própria; adaptamos as ideias em CSS/SVG/`onSeek`.
- **Visualização de áudio** (barras, forma de onda): não combina com explicação de mercado.
- **Presets visuais da HF** e o processo de três roteiros com `SPEC.md`: a identidade é fixa e o `formatos.md` já faz a escolha de estrutura.
