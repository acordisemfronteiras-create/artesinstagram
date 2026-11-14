# Catálogo prompt-motion.com (destilado)

Todas as 240 entradas da biblioteca, lidas em 14/11/2026. Cada bloco traz o link da página e do post original, o que o vídeo mostra, a técnica descrita com as nossas palavras e o quanto ela serve para os Reels do Tiago. Os prompts originais não estão copiados aqui: pertencem aos criadores e ficam a um clique, no link de cada entrada.

Contagem: 34 alto · 85 médio · 121 baixo. Dentro de cada nível, a ordem é por tag.

Tags (quantas entradas): Product UI (107) · Kinetic type (100) · Music (51) · Shapes (43) · Particles (43) · Charts (34) · Diagrams (31) · Characters (27) · Phone (23) · Photos (23) · Code (21) · não informadas (1) · (nenhuma na página) (1) · nenhuma listada (stack WebGL2 (1) · Canvas 2D (1) · Web Audio) (1) · nenhuma (1)

As sugestões "Para os nossos Reels" são ideias de partida: antes de usar qualquer uma, ela passa pelo compliance de `_skill_reels_motion/SKILL.md` (nada de recomendar, citar produto ou emissor, prometer rentabilidade; sem marcas, logos ou pessoas reais).

Observação: cerca de metade da biblioteca é o mesmo pedido curto de "showreel de 15 s, vá com tudo", sem técnica escrita. Essas entradas estão no nível baixo e servem só como referência visual (vale abrir o vídeo).

## Alto: técnicas que já servem para os nossos Reels (34)

### Cycle of life animation
- Criador: @loicRambo · Tipo: Prompt · Tags: Characters · Data: 25/09/2026
- Página: https://prompt-motion.com/loicrambo-ad6830 · Post: https://x.com/loicRambo/status/2103428454355980558
- O que o vídeo mostra: animação de 20 s que acompanha uma pessoa da infância à velhice e morte, em loop.
- Técnica: o roteiro é uma sequência fixa de fases da vida (infância, adolescência, rotina de trabalho, família, velhice), cada uma com seu bloco curto. O último plano corta de volta para o primeiro, o que fecha um loop contínuo. Estilo e técnica ficaram livres.
- Para os nossos Reels: alto — a estrutura de "linha da vida" com loop serve muito bem para planejamento financeiro (juros compostos ao longo das fases, aposentadoria), desde que com personagens genéricos, sem pessoas reais. O loop também aumenta o tempo de exibição no Reels.

### Steam new releases news recap
- Criador: @gigabit_million · Tipo: Prompt · Tags: Charts · Data: 27/09/2026
- Página: https://prompt-motion.com/gigabit-million-16b3a0 · Post: https://x.com/gigabit_million/status/2104068536041959719
- O que o vídeo mostra: resumo de cerca de 60 s dos lançamentos de jogos de dois dias, destacando o atrativo de cada título.
- Técnica: formato de "recap de notícias" com cerca de 60 s, recorte de datas fechado e um ponto de vista definido (o do jogador). Prioriza legibilidade: cada item ganha um destaque claro e curto. Não especifica visual nem render.
- Para os nossos Reels: alto — é o molde de um "resumo do mercado da semana" de 60 s: janela de datas fixa, um card por notícia, um destaque por item e um ponto de vista (o do investidor).

### Token bucket rate limiter
- Criador: @ParkerRex · Tipo: Prompt · Tags: Charts, Diagrams · Data: 24/09/2026
- Página: https://prompt-motion.com/parkerrex-1a54fe · Post: https://x.com/ParkerRex/status/2103206747846701462
- O que o vídeo mostra: uma explicação animada, em diagramas, de como funciona um limitador de requisições do tipo "balde de fichas".
- Técnica: desenha tudo em Canvas puro, sem bibliotecas, e cada quadro é função pura do tempo, para que um renderizador capture screenshots de forma determinística. O diagrama explica um mecanismo passo a passo (fichas entrando e saindo de um balde).
- Para os nossos Reels: alto — é a mesma arquitetura determinística da nossa skill, e o formato "mecanismo explicado por diagrama animado" serve para juros compostos, come-cotas ou reserva de emergência como balde.

### Paper-style product launch film
- Criador: @ik_builds · Tipo: Prompt · Tags: Charts, Diagrams, Music · Data: 26/09/2026
- Página: https://prompt-motion.com/ik-builds-b8bdcf · Post: https://x.com/ik_builds/status/2103890476885585923
- O que o vídeo mostra: filme de 15 s que explica um produto sobre um fundo de papel, com notas manuscritas surgindo, tipografia enorme e cortes secos para cenas escuras.
- Técnica: HyperFrames + GSAP, esforço médio. É um template parametrizado (produto, cores, fontes como variáveis) com uma ideia nova a cada 1,5–2 s, sem narração. Fundo claro de papel, anotações em fonte manuscrita "desenhadas" via stroke-dashoffset e tipografia condensada gigante. As cenas alternam com cortes duros para um carvão escuro. O movimento segue princípios clássicos de animação (squash and stretch, follow-through, smear, overlap, um movimento principal por transição) e proíbe transições genéricas de deslizar ou girar. Todo estado inicial fica definido em t=0 para o vídeo poder ser "seekado" quadro a quadro. O som é estruturado: bateria entra na virada para o escuro, impactos na tipografia e no logo, efeitos CC0 ou gerados. Masterização em -14 LUFS / -2 dBTP, medida de novo após o encode AAC. Também proíbe interface na tela (timecode, scrubber), jargão e números inventados.
- Para os nossos Reels: alto — a regra de estados definidos em t=0 (essencial para render quadro a quadro), o ritmo de uma ideia a cada 1,5–2 s, a virada para o escuro na batida, a meta de loudness e a proibição de números inventados entram direto na nossa skill.

### Oscilloscope-style studio motion graphic
- Criador: @rneayan · Tipo: Prompt · Tags: Charts, Kinetic type · Data: 25/09/2026
- Página: https://prompt-motion.com/rneayan-ea6129 · Post: https://x.com/rneayan/status/2103401461837406275
- O que o vídeo mostra: uma apresentação de estúdio em estilo de osciloscópio, com linhas luminosas de forma de onda e gráficos.
- Técnica: como no anterior, uma única referência estética ("osciloscópio") define tudo: traços finos brilhantes sobre fundo escuro, curvas que se desenham e texto que acompanha as ondas.
- Para os nossos Reels: alto — linhas brilhantes que se desenham sobre fundo escuro são quase um gráfico de preço; em dourado, viram uma linguagem forte para cotações, curvas de juros e volatilidade.

### Animated business explainer
- Criador: @alex_prompter · Tipo: Prompt · Tags: Diagrams · Data: 25/09/2026
- Página: https://prompt-motion.com/alex-prompter-1ea044 · Post: https://x.com/alex_prompter/status/2103499977632997524
- O que o vídeo mostra: explicativo de negócio de 30 s em página HTML única, dividido em cinco cenas.
- Técnica: roteiro fixo em cinco atos: dor do cliente, o que a empresa faz, como funciona em três passos, uma prova e o nome do responsável no fechamento. Texto em negrito, cores da marca preenchidas num campo do prompt e transições suaves entre cenas. A força é a estrutura narrativa, não o motion.
- Para os nossos Reels: alto — o esqueleto problema → solução → 3 passos → prova → assinatura do assessor é um roteiro pronto para Reels de 60 s (basta esticar cada ato).

### Indian civilisation history film
- Criador: @BuildFastWithAI · Tipo: Prompt + Skill · Tags: Diagrams · Data: 28/09/2026
- Página: https://prompt-motion.com/buildfastwithai-53234e · Post: https://x.com/BuildFastWithAI/status/2104451249269780900
- Instalação (só Skill): `npx skills@latest add https://github.com/buildfastwithai/buildfast-skills` · Repo: https://github.com/buildfastwithai/buildfast-skills/tree/main/generative-film-skill
- O que o vídeo mostra: filme histórico animado sobre a civilização indiana, com diagramas, música e efeitos sonoros.
- Técnica: o prompt é um pedido de uma linha por um MP4 criativo com música e efeitos. O motor é a skill "generative-film", que gera um filme animado sobre qualquer tema. Cada quadro é desenhado em código, e a trilha é sintetizada e sincronizada com a batida. A página não detalha o pipeline; os detalhes estão no repositório.
- Para os nossos Reels: alto — é uma skill pronta de "tema → MP4 desenhado em código com trilha sintetizada na batida". Vale estudar o repositório para copiar a arquitetura de render e sincronia de áudio (com licença a verificar).

### White Russian recipe animation
- Criador: @Sarut0biSasuke · Tipo: Prompt · Tags: Diagrams · Data: 25/09/2026
- Página: https://prompt-motion.com/sarut0bisasuke-cefa43 · Post: https://x.com/Sarut0biSasuke/status/2103418429248069973
- O que o vídeo mostra: um copo vazio que se enche camada a camada até virar um White Russian, com o nome e a medida de cada ingrediente aparecendo na entrada.
- Técnica: formato explicativo de 30 s em que a ordem de montagem dita o ritmo: cada ingrediente entra no copo e ganha seu rótulo com a quantidade naquele momento. O prompt deixa a escolha entre JS e HTML ao modelo e não define paleta nem tipografia.
- Para os nossos Reels: alto — a mecânica de "recipiente que se enche em camadas rotuladas" serve direto para explicar uma carteira (renda fixa, ações, FIIs, reserva) com percentuais aparecendo à medida que cada classe entra.

### Kinetic type self-portrait
- Criador: @souravbhar871 · Tipo: Prompt · Tags: Kinetic type · Data: 26/09/2026
- Página: https://prompt-motion.com/souravbhar871-61f424 · Post: https://x.com/souravbhar871/status/2103711849703477361
- O que o vídeo mostra: um autorretrato de 10 s feito só com tipografia em movimento.
- Técnica: o vídeo é construído só com texto, e há uma restrição anti-clichê: proíbe molduras e textos nos cantos da tela, que o autor considera marcas de vídeo feito por IA.
- Para os nossos Reels: alto — a regra de não usar molduras nem rótulos nos cantos vale como restrição de estilo na nossa skill, porque deixa o Reels com cara menos genérica.

### Speech built as architecture
- Criador: @Gdgtify · Tipo: Prompt · Tags: Kinetic type · Data: 25/09/2026
- Página: https://prompt-motion.com/gdgtify-287ddf · Post: https://x.com/Gdgtify/status/2103458245213929495
- O que o vídeo mostra: um poema falado de 20 s em que cada palavra-chave vira uma peça de construção (verga, carga suspensa, apoio, abertura, plataforma) e a última frase se apoia na estrutura montada pelas anteriores.
- Técnica: tipografia como arquitetura: cada palavra recebe uma função estrutural, réguas viram cabos e a linha de base se deforma de modo elástico e controlado, com assentamentos em amortecimento crítico e pelo menos uma pausa imóvel de ~400 ms; no fim a câmera passa por baixo da plataforma e reencontra o quadro inicial, fechando o loop. Visual editorial de monumento: fundo verde muito escuro, creme e um dourado só nos elementos estruturais, combinando uma serifa de alto contraste (fala), uma grotesca pesada (palavras de carga) e uma mono discreta (marcas de tempo). Ritmo guiado pelas pausas da fala em sete blocos, não por compasso; som opcional e desligado. O código é um HTML 1080x1080 com `window.seek(t)` determinístico, sem física acumulada nem aleatoriedade, com timeline periódica (o quadro 0 igual ao último), exportado a 60 fps em passos fixos e com texto desenhado a partir de contornos reais dos glifos; nenhuma palavra some antes de ser lida, e as transições usam oclusão em vez de morph arbitrário.
- Para os nossos Reels: alto — a paleta escura + creme + dourado e o trio de fontes (serifa / grotesca / mono) são quase a nossa identidade, e a regra de "nenhuma palavra sai antes de ser lida" com pausa imóvel cabe direto em frases de efeito sobre investimento.

### TechHalla kinetic type bumper
- Criador: @techhalla · Tipo: Prompt · Tags: Kinetic type · Data: 25/09/2026
- Página: https://prompt-motion.com/techhalla-90b8ec · Post: https://x.com/techhalla/status/2103411244468498547
- O que o vídeo mostra: vinheta de identidade de 20 s em tipografia cinética sobre fundo quase preto, no estilo de cartaz de rua em movimento.
- Técnica: mensagem fixa de cinco frases distribuída em atos (entrada de impacto, tese A com embaralhamento de glifos, tese B por máscara, prova com tachado que vira sublinhado, assinatura e respiro final). Três fontes com papéis distintos (display pesado, empilhadas e mono para rótulos), tracking bem negativo nos títulos e grade de linha de base de 8 px. Animação por glifo (posição, opacidade, desfoque) com atraso de uma semicolcheia a 120 BPM, câmera só com punch-in leve e pans na batida, molas fechadas, loop perfeito e oito stills de checagem antes do render. Proíbe clichês de IA, gradientes, glassmorphism e neon.
- Para os nossos Reels: alto — é o modelo mais próximo do nosso visual: fundo escuro, um acento forte (trocar magenta/verde por dourado), hierarquia de três fontes e estrutura em atos para uma tese de mercado.

### Reflex brand motion reel
- Criador: @reflex_cloud · Tipo: Prompt · Tags: Kinetic type, Music · Data: 25/09/2026
- Página: https://prompt-motion.com/reflex-cloud-72ffe5 · Post: https://x.com/reflex_cloud/status/2103552840027304046
- O que o vídeo mostra: reel de marca de 15 s com gancho forte no primeiro segundo, tipografia cinética, mudanças de cor e cortes na música.
- Técnica: esforço máximo, uma tentativa. O prompt define uma estrutura dramática clara: gancho marcante já no primeiro segundo, depois uma sequência de técnicas distintas (tipografia cinética, jogo de formas, movimentos de câmera, viradas de cor), cortadas no ritmo da música e terminando num quadro final limpo e memorável. Também pede que o modelo não presuma que as ferramentas atuais sejam as melhores e escolha a stack do zero.
- Para os nossos Reels: alto — a estrutura "gancho no 1º segundo, técnicas variadas, quadro final limpo" é a fórmula de retenção de Reels e vale como regra da skill.

### Synced lyrics motion video
- Criador: @samaote · Tipo: Prompt · Tags: Kinetic type, Music · Data: 25/09/2026
- Página: https://prompt-motion.com/samaote-5e2fc2 · Post: https://x.com/samaote/status/2103510974796124569
- O que o vídeo mostra: um lyric video com o texto aparecendo em sincronia com os vocais e a batida de uma faixa enviada.
- Técnica: o áudio é anexado e vira a espinha da linha do tempo; o texto e as animações devem bater com os vocais e o beat. Rodou com esforço Max. A duração é definida pela faixa.
- Para os nossos Reels: alto — dá para sincronizar o texto cinético com a locução ou a trilha do Reels (marcar os tempos da narração e animar cada frase no ataque), o que aumenta muito a retenção.

### What happens in one second
- Criador: @nolkeeg · Tipo: Prompt · Tags: Kinetic type, Particles · Data: 26/09/2026
- Página: https://prompt-motion.com/nolkeeg-bf062e · Post: https://x.com/nolkeeg/status/2103841917603635633
- O que o vídeo mostra: uma peça de texto cinético e partículas sobre o que acontece no mundo em um segundo.
- Técnica: dá liberdade total de tema e estilo, pede para não usar memórias ou skills anteriores e lança um desafio competitivo para elevar a ambição. O modelo escolheu o conceito "em um segundo", que é um gancho de escala e estatística.
- Para os nossos Reels: alto — o conceito "o que acontece em 1 segundo" (ou em 1 minuto) adapta direto para finanças: negociações na bolsa, Pix transacionados, juros compostos girando, com contadores dourados.

### Motion designer showreel (@aichrislee)
- Criador: @aichrislee · Tipo: Prompt · Tags: Kinetic type, Shapes, Music · Data: 26/09/2026
- Página: https://prompt-motion.com/aichrislee-a6cb42 · Post: https://x.com/aichrislee/status/2103878567540961335
- O que o vídeo mostra: um showreel de 15 s em 1920x1080 com tipografia grande, cores fortes e câmera sempre em movimento.
- Técnica: é o prompt mais técnico do lote. Pede um único HTML em que cada quadro é função pura do tempo, com captura quadro a quadro via Playwright e montagem em MP4 com ffmpeg, a 30 fps. Na direção, exige texto grande, cores ousadas, movimento de câmera real, algo mudando a cada segundo e nenhum fade lento. Também manda o modelo construir sem fazer perguntas e entregar o MP4 pronto.
- Para os nossos Reels: alto — é o mesmo pipeline que usamos (HTML determinístico, captura quadro a quadro, ffmpeg); basta trocar para 1080x1920 e aproveitar as regras de ritmo ("algo muda todo segundo", sem fades lentos).

### Orange dot motion system
- Criador: @ultimaxbt · Tipo: Prompt · Tags: Kinetic type, Shapes, Music · Data: 06/10/2026
- Página: https://prompt-motion.com/ultimaxbt-bbebf5 · Post: https://x.com/ultimaxbt/status/2107486052550062398
- O que o vídeo mostra: um ponto laranja que costura todas as cenas: nasce na interface, vira o pingo de uma letra, traça um gráfico de mola, vira forma e volta no cartão final.
- Técnica: um único elemento-guia conecta tudo, e o gráfico é desenhado pela mesma função que move o ponto, o que garante coerência. Fundo creme ou quase preto, um só acento, tipografia pesada com palavras orbitando o ponto e uma malha de pontos (halftone) que reage a ele. Um evento por batida, ~15 s, HTML 1920x1080 a 60 fps via `seek(t)`, tempos separados para texto que sai e texto que entra, e mapa de batidas mais quatro quadros de referência antes do render.
- Para os nossos Reels: alto — um "ponto dourado" que vira cotação, desenha a curva do índice e termina no CTA é um fio condutor elegante para 60 s de finanças.

### SaaS product launch video
- Criador: @xelandre__ · Tipo: Prompt · Tags: Product UI · Data: 25/09/2026
- Página: https://prompt-motion.com/xelandre-363f00 · Post: https://x.com/xelandre__/status/2103473030160687413
- O que o vídeo mostra: vídeo de lançamento de um SaaS com telas do produto em movimento.
- Técnica: a animação é uma página HTML/JS em que cada quadro é uma função pura do tempo, sem depender de relógio real. O Chrome headless, controlado pelo Playwright, captura um quadro por vez, e o ffmpeg monta o MP4. O motion blur é aplicado na montagem, misturando subquadros. A trilha sonora também é gerada por código, em vez de vir de arquivo gravado.
- Para os nossos Reels: alto — é exatamente o nosso pipeline. Vale copiar a ideia de quadro como função de t, o motion blur na etapa do ffmpeg e o áudio sintetizado, que evita problema de licença.

### Taxtello bookkeeping app film
- Criador: @daniel_haida · Tipo: Prompt · Tags: Product UI, Charts · Data: 27/09/2026
- Página: https://prompt-motion.com/daniel-haida-8691d4 · Post: https://x.com/daniel_haida/status/2104139720829636937
- O que o vídeo mostra: filme premium de até 15 s de um app de contabilidade, indo do caos à clareza com telas reais e fechamento na marca.
- Técnica: arco narrativo "caos, controle, clareza, marca" em quatro blocos, mostrando em vez de explicar e fugindo da cara de template de SaaS. Visual em azul-marinho quase preto com dourado usado com parcimônia, UI sempre nítida, luz ambiente sutil, sem glassmorphism nem desfoque "cinematográfico"; uma sans geométrica para texto e uma mono só para valores financeiros; verde só para estado positivo real e vermelho só quando o significado pedir. Movimento com easing suave, entradas sobrepostas em tempos escalonados e transições por objeto compartilhado (um ponto do gráfico vira um documento), proibindo zoom constante, giro 3D, quique e transições genéricas. Ritmo de referência de ~115–120 BPM e uma cue sheet de impactos suaves e cliques discretos em vez de música protegida; tudo em Remotion, determinístico por frame (sem setTimeout), com dados sintéticos e frames de revisão antes do render final.
- Para os nossos Reels: alto — é praticamente o nosso manual de estilo: fundo escuro + dourado raro, mono para números, verde/vermelho só com significado, transição por objeto compartilhado, dados sintéticos e cue sheet sem música protegida.

### Shape morphing through UI states
- Criador: @twoclipping · Tipo: Prompt · Tags: Product UI, Charts, Music · Data: 24/09/2026
- Página: https://prompt-motion.com/twoclipping-5cba86 · Post: https://x.com/twoclipping/status/2103273003555402193
- O que o vídeo mostra: uma única forma que se transforma em 8 a 12 estados de interface (botão, loader, check, player, slider, abas, gráfico com tooltip, toast) e volta ao início em loop.
- Técnica: um HTML quadrado em que todo estilo sai de uma função `seek(t)`, sem transições CSS nem timers. As molas são calculadas em forma fechada e somadas quando o alvo muda; a câmera aproxima para cada estado ocupar o quadro, e um cursor faz cliques e arrastes reais. Uma ação cai em cada batida (120 BPM, ~14 s), com a grade de batidas extraída da música por análise numérica e os efeitos alinhados ao pico do som. O render usa Playwright com 4 subquadros fundidos por ffmpeg `tmix` para motion blur; uma regra útil é não usar `will-change` em elementos que a câmera escala, para o texto não borrar.
- Para os nossos Reels: alto — o motor `seek(t)` + molas fechadas + gráfico que se desenha com tooltip + um evento por batida é exatamente a base de um Reels de mercado com números e gráficos.

### NotchBrowser product teaser
- Criador: @jake11moran · Tipo: Prompt · Tags: Product UI, Kinetic type · Data: 24/09/2026
- Página: https://prompt-motion.com/jake11moran-f60e35 · Post: https://x.com/jake11moran/status/2103237884564414633
- O que o vídeo mostra: teaser de ~27 s, paisagem, que vai do caos de janelas abertas a um navegador escondido no notch do notebook.
- Técnica: feito em HyperFrames, com uma única câmera contínua, sem cortes, e movimentos lentos (push, pull, pan de 1,5 a 3 s, ~metade da velocidade usual) com ease in/out e motion blur só nos trechos rápidos. Texto grande e centralizado, todo em minúsculas, entrando palavra a palavra, com transição de varredura em laranja. Uma lista de ~30 tópicos gira rápido e desacelera até pousar num item seguido de "?"; o produto se revela em etapas (notch, pílula, painel); grão de filme leve, sem áudio.
- Para os nossos Reels: alto — a "roleta" de tópicos que desacelera até um item (ex.: lista de ativos/temas parando em "renda fixa?") e a câmera única e lenta sem cortes são diretamente aplicáveis; evitar a UI/ícones de marcas reais.

### Supademo launch video
- Criador: @jhylee95 · Tipo: Prompt · Tags: Product UI, Kinetic type, Music · Data: 25/09/2026
- Página: https://prompt-motion.com/jhylee95-e1152f · Post: https://x.com/jhylee95/status/2103604431627452427
- O que o vídeo mostra: vídeo de lançamento de uma ferramenta de demos interativas, com gancho imediato, cenas de prova do produto e IA, tudo cortado na batida.
- Técnica: o modelo primeiro pesquisa o valor central da marca e só então escreve a narrativa: gancho no primeiro segundo, depois cenas separadas para prova e diferencial. Visual fiel à marca, tipografia cinética, transições com ênfase e cortes rápidos de rede social. A exigência central é a sincronia: trilha composta para que cada corte, animação e troca de cena caia numa batida ou num drop, ajustando o tempo até casar.
- Para os nossos Reels: alto — "gancho no 1º segundo" + estrutura em cenas de prova + todo corte travado na batida é a receita de retenção de Reels; dá para virar regra na nossa skill.

### Food craving launch film
- Criador: @ultimaxbt · Tipo: Prompt · Tags: Product UI, Kinetic type, Photos, Music · Data: 08/10/2026
- Página: https://prompt-motion.com/ultimaxbt-2ddf1e · Post: https://x.com/ultimaxbt/status/2108210884799549714
- O que o vídeo mostra: filme de lançamento de 15 s de um app de comida em plano contínuo: pedido digitado, app "pensando", cards de pratos e cartão final da marca.
- Técnica: um arquivo HTML em que todo estilo é calculado a partir do tempo dentro de uma função de seek (sem transições CSS nem estado entre quadros), render no Playwright com 8 subquadros mesclados no ffmpeg, 1920x1080 a 60 fps. Ritmo travado em grade musical (130 BPM, 32 batidas ≈ 14,8 s, quatro fases); câmera como um único transform com zoom interpolado em escala logarítmica, molas em forma fechada e elementos compartilhados entre cenas (um botão vira a página seguinte, a cor "inunda" a tela a partir de um objeto e encolhe em outro). Texto sobe de trás de uma linha de máscara; proíbe crossfade, blur-in, 3D, partículas, câmera que inverte direção e pausas acima de 1 s. Um SFX por evento posicionado pelo pico, mix em -14 LUFS.
- Para os nossos Reels: alto — a disciplina "tudo em função de t", o zoom logarítmico, a grade de batidas definindo a duração e as transições por elemento compartilhado/inundação de cor (ótimas para ir de um número a um gráfico) aplicam-se direto ao nosso pipeline; trocar a paleta clara por escuro + dourado.

### Developer portfolio site showreel
- Criador: @wani_shola · Tipo: Prompt · Tags: Product UI, Music · Data: 26/09/2026
- Página: https://prompt-motion.com/wani-shola-16ca7a · Post: https://x.com/wani_shola/status/2103769906638459278
- O que o vídeo mostra: showreel de 90–100 s de um site-portfólio, com páginas reais animadas em molduras de navegador e de celular e um chat respondendo perguntas.
- Técnica: Remotion, 1920x1080. Usa capturas reais do site (home, páginas, modo escuro, versão móvel) dentro de molduras, sempre com o objeto principal centralizado e muito espaço negativo. Perguntas e respostas de chat aparecem em texto grande e em negrito. Paleta de três cores, fontes do próprio site, só easing suave, transições em vez de cortes secos, uma ideia por plano e ritmo que acelera e desacelera com a história. Cortes na batida de uma trilha de ~120 BPM, sem efeitos sonoros extras. Só fatos e números presentes no site, e encerramento com URL e contato.
- Para os nossos Reels: alto — "uma ideia por plano", paleta de 3 cores, pergunta e resposta em texto grande (ótimo para "Pergunta do cliente: ..."), cortes na batida e fechamento com chamada de contato se aplicam diretamente.

### Frame by Frame launch video
- Criador: @notdwd · Tipo: Prompt · Tags: Product UI, Music · Data: 27/09/2026
- Página: https://prompt-motion.com/notdwd-7de38a · Post: https://x.com/notdwd/status/2104229441211969685
- O que o vídeo mostra: "sting" de 12 s, quadrado, de um app de cursos: janela, cursor, ícone que vira barra de menu, prompt digitado, página de lição, dois cards em vidro fosco e logo em fundo preto.
- Técnica: versão anterior do mesmo prompt de @notdwd: entradas personalizáveis com valores padrão, planos que entram em movimento com desaceleração exponencial e saem com desfoque direcional, cortes secos em batidas de 124 BPM e quadro desenhado por função pura do número do frame, sem aleatório não semeado. Exige quatro quadros de teste em pontos definidos antes do render completo e lista cores proibidas.
- Para os nossos Reels: alto — mesmas lições da entrada irmã, mais o fluxo "insumos com padrão + 4 quadros de teste", que encaixa bem na nossa skill.

### Morphing UI states loop
- Criador: @demonugc · Tipo: Prompt · Tags: Product UI, Music · Data: 25/09/2026
- Página: https://prompt-motion.com/demonugc-4c5753 · Post: https://x.com/demonugc/status/2103526713208525162
- O que o vídeo mostra: uma única forma de interface que se transforma em botão, player, slider, toggle, abas, gráfico, paleta de comandos e toast, em loop perfeito no ritmo da música.
- Técnica: um só elemento muda tamanho, raio e cor por 8 a 12 estados de UI, trocando o conteúdo com um leve desfoque, conduzido por um cursor que clica e arrasta de verdade, enquanto a câmera dá zoom para cada estado preencher o quadro. Todo o movimento vem de molas calculadas em forma fechada (pouco overshoot, nada de quique), com uma ação por batida a 120 BPM ao longo de 7 compassos; a grade de batidas é extraída da trilha com numpy e os sons de UI caem nos picos medidos. O HTML (1440x1440) é uma função pura do tempo, `seek(t)`, sem transições CSS, timers nem estado entre quadros; o Playwright renderiza 4 subquadros por frame que o ffmpeg funde (tmix) em motion blur a 60 fps, e um frame por batida é gerado antes para revisão. Cuidados: não usar will-change em elementos escalados pela câmera (o texto borra), dar tempos próprios de entrada e saída aos textos que trocam e fazer o último quadro idêntico ao primeiro, inclusive na velocidade do cursor.
- Para os nossos Reels: alto — a arquitetura `seek(t)` determinística + molas em forma fechada + subquadros com tmix para motion blur + cortes amarrados à grade de batidas medida é exatamente o pipeline de que a nossa skill precisa; basta trocar o formato para 1080x1920 e a paleta para escuro e dourado.

### Prompt Motion site promo
- Criador: @antonio_kodheli · Tipo: Prompt · Tags: Product UI, Music · Data: 06/10/2026
- Página: https://prompt-motion.com/antonio-kodheli-490109 · Post: https://x.com/antonio_kodheli/status/2107518066615582893
- O que o vídeo mostra: promo de 23 s (16:9) de uma galeria de vídeos, que viaja pelo site real: grade de miniaturas, mergulho em vídeos, clique, página de prompt e "Copiado".
- Técnica: o vídeo inteiro é uma única câmera virtual que se move sobre um "mundo" (uma camada só), com uma câmera por vez, usando trilhas de foco x/y e zoom em escala logarítmica. O raio dos cantos vai a zero quando um card ocupa a tela, o que torna exatos o afastamento inicial, o mergulho rápido e o corte casado de volta. O tempo é escrito em batidas de uma música de cerca de 120 BPM (46 batidas a 30 fps), num arquivo de timeline, e os textos ficam num arquivo de cópia, sem números soltos nas cenas. Os efeitos sonoros caem nos picos medidos do áudio, e whooshes invertidos preparam cada impacto. A mixagem mira cerca de −14 LUFS. A paleta é contida, com só um acento de cor (para o marca-texto, o halo do cursor e um ponto), uma família tipográfica sem e mono, e ficam proibidos gradientes, vidro, fade em tudo, tipografia saltitante e pausas mortas. Antes do render completo, o modelo renderiza stills em cada corte, faz QA de quadros congelados e saltos de um quadro e passa por uma crítica separada.
- Para os nossos Reels: alto — é a entrada mais rica do lote. Timeline em batidas, uma câmera contínua, acento único (dourado no nosso caso), arquivo separado de textos, lista de proibições e QA por stills transpõem direto para a nossa skill 1080x1920.

### SaaS launch video
- Criador: @aschapmann · Tipo: Prompt · Tags: Product UI, Music · Data: 27/09/2026
- Página: https://prompt-motion.com/aschapmann-131210 · Post: https://x.com/aschapmann/status/2104230888812724497
- O que o vídeo mostra: lançamento de 30 s de um SaaS em 4–5 cenas com título, tipografia palavra por palavra e revelação final do logo.
- Técnica: Remotion, todo em código para poder editar e renderizar de novo. O agente lê primeiro a landing page e o código para extrair história, textos, cores e fonte. Converte o logo em SVG para animá-lo. O roteiro tem 4–5 cenas fixas: por que o mercado importa, a dor atual, a solução, o ganho do usuário. O estilo é de filme premium, com tipografia palavra por palavra, easing de mola, empurrões e panorâmicas suaves de câmera, profundidade e brilho, e elementos que se constroem na batida. Cada cena fica na tela tempo suficiente para leitura. No som, um efeito suave por elemento que aparece e silêncio no resto. Depois do render, o vídeo é revisado quadro a quadro em busca de sobreposições, cortes de borda e movimento apressado, e corrigido antes da entrega.
- Para os nossos Reels: alto — o arco de 4–5 cenas (contexto, dor, solução, benefício) serve de roteiro para Reels de finanças. A tipografia palavra por palavra com mola, o brilho sobre fundo escuro e o QA quadro a quadro após o render se aplicam diretamente.

### Spotify product film
- Criador: @brainextends · Tipo: Prompt · Tags: Product UI, Music · Data: 26/09/2026
- Página: https://prompt-motion.com/brainextends-e19ac3 · Post: https://x.com/brainextends/status/2103801834930606193
- O que o vídeo mostra: filme de produto de 18 s sobre descoberta musical num app de streaming, com um álbum fictício e fechamento na marca.
- Técnica: toda a ação acontece num "palco" retangular quase preto com cantos arredondados (~80% x 75% da tela) sobre um fundo atmosférico em degradê; uma fonte sans única (Geist/Inter), títulos brancos, secundários cinza e acento de cor só em destaques. Movimento com desaceleração e molas amortecidas sem quique repetido, UI entrando com leve inclinação em perspectiva até ficar frontal, um objeto-herói que mantém identidade entre cenas, cenas de ~1 s. Render determinístico por seek de tempo absoluto (sem timers nem transições CSS), 3 a 5 subamostras temporais por quadro, inspeção por folha de contato; trilha ~120 BPM com entradas nos eventos musicais e SFX abaixo da música. Proíbe partículas, flares, tremor de câmera, marca d'água e contadores de progresso.
- Para os nossos Reels: alto — o "palco escuro sobre fundo atmosférico" adapta-se perfeitamente para preto + degradê dourado, e o objeto-herói persistente (ex.: uma moeda ou um card de ativo) amarra 60 s; descartar a marca real.

### White ball UI motion loop
- Criador: @rossaxbt · Tipo: Prompt · Tags: Product UI, Music · Data: 10/10/2026
- Página: https://prompt-motion.com/rossaxbt-94583b · Post: https://x.com/rossaxbt/status/2108933141406638456
- O que o vídeo mostra: loop de 10 s em que uma bola branca percorre a interface: liga um interruptor, enche um slider até 100, dispara três notificações, digita e envia uma resposta.
- Técnica: layout contínuo sem cortes, com uma única câmera que segue a bola (translação + zoom em escala logarítmica) e recua no final. Fundo quase preto com grade sutil de pontos, controles em grafite e um único acento. Pousos com mola fechada e leve achatamento no impacto; o número do slider é derivado da posição do knob e cada tecla tem tempo fixo, para qualquer quadro ser renderizável isoladamente. Som discreto a cada contato e stills de cada etapa antes do render com Playwright.
- Para os nossos Reels: alto — fundo escuro + grade de pontos + um acento é quase a nossa paleta; o contador ligado a uma barra serve para metas de rentabilidade e o "a bola nunca teleporta" é boa regra de continuidade.

### AllInvestView product promo
- Criador: @rammanq · Tipo: Prompt · Tags: Product UI, Phone, Charts · Data: 26/09/2026
- Página: https://prompt-motion.com/rammanq-f5a90f · Post: https://x.com/rammanq/status/2103788796022034553
- O que o vídeo mostra: promo de uma plataforma de acompanhamento de investimentos, com telas no celular e gráficos.
- Técnica: o pedido é uma frase aberta (fazer a plataforma parecer impressionante, esforço máximo), sem duração definida. O modelo resolveu com mockup de celular, dashboards e gráficos animados.
- Para os nossos Reels: alto — é o tema mais próximo do nosso (carteira e investimentos em gráficos no celular) e serve de referência visual, trocando a marca por uma interface fictícia e o visual pelo escuro + dourado. O prompt em si não ensina técnica.

### Sahi trading terminal reveal
- Criador: @dale_vaz · Tipo: Prompt · Tags: Product UI, Phone, Charts, Particles · Data: 25/09/2026
- Página: https://prompt-motion.com/dale-vaz-cc612a · Post: https://x.com/dale_vaz/status/2103290592679879074
- O que o vídeo mostra: um terminal de trading nasce de um ponto numa tela preta, abre janelas de gráfico, posições, cadeia de opções e watchlist, e termina num celular deitado.
- Técnica: a narrativa é um "powers of ten" de interface: começa num único ponto sobre fundo preto, as janelas se desdobram e a câmera aproxima e afasta em várias escalas. No clímax, a câmera recua até o desktop inteiro virar um ponto e depois mergulha de volta para revelar a versão mobile, com a tela dividida entre gráfico e opções. Tudo numa animação JavaScript autocontida, com ênfase em detalhe e precisão das telas.
- Para os nossos Reels: alto — o zoom de escala (ponto, painel de mercado, ponto de novo) com gráficos e cadeia de opções genéricos é uma abertura forte para Reels sobre bolsa; basta trocar a marca por UI fictícia em preto e dourado.

### UGC ad generator promo
- Criador: @twoclipping · Tipo: Prompt · Tags: Product UI, Phone, Photos, Music · Data: 23/09/2026
- Página: https://prompt-motion.com/twoclipping-6dd14e · Post: https://x.com/twoclipping/status/2102554209166000267
- O que o vídeo mostra: promo de um gerador de anúncios UGC: gancho em texto, interface, parede de clipes com varredura, números grandes, carrossel 3D, celular com resultados, ticker de palavras e logo.
- Técnica: 10 compassos de 2 s a 120 BPM, com storyboard fechado na grade de batidas antes de escrever código. Minimalismo com muito vazio, uma ideia por plano, uma única cor de destaque, sans com tracking apertado, revelação de texto por máscara e nenhum ponto final em tela; transições por match cut com posições medidas em tempo de execução e cortes sempre no tempo forte. Lista longa de clichês proibidos (partículas explodindo, RGB split, tremor, flare, neon) e uma pegadinha técnica: nunca aplicar opacidade ou filtro em elemento `preserve-3d`, só no wrapper. Exige ~20 quadros de teste antes do render.
- Para os nossos Reels: alto — gancho palavra por palavra, bloco de estatísticas grandes, ticker e "uma ideia por plano com um só acento" se traduzem direto para Reels de mercado em escuro + dourado.

### Launch video remake comparison
- Criador: @notdwd · Tipo: Prompt · Tags: Product UI, Photos, Music · Data: 28/09/2026
- Página: https://prompt-motion.com/notdwd-c2037d · Post: https://x.com/notdwd/status/2104401208958230764
- O que o vídeo mostra: "sting" de lançamento de 12 s, quadrado, em estética keynote branca e azul: janela de app, cursor, ícone que vira barra de menu, prompt digitado, página de resposta, cards e cartão final preto.
- Técnica: oito cenas com tempos em número de quadro e cortes presos a batidas de 124 BPM. Cada plano entra já em movimento com desaceleração exponencial e sai acelerando ou com rampa de desfoque proporcional à velocidade; não há corte sobre quadro parado. A página é desenhada por função pura do número do quadro, com tabelas de keyframes e sem `Math.random` (só hashes com semente, para o render ser determinístico). Áudio sintetizado e masterizado em −14 LUFS; paleta restrita com cores proibidas listadas.
- Para os nossos Reels: alto — a regra "entra em movimento, sai com desfoque de velocidade", os keyframes por quadro e o aleatório com semente são diretamente aplicáveis ao nosso render quadro a quadro.

### Ora 2 image model launch film
- Criador: @rossaxbt · Tipo: Prompt · Tags: Product UI, Photos, Music · Data: 07/10/2026
- Página: https://prompt-motion.com/rossaxbt-3085b7 · Post: https://x.com/rossaxbt/status/2107845961691091295
- O que o vídeo mostra: filme de lançamento quadrado de 22 s de um modelo de imagens, em 7 cenas sincronizadas com narração sintética e música com drop.
- Técnica: um único canvas HTML em que cada quadro é função pura do tempo, renderizado com Playwright a 60 fps com 8 subquadros por quadro (motion blur) e codificado no ffmpeg; antes de entregar, gera folha de contato e checa saltos entre quadros. Câmera em deriva contínua (zoom de 1.0 a 1.04 por cena) e cada cena nova começa no zoom em que a anterior terminou, para não haver pulo; fades de no mínimo 0,3 s, trocas de imagem na semicolcheia e de cena no início das frases faladas. Legendas surgem palavra a palavra no instante da fala; painéis em "vidro líquido" (desfoque do fundo, brilho no topo, sombra suave) e palavra-chave em gradiente de marca. Áudio com ducking da música sob a voz (voz ~9 dB acima nos médios), um SFX curto por evento alinhado ao pico e mix final em -14 LUFS; proíbe flashes brancos, cortes secos e 3D.
- Para os nossos Reels: alto — a arquitetura (canvas determinístico + Playwright + subquadros + ffmpeg), a legenda palavra-a-palavra presa à narração, a câmera com zoom contínuo e as regras de mix (ducking, -14 LUFS) são exatamente o que um Reels de 60 s com locução precisa; trocar fundo branco por escuro + dourado.

## Médio: aproveitáveis com adaptação (85)

### Animated agent session story
- Criador: @jake11moran · Tipo: Skill · Tags: Characters · Data: 24/09/2026
- Página: https://prompt-motion.com/jake11moran-a269c4 · Post: https://x.com/jake11moran/status/2103247490237825416
- Instalação (só Skill): `npx skills add heygen-com/hyperframes-community-skills --skill session-story` · Repo: https://github.com/heygen-com/hyperframes-community-skills/tree/master/skills/session-story
- O que o vídeo mostra: curta animado com personagens e trilha que conta uma sessão típica de trabalho entre o usuário e o agente de código.
- Técnica: a skill lê o histórico local de sessões do agente, escolhe uma sessão representativa e a converte em roteiro de um filme curto com música, renderizado em HyperFrames. A página não detalha estilo, ritmo ou som; isso está no SKILL.md do repositório, não consultado aqui.
- Para os nossos Reels: médio — o padrão "dados reais viram roteiro automaticamente" serve para gerar Reels a partir de um relatório de mercado ou planilha; vale ler o repositório (é a mesma família HyperFrames do teaser acima).

### Lighthouse keeper silent short
- Criador: @KamStudioLabs · Tipo: Prompt · Tags: Characters · Data: 23/09/2026
- Página: https://prompt-motion.com/kamstudiolabs-0b0824 · Post: https://x.com/KamStudioLabs/status/2102908742518100086
- O que o vídeo mostra: um curta silencioso de 45 s sobre um faroleiro, sem diálogos.
- Técnica: proíbe diálogo e exige que o som conte metade da história (ambiência, efeitos, música). O modelo inventa o enredo.
- Para os nossos Reels: médio — o princípio de que o desenho de som carrega a narrativa vale para Reels sem locução (assistidos no mudo ou com trilha), com efeitos sonoros marcando cada virada.

### Scrabble tile character story
- Criador: @Anilraok · Tipo: Prompt · Tags: Characters · Data: 24/09/2026
- Página: https://prompt-motion.com/anilraok-eff262 · Post: https://x.com/Anilraok/status/2103087766662009118
- O que o vídeo mostra: uma pequena história em 3D com peças de jogo de letras como personagens, promovendo um app de quebra-cabeça.
- Técnica: o modelo primeiro inventa uma história que promova o app de forma sutil ou que gere engajamento, e depois a anima em Three.js com ambição de qualidade "estilo Pixar". O roteiro é a primeira etapa, separada da animação.
- Para os nossos Reels: médio — o fluxo "primeiro a história, depois a animação" e a promoção sutil (não comercial) servem para Reels narrativos; os personagens poderiam ser objetos, como moedas e blocos, em vez de pessoas.

### Shadow theatre home story
- Criador: @x4b47x · Tipo: Prompt · Tags: Characters · Data: 24/09/2026
- Página: https://prompt-motion.com/x4b47x-9cc84f · Post: https://x.com/x4b47x/status/2103019799614034026
- O que o vídeo mostra: uma animação vertical em estilo de teatro de sombras com recortes de papel, sobre o que faz um lugar ser um lar.
- Técnica: as restrições técnicas são claras: JavaScript puro, formato 9:16, entre 30 e 60 s, e áudio gerado por código (sem arquivos de som externos). O conceito parte de uma pergunta aberta e de uma única linguagem visual, o teatro de sombras.
- Para os nossos Reels: médio — o formato vertical de 30 a 60 s com áudio sintetizado é exatamente o nosso; dá para adaptar silhuetas recortadas em dourado sobre fundo escuro para contar histórias, como "o que é liberdade financeira".

### Recursion explained in genres
- Criador: @emollick · Tipo: Prompt · Tags: Characters, Code · Data: 26/09/2026
- Página: https://prompt-motion.com/emollick-8661a8 · Post: https://x.com/emollick/status/2103688362960019567
- O que o vídeo mostra: explicação de recursão em segmentos rápidos, cada um num gênero visual diferente.
- Técnica: prompt de uma linha: explicar um conceito várias vezes, trocando radicalmente de gênero a cada trecho, com tom autorreferente e ritmo acelerado. A variedade de estilos é o que segura a atenção.
- Para os nossos Reels: médio — o formato "um conceito, vários estilos" pode render um Reels sobre juros compostos ou diversificação, desde que os estilos fiquem dentro da paleta escura + dourado.

### DeFi Saver stop-motion explainer
- Criador: @_nikolajankovic · Tipo: Prompt · Tags: Charts, Diagrams · Data: 23/09/2026
- Página: https://prompt-motion.com/nikolajankovic-ce4ff4 · Post: https://x.com/_nikolajankovic/status/2102867033100616097
- O que o vídeo mostra: explicador em estilo stop-motion desenhado à mão, com gráficos e diagramas, em que um produto de finanças descentralizadas se apresenta em primeira pessoa.
- Técnica: duas instruções apenas: estética de stop-motion feito à mão e narrativa em que o próprio produto se explica em primeira pessoa. Ritmo, paleta, som e render ficaram com o modelo.
- Para os nossos Reels: médio — tema financeiro e a ideia de o conceito "falar por si" (ex.: o CDI se explicando) são aproveitáveis; o visual stop-motion à mão pode virar variação de série, mas foge do padrão escuro/dourado.

### Derivative concept explainer
- Criador: @LinearUncle · Tipo: Prompt · Tags: Charts, Diagrams · Data: 24/09/2026
- Página: https://prompt-motion.com/linearuncle-5d2bae · Post: https://x.com/LinearUncle/status/2103128559174971663
- O que o vídeo mostra: aula animada sobre derivadas com gráficos matemáticos e narração sintetizada.
- Técnica: prompt em chinês pedindo explicação didática, com exemplos práticos e um tom que faça pensar, renderizada em Manim e narrada com edge-tts. O peso está na escolha da ferramenta (animação matemática) e na voz gerada.
- Para os nossos Reels: médio — Manim + TTS é uma rota para explicar juros compostos ou volatilidade com curvas precisas; o visual padrão do Manim precisaria ser adaptado ao escuro + dourado.

### Mathematics motion showreel
- Criador: @Math_files · Tipo: Prompt · Tags: Charts, Diagrams · Data: 28/09/2026
- Página: https://prompt-motion.com/math-files-39c9d0 · Post: https://x.com/Math_files/status/2104486181853610052
- O que o vídeo mostra: showreel de ~20 s sobre matemática, com gráficos e diagramas animados.
- Técnica: brief aberto de 20 s que pede um showreel ao mesmo tempo de motion e de matemática, em grande escala; não fixa estilo, câmera, som nem ferramenta. O vídeo resultante se apoia em gráficos e diagramas.
- Para os nossos Reels: médio — o vídeo é boa referência visual de gráficos/curvas animadas (juros compostos, curvas de rendimento), mas o prompt não ensina como fazê-los.

### Backlink audit data promo
- Criador: @PalashBagchi11 · Tipo: Prompt · Tags: Charts, Kinetic type · Data: 24/09/2026
- Página: https://prompt-motion.com/palashbagchi11-0a4b6b · Post: https://x.com/PalashBagchi11/status/2102924409124389221
- O que o vídeo mostra: uma peça promocional de dados de auditoria de SEO, com gráficos e tipografia cinética (pelo título e pelas tags).
- Técnica: o prompt publicado é só a etapa final de uma conversa. Ele pede uma trilha rápida e livre de royalties e a entrega em duas proporções, horizontal e vertical. Ou seja, mostra o vídeo sendo construído para gerar as duas versões a partir da mesma base.
- Para os nossos Reels: médio — a combinação de gráficos de dados com texto cinético é próxima do nosso tema, e a ideia de exportar 9:16 e 16:9 da mesma composição é útil.

### Moroccan political history timeline
- Criador: @TrigLyceee · Tipo: Prompt · Tags: Charts, Kinetic type · Data: 26/09/2026
- Página: https://prompt-motion.com/triglyceee-bd5b08 · Post: https://x.com/TrigLyceee/status/2103804459986161719
- O que o vídeo mostra: linha do tempo animada da vida política do Marrocos desde a independência.
- Técnica: uma frase em francês pedindo um resumo histórico em vídeo; o modelo escolhe o formato de linha do tempo com dados e texto cinético. Sem especificações de estilo ou render.
- Para os nossos Reels: médio — o formato "linha do tempo com marcos e números" se adapta bem a Reels como "a história da Selic" ou "crises da bolsa desde 1990" (sem pessoas reais).

### Studio1 intro showreel
- Criador: @Astrodevil_ · Tipo: Prompt · Tags: Charts, Kinetic type · Data: 25/09/2026
- Página: https://prompt-motion.com/astrodevil-3f2054 · Post: https://x.com/Astrodevil_/status/2103600734017392708
- O que o vídeo mostra: vídeo de lançamento de 15 s que apresenta um estúdio a partir dos números de um estudo de caso.
- Técnica: além do pedido padrão de showreel, o prompt manda o modelo usar dados reais de um estudo de caso como matéria-prima. Gráficos e tipografia cinética transformam esses números em cenas. Ancorar o vídeo em dados fornecidos, em vez de inventados, é o ponto relevante.
- Para os nossos Reels: médio — a lógica de "alimentar com um documento de dados e animar os números" é exatamente a de um Reels sobre um relatório de mercado.

### Recruiter self-intro reel
- Criador: @blushpetal795 · Tipo: Prompt · Tags: Charts, Kinetic type, Particles · Data: 26/09/2026
- Página: https://prompt-motion.com/blushpetal795-0c85c2 · Post: https://x.com/blushpetal795/status/2103744870041170220
- O que o vídeo mostra: uma autoapresentação de 15 s para recrutadores, com gráficos, texto cinético e partículas.
- Técnica: o mesmo briefing de showreel de 15 s, com o enquadramento de "apresentar-se a um recrutador". Pelas tags, o resultado mistura gráficos de dados com tipografia, como um currículo animado.
- Para os nossos Reels: médio — o formato "apresentação pessoal com números animados" serve para um Reels de apresentação do assessor (anos de experiência, clientes, certificações), sem rosto.

### Bold typographic motion showreel
- Criador: @motiondsgnr · Tipo: Prompt · Tags: Charts, Kinetic type, Shapes · Data: 26/09/2026
- Página: https://prompt-motion.com/motiondsgnr-9dcfa6 · Post: https://x.com/motiondsgnr/status/2103692944771313960
- O que o vídeo mostra: showreel de 15 s com tipografia grande e marcante, formas geométricas e gráficos animados.
- Técnica: usa o prompt padrão de showreel de currículo (15 s, "go all out"), sem especificar estilo. Pelas tags, o resultado combina tipografia cinética pesada com formas geométricas e elementos de gráfico em sequência rápida. É a referência de "type + shapes + charts" do lote.
- Para os nossos Reels: médio — a mistura de tipografia forte com mini-gráficos funciona em abertura de Reels financeiro, mas é preciso escrever as regras de estilo (o prompt não traz nenhuma).

### AI data centre 3D film
- Criador: @mdaman010 · Tipo: Prompt · Tags: Diagrams · Data: 26/09/2026
- Página: https://prompt-motion.com/mdaman010-e7226a · Post: https://x.com/mdaman010/status/2103845689713111079
- O que o vídeo mostra: um passeio 3D explicativo pelo interior de um data center de IA (racks, refrigeração, fluxo de dados).
- Técnica: HTML puro, esforço alto, uma tentativa. O prompt é uma única pergunta aberta, do tipo "mostre o que acontece dentro de". O modelo decide a estrutura didática (camadas, fluxos, diagramas em perspectiva). Funciona como explicador visual de um sistema complexo.
- Para os nossos Reels: médio — o formato "mostre o que acontece dentro de X" combina com temas financeiros (dentro de uma bolsa, do caminho de uma ordem, de um fundo).

### AI data centre 3D tour
- Criador: @Sayan_shanky · Tipo: Prompt · Tags: Diagrams · Data: 26/09/2026
- Página: https://prompt-motion.com/sayan-shanky-f850d8 · Post: https://x.com/Sayan_shanky/status/2103736579449868515
- O que o vídeo mostra: tour 3D em HTML pelo interior de um data center de IA.
- Técnica: prompt de uma linha pedindo para "mostrar o que acontece dentro" de um data center; formato de tour 3D em HTML, com diagramas, foi escolha do modelo (esforço alto, uma tentativa). Sem detalhes de estilo, ritmo ou som.
- Para os nossos Reels: médio — o formato "tour por dentro de" serve para explicar mecanismos (por dentro de um fundo, de uma bolsa de valores) e o tema data center rende pauta de investimento em IA.

### Celld job ownership explainer
- Criador: @0xnfrith · Tipo: Prompt · Tags: Diagrams · Data: 25/09/2026
- Página: https://prompt-motion.com/0xnfrith-5be616 · Post: https://x.com/0xnfrith/status/2103358957050068999
- O que o vídeo mostra: explicador animado, com diagramas, do valor de um produto de gestão de tarefas.
- Técnica: o prompt só pede uma animação que justifique por que o produto merece existir (proposta de valor); não há especificação de estilo, duração, som ou render. A forma de diagrama foi escolha do modelo.
- Para os nossos Reels: médio — o enquadramento "por que isto merece seu lugar na carteira" é um bom gancho de roteiro para explicar um ativo, mas não traz técnica visual.

### First & 10 yellow line explainer
- Criador: @blueoctopusai · Tipo: Prompt · Tags: Diagrams · Data: 30/09/2026
- Página: https://prompt-motion.com/blueoctopusai-dd17bd · Post: https://x.com/blueoctopusai/status/2105116391439270222
- O que o vídeo mostra: explicativo de como funciona a linha amarela virtual das transmissões de futebol americano.
- Técnica: prompt de uma linha que só pede um vídeo explicando um mecanismo do mundo real; toda a direção visual fica com o modelo. Vale como prova de que "explique como X funciona" já rende um diagrama animado, desde que o assunto seja um processo concreto.
- Para os nossos Reels: médio — o formato "como funciona X" serve para mecanismos financeiros (como a Selic chega ao crédito), mas a direção precisa vir da nossa skill.

### Negroni recipe animation
- Criador: @Ror_Fly · Tipo: Prompt · Tags: Diagrams · Data: 23/09/2026
- Página: https://prompt-motion.com/ror-fly-9950f1 · Post: https://x.com/Ror_Fly/status/2102853258582880547
- O que o vídeo mostra: explicativo de 30 s em que um copo vazio recebe cada ingrediente, com a medida indicada, até virar o drinque pronto.
- Técnica: pedido curto de explainer passo a passo: cada componente entra com seu rótulo e quantidade, e o recipiente vai enchendo até o resultado final. O autor deixa o modelo escolher entre JS e HTML; não define estilo nem som.
- Para os nossos Reels: médio — a metáfora do recipiente que enche com ingredientes rotulados serve bem para "montando uma carteira" (renda fixa, ações, FIIs com percentuais).

### Prompting mistakes video tutorial
- Criador: @henkvaness · Tipo: Prompt · Tags: Diagrams · Data: 26/09/2026
- Página: https://prompt-motion.com/henkvaness-0e06af · Post: https://x.com/henkvaness/status/2103801351993975279
- O que o vídeo mostra: tutorial educativo sobre erros comuns na escrita de prompts, gerado a partir de um artigo.
- Técnica: o insumo é um artigo de texto e o pedido é transformá-lo em vídeo educativo, em one-shot. A página não traz estilo, duração nem render; o interessante é o fluxo "texto longo vira vídeo".
- Para os nossos Reels: médio — o fluxo "artigo, relatório ou carta mensal vira vídeo" é útil para converter o conteúdo escrito do assessor em Reels.

### Replica symmetry breaking whiteboard
- Criador: @tak3sh8 · Tipo: Prompt · Tags: Diagrams · Data: 26/09/2026
- Página: https://prompt-motion.com/tak3sh8-be5012 · Post: https://x.com/tak3sh8/status/2103667481139441895
- O que o vídeo mostra: animação de lousa desenhada à mão explicando a quebra de simetria de réplicas no modelo SK de vidros de spin.
- Técnica: fluxo em duas etapas: primeiro uma animação curta, em estilo quadro branco com traço feito à mão, explicando o conceito; depois a mesma peça exportada em MP4 com narração. O prompt não fixa duração, paleta nem ferramenta; o valor está no formato didático em duas passadas (visual, depois voz).
- Para os nossos Reels: médio — o estilo "lousa" e o fluxo visual-depois-narração servem para explicar conceitos (juros compostos, marcação a mercado, duration), com traço dourado sobre fundo escuro no lugar do quadro branco.

### Pixel art LLM history
- Criador: @PluginPlay__ · Tipo: Prompt · Tags: Diagrams, Characters · Data: 26/09/2026
- Página: https://prompt-motion.com/pluginplay-3d4006 · Post: https://x.com/PluginPlay__/status/2103910844677472343
- O que o vídeo mostra: animação em pixel art que conta a história dos LLMs, chega ao autoaperfeiçoamento recursivo e termina em caos crescente.
- Técnica: o vídeo cabe num único arquivo HTML autocontido, de até 15 s, em três atos (histórico → virada → escalada caótica). O render é em "bumerangue": a animação toca para frente e depois de trás para frente.
- Para os nossos Reels: médio — a linha do tempo em três atos com escalada serve para "história das crises do mercado", e o HTML autocontido bate com a nossa stack. Pixel art e bumerangue não combinam com o tom premium.

### What is Git explainer
- Criador: @Yunn260414 · Tipo: Prompt · Tags: Diagrams, Code · Data: 27/09/2026
- Página: https://prompt-motion.com/yunn260414-60d996 · Post: https://x.com/Yunn260414/status/2104044910769016888
- O que o vídeo mostra: explicador animado em JavaScript, com narração em chinês, que ensina Git do zero.
- Técnica: vídeo gerado em JS, didático e progressivo, para quem não tem base nenhuma, cobrindo também os comandos comuns; exige narração em áudio e libera instalar ferramentas e pesquisar na web. Visual e ritmo ficam livres.
- Para os nossos Reels: médio — o molde "explicar do zero, em camadas, com narração" é o que um assessor precisa para educação financeira; trocar idioma para PT-BR.

### Risograph studio intro
- Criador: @rneayan · Tipo: Prompt · Tags: Diagrams, Kinetic type · Data: 25/09/2026
- Página: https://prompt-motion.com/rneayan-474bcf · Post: https://x.com/rneayan/status/2103401006281441493
- O que o vídeo mostra: uma apresentação de estúdio com estética de impressão risográfica (granulado, cores chapadas, registro desalinhado) e diagramas.
- Técnica: a técnica toda é nomear uma estética de impressão conhecida, que já carrega textura, paleta limitada e desalinhamento. Com essa referência, o modelo resolve o resto.
- Para os nossos Reels: médio — mostra que nomear uma linguagem gráfica concreta funciona; para nós valeria testar textura de papel-moeda ou gravura de cédula em dourado.

### History of AI timeline
- Criador: @kloss_xyz · Tipo: Prompt · Tags: Diagrams, Kinetic type, Particles · Data: 26/09/2026
- Página: https://prompt-motion.com/kloss-xyz-fe0c31 · Post: https://x.com/kloss_xyz/status/2103652674336067876
- O que o vídeo mostra: linha do tempo animada com os marcos da história da IA.
- Técnica: prompt de uma frase pedindo um vídeo com momentos-chave de uma história; a forma de linha do tempo com datas e texto cinético foi escolha do modelo.
- Para os nossos Reels: médio — o formato linha do tempo serve bem para "crises que o mercado já superou" ou "história da Selic", com marcos em dourado sobre fundo escuro.

### Festival lineup promo reel
- Criador: @GonzaloMacagno · Tipo: Prompt · Tags: Kinetic type · Data: 23/09/2026
- Página: https://prompt-motion.com/gonzalomacagno-2de1a9 · Post: https://x.com/GonzaloMacagno/status/2102897651008344202
- O que o vídeo mostra: um reel publicitário de 10 s com a programação de um festival em tipografia cinética.
- Técnica: o prompt, em espanhol, passa as informações brutas (a lista de atrações) e pede um reel "bem publicitário" de 10 s; o modelo hierarquiza os dados em texto cinético.
- Para os nossos Reels: médio — o fluxo "dados brutos para hierarquia tipográfica animada" serve para agenda econômica da semana (Copom, payroll, balanços) em formato vertical.

### Overthinking motion study
- Criador: @gizakdag · Tipo: Prompt · Tags: Kinetic type · Data: 25/09/2026
- Página: https://prompt-motion.com/gizakdag-cf4ae6 · Post: https://x.com/gizakdag/status/2103566030916239768
- O que o vídeo mostra: estudo de tipografia cinética de 15 s sobre o tema "overthinking".
- Técnica: showreel de 15 s guiado por um tema abstrato (excesso de pensamento) e por imagens de referência anexadas, que definem o estilo. Não há instruções explícitas de paleta, câmera ou render; a força vem do anexo de referências.
- Para os nossos Reels: médio — o tema (ansiedade/excesso de análise) conversa com psicologia do investidor, e a tática de anexar referências visuais para travar o estilo é útil.

### Chaotic Claude POV video
- Criador: @kloss_xyz · Tipo: Prompt · Tags: Kinetic type, Code · Data: 26/09/2026
- Página: https://prompt-motion.com/kloss-xyz-15182a · Post: https://x.com/kloss_xyz/status/2103664956482941143
- O que o vídeo mostra: vídeo vertical 9:16 caótico, estilo "brain rot", narrado em primeira pessoa por uma IA sobre seu dia a dia.
- Técnica: geração inteira em Python com render final no ffmpeg, em formato vertical. Pede narrativa em primeira pessoa com personalidade forte, motion e sound design de alto nível; tipografia cinética como protagonista. Não especifica paleta, ritmo ou duração.
- Para os nossos Reels: médio — confirma pipeline Python + ffmpeg em 9:16 e o recurso de narrador em primeira pessoa (ex.: "eu sou a Selic..."), mas o tom caótico não serve.

### What day is it
- Criador: @tankazunori0914 · Tipo: Prompt · Tags: Kinetic type, Music · Data: 02/10/2026
- Página: https://prompt-motion.com/tankazunori0914-0fc886 · Post: https://x.com/tankazunori0914/status/2105917770907156748
- O que o vídeo mostra: uma peça de tipografia cinética com trilha que responde, em 30 s, qual é o dia da semana de hoje.
- Técnica: prompt mínimo em japonês que transforma uma pergunta banal num motion de 30 s com música, pedindo ao modelo esforço máximo. Feito com Opus 5.5 sobre o HyperFrames, que cuida da renderização quadro a quadro. A página não traz estilo, paleta nem tipografia: toda a direção visual fica com o modelo.
- Para os nossos Reels: médio — a ideia de responder uma pergunta simples ("que dia é hoje?") com tipografia cinética serve de abertura para um Reels de agenda da semana (Copom, payroll, balanços), desde que a gente defina a paleta e o ritmo.

### Particle sphere motion reel
- Criador: @blue_clarity · Tipo: Prompt · Tags: Kinetic type, Particles · Data: 25/09/2026
- Página: https://prompt-motion.com/blue-clarity-ef56d0 · Post: https://x.com/blue_clarity/status/2103564589065449603
- O que o vídeo mostra: reel de 15 s centrado numa esfera de partículas com tipografia cinética.
- Técnica: brief aberto de showreel de 15 s, com esforço médio e uma iteração; esfera de partículas e tipo cinético foram escolhas do modelo, não instruções.
- Para os nossos Reels: médio — uma esfera/nuvem de partículas douradas sobre fundo escuro é um bom elemento de abertura ou de transição; o prompt em si não ajuda.

### Engraving-style Claude ad
- Criador: @LexnLin · Tipo: Prompt · Tags: Kinetic type, Photos · Data: 02/10/2026
- Página: https://prompt-motion.com/lexnlin-038035 · Post: https://x.com/LexnLin/status/2106101651010449796
- O que o vídeo mostra: anúncio rápido de 10 a 15 s com imagens editoriais em estilo gravura, grafismos pintados sobre as fotos e texto que se transforma.
- Técnica: o prompt parte de um vídeo de referência de 5 s e pede para copiar a duração dos planos e as transições, não o design. Pede pesquisa de peças anteriores da marca, modo claro limpo (evitando o "bege artístico" e rótulos pequenos sobre títulos), imagens que crescem, encolhem ou se multiplicam, morph de texto perfeito e zooms. Termina obrigatoriamente no logo.
- Para os nossos Reels: médio — a ideia de usar um vídeo de referência só para medir cortes e ritmo é útil; o resto depende de marca e fotos, que não usamos.

### Handwoven textiles brand explainer
- Criador: @AmitSingha89 · Tipo: Prompt · Tags: Kinetic type, Photos · Data: 26/09/2026
- Página: https://prompt-motion.com/amitsingha89-150378 · Post: https://x.com/AmitSingha89/status/2103737604277780553
- O que o vídeo mostra: um vídeo explicativo de uma marca de tecidos artesanais, com fotos e texto animado.
- Técnica: o briefing aponta só o site da marca e define o público como quem visita pela primeira vez. O modelo deriva roteiro, fotos e tom a partir do site. O recorte de público ("primeiro contato") orienta o nível de explicação.
- Para os nossos Reels: médio — o recorte "explicar para quem nunca ouviu falar" é um bom molde para Reels educativos de investimento, como "o que é um FII, para quem nunca investiu".

### Claude self-intro motion graphic
- Criador: @1littlecoder · Tipo: Prompt · Tags: Kinetic type, Shapes · Data: 25/09/2026
- Página: https://prompt-motion.com/1littlecoder-9fef89 · Post: https://x.com/1littlecoder/status/2103587706999914649
- O que o vídeo mostra: motion de 10 s em que a IA se apresenta, com tipografia cinética e formas.
- Técnica: 10 s, máximo de criatividade e dinamismo, com uma restrição explícita: nada de molduras nem textos encostados nos cantos, vistos como marca registrada de vídeo feito por IA. Resto em aberto.
- Para os nossos Reels: médio — a restrição anti-"cara de IA" (sem bordas, sem rótulos nos cantos) é uma regra simples e valiosa para nossa skill.

### Code-only motion design reel
- Criador: @johnsavage_ai · Tipo: Prompt · Tags: Kinetic type, Shapes · Data: 25/09/2026
- Página: https://prompt-motion.com/johnsavage-ai-b091c0 · Post: https://x.com/johnsavage_ai/status/2103600308010041677
- O que o vídeo mostra: showreel de 15 s feito só com código, à base de texto e formas geométricas.
- Técnica: o diferencial é a restrição de usar apenas código, sem imagens nem ferramentas externas. Tudo o que aparece (tipografia, formas, movimento) é desenhado e animado programaticamente.
- Para os nossos Reels: médio — "só código, zero assets" é exatamente a nossa regra (sem logos nem fotos). Mostra que dá para ter um resultado rico só com texto e geometria.

### Geometric motion designer showreel
- Criador: @LeonKohli · Tipo: Prompt · Tags: Kinetic type, Shapes · Data: 25/09/2026
- Página: https://prompt-motion.com/leonkohli-6dc01b · Post: https://x.com/LeonKohli/status/2103517696038191220
- O que o vídeo mostra: showreel de 15 s baseado em formas geométricas e tipografia cinética.
- Técnica: é o template padrão de showreel. O modelo construiu tudo a partir de primitivas geométricas (círculos, barras, linhas) que se transformam junto com o texto.
- Para os nossos Reels: médio — formas geométricas que viram barras ou linhas de gráfico são uma ponte natural para visualizar dados financeiros.

### Swiss-style motion showreel
- Criador: @levabashidze · Tipo: Prompt · Tags: Kinetic type, Shapes · Data: 26/09/2026
- Página: https://prompt-motion.com/levabashidze-2d713a · Post: https://x.com/levabashidze/status/2103786742520184909
- O que o vídeo mostra: showreel de 15 s em linguagem suíça, com grid, sans-serif e formas geométricas.
- Técnica: é o desafio padrão de showreel de 15 s, com a instrução extra de não fazer perguntas e entregar direto (esforço máximo). O modelo escolheu sozinho o estilo tipográfico internacional: grid rígido, composição assimétrica e formas simples animadas com o texto.
- Para os nossos Reels: médio — grid suíço com sans-serif forte casa bem com dados financeiros e paleta escura + dourado. Vale como direção tipográfica.

### Type, form, space showreel
- Criador: @Web3Wesley · Tipo: Prompt · Tags: Kinetic type, Shapes · Data: 26/09/2026
- Página: https://prompt-motion.com/web3wesley-7bb108 · Post: https://x.com/Web3Wesley/status/2103644329294365164
- O que o vídeo mostra: showreel abstrato de 15 s explorando tipografia, forma e espaço.
- Técnica: prompt padrão de showreel, rodado com esforço máximo numa tentativa. Pelo título e pelas tags, o modelo organizou o vídeo em três "capítulos" visuais (tipo, forma, espaço), com tipografia cinética e geometria.
- Para os nossos Reels: médio — dividir em capítulos com rótulo, à moda de "tipo/forma/espaço", serve para Reels em 3 atos (ex.: "Risco · Prazo · Retorno").

### Blue editorial motion showreel
- Criador: @fionntobin · Tipo: Prompt · Tags: Kinetic type, Shapes, Music · Data: 25/09/2026
- Página: https://prompt-motion.com/fionntobin-97b7af · Post: https://x.com/fionntobin/status/2103510776690479597
- O que o vídeo mostra: showreel de 15 s com visual editorial em azul, tipografia animada, formas e trilha.
- Técnica: usa o template de showreel de 15 s numa tentativa só. O modelo optou por uma paleta praticamente monocromática (azul) e diagramação de revista, com texto e formas sincronizados à música.
- Para os nossos Reels: médio — confirma que uma paleta de uma cor dominante com layout editorial fica sofisticada. É a mesma lógica do nosso escuro + dourado.

### Easing and morphing showreel
- Criador: @RoundtableSpace · Tipo: Prompt · Tags: Kinetic type, Shapes, Music · Data: 28/09/2026
- Página: https://prompt-motion.com/roundtablespace-d3a1be · Post: https://x.com/RoundtableSpace/status/2104424611010232366
- O que o vídeo mostra: showreel de 15 s focado em curvas de easing e morphing de formas, no tempo da música.
- Técnica: o prompt é só "showreel de 15 s, esforço máximo"; o foco em easing e morphing veio do modelo. Sem especificação de estilo, som ou render.
- Para os nossos Reels: médio — morphing (ex.: barra que vira linha, moeda que vira gráfico) é uma transição forte para finanças; vale ver o vídeo como referência.

### EyezOn 100 users thank-you
- Criador: @Sudiyasa_ · Tipo: Prompt · Tags: Kinetic type, Shapes, Music · Data: 26/09/2026
- Página: https://prompt-motion.com/sudiyasa-f48ac9 · Post: https://x.com/Sudiyasa_/status/2103638831669076027
- O que o vídeo mostra: reel de agradecimento de 15 s pelos primeiros 100 usuários de um bot, com tipografia, formas e música.
- Técnica: prompt padrão de showreel aplicado a um marco (100 usuários). Pelas tags, o resultado celebra o número com tipografia cinética, formas geométricas e trilha.
- Para os nossos Reels: médio — o formato "celebração de marco com número grande" serve para posts de marco (ex.: "100 clientes", "5 anos de mercado"), desde que sem dados inventados.

### Kinetic type showreel
- Criador: @itsuki_dev · Tipo: Prompt · Tags: Kinetic type, Shapes, Music · Data: 25/09/2026
- Página: https://prompt-motion.com/itsuki-dev-10942d · Post: https://x.com/itsuki_dev/status/2103438087204618392
- O que o vídeo mostra: showreel de 15 s centrado em tipografia cinética e formas abstratas com música.
- Técnica: é o template padrão de showreel de 15 s. O modelo apoiou a peça na palavra como elemento principal, com formas de apoio e cortes no ritmo da trilha.
- Para os nossos Reels: médio — a abordagem "o texto é o protagonista" funciona para Reels de finanças narrados em frases curtas, mas a técnica não está descrita.

### Poster breaking its frame
- Criador: @pankajkumar_dev · Tipo: Prompt · Tags: Kinetic type, Shapes, Music · Data: 25/09/2026
- Página: https://prompt-motion.com/pankajkumar-dev-0bee87 · Post: https://x.com/pankajkumar_dev/status/2103502614134718609
- O que o vídeo mostra: um pôster tipográfico que rompe a própria moldura.
- Técnica: prompt de uma linha com um conceito visual forte (o conteúdo sai do limite do quadro). Mostra como um único conceito nomeado já organiza o vídeo.
- Para os nossos Reels: médio — o gesto de "romper a moldura" serve para um número que estoura o gráfico (ex.: dólar furando uma máxima), sem copiar o visual.

### Motion designer portrait showreel
- Criador: @ndhabarde11 · Tipo: Prompt · Tags: Kinetic type, Shapes, Particles · Data: 26/09/2026
- Página: https://prompt-motion.com/ndhabarde11-f155b4 · Post: https://x.com/ndhabarde11/status/2103832593355686104
- O que o vídeo mostra: showreel vertical de 15 s com tipografia cinética, formas e partículas.
- Técnica: o molde de showreel de 15 s, com a diferença de pedir explicitamente o formato retrato. Nada mais é especificado.
- Para os nossos Reels: médio — é uma das poucas peças nativamente verticais do lote, boa referência de composição 9:16, mas sem técnica escrita.

### Motion techniques showreel
- Criador: @lukasersil · Tipo: Prompt · Tags: Kinetic type, Shapes, Particles · Data: 26/09/2026
- Página: https://prompt-motion.com/lukasersil-0ed38e · Post: https://x.com/lukasersil/status/2103742861971726495
- O que o vídeo mostra: showreel de 15 s que encadeia muitas técnicas (tipo cinético, geometria, fluidos, partículas, máscaras, profundidade).
- Técnica: pede variedade de técnicas avançadas, mas com cara de direção de arte coesa e não de catálogo de efeitos. A câmera deve ser fluida e contínua, com cada plano "desaguando" no seguinte, ritmo rápido e confiante e atenção à cadência das transições. Não define paleta, fonte nem ferramenta.
- Para os nossos Reels: médio — a regra "cada plano nasce do anterior, sem colagem de efeitos" é uma boa diretriz para 60 s; o resto é genérico.

### Motion design principles reel
- Criador: @tolgayhickiran · Tipo: Prompt · Tags: Kinetic type, Shapes, Particles, Music · Data: 25/09/2026
- Página: https://prompt-motion.com/tolgayhickiran-e90799 · Post: https://x.com/tolgayhickiran/status/2103619422128935120
- O que o vídeo mostra: reel de 15 s que demonstra princípios de motion design com texto, formas, partículas e música.
- Técnica: usa o template padrão de showreel (esforço médio, uma tentativa). Pelo título, o modelo organizou o vídeo como uma sequência de princípios de animação ilustrados, cada um como um pequeno bloco.
- Para os nossos Reels: médio — o formato "lista de N princípios, um bloco por item" serve para "5 regras de investimento", mas a técnica não está detalhada.

### Beat-synced bouncing 3D ball
- Criador: @Gorden_Sun · Tipo: Prompt · Tags: Music · Data: 30/09/2026
- Página: https://prompt-motion.com/gorden-sun-041f56 · Post: https://x.com/Gorden_Sun/status/2105302007896797351
- O que o vídeo mostra: uma esfera 3D cai e quica entre objetos que acendem a cada batida de uma sequência de música clássica instrumental.
- Técnica: Three.js puro (Blender proibido), com o objetivo de parecer animação 3D profissional. Os quiques e o acendimento dos objetos são sincronizados com os pontos rítmicos da música, e as trocas de cena acompanham as trocas de faixa; pede pitadas de humor.
- Para os nossos Reels: médio — a ideia de "objetos que acendem na batida" serve para destacar números/barras no compasso da trilha; a esfera em si não serve.

### Black hole time story
- Criador: @RebutonePress · Tipo: Prompt · Tags: nenhuma · Data: 25/09/2026
- Página: https://prompt-motion.com/rebutonepress-810f78 · Post: https://x.com/RebutonePress/status/2103478369245688099
- O que o vídeo mostra: narrativa de cerca de 5 minutos sobre o tempo, com tema de buraco negro, áudio e legendas.
- Técnica: o prompt, em chinês, pede uma história longa sobre o tempo, com áudio e legendas embutidos. O agente escolhe e instala sozinho as ferramentas num ambiente devshell. Ao final, ele deve apagar tudo o que for intermediário e deixar só o arquivo de vídeo. O prompt não dá direção visual.
- Para os nossos Reels: médio — a disciplina de pipeline serve para a nossa skill: legenda gravada no vídeo e limpeza dos artefatos intermediários depois do render.

### Tengwang Pavilion moonlit river
- Criador: @DemitiyaGeekzen · Tipo: Prompt · Tags: nenhuma listada (stack WebGL2, Canvas 2D, Web Audio) · Data: 25/09/2026
- Página: https://prompt-motion.com/demitiyageekzen-7770ad · Post: https://x.com/DemitiyaGeekzen/status/2103517910274818523
- O que o vídeo mostra: paisagem noturna de um pavilhão chinês clássico à beira de um rio sob a lua.
- Técnica: o prompt, em chinês, deixa o modelo deduzir um tema do gosto do usuário e escolhê-lo sozinho. Pede um vídeo de ~30 s e uma página HTML interativa, para mostrar o máximo da capacidade de front-end. A stack combina WebGL2 (água, luz), Canvas 2D (camadas) e Web Audio (som gerado no navegador).
- Para os nossos Reels: médio — a combinação WebGL2 para reflexos e brilho, Canvas 2D e Web Audio é uma boa stack para fundos noturnos com luz dourada e som sem arquivos externos.

### Collision-driven music machine
- Criador: @KamStudioLabs · Tipo: Prompt · Tags: Particles, Music · Data: 23/09/2026
- Página: https://prompt-motion.com/kamstudiolabs-447565 · Post: https://x.com/KamStudioLabs/status/2102899866762440893
- O que o vídeo mostra: uma máquina física de 45 s em que bolas ou partículas colidem, e cada colisão dispara uma nota de uma música original.
- Técnica: o princípio central é amarrar o som ao visual, porque cada nota nasce de uma colisão visível. Isso força uma simulação determinística em que os eventos de física e a partitura são a mesma linha do tempo. Foi feito em HTML numa única tentativa.
- Para os nossos Reels: médio — a regra "todo som tem uma causa visível na tela" é ótima para Reels; por exemplo, um "tick" a cada candle que fecha ou a cada número que trava.

### Email verification tool promo
- Criador: @KmAsiff · Tipo: Prompt · Tags: Product UI · Data: 26/09/2026
- Página: https://prompt-motion.com/kmasiff-cc72cb · Post: https://x.com/KmAsiff/status/2103810247131549880
- O que o vídeo mostra: promo de 20 s de uma ferramenta de verificação de e-mail, passando por muitos casos de uso.
- Técnica: pede amplitude, isto é, o máximo de casos de uso em 20 s, o que leva a cortes rápidos e variados. A estética de SaaS moderno vem de duas referências citadas: vídeos de startups de aceleradora e os vídeos sociais da própria Anthropic (esforço alto).
- Para os nossos Reels: médio — o formato "muitos casos de uso em sequência rápida" serve para "onde aplicar sua reserva de emergência", mas não há detalhe técnico.

### HTML app demo skill
- Criador: @MengTo · Tipo: Skill · Tags: Product UI · Data: 21/10/2026
- Página: https://prompt-motion.com/mengto-a7f4679 · Post: https://x.com/MengTo/status/2112843787777249661
- Instalação (só Skill): `npx skills add MengTo/Skills --skill html-demo` · Repo: https://github.com/MengTo/Skills/tree/main/agent-skills/web-design/html-demo
- O que o vídeo mostra: demo de produto numa janela estilo macOS que reproduz o uso do app passo a passo.
- Técnica: todo quadro é desenhado a partir de um único relógio, o que permite loop, scrub, pular para um passo e congelar. É o mesmo princípio do render determinístico: o estado visual é função do tempo, nunca acumulado.
- Para os nossos Reels: médio — confirma e empacota o padrão de relógio único que já usamos; útil como referência de estrutura de código, não de estética.

### Muse connector tracker promo
- Criador: @elliot_garreffa · Tipo: Prompt · Tags: Product UI · Data: 27/09/2026
- Página: https://prompt-motion.com/elliot-garreffa-f334bc · Post: https://x.com/elliot_garreffa/status/2104213514944446825
- O que o vídeo mostra: promo de um rastreador de conectores com telas de produto animadas.
- Técnica: Remotion. O diferencial está no processo: o modelo recebe URL do produto, guia de marca e um ou dois vídeos de referência, escreve primeiro um storyboard listando as funções a mostrar e só depois constrói o vídeo. O storyboard antes do código evita improviso e cenas soltas.
- Para os nossos Reels: médio — o fluxo "insumos (guia de marca + referências) → storyboard aprovado → código" deve ser uma etapa da nossa skill.

### Reddit marketing tool launch video
- Criador: @anthonyriera · Tipo: Skill · Tags: Product UI, Characters · Data: 26/09/2026
- Página: https://prompt-motion.com/anthonyriera-9b1b2a · Post: https://x.com/anthonyriera/status/2103784508860305566
- Instalação (só Skill): `/plugin marketplace add Rieranthony/product-film-skill` e `/plugin install product-film@product-film-skill` · Repo: https://github.com/Rieranthony/product-film-skill
- O que o vídeo mostra: vídeo de lançamento de uma ferramenta de marketing, com componentes reais do produto animados.
- Técnica: a skill lê o design system do produto, entrevista o usuário sobre o filme e só então gera e renderiza o vídeo em Remotion, reaproveitando os componentes reais, logo e música. Foi refinada em várias rodadas.
- Para os nossos Reels: médio — o passo de "entrevista antes de construir" e a leitura de um design system são boas ideias para a nossa skill; Remotion é uma alternativa ao nosso render HTML.

### Stock analysis app promo
- Criador: @AIStockSavvy · Tipo: Prompt · Tags: Product UI, Charts · Data: 25/09/2026
- Página: https://prompt-motion.com/aistocksavvy-3fb9f5 · Post: https://x.com/AIStockSavvy/status/2103482258774483320
- O que o vídeo mostra: promo de cerca de 15 s de um app de análise de ações, com telas e gráficos.
- Técnica: pede uma peça curta de portfólio com timing preciso, transições suaves e tom ousado, aproveitando cada segundo. Não define paleta, tipo nem câmera; o tema financeiro vem do produto (gráficos de ações e telas de análise).
- Para os nossos Reels: médio — o tema bate com o nosso e vale ver o vídeo como referência de gráficos de ações animados, mas o prompt em si não ensina técnica.

### TasteSkill dashboard showcase
- Criador: @LexnLin · Tipo: Skill · Tags: Product UI, Charts · Data: 20/10/2026
- Página: https://prompt-motion.com/lexnlin-f9b3bd8 · Post: https://x.com/LexnLin/status/2112674349132194185
- Instalação (só Skill): `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"` · Repo: https://github.com/Leonxlnx/taste-skill
- O que o vídeo mostra: vitrine animada de dashboards com gráficos gerados pela skill.
- Técnica: a skill dá ao agente uma direção de arte, imagens reais e checagens no navegador para que sites, dashboards e telas saiam com visual próprio, sem cara de template. A página não detalha o motion em si; o ganho está na qualidade do layout de dashboard antes de animar.
- Para os nossos Reels: médio — pode ajudar a gerar painéis e gráficos de mercado com melhor acabamento para depois animarmos; vale olhar o repositório.

### Voice agent SaaS launch
- Criador: @FractaDev · Tipo: Prompt · Tags: Product UI, Charts · Data: 26/09/2026
- Página: https://prompt-motion.com/fractadev-149adc · Post: https://x.com/FractaDev/status/2103941789744861266
- O que o vídeo mostra: lançamento "premium" de um SaaS de agentes de voz, com componentes reais da interface e gráficos.
- Técnica: o modelo inspeciona o projeto frontend e reaproveita os componentes de UI de verdade no vídeo, em vez de desenhar mockups. Pede acabamento de lançamento de alto nível e esforço máximo. O prompt não define duração, paleta nem som.
- Para os nossos Reels: médio — a ideia de montar o vídeo com componentes reais de código serve para nós: dá para ter uma biblioteca própria de cards, gráficos e tickers (fictícios) reutilizada em todo Reels.

### MotionSites one million visitors
- Criador: @viktoroddy · Tipo: Prompt · Tags: Product UI, Charts, Code · Data: 26/09/2026
- Página: https://prompt-motion.com/viktoroddy-98c1d8 · Post: https://x.com/viktoroddy/status/2103802280617402509
- O que o vídeo mostra: vídeo comemorativo de um marco de 1 milhão de visitantes mensais, com gráficos e telas.
- Técnica: prompt curto centrado num único número-marco e num prazo; a celebração com gráfico subindo e contador foi decisão do modelo.
- Para os nossos Reels: médio — o formato "um número grande como herói" (ex.: patrimônio sob custódia, CDI do ano) é reaproveitável, mas o prompt não ensina como.

### Bold Pilot SEO promo
- Criador: @utopyaszx · Tipo: Prompt · Tags: Product UI, Charts, Kinetic type · Data: 28/09/2026
- Página: https://prompt-motion.com/utopyaszx-1b2f94 · Post: https://x.com/utopyaszx/status/2104665591428624771
- O que o vídeo mostra: promo de 15 s de uma ferramenta de SEO, com gráficos de crescimento, telas e tipografia cinética.
- Técnica: prompt padrão de showreel (15 s, esforço máximo), com esforço médio do modelo. Pelas tags, o resultado combina gráficos de métricas subindo com tipografia em movimento e recortes da interface.
- Para os nossos Reels: médio — "gráfico subindo + número grande + palavra-chave" é a fórmula visual que um Reels de rentabilidade usa, mas é preciso definir as regras nós mesmos.

### Motion designer showreel (@danilowm)
- Criador: @danilowm · Tipo: Prompt · Tags: Product UI, Charts, Kinetic type · Data: 26/09/2026
- Página: https://prompt-motion.com/danilowm-d3720d · Post: https://x.com/danilowm/status/2103661844661412022
- O que o vídeo mostra: showreel de 15 s com UI, gráficos e texto cinético, gerado com HyperFrames.
- Técnica: o template de showreel de 15 s roda pela skill HyperFrames dentro do editor (instalada antes pelo terminal), com a instrução de usar todo o contexto do projeto, que aparece em português no prompt. O resultado se apoia em interface, gráficos de dados e tipografia animada.
- Para os nossos Reels: médio — HyperFrames (HTML → vídeo) é uma alternativa próxima da nossa stack e vale investigar. Gráficos + texto cinético é o vocabulário certo para finanças.

### Cinetic skill launch film
- Criador: @LexnLin · Tipo: Skill · Tags: Product UI, Code · Data: 04/10/2026
- Página: https://prompt-motion.com/lexnlin-6161a6 · Post: https://x.com/LexnLin/status/2106891315371737480
- Instalação (só Skill): `npx skills add Leonxlnx/cinetic` · Repo: https://github.com/Leonxlnx/cinetic
- O que o vídeo mostra: filme de lançamento cinematográfico gerado por código.
- Técnica: a skill recebe conceito, marca e trilha e faz o agente construir e renderizar um filme curto de lançamento em código. A página não detalha o método; é preciso abrir o repositório para ver as regras.
- Para os nossos Reels: médio — é uma skill concorrente/irmã da nossa; vale estudar o repositório para comparar o fluxo (insumos, storyboard, render).

### Database client launch video
- Criador: @iamMXFSCHR · Tipo: Prompt · Tags: Product UI, Code · Data: 25/09/2026
- Página: https://prompt-motion.com/iammxfschr-d68f90 · Post: https://x.com/iamMXFSCHR/status/2103619221296955831
- O que o vídeo mostra: um vídeo de lançamento de um cliente de banco de dados, com interface e código.
- Técnica: pede algo "moderno, elegante e impactante", com referência explícita ao estilo de vídeos de lançamento de uma empresa de IA (sobriedade, tipografia limpa, muito respiro). O prompt completo não aparece na página.
- Para os nossos Reels: médio — a direção "elegante, sóbria e com respiro" combina com o posicionamento premium escuro e dourado de um assessor.

### mdfor.dev product intro video
- Criador: @HO_BA · Tipo: Prompt · Tags: Product UI, Code · Data: 26/09/2026
- Página: https://prompt-motion.com/ho-ba-f3f0e9 · Post: https://x.com/HO_BA/status/2103845264649761062
- O que o vídeo mostra: apresentação de 30 s de uma ferramenta, com telas desmontadas em componentes animados e música.
- Técnica: o prompt exige que capturas e ícones reais sejam decompostos em partes animáveis em vez de aparecerem como imagens estáticas, com movimento "suculento", padrão de produção profissional e animação sincronizada à batida da música.
- Para os nossos Reels: médio — o princípio "nunca mostrar print estático, desmontar em peças animáveis" vale para tabelas e gráficos de mercado.

### org2html product showreel
- Criador: @kyonax_on_tech · Tipo: Prompt · Tags: Product UI, Code · Data: 25/09/2026
- Página: https://prompt-motion.com/kyonax-on-tech-aabc1d · Post: https://x.com/kyonax_on_tech/status/2103482598144049316
- O que o vídeo mostra: showreel de 15 s de uma ferramenta de desenvolvedor, com casos de uso, fluxo, funcionamento e logo em ASCII.
- Técnica: é o template de showreel com três obrigações de conteúdo: mostrar casos de uso, o fluxo e "como funciona". Exige respeitar a paleta já existente do projeto e usar um logo em arte ASCII. A estética fica com cara de terminal e código.
- Para os nossos Reels: médio — a estrutura em três blocos (para que serve → como flui → como funciona) é um bom esqueleto para Reels explicativos de produto financeiro, e a ideia de fixar a paleta de antemão vale para o nosso escuro + dourado.

### FundMyCompute platform overview
- Criador: @JayScambler · Tipo: Prompt · Tags: Product UI, Diagrams · Data: 28/09/2026
- Página: https://prompt-motion.com/jayscambler-3f8889 · Post: https://x.com/JayScambler/status/2104634653491495095
- O que o vídeo mostra: visão geral de 20 s de uma plataforma de financiamento de computação, com telas e diagramas de fluxo.
- Técnica: o prompt padrão de showreel foi adaptado para "visão geral da plataforma" em 20 s. Pelas tags, o resultado explica o funcionamento com diagramas (quem financia, quem recebe) intercalados com telas do produto.
- Para os nossos Reels: médio — o diagrama de fluxo de dinheiro entre partes é um recurso natural para explicar produtos financeiros (como funciona um FII, um CDB).

### Whiteboard skill tutorial
- Criador: @lemomo_ai · Tipo: Prompt · Tags: Product UI, Diagrams · Data: 27/09/2026
- Página: https://prompt-motion.com/lemomo-ai-0d9cff · Post: https://x.com/lemomo_ai/status/2104070024575242622
- O que o vídeo mostra: tutorial em estilo whiteboard explainer ensinando a gerar vídeos com uma skill do próprio autor.
- Técnica: um único pedido gera o filme inteiro, explicando o próprio fluxo de trabalho (skill + modelo) em formato de quadro branco desenhado. A página não detalha paleta, ritmo nem render.
- Para os nossos Reels: médio — o formato "tutorial em lousa" serve para Reels do tipo "como funciona", mas o conteúdo é sobre a ferramenta, não sobre finanças.

### Amazon wholesale pitch video
- Criador: @ceowinkz · Tipo: Prompt · Tags: Product UI, Kinetic type · Data: 26/09/2026
- Página: https://prompt-motion.com/ceowinkz-7c776b · Post: https://x.com/ceowinkz/status/2103647124126683602
- O que o vídeo mostra: um pitch de 15 s de uma empresa de atacado para convencer marcas a vender pela Amazon.
- Técnica: o briefing é persuasivo: em 15 s, dizer a um público específico (donos de marca) "por que nos deixar cuidar disso". A estrutura implícita é problema, proposta e chamada, com texto cinético e telas de interface.
- Para os nossos Reels: médio — o arco "por que deixar um especialista cuidar disso" serve para um Reels de captação do assessor, sem citar marcas.

### Landing page 3D scroll
- Criador: @twoclipping · Tipo: Prompt · Tags: Product UI, Kinetic type · Data: 14/10/2026
- Página: https://prompt-motion.com/twoclipping-d89be5 · Post: https://x.com/twoclipping/status/2110329502676951367
- O que o vídeo mostra: voo de câmera 3D de ~14,5 s sobre uma landing page deitada num piso claro, que sobe para uma vista aérea, mergulha no hero e termina num cartão com título.
- Técnica: a página é capturada com Playwright, cada elemento vira camada transparente com posição salva em JSON e tudo é remontado numa cena WebGL2 com câmera inclinada, velocidade de cruzeiro constante, subida em escala logarítmica e profundidade de campo por pixel. Os marcos de tempo são fixos ao décimo de segundo; o título final entra palavra por palavra a cada ~0,05 s. Render a 60 fps com 16 subquadros de motion blur e prévia de checagem antes do final; proíbe cortes, crossfades, giros e texto antes do cartão.
- Para os nossos Reels: médio — a estrutura "voo contínuo, vista geral, mergulho, cartão final" funciona para percorrer um relatório ou painel de mercado, mas o pipeline WebGL é pesado demais para um Reels padrão.

### YouTube transcript product ad
- Criador: @tstfully · Tipo: Prompt · Tags: Product UI, Kinetic type · Data: 27/09/2026
- Página: https://prompt-motion.com/tstfully-0aa6b4 · Post: https://x.com/tstfully/status/2104033772949680192
- O que o vídeo mostra: anúncio de 15 s no qual alguém cola um link de vídeo e recebe toda a transcrição em texto animado.
- Técnica: o prompt descreve uma única ação do usuário e seu resultado (colar link, receber transcrição) em 15 s. O vídeo se apoia na demonstração do fluxo e numa cascata de texto em tipografia cinética. Um único "antes → depois" sustenta o anúncio inteiro.
- Para os nossos Reels: médio — a estrutura "uma ação → resultado em cascata de texto ou números" funciona para mostrar, por exemplo, um aporte mensal virando uma pilha de valores.

### Jev engineering showreel
- Criador: @polydao · Tipo: Prompt · Tags: Product UI, Kinetic type, Music · Data: 26/09/2026
- Página: https://prompt-motion.com/polydao-7a572b · Post: https://x.com/polydao/status/2103783134206566862
- O que o vídeo mostra: showreel de 24 s sobre um tema de engenharia, com UI, tipografia cinética e cortes no tempo da música.
- Técnica: modelo de prompt com campos para tema e cores da marca, duração fixa de 24 s, ritmo de cortes marcados e trilha sincronizada com esses cortes. Não detalha fonte, câmera nem render.
- Para os nossos Reels: médio — o formato "template com [TEMA] e [CORES]" é o mesmo que nossa skill precisa (tema do dia + paleta fixa escura/dourada).

### Portfolio motion reel
- Criador: @heyiammallik · Tipo: Prompt · Tags: Product UI, Kinetic type, Particles · Data: 26/09/2026
- Página: https://prompt-motion.com/heyiammallik-e72d17 · Post: https://x.com/heyiammallik/status/2103837803587293397
- O que o vídeo mostra: reel de ~30 s feito a partir de um portfólio, com tipografia cinética, partículas e telas.
- Técnica: o prompt define um processo, não um estilo. O modelo assume o papel de motion designer profissional, analisa o portfólio e pesquisa técnicas atuais de motion e som. Depois questiona a própria estratégia e recomeça se o resultado não atingir padrão profissional, com a premissa de que cada quadro importa do primeiro ao último.
- Para os nossos Reels: médio — o ciclo de autocrítica (planejar, questionar, refazer se abaixo do padrão) é um bom passo de QA para a skill.

### Sherwood agentic hedge fund explainer
- Criador: @imthatcarlos · Tipo: Prompt · Tags: Product UI, Kinetic type, Photos · Data: 23/09/2026
- Página: https://prompt-motion.com/imthatcarlos-e04bfe · Post: https://x.com/imthatcarlos/status/2102849219388133592
- O que o vídeo mostra: explicador de um protocolo que permite hedge funds operados por agentes de IA, usando a identidade e componentes do app.
- Técnica: feito em Remotion (vídeo em React). O prompt autoriza o modelo a reaproveitar a identidade visual e os componentes da landing page e do app, e pede um explicador moderno e direto sobre um conceito financeiro complexo. Não fixa duração, paleta nem som.
- Para os nossos Reels: médio — o tema (fundos, gestão) é próximo e a ideia de montar o vídeo com componentes de UI reutilizáveis vale para a nossa skill; o produto em si é de terceiro.

### Voice agent landing page
- Criador: @pankajstwt · Tipo: Prompt · Tags: Product UI, Music · Data: 20/10/2026
- Página: https://prompt-motion.com/pankajstwt-49978ed · Post: https://x.com/pankajstwt/status/2112540104896241791
- O que o vídeo mostra: travelling 3D de 14,5 s pela landing page de um agente de voz, terminando num cartão com marca e frase final.
- Técnica: variante do prompt de voo 3D sobre landing page: captura com Playwright, elementos flutuantes como camadas transparentes, cena WebGL2 com profundidade de campo, sombras suaves e 16 subquadros de motion blur. Câmera só avança, com subida aérea e mergulho em marcos fixos, batida da trilha no cartão final e whooshes antes. Exige prévias estáticas em tempos definidos e aprovação antes do render.
- Para os nossos Reels: médio — o fluxo "prévias em tempos-chave, aprovação, depois render" é ótimo; o voo WebGL só compensa se um dia quisermos percorrer um relatório longo.

### Browser automation skill launch
- Criador: @hqmank · Tipo: Prompt · Tags: Product UI, Music, Code · Data: 26/09/2026
- Página: https://prompt-motion.com/hqmank-7c61f1 · Post: https://x.com/hqmank/status/2103831140033241156
- O que o vídeo mostra: vídeo de lançamento de 20 s de uma ferramenta open-source de automação de navegador, pensado para o topo do README.
- Técnica: 20 s, dinâmico, com um slogan de três frases curtas como espinha do roteiro ("dê um site, escreva um objetivo, ..."); sem especificação de estilo, som ou render.
- Para os nossos Reels: médio — o slogan em três batidas curtas é uma boa estrutura de gancho/CTA para Reels ("defina a meta, escolha o prazo, ..."); o resto é genérico.

### Product intro synced to music
- Criador: @BogdanDragomir · Tipo: Prompt · Tags: Product UI, Particles, Music · Data: 27/09/2026
- Página: https://prompt-motion.com/bogdandragomir-35e024 · Post: https://x.com/BogdanDragomir/status/2104045641538412658
- O que o vídeo mostra: vinheta de apresentação de um produto (não identificado), com UI e partículas sincronizadas a uma trilha original.
- Técnica: o modelo compõe a trilha do zero e sincroniza as cenas com ela, tratando a peça como obra-prima de portfólio. Não há estilo, duração nem render especificados; o ponto central é gerar o áudio dentro do próprio pipeline para controlar a sincronia.
- Para os nossos Reels: médio — gerar a trilha no próprio código (por exemplo, sintetizada) evita problemas de direitos e garante sincronia exata com os cortes.

### Design portfolio video reel
- Criador: @kikelopezdesign · Tipo: Prompt · Tags: Product UI, Phone · Data: 25/09/2026
- Página: https://prompt-motion.com/kikelopezdesign-7cc9e8 · Post: https://x.com/kikelopezdesign/status/2103527289619173471
- O que o vídeo mostra: um vídeo de 20 s do portfólio de um designer, com telas e mockup de celular.
- Técnica: a restrição de origem é forte: usar só os recursos do próprio portfólio, construindo do zero. Isso garante consistência visual com a identidade existente.
- Para os nossos Reels: médio — a regra "use só os recursos da identidade do cliente" vira, para nós, "use só a paleta e os elementos do kit do assessor", o que dá consistência entre Reels.

### Sotto reading app explainer
- Criador: @1stnoel_ · Tipo: Prompt · Tags: Product UI, Phone · Data: 24/09/2026
- Página: https://prompt-motion.com/1stnoel-c20a89 · Post: https://x.com/1stnoel_/status/2103247530259603851
- O que o vídeo mostra: explicador educativo de 1 minuto sobre um app de leitura, com telas em celular e narração sintetizada.
- Técnica: o prompt pede um vídeo educativo de um minuto sobre o site do app com narração em voz sintetizada. O modelo pesquisa o site, escreve o roteiro, gera a voz e sincroniza as telas com a fala.
- Para os nossos Reels: médio — o formato educativo de 60 s com voz sintetizada corresponde à nossa duração; vale testar narração gerada sincronizada com as cenas.

### Tennis game launch video
- Criador: @deifosv · Tipo: Prompt · Tags: Product UI, Phone · Data: 24/09/2026
- Página: https://prompt-motion.com/deifosv-04e4d3 · Post: https://x.com/deifosv/status/2103197522382786581
- O que o vídeo mostra: lançamento de um jogo de tênis com estatísticas ao vivo do site, versões desktop e celular e vários temas.
- Técnica: o vídeo puxa números reais do site do jogo para dar prova social, alterna desktop e mobile e mostra variações de tema. Um detalhe útil: pede ao modelo que também escreva um prompt separado para gerar a trilha num gerador de música, separando o som do código.
- Para os nossos Reels: médio — dois truques aproveitáveis: números "ao vivo" como prova (cotação, CDI, IPCA) e gerar à parte o prompt da trilha para manter som e visual coerentes.

### sweetRegret app update reel
- Criador: @thilina_a · Tipo: Prompt · Tags: Product UI, Phone, Characters · Data: 28/09/2026
- Página: https://prompt-motion.com/thilina-a-891c09 · Post: https://x.com/thilina_a/status/2104455320424915273
- O que o vídeo mostra: um reel de 25 s apresentando as novidades das versões 1.3 e 1.4 de um app, com mockup de celular e personagem.
- Técnica: um briefing curto com duração fixa e duas tarefas: exibir habilidade de motion e listar as mudanças de versão. A estrutura implícita é uma sequência de "cards de novidade" dentro de um telefone.
- Para os nossos Reels: médio — o formato "lista de novidades em cards dentro de um celular" adapta bem para "3 mudanças do mês no mercado" ou "o que mudou no IR".

### Datagran ChatGPT ads explainer
- Criador: @charlesmendez · Tipo: Prompt · Tags: Product UI, Phone, Charts · Data: 23/09/2026
- Página: https://prompt-motion.com/charlesmendez-73b6e4 · Post: https://x.com/charlesmendez/status/2102847039415476517
- O que o vídeo mostra: um explicativo de produto que segue o fluxo de criação de uma campanha, passando por métricas, atribuição, agente de voz, follow-up e analytics.
- Técnica: o prompt dá um roteiro em etapas numeradas (uma cena por etapa) e um tom "moderno e com punch". A clareza vem do roteiro sequencial, não da especificação visual.
- Para os nossos Reels: médio — o roteiro em passos encadeados, cada um virando uma cena, é um bom molde para "como funciona a sua carteira, passo a passo".

### Ren app launch video
- Criador: @macrohou · Tipo: Prompt · Tags: Product UI, Phone, Charts · Data: 25/09/2026
- Página: https://prompt-motion.com/macrohou-33959d · Post: https://x.com/macrohou/status/2103545787875733862
- O que o vídeo mostra: lançamento de 30 s de um app móvel, com telas em mockup de celular e gráficos.
- Técnica: o modelo recebe acesso ao repositório do app e extrai dali telas, cores e funções. O prompt pede 30 s e destaca motion e design de som, com liberdade total ("go crazy"). Usar o código-fonte como fonte de verdade visual evita telas inventadas.
- Para os nossos Reels: médio — o mockup de celular com gráficos serve para mostrar simulações ou carteiras genéricas; a ênfase em som também é útil.

### Motion designer showreel (@KangarooHere)
- Criador: @KangarooHere · Tipo: Prompt · Tags: Product UI, Phone, Charts, Kinetic type · Data: 25/09/2026
- Página: https://prompt-motion.com/kangaroohere-b10f8d · Post: https://x.com/KangarooHere/status/2103617278671818789
- O que o vídeo mostra: showreel de 20 s para uma newsletter, com UI no celular, gráficos e texto cinético.
- Técnica: é o template de showreel esticado para 20 s, com o contexto de uma newsletter (esforço médio). O modelo resolveu com mockup de celular, gráficos animados e tipografia em movimento.
- Para os nossos Reels: médio — o par "newsletter + gráficos no celular" é próximo de um conteúdo de assessor (resumo semanal de mercado), mas não há instrução detalhada.

### Ondefica app motion reel
- Criador: @jesscaroline7 · Tipo: Prompt · Tags: Product UI, Phone, Charts, Kinetic type · Data: 27/09/2026
- Página: https://prompt-motion.com/jesscaroline7-1ff7cb · Post: https://x.com/jesscaroline7/status/2104336637752955094
- O que o vídeo mostra: reel de um app com telas de celular, gráficos e tipografia cinética.
- Técnica: o molde de showreel ("ir com tudo"), executado em HyperFrames com esforço máximo e algumas iterações. A página não traz estilo, duração nem som; a qualidade veio das rodadas de ajuste, não do texto.
- Para os nossos Reels: médio — vale assistir como referência de celular + gráficos animados, e o HyperFrames aparece de novo como stack para render quadro a quadro.

### Badge unlock screen animation
- Criador: @BThreeAgency · Tipo: Prompt · Tags: Product UI, Phone, Particles · Data: 26/09/2026
- Página: https://prompt-motion.com/bthreeagency-b9b8d9 · Post: https://x.com/BThreeAgency/status/2103739079745827092
- O que o vídeo mostra: tela de celular em que um distintivo é desbloqueado, inclinando em 3D e celebrado com partículas douradas.
- Técnica: reproduz um frame do Figma sem mudar nada do visual e só acrescenta movimento. O distintivo se comporta como um objeto 3D sólido que inclina na direção do cursor com física plausível; a cena tem uma preparação antes da celebração, que vem com partículas douradas. Movimento rápido e suave, sem quique.
- Para os nossos Reels: médio — o momento "conquista" (moeda ou selo dourado que inclina e solta partículas douradas após uma preparação) serve como clímax de Reels sobre meta batida ou primeiro milhão.

### Matra caption app promo
- Criador: @gautam_mer1 · Tipo: Prompt · Tags: Product UI, Phone, Photos · Data: 26/09/2026
- Página: https://prompt-motion.com/gautam-mer1-2ae354 · Post: https://x.com/gautam_mer1/status/2103703336780530003
- O que o vídeo mostra: promo de 30 s de um app de legendas, com estética de comercial "estilo Apple".
- Técnica: o prompt pede só a duração (30 s) e uma referência de estética minimalista de produto. O modelo traduziu isso em Remotion/React, numa tentativa. A referência de estilo resume em poucas palavras um conjunto inteiro de decisões (fundo limpo, revelações lentas, foco no produto).
- Para os nossos Reels: médio — mostra que uma referência de estilo bem escolhida orienta o modelo. Na nossa skill, uma referência curta de estética (ex.: "editorial de banco privado") pode ajudar.

### Photo print app launch film
- Criador: @twoclipping · Tipo: Prompt · Tags: Product UI, Phone, Photos, Music · Data: 26/09/2026
- Página: https://prompt-motion.com/twoclipping-221cab · Post: https://x.com/twoclipping/status/2103835273813496100
- O que o vídeo mostra: filme de lançamento de um app de impressão de fotos em plano contínuo, estilo keynote, em que cada cena nasce da anterior.
- Técnica: o agente primeiro pede insumos (nome, fotos, música de ~120 BPM com drop) e depois monta ~27 s com um evento por batida. Nada entra por fade ou corte: texto sobe por máscara, ícones surgem com mola, barras se desenham e um bloco preto inunda a tela; um cursor comanda as mudanças e o zoom o acompanha. Tudo é função do tempo (`seek(t)`), o efeito de vidro usa deslocamento SVG sobre clones da cena e o vídeo de fundo é recodificado em quadros-chave puros para o seek ser exato. Proíbe crossfade, blur-in, flip 3D, partículas e pausas acima de 1 s.
- Para os nossos Reels: médio — as regras de transição (máscara, inundação de bloco, nada de fade) e o "um evento por batida" valem para finanças; a parte de fotos e vidro líquido é dispensável.

### Ball escaping twelve rings
- Criador: @kantamk · Tipo: Prompt · Tags: Shapes, Music · Data: 24/09/2026
- Página: https://prompt-motion.com/kantamk-61f410 · Post: https://x.com/kantamk/status/2103148907228176511
- O que o vídeo mostra: uma bola quicando dentro de 12 anéis concêntricos que vão se rompendo, com som a cada impacto.
- Técnica: o pedido era só algo "que possa viralizar". O modelo escolheu o formato hipnótico de simulação física com som por colisão e progresso visível (anel após anel), que prende até o fim.
- Para os nossos Reels: médio — a mecânica de "progresso visível até o fim" (anéis caindo como metas batidas) serve como gancho de retenção, por exemplo um patrimônio rompendo faixas até a meta.

## Baixo: prompts genéricos, marcas reais ou estilo que não combina (121)

### Porco Rosso sunset dogfight
- Criador: @NFT_Chen · Tipo: Prompt · Tags: (nenhuma na página) · Data: 26/09/2026
- Página: https://prompt-motion.com/nft-chen-5f8bb0 · Post: https://x.com/NFT_Chen/status/2103882415299350878
- O que o vídeo mostra: combate aéreo 3D sobre o mar ao pôr do sol, em homenagem a um filme de animação, com o texto "just breathe".
- Técnica: cena 3D em Three.js com aviões, cúmulos e mar com reflexo, em paleta de pôr do sol com nuvens roxas. Pede linguagem de câmera inspirada em animação japonesa e uma frase única na tela. Gerado em uma tentativa, sem detalhes de ritmo ou som.
- Para os nossos Reels: baixo — referência a obra protegida e tema sem relação com finanças; no máximo a ideia de céu/luz de fim de tarde como clima.

### Animated space cartoon episode
- Criador: @Ryzoft · Tipo: Prompt · Tags: Characters · Data: 24/09/2026
- Página: https://prompt-motion.com/ryzoft-4f85bd · Post: https://x.com/Ryzoft/status/2102989395359887481
- O que o vídeo mostra: episódio animado original de ficção espacial, com personagens, feito em Three.js.
- Técnica: o prompt pede que o modelo invente a história e a transforme num episódio completo em Three.js, com referência de qualidade a desenho dos anos 90 e produção de cinema espacial dos anos 80. A técnica está em delegar o roteiro e fixar só a referência estética.
- Para os nossos Reels: baixo — narrativa de ficção com personagens está longe do formato; só mostra que dá para narrar em cenas 3D.

### Anime robot combining sequence
- Criador: @allforbigfire · Tipo: Prompt · Tags: Characters · Data: 27/09/2026
- Página: https://prompt-motion.com/allforbigfire-86ff3c · Post: https://x.com/allforbigfire/status/2104193522715029657
- O que o vídeo mostra: cena em CG estilo anime na qual três veículos se transformam e se combinam num robô gigante.
- Técnica: feito em Python. O prompt, em japonês, só pergunta se é possível fazer a sequência de transformação e combinação. Há indício de trilha de fundo. O valor está na coreografia de peças que se encaixam.
- Para os nossos Reels: baixo — o tema não serve, embora "peças que se encaixam num todo" seja uma boa metáfora de diversificação de carteira.

### Chuseok pixel night scene
- Criador: @hoyoyoda · Tipo: Prompt · Tags: Characters · Data: 25/09/2026
- Página: https://prompt-motion.com/hoyoyoda-3a5c08 · Post: https://x.com/hoyoyoda/status/2103400046922543147
- O que o vídeo mostra: cena noturna em pixel art do Chuseok, o festival coreano da colheita (lua cheia, elementos tradicionais).
- Técnica: o prompt, em coreano, pede que o modelo pesquise antes os elementos típicos do feriado e depois monte uma animação em pixel art com eles. A técnica está no "pesquisar primeiro, compor depois". Estilo, paleta e duração ficam livres.
- Para os nossos Reels: baixo — pixel art e tema cultural fogem da estética escura e dourada, mas pesquisar antes de compor vale para datas sazonais (fim de ano, IR).

### Deliberately terrible motion showreel
- Criador: @HenkPoley · Tipo: Prompt · Tags: Characters · Data: 27/09/2026
- Página: https://prompt-motion.com/henkpoley-3d3407 · Post: https://x.com/HenkPoley/status/2104220387613761980
- O que o vídeo mostra: paródia de 1 minuto, em HTML, de um showreel propositalmente ruim.
- Técnica: inverte o desafio e pede o pior motion possível, com esforço mínimo, numa única página HTML de cerca de 1 minuto. O humor vem do amadorismo intencional. O prompt não descreve nada de visual.
- Para os nossos Reels: baixo — é humor de nicho e contraria o tom premium. No máximo, serve como lista do que evitar.

### Pelican riding a bicycle
- Criador: @AxtonLiu · Tipo: Prompt · Tags: Characters · Data: 24/09/2026
- Página: https://prompt-motion.com/axtonliu-0b861d · Post: https://x.com/AxtonLiu/status/2103119648271290566
- O que o vídeo mostra: animação elaborada de um pelicano pedalando uma bicicleta (o teste clássico de raciocínio espacial).
- Técnica: prompt em chinês que pede a versão mais complexa e refinada possível desse teste, com liberdade total de tecnologia e sem pressa. Não fixa estilo, câmera, ritmo ou som.
- Para os nossos Reels: baixo — personagem e tema sem uso em conteúdo financeiro.

### Pixel art card battle game
- Criador: @aisongman · Tipo: Prompt · Tags: Characters · Data: 26/09/2026
- Página: https://prompt-motion.com/aisongman-71ffac · Post: https://x.com/aisongman/status/2103763192971461057
- O que o vídeo mostra: um jogo de cartas 1 contra 1 em pixel art, gravado em ação.
- Técnica: o pedido é construir um jogo jogável em pixel art, inspirado num card game conhecido, sem outras restrições (uma tentativa). O vídeo é a gravação do jogo, não motion design.
- Para os nossos Reels: baixo — é jogo e pixel art, sem relação com o nosso formato.

### Pixel wizard crypto animation
- Criador: @0xEvinho · Tipo: Prompt · Tags: Characters · Data: 24/09/2026
- Página: https://prompt-motion.com/0xevinho-3777d8 · Post: https://x.com/0xEvinho/status/2103212966703436195
- O que o vídeo mostra: um mago em pixel art numa animação com referências a criptomoedas.
- Técnica: uma tentativa. O prompt pede uma variação de um vídeo anterior, trocando o tema para cripto, ou seja, reaproveita uma referência existente e muda só o assunto. A página não mostra outras instruções.
- Para os nossos Reels: baixo — personagem em pixel art com tema cripto não combina com o tom sóbrio de assessoria.

### Shop chatbot mascot promo
- Criador: @anas0ra · Tipo: Prompt · Tags: Characters · Data: 25/09/2026
- Página: https://prompt-motion.com/anas0ra-e57aea · Post: https://x.com/anas0ra/status/2103490331815952637
- O que o vídeo mostra: uma promoção de loja online estrelada pela mascote do chatbot.
- Técnica: um pedido casual em francês, só com o link do site; o modelo deduziu a mascote e o tom a partir dele.
- Para os nossos Reels: baixo — a peça é centrada em personagem e marca.

### Sketchbook animals come alive
- Criador: @abderrahmen_g · Tipo: Prompt · Tags: Characters · Data: 24/09/2026
- Página: https://prompt-motion.com/abderrahmen-g-9e8ed0 · Post: https://x.com/abderrahmen_g/status/2103103836541899031
- O que o vídeo mostra: animais desenhados à mão num caderno de esboços que ganham vida e se movem.
- Técnica: o modelo assume o papel de videomaker e anima, em JavaScript, desenhos à mão enviados como insumo, aproveitando ao máximo esses traços para dar autenticidade. O som deve acompanhar os quadros. O prompt também passa vídeos de referência como inspiração, com o aviso de não copiá-los. O texto do prompt aparece truncado na página.
- Para os nossos Reels: baixo — o tom lúdico e de personagem não combina com finanças; vale só a ideia de passar ao modelo assets próprios e vídeos de referência "para inspirar, não copiar".

### Starry Night cat-spotting game
- Criador: @MandelDuck · Tipo: Prompt · Tags: Characters · Data: 26/09/2026
- Página: https://prompt-motion.com/mandelduck-95fd08 · Post: https://x.com/MandelDuck/status/2103802923465768972
- O que o vídeo mostra: jogo 3D em que se caminha por uma cidade pintada no estilo de um quadro pós-impressionista procurando gatos escondidos.
- Técnica: pedido único e curto de um jogo 3D explorável a partir de uma pintura famosa; não fixa câmera, paleta, som ou tecnologia. É interativo, não um vídeo linear.
- Para os nossos Reels: baixo — formato de jogo, sem relação com o nosso tema.

### The Last Light animated short
- Criador: @faroukzy · Tipo: Prompt · Tags: Characters · Data: 25/09/2026
- Página: https://prompt-motion.com/faroukzy-9ff23e · Post: https://x.com/faroukzy/status/2103387771180138551
- O que o vídeo mostra: curta animado de 4 minutos com personagens, sobre uma "última luz".
- Técnica: uma tentativa. O prompt é uma única frase pedindo um curta de 4 minutos impressionante, sem nenhuma especificação. Mostra até onde o modelo vai sozinho em duração longa.
- Para os nossos Reels: baixo — duração e narrativa de personagem fogem do formato.

### Animated short about a bug
- Criador: @KamStudioLabs · Tipo: Prompt · Tags: Characters, Code · Data: 23/09/2026
- Página: https://prompt-motion.com/kamstudiolabs-c9bb28 · Post: https://x.com/KamStudioLabs/status/2102903173161877996
- O que o vídeo mostra: curta animado de 90 s sobre um bug de software que não quer ser corrigido.
- Técnica: o prompt, de uma frase, só dá a premissa narrativa (personificar um bug com uma motivação) e a duração. O modelo cria personagem, roteiro e animação em código. A força está na premissa com conflito.
- Para os nossos Reels: baixo — personagens não se encaixam, mas "personificar um conceito com uma motivação" (a inflação que come o dinheiro parado) pode virar metáfora visual abstrata.

### Clay-style music video
- Criador: @DavidShulmanFL · Tipo: Prompt · Tags: Characters, Music · Data: 25/09/2026
- Página: https://prompt-motion.com/davidshulmanfl-371638 · Post: https://x.com/DavidShulmanFL/status/2103336310089842921
- O que o vídeo mostra: clipe musical de 60 s com visual de animação em massinha e uma canção original.
- Técnica: o prompt pede um clipe de 60 s inspirado na linguagem dos videoclipes em stop-motion dos anos 80, com referências modernas, e uma canção original no espírito da mesma época. O resultado usa uma estética de massinha simulada em código.
- Para os nossos Reels: baixo — estética lúdica e personagens não combinam; o clipe só confirma que 60 s com trilha original são viáveis.

### Claude motion reel
- Criador: @jasonzhou1993 · Tipo: Prompt · Tags: Charts, Kinetic type, Particles · Data: 26/09/2026
- Página: https://prompt-motion.com/jasonzhou1993-8595e0 · Post: https://x.com/jasonzhou1993/status/2103663364958515541
- O que o vídeo mostra: showreel de 15 s com gráficos, texto cinético e partículas.
- Técnica: pedido genérico de showreel de 15 s, sem especificações.
- Para os nossos Reels: baixo — sem técnica descrita.

### Claude motion designer showreel (@3xtihor)
- Criador: @3xtihor · Tipo: Prompt · Tags: Charts, Kinetic type, Shapes, Music · Data: 25/09/2026
- Página: https://prompt-motion.com/3xtihor-0f6911 · Post: https://x.com/3xtihor/status/2103551886272159839
- O que o vídeo mostra: showreel de 15 s com gráficos, texto cinético, formas e música.
- Técnica: é o template padrão de showreel, sem direção. O modelo trouxe gráficos animados como parte do repertório.
- Para os nossos Reels: baixo — gráficos animados interessam, mas não há instrução reaproveitável.

### Motion designer showreel
- Criador: @eyishazyer · Tipo: Prompt · Tags: Charts, Kinetic type, Shapes, Music · Data: 26/09/2026
- Página: https://prompt-motion.com/eyishazyer-af035b · Post: https://x.com/eyishazyer/status/2103816865852129686
- O que o vídeo mostra: showreel de 15 s com gráficos, tipografia cinética, formas e música.
- Técnica: mesmo brief curto de showreel de currículo de 15 s com pedido de ambição; sem especificação de estilo, som ou render.
- Para os nossos Reels: baixo — o vídeo pode servir de referência de gráficos animados, mas o prompt não ensina nada.

### Drone Emprit showreel
- Criador: @ismailfahmi · Tipo: Prompt · Tags: Charts, Particles · Data: 25/09/2026
- Página: https://prompt-motion.com/ismailfahmi-557268 · Post: https://x.com/ismailfahmi/status/2103557833153466403
- O que o vídeo mostra: showreel de 15 s de uma ferramenta de inteligência de mídia, com gráficos e partículas.
- Técnica: pedido genérico de showreel de 15 s focado nas capacidades do produto, sem especificações de estilo ou código.
- Para os nossos Reels: baixo — só a referência visual de gráficos de dados em movimento.

### Flexprice motion showreel
- Criador: @sudeepsd_ · Tipo: Prompt · Tags: Charts, Particles · Data: 26/09/2026
- Página: https://prompt-motion.com/sudeepsd-1a3485 · Post: https://x.com/sudeepsd_/status/2103776623548158453
- O que o vídeo mostra: showreel de 15 s de uma plataforma de cobrança e precificação, com gráficos e partículas.
- Técnica: o mesmo molde de showreel de 15 s, mas pedindo que o modelo use o que já sabe sobre a empresa para escolher o conteúdo. Não há paleta, câmera, som nem render especificados; gráficos e partículas aparecem como linguagem pelas tags.
- Para os nossos Reels: baixo — briefing genérico; serve só como referência visual de gráficos com partículas.

### Motion designer showreel
- Criador: @himanshutwtxs · Tipo: Prompt · Tags: Diagrams, Kinetic type, Particles · Data: 25/09/2026
- Página: https://prompt-motion.com/himanshutwtxs-5f4b43 · Post: https://x.com/himanshutwtxs/status/2103495232637882858
- O que o vídeo mostra: showreel de 15 s com diagramas, texto cinético e partículas, gerado de primeira (one-shot).
- Técnica: pedido aberto de showreel de 15 s, sem parâmetros. O mérito está no modelo em esforço máximo, não no prompt.
- Para os nossos Reels: baixo — sem técnica descrita.

### Motion principles showreel
- Criador: @ChatGptAstra · Tipo: Prompt · Tags: Diagrams, Kinetic type, Particles · Data: 26/09/2026
- Página: https://prompt-motion.com/chatgptastra-0d95c7 · Post: https://x.com/ChatGptAstra/status/2103834787647807540
- O que o vídeo mostra: motion de 15 s que exibe princípios de animação com diagramas, tipo cinético e partículas.
- Técnica: uma única frase em chinês pedindo 15 s de motion com "estética de designer avançado"; nenhuma especificação adicional. A página cita uma versão mais forte do prompt em outro endereço, não incluída.
- Para os nossos Reels: baixo — prompt sem conteúdo técnico.

### Lead Notifi product ad
- Criador: @leadnotifi · Tipo: Prompt · Tags: Diagrams, Kinetic type, Shapes · Data: 25/09/2026
- Página: https://prompt-motion.com/leadnotifi-e83f94 · Post: https://x.com/leadnotifi/status/2103628028391960983
- O que o vídeo mostra: um anúncio de 15 s com diagramas, formas e texto cinético.
- Técnica: reaproveita o briefing padrão de showreel de 15 s para um anúncio de produto.
- Para os nossos Reels: baixo — não há técnica explícita.

### Motion designer showreel (@TeslaChartz)
- Criador: @TeslaChartz · Tipo: Prompt · Tags: Diagrams, Kinetic type, Shapes · Data: 26/09/2026
- Página: https://prompt-motion.com/teslachartz-c58b32 · Post: https://x.com/TeslaChartz/status/2103746486978887985
- O que o vídeo mostra: um showreel de 15 s com diagramas, formas e texto cinético.
- Técnica: o mesmo briefing padrão de showreel de 15 s; o modelo optou por diagramas e formas geométricas.
- Para os nossos Reels: baixo — o resultado com diagramas é visualmente próximo do nosso tema, mas o prompt não traz regras.

### LiteLLM promo reel
- Criador: @MisbahSy · Tipo: Prompt · Tags: Diagrams, Music, Code · Data: 26/09/2026
- Página: https://prompt-motion.com/misbahsy-80eaec · Post: https://x.com/MisbahSy/status/2103831201114882277
- O que o vídeo mostra: reel promocional de 15 s de uma ferramenta de desenvolvimento, com diagramas e trechos de código ritmados por música.
- Técnica: o prompt é curto. Pede um vídeo de 15 s em formato de showreel de currículo e liberdade total ("go all out"), sem estilo, paleta ou técnica definidos. O resultado depende de o modelo escolher sozinho diagramas, blocos de código e cortes na música. A página indica uma "versão mais forte" do prompt no template de showreel do site.
- Para os nossos Reels: baixo — a ideia de "showreel" é genérica; só serve como lembrete de que diagramas com cortes na batida dão energia.

### Chain.wtf pitch video
- Criador: @SPEARwtf · Tipo: Prompt · Tags: Kinetic type · Data: 26/09/2026
- Página: https://prompt-motion.com/spearwtf-3c1fd1 · Post: https://x.com/SPEARwtf/status/2103857153308029058
- O que o vídeo mostra: um pitch de 30 s de um projeto, com tipografia cinética.
- Técnica: um briefing mínimo (projeto e 30 s); o texto em movimento carrega toda a narrativa.
- Para os nossos Reels: baixo — não há técnica explícita.

### GravityDEX anime hype edit
- Criador: @MicheleHarmonic · Tipo: Prompt · Tags: Kinetic type · Data: 24/09/2026
- Página: https://prompt-motion.com/micheleharmonic-77628e · Post: https://x.com/MicheleHarmonic/status/2103111448352244175
- O que o vídeo mostra: edit de hype que mistura uma DEX cripto com um personagem de anime, em tipografia cinética.
- Técnica: prompt curto em one-shot que cruza uma marca com um personagem de anime para gerar energia de hype. Não há instruções de estilo, ritmo ou render.
- Para os nossos Reels: baixo — usa personagem protegido e marca de terceiros, e o tom é incompatível.

### Shin Majin-shiki promo
- Criador: @Majin_AppSheet · Tipo: Prompt · Tags: Kinetic type · Data: 25/09/2026
- Página: https://prompt-motion.com/majin-appsheet-2d3c1a · Post: https://x.com/Majin_AppSheet/status/2103497319899693327
- O que o vídeo mostra: vídeo promocional (PV) em tipografia cinética, em japonês.
- Técnica: prompt de poucas palavras em japonês pedindo um PV do método do autor, renderizado com HyperFrames. Não há instruções de estilo ou ritmo.
- Para os nossos Reels: baixo — sem técnica descrita.

### Anime maid dance showreel
- Criador: @_topi_003 · Tipo: Prompt · Tags: Kinetic type, Characters, Music · Data: 27/09/2026
- Página: https://prompt-motion.com/topi-003-b0e12c · Post: https://x.com/_topi_003/status/2104088986969055288
- O que o vídeo mostra: uma personagem de anime, criada a partir de uma imagem enviada, dançando por 15 s com tipografia e música.
- Técnica: o prompt, em japonês, parte de uma imagem de referência e pede uma dança enérgica de 15 s em formato de showreel, com esforço máximo. A técnica consiste em animar uma personagem 2D a partir de uma ilustração estática, com texto e música.
- Para os nossos Reels: baixo — personagem e dança não combinam com a proposta nem com a regra de não usar pessoas.

### Lightspark social promo video
- Criador: @davidmarcus · Tipo: Prompt · Tags: Kinetic type, Code · Data: 25/09/2026
- Página: https://prompt-motion.com/davidmarcus-a28a60 · Post: https://x.com/davidmarcus/status/2103275618045686217
- O que o vídeo mostra: vídeo curto para redes sociais, com tipografia cinética, promovendo uma empresa de pagamentos.
- Técnica: prompt curto pedindo algo "punchy and modern", com som e qualidade de produção, gerado de primeira. Sem especificações adicionais.
- Para os nossos Reels: baixo — tema próximo (pagamentos), mas sem técnica descrita.

### Claude motion designer showreel (@CrazyAlphaaa)
- Criador: @CrazyAlphaaa · Tipo: Prompt · Tags: Kinetic type, Particles · Data: 25/09/2026
- Página: https://prompt-motion.com/crazyalphaaa-bc7e75 · Post: https://x.com/CrazyAlphaaa/status/2103568486249480622
- O que o vídeo mostra: showreel de 15 s com texto cinético e partículas.
- Técnica: é o mesmo template de showreel de 15 s com esforço máximo. As decisões de estilo são todas do modelo.
- Para os nossos Reels: baixo — é genérico e não acrescenta técnica.

### Kinetic type motion showreel
- Criador: @_topi_003 · Tipo: Prompt · Tags: Kinetic type, Particles · Data: 27/09/2026
- Página: https://prompt-motion.com/topi-003-9ca6b5 · Post: https://x.com/_topi_003/status/2104086342204592443
- O que o vídeo mostra: showreel de 15 s de tipografia cinética com partículas.
- Técnica: versão em japonês do molde de showreel de 15 s, dinâmico e com esforço máximo. Sem especificação de estilo, som ou render.
- Para os nossos Reels: baixo — sem técnica a extrair.

### Motion designer showreel
- Criador: @hanifproduktif · Tipo: Prompt · Tags: Kinetic type, Particles · Data: 25/09/2026
- Página: https://prompt-motion.com/hanifproduktif-54bdee · Post: https://x.com/hanifproduktif/status/2103404901451829311
- O que o vídeo mostra: showreel de 15 s com tipografia cinética e partículas.
- Técnica: coloca o modelo no papel de candidato a uma vaga de motion designer numa agência e pede 15 s mostrando habilidades; nenhuma especificação de estilo, som ou render.
- Para os nossos Reels: baixo — só o truque de role-play ("você está se candidatando") para elevar a ambição.

### ODATANO Cardano hype edit
- Criador: @maxalexweber · Tipo: Prompt · Tags: Kinetic type, Particles · Data: 24/09/2026
- Página: https://prompt-motion.com/maxalexweber-67688b · Post: https://x.com/maxalexweber/status/2103118009535459784
- O que o vídeo mostra: um edit de hype para um projeto do ecossistema Cardano, com tipografia cinética e partículas.
- Técnica: prompt de uma linha, em one-shot, que pede um edit de alta energia. Não há especificação de cor, ritmo nem render; as tags indicam texto em movimento rápido sobre partículas.
- Para os nossos Reels: baixo — é hype de cripto, sem instrução técnica, e o tom não combina com assessoria.

### Photon journey from the Sun
- Criador: @apoorvjain25 · Tipo: Prompt · Tags: Kinetic type, Particles · Data: 29/09/2026
- Página: https://prompt-motion.com/apoorvjain25-d24184 · Post: https://x.com/apoorvjain25/status/2104818940467945542
- O que o vídeo mostra: a jornada de um fóton saindo do Sol, com tipografia cinética e partículas.
- Técnica: prompt curto de 20 s, tema livre, "make it crazy"; sem instruções de estilo. O que se aproveita é a ideia de narrar a viagem de uma unidade (um fóton) de ponta a ponta.
- Para os nossos Reels: baixo — partículas e tom espetacular não combinam com a nossa linha; a ideia de "viagem de uma unidade" já está no banco (ex.: o caminho de um real).

### Nohandslabs brand promo
- Criador: @robvjourney · Tipo: Prompt · Tags: Kinetic type, Particles, Code · Data: 26/09/2026
- Página: https://prompt-motion.com/robvjourney-ce3e1a · Post: https://x.com/robvjourney/status/2103768390322237474
- O que o vídeo mostra: promo de marca de 15 s baseado num site, com texto cinético e partículas.
- Técnica: o modelo recebe só um link do site e a ordem de usar tudo o que tem. Ele extrai o conteúdo e transforma em 15 s de tipografia animada com partículas, gerados por código.
- Para os nossos Reels: baixo — não há técnica descrita além do texto + partículas.

### Personal research intro reel
- Criador: @Madhav_XO · Tipo: Prompt · Tags: Kinetic type, Particles, Code · Data: 25/09/2026
- Página: https://prompt-motion.com/madhav-xo-f97f20 · Post: https://x.com/Madhav_XO/status/2103605007396524440
- O que o vídeo mostra: intro pessoal de 10 s com tipografia cinética e partículas, sobre a área de pesquisa do autor.
- Técnica: o prompt, de uma linha, pede um vídeo de 10 s sobre "o que você sabe sobre mim", ou seja, usa a memória ou o contexto do modelo como briefing. Pelas tags, o resultado combina partículas geradas por código com texto em movimento.
- Para os nossos Reels: baixo — personalização via memória não se aplica; partículas e tipografia já são técnicas conhecidas.

### Keyframe motion design reel
- Criador: @Grace_sunnyy · Tipo: Prompt · Tags: Kinetic type, Particles, Music · Data: 03/10/2026
- Página: https://prompt-motion.com/grace-sunnyy-29bc61 · Post: https://x.com/Grace_sunnyy/status/2106532575712022677
- O que o vídeo mostra: um portfólio de 15 s com texto cinético, partículas e música.
- Técnica: é um prompt em chinês com liberdade total de ferramenta. Prioriza direção de arte ousada, composição marcante e expressão de movimento forte, com a exigência de que cada segundo tenha valor.
- Para os nossos Reels: baixo — vale só como lembrete de densidade ("cada segundo conta"); não há especificação técnica.

### Kinetic type and particle showreel
- Criador: @m1n9_k7 · Tipo: Prompt · Tags: Kinetic type, Particles, Music · Data: 25/09/2026
- Página: https://prompt-motion.com/m1n9-k7-ff9ab9 · Post: https://x.com/m1n9_k7/status/2103580011882295601
- O que o vídeo mostra: showreel de 15 s com tipografia cinética, partículas e trilha musical.
- Técnica: o pedido é mínimo, só um showreel "de currículo" de 15 s, dinâmico e com esforço máximo (Opus 5.5, esforço alto, uma tentativa). Estilo, tipografia, paleta, câmera e som ficaram todos por conta do modelo. O resultado combina texto animado com sistemas de partículas sobre música.
- Para os nossos Reels: baixo — mostra só que texto cinético com partículas funciona como abertura. Não há instrução reaproveitável além disso.

### Branding agency showreel
- Criador: @jacksonfall · Tipo: Prompt · Tags: Kinetic type, Photos · Data: 26/09/2026
- Página: https://prompt-motion.com/jacksonfall-54b2ac · Post: https://x.com/jacksonfall/status/2103925420211229164
- O que o vídeo mostra: showreel de 30 s de uma agência de branding fictícia para fundadores de startups.
- Técnica: pedido aberto de showreel de 30 s com duas restrições: todos os gráficos feitos do zero e um posicionamento de nicho definido. O resto fica com o modelo.
- Para os nossos Reels: baixo — só reforça "gráficos do zero, sem banco de imagens", que já é nossa regra.

### fal motion design showreel
- Criador: @influencer_seo · Tipo: Prompt · Tags: Kinetic type, Photos · Data: 29/09/2026
- Página: https://prompt-motion.com/influencer-seo-ce8c33 · Post: https://x.com/influencer_seo/status/2104827314400026936
- O que o vídeo mostra: showreel de 15 s de uma plataforma de mídia generativa, com tipografia cinética e imagens geradas.
- Técnica: o molde de showreel de 15 s, com o detalhe de mandar o modelo usar a API de geração da própria plataforma para criar as imagens do vídeo. Fora isso, não há estilo, som nem render definidos.
- Para os nossos Reels: baixo — depende de imagens geradas por API externa; a nossa linha é motion puro em código.

### Claude motion design showreel
- Criador: @rendesr · Tipo: Prompt · Tags: Kinetic type, Shapes · Data: 25/09/2026
- Página: https://prompt-motion.com/rendesr-86be44 · Post: https://x.com/rendesr/status/2103395846578676116
- O que o vídeo mostra: showreel de 15 s de tipografia cinética e formas geométricas.
- Técnica: o mesmo molde de showreel de 15 s, sem nenhuma diretriz de estilo, cor, som ou render.
- Para os nossos Reels: baixo — sem técnica a extrair.

### Claude motion reel
- Criador: @codeSTACKr · Tipo: Prompt · Tags: Kinetic type, Shapes · Data: 26/09/2026
- Página: https://prompt-motion.com/codestackr-c071bf · Post: https://x.com/codeSTACKr/status/2103656229717328129
- O que o vídeo mostra: showreel de 15 s com tipografia cinética e formas.
- Técnica: o brief padrão de showreel profissional de 15 s com pedido de ambição; sem especificação técnica. A página cita uma versão mais forte do prompt, não incluída.
- Para os nossos Reels: baixo — nada reaproveitável no prompt.

### Kinetic type showreel
- Criador: @zheke · Tipo: Prompt · Tags: Kinetic type, Shapes · Data: 25/09/2026
- Página: https://prompt-motion.com/zheke-38deff · Post: https://x.com/zheke/status/2103418664854622583
- O que o vídeo mostra: showreel de tipografia cinética com formas geométricas.
- Técnica: prompt de uma linha pedindo que o modelo mostre suas habilidades de motion design. Nada é especificado; o resultado é pura interpretação do modelo.
- Para os nossos Reels: baixo — sem técnica a extrair.

### Motion design showreel
- Criador: @samuel_spitz · Tipo: Prompt · Tags: Kinetic type, Shapes · Data: 25/09/2026
- Página: https://prompt-motion.com/samuel-spitz-974923 · Post: https://x.com/samuel_spitz/status/2103544855276503053
- O que o vídeo mostra: showreel de tipografia cinética e formas geométricas que exibe uma gama ampla de técnicas de motion.
- Técnica: prompt aberto que posiciona o vídeo como a peça central do portfólio de um designer de ponta e pede para levar o ofício ao limite. Não define estilo, duração nem som; a força do resultado vem do enquadramento ambicioso do pedido.
- Para os nossos Reels: baixo — sem técnica concreta; no máximo inspira transições entre blocos de texto e formas.

### 3D motion design showreel
- Criador: @sahildesigner23 · Tipo: Prompt · Tags: Kinetic type, Shapes, Music · Data: 25/09/2026
- Página: https://prompt-motion.com/sahildesigner23-ee3155 · Post: https://x.com/sahildesigner23/status/2103536115563307120
- O que o vídeo mostra: um showreel de 15 s com formas em pseudo-3D, texto animado e trilha musical.
- Técnica: o mesmo briefing curto de "showreel dinâmico de 15 s", rodado com esforço Max. A diferença está no esforço do modelo e na tag Music, que indica trilha sincronizada. Não há instruções de estilo, câmera ou render.
- Para os nossos Reels: baixo — mostra só que mais esforço do modelo rende cenas 3D mais ricas; não há técnica explícita para copiar.

### Abstract motion design reel
- Criador: @ajith_io · Tipo: Prompt · Tags: Kinetic type, Shapes, Music · Data: 25/09/2026
- Página: https://prompt-motion.com/ajith-io-b5626e · Post: https://x.com/ajith_io/status/2103449416325890146
- O que o vídeo mostra: reel abstrato de 15 s com formas, tipografia cinética e trilha.
- Técnica: o prompt é o pedido aberto de showreel de 15 s, sem nenhum parâmetro de estilo, ritmo ou código. Serve como amostra do que o modelo produz sozinho.
- Para os nossos Reels: baixo — sem instruções aproveitáveis.

### Claude motion design reel
- Criador: @ghinaiya_nirmal · Tipo: Prompt · Tags: Kinetic type, Shapes, Music · Data: 25/09/2026
- Página: https://prompt-motion.com/ghinaiya-nirmal-5d8fec · Post: https://x.com/ghinaiya_nirmal/status/2103540656182308943
- O que o vídeo mostra: reel livre de 15 s com tipografia, formas e trilha.
- Técnica: é uma carta branca total (um reel próprio de 15 s com esforço máximo). Toda a variedade vem das escolhas do modelo: texto animado, geometria e música.
- Para os nossos Reels: baixo — não há instrução para destilar.

### Claude motion designer showreel
- Criador: @stephanlivera · Tipo: Prompt · Tags: Kinetic type, Shapes, Music · Data: 25/09/2026
- Página: https://prompt-motion.com/stephanlivera-df17a2 · Post: https://x.com/stephanlivera/status/2103315922098470926
- O que o vídeo mostra: showreel de 15 s com tipografia cinética, formas geométricas e música, feito com Opus 5.5 em esforço máximo.
- Técnica: o prompt é só um pedido aberto: um vídeo de motion de 15 s no formato de showreel de currículo, com a instrução de "ir com tudo". Não define estilo, paleta, fontes nem código, então o resultado depende do repertório do modelo e do esforço máximo de raciocínio.
- Para os nossos Reels: baixo — não traz técnica reaproveitável; serve só para mostrar que um pedido aberto, com esforço alto, já rende tipografia cinética aceitável.

### Bold kinetic type showreel
- Criador: @shneural · Tipo: Prompt · Tags: Kinetic type, Shapes, Particles · Data: 24/09/2026
- Página: https://prompt-motion.com/shneural-2abdfa · Post: https://x.com/shneural/status/2103151003272962130
- O que o vídeo mostra: showreel de 15 s com tipografia em negrito, formas e partículas.
- Técnica: mesmo pedido genérico de showreel de 15 s, sem especificações de estilo, cor, fonte ou render. Tudo o que aparece (letras grandes, formas, partículas) foi decisão do modelo.
- Para os nossos Reels: baixo — nada de técnica explícita; no máximo a referência visual de tipografia pesada em movimento.

### Claude motion design showreel
- Criador: @sudo_kiran · Tipo: Prompt · Tags: Kinetic type, Shapes, Particles · Data: 25/09/2026
- Página: https://prompt-motion.com/sudo-kiran-49176d · Post: https://x.com/sudo_kiran/status/2103463886372696074
- O que o vídeo mostra: showreel abstrato com tipografia cinética, formas e partículas, gerado em uma tentativa.
- Técnica: o prompt publicado é praticamente só um pedido de esforço máximo ("Go all out"), sem nenhuma especificação de estilo, duração, som ou render. O resultado depende inteiramente do modelo, num one-shot.
- Para os nossos Reels: baixo — não há instrução reaproveitável.

### Kinetic shapes showreel
- Criador: @Shinskinakamoto · Tipo: Prompt · Tags: Kinetic type, Shapes, Particles · Data: 25/09/2026
- Página: https://prompt-motion.com/shinskinakamoto-20190b · Post: https://x.com/Shinskinakamoto/status/2103580532852589043
- O que o vídeo mostra: um showreel de 15 s com formas cinéticas, partículas e texto.
- Técnica: o briefing padrão de showreel de 15 s, sem instruções adicionais.
- Para os nossos Reels: baixo — não há técnica explícita.

### Motion design showreel
- Criador: @safarkhanshuvo · Tipo: Prompt · Tags: Kinetic type, Shapes, Particles · Data: 25/09/2026
- Página: https://prompt-motion.com/safarkhanshuvo-ffd52d · Post: https://x.com/safarkhanshuvo/status/2103520091552059752
- O que o vídeo mostra: um showreel de 15 s com tipografia cinética, formas geométricas e partículas (pelas tags), que exibe o repertório de um motion designer.
- Técnica: briefing mínimo, que fixa só a duração (15 s), o formato "showreel de currículo" e um pedido de intensidade máxima ("go all out"). Estilo, paleta e técnica de render ficam a cargo do modelo. A página aponta um template mais detalhado de showreel no próprio site.
- Para os nossos Reels: baixo — serve só como prova de que um briefing aberto com duração fixa gera variedade, mas não traz nenhuma regra reaproveitável.

### Motion designer showreel (@VanshWTFFF)
- Criador: @VanshWTFFF · Tipo: Prompt · Tags: Kinetic type, Shapes, Particles · Data: 26/09/2026
- Página: https://prompt-motion.com/vanshwtfff-db0466 · Post: https://x.com/VanshWTFFF/status/2103644352794992798
- O que o vídeo mostra: showreel curtíssimo, de 10 s, com texto cinético, formas e partículas.
- Técnica: é o template de showreel comprimido para 10 s (esforço máximo), o que obriga a cortes muito rápidos e alta densidade de eventos.
- Para os nossos Reels: baixo — 10 s de pura energia não sustenta 60 s de conteúdo. No máximo, serve de gancho de abertura.

### Claude motion design reel
- Criador: @tequilafunks · Tipo: Prompt · Tags: Kinetic type, Shapes, Particles, Music · Data: 25/09/2026
- Página: https://prompt-motion.com/tequilafunks-97f6c9 · Post: https://x.com/tequilafunks/status/2103528644828127728
- O que o vídeo mostra: showreel de motion de 15 s com tipografia cinética, formas, partículas e trilha, feito em Remotion.
- Técnica: brief curto do tipo "showreel de currículo de 15 s, seja ambicioso", sem especificar paleta, fonte ou câmera. O diferencial está na stack: Remotion (vídeo programático em React), que já resolve render quadro a quadro. Todo o resto foi escolha do modelo.
- Para os nossos Reels: baixo — prompt aberto demais; só confirma Remotion como alternativa de stack ao HTML + Playwright.

### Claude motion design showreel
- Criador: @ayushunleashed · Tipo: Prompt · Tags: Kinetic type, Shapes, Particles, Music · Data: 26/09/2026
- Página: https://prompt-motion.com/ayushunleashed-ece3e3 · Post: https://x.com/ayushunleashed/status/2103794962257084755
- O que o vídeo mostra: showreel de 15 s com tipografia cinética, formas, partículas e música.
- Técnica: o mesmo brief curto de "showreel de currículo de 15 s, vá com tudo", sem nenhuma especificação de estilo, som ou render. Tudo foi decidido pelo modelo.
- Para os nossos Reels: baixo — nada reaproveitável no prompt.

### Motion designer showreel (@zaqailo)
- Criador: @zaqailo · Tipo: Prompt · Tags: Kinetic type, Shapes, Particles, Music · Data: 26/09/2026
- Página: https://prompt-motion.com/zaqailo-212ad3 · Post: https://x.com/zaqailo/status/2103768009017835623
- O que o vídeo mostra: showreel de 15 s com texto cinético, formas, partículas e música.
- Técnica: é o desafio padrão de showreel de 15 s, sem direção visual. O modelo combinou tipografia animada, geometria, partículas e trilha.
- Para os nossos Reels: baixo — não traz nada além do template genérico.

### UK dubstep track with ASCII visuals
- Criador: @Rames_Jusso · Tipo: Prompt · Tags: Music, Code · Data: 24/09/2026
- Página: https://prompt-motion.com/rames-jusso-589f80 · Post: https://x.com/Rames_Jusso/status/2103200703598776559
- O que o vídeo mostra: faixa de dubstep sintetizada com visual em ASCII art reagindo ao som.
- Técnica: HyperFrames. O prompt só define gênero e andamento (140 BPM, referências do dubstep britânico). O modelo gera a música e um visual em caracteres ASCII sincronizado com os graves. O interessante é o casamento entre áudio gerado e visual reativo.
- Para os nossos Reels: baixo — estética e gênero musical inadequados, mas a ideia de visual reagindo ao áudio (um ticker em ASCII?) pode inspirar uma vinheta.

### Four seasons train window
- Criador: @itsolelehmann · Tipo: Prompt · Tags: não informadas · Data: 24/09/2026
- Página: https://prompt-motion.com/itsolelehmann-e47532 · Post: https://x.com/itsolelehmann/status/2103124033365762215
- O que o vídeo mostra: as quatro estações passando pela janela de um vagão aconchegante, com uma xícara de café na mesa, em estética simétrica e pastel de cinema.
- Técnica: prompt de uma frase que define cena, objeto de primeiro plano e uma referência de diretor como guia de estilo. A passagem do tempo pela janela é o único movimento narrativo.
- Para os nossos Reels: baixo — estética ilustrativa fora da nossa linha, embora a metáfora "o tempo passa pela janela" combine com longo prazo.

### Distilbook promo showreel
- Criador: @ajith_io · Tipo: Prompt · Tags: Particles · Data: 26/09/2026
- Página: https://prompt-motion.com/ajith-io-4c248f · Post: https://x.com/ajith_io/status/2103800569584562538
- O que o vídeo mostra: showreel promocional de ~40 s de um produto, com partículas e trilha de clima épico.
- Técnica: brief aberto de 40 s cujo único detalhe concreto é o som: trilha original que evoca o clima de uma trilha de cinema conhecida, sem usar a música real. Visual, fonte e câmera ficam com o modelo.
- Para os nossos Reels: baixo — só a regra "compor trilha original inspirada no clima, nunca usar a faixa protegida", que já vale para nós.

### Recipe brand 20th anniversary
- Criador: @deebeeeff · Tipo: Prompt · Tags: Particles · Data: 29/09/2026
- Página: https://prompt-motion.com/deebeeeff-50fcd0 · Post: https://x.com/deebeeeff/status/2104952364365234301
- O que o vídeo mostra: uma vinheta de 10 s com partículas, comemorando os 20 anos de uma marca de receitas.
- Técnica: um briefing curto (10 s, "dinâmico", aniversário), com a imagem da marca anexada como base visual. Rodou com esforço Medium. O modelo extrai cores e formas da imagem enviada.
- Para os nossos Reels: baixo — usa marca real; dá para aproveitar só a estrutura de vinheta curta com partículas para marcos, como "10 anos de carreira".

### Fiery samurai kata
- Criador: @chrisjdimarco · Tipo: Prompt · Tags: Particles, Characters · Data: 24/09/2026
- Página: https://prompt-motion.com/chrisjdimarco-f068db · Post: https://x.com/chrisjdimarco/status/2103232192847524106
- O que o vídeo mostra: um samurai executando um kata no lugar, cercado de efeitos de fogo e partículas.
- Técnica: o personagem e os efeitos são feitos só em JavaScript, sem assets externos. O prompt pede poses e movimentos variados e difíceis, sem sair do lugar, num visual "flamejante". A restrição de ponto fixo simplifica câmera e enquadramento e concentra o espetáculo na animação.
- Para os nossos Reels: baixo — personagem humano e tema marcial fogem da proposta; partículas de brasa dourada podem servir de textura.

### Talking-head clip edit
- Criador: @sab8a · Tipo: Prompt · Tags: Photos · Data: 24/09/2026
- Página: https://prompt-motion.com/sab8a-364a5a · Post: https://x.com/sab8a/status/2103144778481475686
- O que o vídeo mostra: um clipe bruto de pessoa falando para a câmera transformado numa edição dinâmica com legendas, grafismos e música.
- Técnica: pedido de uma linha para cortar o material bruto em edição enérgica, com legendas, gráficos sobrepostos e trilha, feito no editor OpenEdit. Não há regras detalhadas na página.
- Para os nossos Reels: baixo — depende de gravação de uma pessoa real, o que está fora do nosso formato.

### AIsa API key promo
- Criador: @0xfemyn · Tipo: Prompt · Tags: Product UI · Data: 26/09/2026
- Página: https://prompt-motion.com/0xfemyn-e114d3 · Post: https://x.com/0xfemyn/status/2103796337041137833
- O que o vídeo mostra: promo de 15 s de uma chave de API de uma plataforma de IA.
- Técnica: pedido curto de 15 s, dinâmico e usando o máximo de recursos. Sem diretrizes de estilo, som ou render.
- Para os nossos Reels: baixo — sem técnica a extrair.

### AjustaCV Pro pricing promo
- Criador: @thayto_dev · Tipo: Prompt · Tags: Product UI · Data: 27/09/2026
- Página: https://prompt-motion.com/thayto-dev-44b911 · Post: https://x.com/thayto_dev/status/2104200591278739735
- O que o vídeo mostra: promo de 15 s da tabela de preços de um app de currículos.
- Técnica: pedido genérico de showreel de 15 s, em esforço máximo, renderizado com HyperFrames. Sem parâmetros.
- Para os nossos Reels: baixo — sem técnica aproveitável.

### Brieform product presentation
- Criador: @MajorBaguette · Tipo: Prompt · Tags: Product UI · Data: 26/09/2026
- Página: https://prompt-motion.com/majorbaguette-fb11d7 · Post: https://x.com/MajorBaguette/status/2103849602826834228
- O que o vídeo mostra: uma apresentação de produto de 30 s centrada em telas de interface.
- Técnica: um briefing mínimo (produto e 30 s) executado em Remotion. Todas as decisões de cena ficam com o modelo.
- Para os nossos Reels: baixo — não há técnica explícita.

### DistilBook product explainer
- Criador: @sudo_kiran · Tipo: Prompt · Tags: Product UI · Data: 25/09/2026
- Página: https://prompt-motion.com/sudo-kiran-4f8b59 · Post: https://x.com/sudo_kiran/status/2103486573476254201
- O que o vídeo mostra: explicador de 30 s de um produto digital, feito a partir da URL do produto.
- Técnica: é um template curto com um campo para a URL do produto. O modelo lê o site e monta sozinho um explicador dinâmico de 30 s. Não há roteiro, cena a cena, paleta nem som definidos.
- Para os nossos Reels: baixo — só confirma o padrão "uma fonte de conteúdo + duração fixa". Falta direção visual.

### Distilbook product video
- Criador: @ajith_io · Tipo: Prompt · Tags: Product UI · Data: 25/09/2026
- Página: https://prompt-motion.com/ajith-io-c52e09 · Post: https://x.com/ajith_io/status/2103469807375208546
- O que o vídeo mostra: vídeo de produto de 40 s sobre o Distilbook.
- Técnica: o prompt manda o modelo pesquisar o produto antes e então fazer um showreel de 40 s "com tudo". Não especifica estilo nem código; o passo de pesquisa prévia é o único ponto de método.
- Para os nossos Reels: baixo — só a ideia de pesquisar o tema antes de roteirizar.

### FigPad product promo
- Criador: @Ai_Baymax · Tipo: Prompt · Tags: Product UI · Data: 25/09/2026
- Página: https://prompt-motion.com/ai-baymax-0ef9dd · Post: https://x.com/Ai_Baymax/status/2103411004902416787
- O que o vídeo mostra: um promo de 1 minuto de um produto, com telas de interface.
- Técnica: o modelo gera o promo a partir do código-fonte do produto, reconstruindo a interface real em vez de inventá-la. Dura 1 minuto e foi feito numa única tentativa.
- Para os nossos Reels: baixo — trata de produto de software; a única coisa útil é a referência de que um minuto inteiro sai de uma vez.

### Gene Spectra promo
- Criador: @madebyjmayala · Tipo: Prompt · Tags: Product UI · Data: 25/09/2026
- Página: https://prompt-motion.com/madebyjmayala-b9204d · Post: https://x.com/madebyjmayala/status/2103578285892649220
- O que o vídeo mostra: promo de 15 s de um produto, feito com os elementos do site atual da marca.
- Técnica: o modelo pega os ativos do site no ar (imagens, UI, textos) e os reaproveita onde fizer sentido, para manter a coerência com a marca. A duração é de 15 s, com esforço máximo e uma tentativa só.
- Para os nossos Reels: baixo — nós não usamos marcas, mas a ideia de partir de um kit visual fixo (no nosso caso, um kit próprio do assessor) é válida.

### Lidlezz app promo
- Criador: @cansincengiz_me · Tipo: Prompt · Tags: Product UI · Data: 25/09/2026
- Página: https://prompt-motion.com/cansincengiz-me-cf68dd · Post: https://x.com/cansincengiz_me/status/2103532681774424245
- O que o vídeo mostra: promo de 15 s de um app, a partir do link do produto.
- Técnica: o prompt, em turco, é um desafio de 15 s para promover o app linkado, com o público do X como juiz. Não traz nenhuma direção visual, sonora ou técnica.
- Para os nossos Reels: baixo — não há técnica aproveitável.

### Norilu product launch video
- Criador: @sachaarbonel · Tipo: Prompt · Tags: Product UI · Data: 25/09/2026
- Página: https://prompt-motion.com/sachaarbonel-8f14f4 · Post: https://x.com/sachaarbonel/status/2103614797501673648
- O que o vídeo mostra: vídeo de lançamento de produto montado a partir dos designs já existentes do app.
- Técnica: pede um lançamento profissional em motion e dá ao modelo acesso ao arquivo de design do produto, para que as telas venham do material real em vez de serem inventadas. O texto exibido na página está truncado, sem mais detalhes de estilo ou render.
- Para os nossos Reels: baixo — a única lição é alimentar o modelo com um arquivo de design-base (no nosso caso, um kit de componentes escuro e dourado).

### ocrX app launch video
- Criador: @mehul4795 · Tipo: Prompt · Tags: Product UI · Data: 25/09/2026
- Página: https://prompt-motion.com/mehul4795-4a7007 · Post: https://x.com/mehul4795/status/2103420457110417532
- O que o vídeo mostra: vídeo de lançamento de um app Android de OCR.
- Técnica: o prompt é uma linha só (vídeo de lançamento do app) e não dá nenhuma direção visual, de ritmo ou de som.
- Para os nossos Reels: baixo — não há técnica para extrair.

### Step race app promo
- Criador: @marklaunches · Tipo: Prompt · Tags: Product UI · Data: 26/09/2026
- Página: https://prompt-motion.com/marklaunches-3b9492 · Post: https://x.com/marklaunches/status/2103811146411041046
- O que o vídeo mostra: promo de um app de corrida de passos, com telas do produto e tom emocional.
- Técnica: uma tentativa. O prompt é um pedido aberto de vídeo "incrível" com tom emocional, sem especificações. A única alavanca é o tom (emocional em vez de técnico), que leva o modelo a narrativa e ritmo mais dramáticos.
- Para os nossos Reels: baixo — só reforça que vale definir o tom emocional no briefing (por exemplo, segurança e tranquilidade financeira).

### Supasito launch video
- Criador: @wozu_co · Tipo: Prompt · Tags: Product UI · Data: 01/10/2026
- Página: https://prompt-motion.com/wozu-co-242285 · Post: https://x.com/wozu_co/status/2105662660779893062
- O que o vídeo mostra: vídeo de lançamento de menos de 15 s de um site, com telas animadas.
- Técnica: o prompt, de uma linha, pede um vídeo de lançamento para um domínio, com teto de duração abaixo de 15 s. O modelo pesquisa o site e define o resto.
- Para os nossos Reels: baixo — nada além da duração curta.

### SuperX feature release teaser
- Criador: @robj3d3 · Tipo: Prompt · Tags: Product UI · Data: 05/10/2026
- Página: https://prompt-motion.com/robj3d3-b18fad · Post: https://x.com/robj3d3/status/2107040421989994822
- O que o vídeo mostra: teaser de 15 s da próxima versão de um produto, com telas.
- Técnica: o modelo lê o roadmap do produto e transforma o conteúdo num teaser de 15 s "sem economizar". O método está em alimentar o roteiro com um documento-fonte.
- Para os nossos Reels: baixo — a ideia de partir de um documento-fonte (ex.: relatório mensal) é útil, mas não há técnica visual.

### Three.js Skyraider aircraft model
- Criador: @BuildFastWithAI · Tipo: Prompt · Tags: Product UI · Data: 24/09/2026
- Página: https://prompt-motion.com/buildfastwithai-ed9447 · Post: https://x.com/BuildFastWithAI/status/2103152898708582551
- O que o vídeo mostra: modelo 3D de um avião militar antigo, montado e girando em Three.js.
- Técnica: Three.js, esforço alto, uma tentativa. O prompt só pede a modelagem procedural de uma aeronave específica. Mostra que o modelo consegue montar geometria 3D detalhada só com primitivas em código.
- Para os nossos Reels: baixo — tema sem relação; no máximo prova que objetos 3D procedurais (uma moeda, um cofre) são viáveis em Three.js.

### Website analyzer product promo
- Criador: @en______ra · Tipo: Prompt · Tags: Product UI · Data: 27/09/2026
- Página: https://prompt-motion.com/en-ra-81c6dd · Post: https://x.com/en______ra/status/2104035188061986980
- O que o vídeo mostra: promo de 15 s de um analisador de sites, com telas do produto.
- Técnica: o molde de showreel de 15 s, com o nome do projeto como campo a substituir. Sem mais especificações.
- Para os nossos Reels: baixo — sem técnica a extrair.

### Mascot referral program promo
- Criador: @paulo_kombucha · Tipo: Prompt · Tags: Product UI, Characters · Data: 28/09/2026
- Página: https://prompt-motion.com/paulo-kombucha-96431c · Post: https://x.com/paulo_kombucha/status/2104481235028283883
- O que o vídeo mostra: promo de 15 s de um programa de indicações, conduzido por um mascote e por telas do produto.
- Técnica: briefing curto de 15 s e alto dinamismo; o mascote e a UI aparecem pelas tags e pela capa, não pelo texto. Sem instruções de estilo, som ou render.
- Para os nossos Reels: baixo — mascote e programa de indicação não se encaixam, e o prompt não traz técnica.

### Dub promo video
- Criador: @steventey · Tipo: Prompt · Tags: Product UI, Charts · Data: 25/09/2026
- Página: https://prompt-motion.com/steventey-0d20e4 · Post: https://x.com/steventey/status/2103625902211088880
- O que o vídeo mostra: promo de lançamento de SaaS de 15 s, com telas e gráficos de métricas.
- Técnica: o prompt é o pedido genérico de showreel de 15 s aplicado a um produto SaaS, em uma iteração com esforço alto. Sem parâmetros de estilo ou código.
- Para os nossos Reels: baixo — nada além da referência visual de gráficos de métricas animados.

### founder.page launch video
- Criador: @RatheeJaisal · Tipo: Prompt · Tags: Product UI, Charts · Data: 26/09/2026
- Página: https://prompt-motion.com/ratheejaisal-1f4538 · Post: https://x.com/RatheeJaisal/status/2103774864742154698
- O que o vídeo mostra: vídeo de lançamento de até 20 s que passa por todas as funcionalidades de um produto, com telas e gráficos.
- Técnica: limite máximo de 20 s, ritmo acelerado, cobrir todas as funções principais e manter o visual da marca; sem outros detalhes.
- Para os nossos Reels: baixo — prompt genérico; o vídeo pode servir de referência de gráficos em UI.

### Crux motion design showreel
- Criador: @marouanegazouzi · Tipo: Prompt · Tags: Product UI, Charts, Kinetic type, Music · Data: 25/09/2026
- Página: https://prompt-motion.com/marouanegazouzi-6071d5 · Post: https://x.com/marouanegazouzi/status/2103608571435131257
- O que o vídeo mostra: showreel de 15 s com UI, gráficos, texto cinético e música.
- Técnica: é o template padrão de showreel (esforço máximo). O modelo combinou interface, gráficos animados e tipografia ao ritmo da trilha.
- Para os nossos Reels: baixo — o vocabulário é o certo (gráficos + texto), mas não há instrução concreta.

### AgentHud project motion video
- Criador: @Jazzen_Chen · Tipo: Prompt · Tags: Product UI, Code · Data: 26/09/2026
- Página: https://prompt-motion.com/jazzen-chen-4542ae · Post: https://x.com/Jazzen_Chen/status/2103751442393894989
- O que o vídeo mostra: um vídeo de apresentação de um projeto de software, com interface e trechos de código.
- Técnica: um prompt de uma frase rodado dentro do próprio repositório do projeto, com esforço Max. O modelo lê o código para extrair telas e funcionalidades.
- Para os nossos Reels: baixo — é focado em software.

### AI Arena product promo
- Criador: @ezshine · Tipo: Prompt · Tags: Product UI, Code · Data: 25/09/2026
- Página: https://prompt-motion.com/ezshine-c90d73 · Post: https://x.com/ezshine/status/2103501705698750731
- O que o vídeo mostra: apresentação dos principais recursos de um projeto de software, com telas e código.
- Técnica: briefing de uma frase pedindo um vídeo de apresentação de produto com padrão profissional, entregue em MP4 16:9. O modelo lê o projeto, escolhe os destaques e decide estilo e pipeline sozinho.
- Para os nossos Reels: baixo — horizontal, ligado a um produto específico e sem técnica explícita.

### Lism CSS 1.0 release video
- Criador: @ddryo_loos · Tipo: Prompt · Tags: Product UI, Code · Data: 02/10/2026
- Página: https://prompt-motion.com/ddryo-loos-300829 · Post: https://x.com/ddryo_loos/status/2105824736072925621
- O que o vídeo mostra: vídeo de 15 s para redes anunciando a versão 1.0 de um framework CSS.
- Técnica: prompt curto em japonês: 15 s, para redes sociais, "simples, mas com dinamismo". Nada sobre fonte, cor, câmera, som ou render.
- Para os nossos Reels: baixo — só o lema "simples com dinamismo", que já é nosso padrão.

### Second brain service promo
- Criador: @TheViableEdge · Tipo: Prompt · Tags: Product UI, Code · Data: 27/09/2026
- Página: https://prompt-motion.com/theviableedge-9065be · Post: https://x.com/TheViableEdge/status/2104207707980869918
- O que o vídeo mostra: promo de 15 s de um serviço de "segundo cérebro", usada como peça principal da página de vendas de um curso.
- Técnica: briefing de showreel de 15 s, renderizado em Remotion e pensado para o topo de uma página de vendas. Não especifica estilo, cor nem som.
- Para os nossos Reels: baixo — sem técnica escrita a reaproveitar.

### Alan agent platform promo
- Criador: @prasad_pilla · Tipo: Prompt · Tags: Product UI, Diagrams · Data: 26/09/2026
- Página: https://prompt-motion.com/prasad-pilla-2c0cba · Post: https://x.com/prasad_pilla/status/2103728953785496049
- O que o vídeo mostra: promo de 15 s de uma plataforma de agentes de IA, com telas de produto e diagramas.
- Técnica: briefing de uma frase com o formato "showreel de motion designer" (15 s, dinâmico, ambição máxima) aplicado a uma marca. Não define estilo, cor, câmera nem render; o resultado depende do que o modelo sabe sobre o produto.
- Para os nossos Reels: baixo — é promo de produto de terceiro e o prompt não traz técnica reaproveitável.

### DistilBook motion explainer
- Criador: @sudo_kiran · Tipo: Prompt · Tags: Product UI, Diagrams · Data: 29/09/2026
- Página: https://prompt-motion.com/sudo-kiran-b055de · Post: https://x.com/sudo_kiran/status/2104846546768670892
- O que o vídeo mostra: explicador de produto de ~30 s com telas de interface e diagramas.
- Técnica: brief de explicador de produto de 30 s com campo para a URL do produto e pedido de resultado impressionante; sem especificação de estilo, som ou render.
- Para os nossos Reels: baixo — prompt genérico.

### DistilBook product explainer
- Criador: @sudo_kiran · Tipo: Prompt · Tags: Product UI, Diagrams · Data: 26/09/2026
- Página: https://prompt-motion.com/sudo-kiran-6609ed · Post: https://x.com/sudo_kiran/status/2103761658745335993
- O que o vídeo mostra: explicador de 30 s de um produto que resume livros, com telas e diagramas.
- Técnica: template genérico em que o usuário só troca o link do produto; pede bom roteiro, boa cor, boa música e algo que dê vontade de rever. É vago em tudo, exceto na duração de 30 s.
- Para os nossos Reels: baixo — serve só como lembrete de que roteiro e replay valem mais que efeito; não há técnica.

### Visual guides library launch
- Criador: @techyoutbe · Tipo: Prompt · Tags: Product UI, Diagrams, Code · Data: 25/09/2026
- Página: https://prompt-motion.com/techyoutbe-945b56 · Post: https://x.com/techyoutbe/status/2103465227807588678
- O que o vídeo mostra: lançamento de uma biblioteca de guias visuais no formato de vídeo de lançamento de SaaS.
- Técnica: pede ao modelo que escolha um SaaS conhecido, busque na web os assets reais (logos, imagens) e monte um vídeo de lançamento no padrão do Twitter, focado em recursos e benefícios. Não fixa estilo, duração nem render.
- Para os nossos Reels: baixo — depende de logos e marcas reais, o que as nossas regras proíbem.

### Chunku product promo
- Criador: @reyzostyle · Tipo: Prompt · Tags: Product UI, Kinetic type · Data: 30/09/2026
- Página: https://prompt-motion.com/reyzostyle-b55864 · Post: https://x.com/reyzostyle/status/2105421514665542114
- O que o vídeo mostra: promo de 10 s de um produto digital, com telas da interface e tipografia cinética.
- Técnica: feito em HyperFrames numa única tentativa. O prompt aponta para a URL do produto, pede 10 s em formato de showreel e esforço máximo, sem outras regras. O que funciona vem da pesquisa automática da página do produto (cores, telas, textos), convertida em tipografia em movimento.
- Para os nossos Reels: baixo — mostra que HyperFrames resolve um one-shot curto, mas não traz técnica específica.

### Email tool promo reel
- Criador: @melvynx · Tipo: Prompt · Tags: Product UI, Kinetic type · Data: 26/09/2026
- Página: https://prompt-motion.com/melvynx-6cde6c · Post: https://x.com/melvynx/status/2103714680577638493
- O que o vídeo mostra: reel promocional de ~15 s de uma ferramenta de e-mail, montado a partir do site do produto.
- Técnica: o prompt é um brief mínimo, um motion dinâmico de cerca de 15 s cujo único insumo é a URL de um site (campo a preencher). O modelo extrai do site a identidade e as telas e decide tudo o mais (tipo, cor, ritmo). Não há instruções de estilo, câmera, som ou render.
- Para os nossos Reels: baixo — só vale a ideia de alimentar o gerador com uma fonte (URL/relatório) como matéria-prima; não traz técnica reaproveitável.

### Tally product demo
- Criador: @VisheshBaghell · Tipo: Prompt · Tags: Product UI, Kinetic type · Data: 26/09/2026
- Página: https://prompt-motion.com/visheshbaghell-3aba37 · Post: https://x.com/VisheshBaghell/status/2103772327146119508
- O que o vídeo mostra: demo de produto do site do autor, percorrendo todas as funcionalidades com texto cinético.
- Técnica: o prompt delega o trabalho a uma skill pessoal de demos e só pede que ela cubra todos os recursos do produto. Não descreve estilo, ritmo nem render; o valor está na skill, que não está publicada na página.
- Para os nossos Reels: baixo — sem técnica visível e focado em produto.

### Trezio app motion reel
- Criador: @agonaliu_ · Tipo: Prompt · Tags: Product UI, Kinetic type · Data: 27/09/2026
- Página: https://prompt-motion.com/agonaliu-466a8f · Post: https://x.com/agonaliu_/status/2104117465475326227
- O que o vídeo mostra: reel de 15 s de um app, com telas e tipografia cinética.
- Técnica: briefing genérico de showreel de 15 s, em one-shot. Não define estilo, cor, som nem render.
- Para os nossos Reels: baixo — sem técnica a extrair.

### QuickDesign brand promo
- Criador: @quickdesignio · Tipo: Prompt · Tags: Product UI, Kinetic type, Music · Data: 25/09/2026
- Página: https://prompt-motion.com/quickdesignio-dd93d0 · Post: https://x.com/quickdesignio/status/2103617779857338399
- O que o vídeo mostra: promo de marca de 15 s para uma ferramenta de design, com telas do produto e texto cinético.
- Técnica: o brief tem dois objetivos ao mesmo tempo, vender o produto e exibir habilidade de motion, em 15 s de ritmo dinâmico. Não define estética, fontes, cores nem som. O resultado mistura UI do produto, tipografia animada e música.
- Para os nossos Reels: baixo — a ideia de dar ao vídeo um objetivo de conteúdo e um de forma é útil, mas o prompt não traz técnica concreta.

### Distilbook motion showreel
- Criador: @itisRazak · Tipo: Prompt · Tags: Product UI, Kinetic type, Particles, Music · Data: 25/09/2026
- Página: https://prompt-motion.com/itisrazak-3ad902 · Post: https://x.com/itisRazak/status/2103517930424332386
- O que o vídeo mostra: showreel de ~40 s sobre o Distilbook, com telas, texto cinético, partículas e música.
- Técnica: mesmo pedido curto de pesquisar o produto e fazer um showreel de 40 s, gerado de primeira; sem regras de estilo ou código.
- Para os nossos Reels: baixo — sem técnica aproveitável.

### Travel visa service promo
- Criador: @thismacapital · Tipo: Prompt · Tags: Product UI, Kinetic type, Photos · Data: 26/09/2026
- Página: https://prompt-motion.com/thismacapital-dfba20 · Post: https://x.com/thismacapital/status/2103773635714375808
- O que o vídeo mostra: promo de 15 s de um serviço de vistos de viagem, com telas, texto cinético e fotos.
- Técnica: pedido genérico de showreel de 15 s, sem especificações. O resultado é escolha do modelo.
- Para os nossos Reels: baixo — sem instruções técnicas.

### Personal skills showreel
- Criador: @ibrahimwasim240 · Tipo: Prompt · Tags: Product UI, Particles, Characters · Data: 26/09/2026
- Página: https://prompt-motion.com/ibrahimwasim240-809370 · Post: https://x.com/ibrahimwasim240/status/2103943233432940763
- O que o vídeo mostra: um showreel de habilidades de 25 s com telas de interface, partículas e personagem.
- Técnica: uma variação do briefing de showreel, com 25 s e esforço Max. Não há instruções de estilo ou render.
- Para os nossos Reels: baixo — não traz técnica explícita.

### Bento.surf product video
- Criador: @bizibeast · Tipo: Prompt · Tags: Product UI, Phone · Data: 26/09/2026
- Página: https://prompt-motion.com/bizibeast-10f264 · Post: https://x.com/bizibeast/status/2103696876130505124
- O que o vídeo mostra: vídeo de 40 s de um produto web, com telas em navegador e celular.
- Técnica: uma tentativa. O prompt manda pesquisar o produto antes e depois fazer um showreel de 40 s com esforço máximo. A etapa explícita de pesquisa dá ao modelo textos e telas reais.
- Para os nossos Reels: baixo — só confirma a etapa de pesquisa; sem regras visuais.

### Enxovaly baby app promo
- Criador: @gabrielbuzziv · Tipo: Prompt · Tags: Product UI, Phone · Data: 25/09/2026
- Página: https://prompt-motion.com/gabrielbuzziv-4ff0c6 · Post: https://x.com/gabrielbuzziv/status/2103590703289057430
- O que o vídeo mostra: promo de 15 s de um app de enxoval de bebê, com telas do produto num celular.
- Técnica: o prompt é o pedido genérico de showreel de 15 s; o diferencial é a stack HyperFrames (HTML renderizado como vídeo). Estilo, paleta e ritmo ficaram por conta do modelo.
- Para os nossos Reels: baixo — só confirma que HyperFrames é uma alternativa de render HTML; nenhuma instrução aproveitável.

### Commotion app showreel
- Criador: @Amol909S · Tipo: Prompt · Tags: Product UI, Phone, Code · Data: 25/09/2026
- Página: https://prompt-motion.com/amol909s-27533e · Post: https://x.com/Amol909S/status/2103456534768607293
- O que o vídeo mostra: showreel de 20 s de um app, destacando o layout em mosaico e o classificador automático de modelos.
- Técnica: usa o template de showreel com uma lista obrigatória de funcionalidades a destacar, mais o que o modelo julgar relevante (esforço médio). Cada recurso ganha seu bloco de demonstração em ritmo dinâmico.
- Para os nossos Reels: baixo — só confirma que listar os pontos obrigatórios no prompt dá foco ao vídeo.

### Fitters Bible app promo
- Criador: @Adamdesgns · Tipo: Prompt · Tags: Product UI, Phone, Diagrams · Data: 25/09/2026
- Página: https://prompt-motion.com/adamdesgns-478d6d · Post: https://x.com/Adamdesgns/status/2103542756555768014
- O que o vídeo mostra: promo de 15 s de um app de referência técnica para encanadores industriais, com telas em celular e diagramas.
- Técnica: prompt padrão de showreel (15 s, esforço máximo), numa tentativa. Pelas tags, o resultado mistura mockup de celular com diagramas técnicos explicativos.
- Para os nossos Reels: baixo — tema e prompt genéricos; nada específico a aproveitar.

### Claude self-promo spot
- Criador: @slvDev · Tipo: Prompt · Tags: Product UI, Phone, Kinetic type · Data: 25/09/2026
- Página: https://prompt-motion.com/slvdev-64c45a · Post: https://x.com/slvDev/status/2103569170075975986
- O que o vídeo mostra: spot autopromocional de 15 s ou mais, com telas de interface num celular e texto cinético.
- Técnica: o prompt é uma linha só, pedindo uma autopromoção de pelo menos 15 s (esforço máximo, uma tentativa). Pelas tags, o modelo resolveu com mockup de celular, UI e tipografia animada. Não há especificação de cor, ritmo ou som.
- Para os nossos Reels: baixo — o formato celular + UI combina com o vertical, mas não há instrução para destilar.

### Hoplite cloud handoff launch
- Criador: @ryan_morr · Tipo: Prompt · Tags: Product UI, Phone, Kinetic type · Data: 27/09/2026
- Página: https://prompt-motion.com/ryan-morr-ccc796 · Post: https://x.com/ryan_morr/status/2104249941136666741
- O que o vídeo mostra: lançamento de recurso em que, ao fechar o notebook, agentes de IA continuam rodando na nuvem.
- Técnica: o prompt só descreve a funcionalidade a mostrar e manda reutilizar os elementos de marca existentes do produto; não define estilo, câmera, ritmo ou render.
- Para os nossos Reels: baixo — útil só como lembrete de dar ao modelo um kit de identidade pronto (nosso escuro + dourado) em vez de deixá-lo inventar.

### Parenting app hype video
- Criador: @francoxavier33 · Tipo: Prompt · Tags: Product UI, Phone, Kinetic type · Data: 25/09/2026
- Página: https://prompt-motion.com/francoxavier33-d2dfd2 · Post: https://x.com/francoxavier33/status/2103486218323341663
- O que o vídeo mostra: vídeo "hype" de lançamento de um app de parentalidade, com telas no celular e texto cinético.
- Técnica: o pedido é uma linha (vídeo hype de demo/lançamento). O vídeo foi feito em Remotion, com algumas rodadas de ajuste. O modelo usou mockup de celular e tipografia animada. O prompt não especifica paleta, duração nem som.
- Para os nossos Reels: baixo — tema e marca alheios. Só reforça o padrão celular + UI + texto cinético.

### Dubz Up motion showreel
- Criador: @Devius_Maximus · Tipo: Prompt · Tags: Product UI, Phone, Kinetic type, Characters · Data: 29/09/2026
- Página: https://prompt-motion.com/devius-maximus-beab45 · Post: https://x.com/Devius_Maximus/status/2105069053521887428
- O que o vídeo mostra: showreel de um projeto pessoal com telas em celular, tipografia cinética e personagens.
- Técnica: prompt padrão de showreel ("go all out") aplicado a um projeto, sem duração nem estilo definidos. Pelas tags, o resultado combina mockup de celular, texto em movimento e mascotes.
- Para os nossos Reels: baixo — não há instruções reaproveitáveis.

### ViralGrow product promo
- Criador: @samuel_yostt · Tipo: Prompt · Tags: Product UI, Phone, Photos · Data: 01/10/2026
- Página: https://prompt-motion.com/samuel-yostt-891f87 · Post: https://x.com/samuel_yostt/status/2105746669035733275
- O que o vídeo mostra: promo de 15 s do ViralGrow com telas no celular e fotos.
- Técnica: pedido de showreel de 15 s com uma única restrição útil: seguir o estilo visual da landing page do produto. Sem detalhes de fonte, cor ou código.
- Para os nossos Reels: baixo — só a ideia de ancorar o estilo numa referência existente (no nosso caso, a identidade escura + dourado do assessor).

### CloudJoi search showcase
- Criador: @lester_tyy · Tipo: Prompt · Tags: Product UI, Photos · Data: 26/09/2026
- Página: https://prompt-motion.com/lester-tyy-f897f7 · Post: https://x.com/lester_tyy/status/2103733819568480587
- O que o vídeo mostra: uma demonstração da função de busca de um produto online, com interface e fotos.
- Técnica: o modelo estuda o produto a partir de um link e monta o vídeo em Remotion (React). A técnica está na combinação de pesquisa autônoma com um framework de vídeo declarativo.
- Para os nossos Reels: baixo — trata de produto de software; Remotion é uma alternativa ao nosso HTML+captura, mas não muda o essencial.

### Five scroll-based sections
- Criador: @ercankeskinx · Tipo: Prompt · Tags: Product UI, Photos · Data: 24/09/2026
- Página: https://prompt-motion.com/ercankeskinx-ec2568 · Post: https://x.com/ercankeskinx/status/2102995443818897906
- O que o vídeo mostra: cinco seções de site animadas por rolagem, cada uma com layout e contexto bem diferentes.
- Técnica: pede variedade máxima: cinco blocos de scroll-animation sem repetir padrão, com contexto e layout a cargo do modelo. Sem paleta, ritmo nem render definidos.
- Para os nossos Reels: baixo — é linguagem de site; no máximo inspira cenas verticais que "rolam" entre blocos de conteúdo.

### GenVizu product launch
- Criador: @listudio · Tipo: Prompt · Tags: Product UI, Photos · Data: 28/09/2026
- Página: https://prompt-motion.com/listudio-820c7b · Post: https://x.com/listudio/status/2104431418114023803
- O que o vídeo mostra: um vídeo de lançamento de produto com telas de interface e imagens, para uso no hero de um site e em go-to-market.
- Técnica: o modelo pesquisa sozinho o produto a partir de um link e monta o roteiro e as telas com base no que encontra. Não há especificações de estilo; a técnica é delegar a pesquisa.
- Para os nossos Reels: baixo — trata de produto de software; a ideia de deixar o modelo ler uma fonte, como um relatório, antes de roteirizar é a única coisa transferível.

### Photo retouch app promo
- Criador: @oliahmed205 · Tipo: Prompt · Tags: Product UI, Photos · Data: 28/09/2026
- Página: https://prompt-motion.com/oliahmed205-3e31c4 · Post: https://x.com/oliahmed205/status/2104679078465069378
- O que o vídeo mostra: promo de 15 s de um app de retoque de fotos montado com capturas de tela.
- Técnica: o modelo recebe o papel de "editor de vídeo muito profissional" e as capturas e ativos do produto como matéria-prima, num vídeo de 15 s. O prompt não dá direção de estética, ritmo nem som.
- Para os nossos Reels: baixo — só o recurso de dar um papel profissional ao modelo. Não há técnica.

### PicTwin AI app ad
- Criador: @l3d1c · Tipo: Prompt · Tags: Product UI, Photos · Data: 25/09/2026
- Página: https://prompt-motion.com/l3d1c-0e35a3 · Post: https://x.com/l3d1c/status/2103536553930752011
- O que o vídeo mostra: anúncio de um app de IA para fotos, com telas e imagens de exemplo.
- Técnica: o prompt é de "meta-nível": pede que o modelo primeiro escreva um prompt de motion design para o anúncio do site e então execute. A página só mostra essa linha.
- Para os nossos Reels: baixo — o tema não se aplica, mas a ideia de o modelo escrever o próprio briefing antes de executar é um passo útil.

### Pixelup Labs studio showreel
- Criador: @arjunsh1607 · Tipo: Prompt · Tags: Product UI, Photos · Data: 27/09/2026
- Página: https://prompt-motion.com/arjunsh1607-93005d · Post: https://x.com/arjunsh1607/status/2104295133432922126
- O que o vídeo mostra: showreel de 15 s de um estúdio, com interface e fotos.
- Técnica: brief curto de 15 s para a marca do estúdio, pedindo atenção extrema a detalhes e ambição; nenhuma especificação de estilo, som ou render.
- Para os nossos Reels: baixo — nada reaproveitável no prompt.

### Quetzal social app reel
- Criador: @miskinho_ · Tipo: Prompt · Tags: Product UI, Photos · Data: 26/09/2026
- Página: https://prompt-motion.com/miskinho-443898 · Post: https://x.com/miskinho_/status/2103847584531956105
- O que o vídeo mostra: reel de 15 s de um app social, com telas e fotos.
- Técnica: aplica o template de showreel a um produto, num vídeo único de 15 s, dinâmico e com esforço máximo. Não define visual nem som.
- Para os nossos Reels: baixo — não há técnica explícita, e fotos de rede social não se aplicam ao nosso tema.

### Studio website showreel
- Criador: @andginja · Tipo: Prompt · Tags: Product UI, Photos · Data: 25/09/2026
- Página: https://prompt-motion.com/andginja-333d32 · Post: https://x.com/andginja/status/2103492000733618685
- O que o vídeo mostra: showreel de 15 s do site de um estúdio, com páginas e fotos do portfólio em movimento.
- Técnica: uma tentativa. O prompt pede 15 s sobre o site e esforço máximo, sem mais regras. O modelo usa as imagens e páginas do próprio site como material, com transições entre seções.
- Para os nossos Reels: baixo — depende de fotos, e nós evitamos imagens de pessoas e marcas.

### Tented image gen product video
- Criador: @justincooperman · Tipo: Prompt · Tags: Product UI, Photos · Data: 24/09/2026
- Página: https://prompt-motion.com/justincooperman-e7bbc4 · Post: https://x.com/justincooperman/status/2103201167367188876
- O que o vídeo mostra: clipe em Blender em que um usuário pede imagens de marca e elas aparecem aplicadas em peças de conteúdo.
- Técnica: o brief é uma frase que conta o fluxo de uso como mini-história (pedido → imagens geradas → imagens dentro do conteúdo). O render é em Blender, numa tentativa só. O prompt não define estilo, câmera, duração nem som.
- Para os nossos Reels: baixo — usa Blender (fora da nossa stack). Só a estrutura "pedido → resultado aplicado" serve como roteiro.

### Psychedelic hypnotic eye showreel
- Criador: @monokern · Tipo: Prompt · Tags: Shapes · Data: 25/09/2026
- Página: https://prompt-motion.com/monokern-ade5b6 · Post: https://x.com/monokern/status/2103563538828832979
- O que o vídeo mostra: showreel de 20 s de formas psicodélicas e hipnóticas em torno de um olho.
- Técnica: brief curto (20 s, dinâmico, psicodélico e hipnótico, esforço máximo), sem especificar paleta, fonte, câmera, som ou render. A página menciona uma versão "mais forte" do prompt não incluída.
- Para os nossos Reels: baixo — estética psicodélica não combina com a sobriedade de um assessor de investimentos.

### TypingMind logo reveal
- Criador: @tdinh_me · Tipo: Prompt · Tags: Shapes · Data: 26/09/2026
- Página: https://prompt-motion.com/tdinh-me-815acb · Post: https://x.com/tdinh_me/status/2103704250329301409
- O que o vídeo mostra: revelação lenta de um logo montado peça por peça a partir de formas.
- Técnica: pedido curto de uma transição lenta em que o símbolo vai sendo construído aos poucos até a revelação. Sem detalhes de estilo, duração ou código.
- Para os nossos Reels: baixo — a ideia de montar um símbolo a partir de formas poderia virar o fechamento com um ícone neutro, mas não usamos logos.

### Distilbook motion showreel
- Criador: @ajith_io · Tipo: Prompt · Tags: Shapes, Particles · Data: 25/09/2026
- Página: https://prompt-motion.com/ajith-io-ea7f2d · Post: https://x.com/ajith_io/status/2103541149709615243
- O que o vídeo mostra: showreel de ~30 s de um produto, com formas e partículas, replicando o estilo de um vídeo de referência.
- Técnica: o prompt manda pesquisar o produto e baixar um vídeo de referência para copiar o estilo dele; o resto é pedido de energia alta. Não há especificação própria de visual, som ou render.
- Para os nossos Reels: baixo — o método "pesquisar o tema antes + seguir uma referência" é válido, mas a técnica em si fica no vídeo de referência.

### Flowdrive motion showreel
- Criador: @manuelogomigo · Tipo: Prompt · Tags: Shapes, Particles · Data: 25/09/2026
- Página: https://prompt-motion.com/manuelogomigo-f33ca9 · Post: https://x.com/manuelogomigo/status/2103614667038052364
- O que o vídeo mostra: showreel abstrato de 15 s com formas geométricas e partículas para um produto.
- Técnica: usa o prompt padrão de showreel (15 s, "go all out") sem mais regras. Pelas tags, o resultado é abstrato, com formas e partículas fluindo. Não há instruções reaproveitáveis além da duração.
- Para os nossos Reels: baixo — fluxo de partículas pode virar metáfora de "fluxo de capital", mas o prompt não ensina como fazer.

### Full Stop figure sequence
- Criador: @HBCoop_ · Tipo: Prompt · Tags: Shapes, Particles · Data: 05/10/2026
- Página: https://prompt-motion.com/hbcoop-de365c · Post: https://x.com/HBCoop_/status/2107139305324122491
- O que o vídeo mostra: uma sequência abstrata de figuras, formas e partículas criada livremente pelo modelo.
- Técnica: carta branca total: o modelo escolhe tema e linguagem só para demonstrar o que sabe fazer, com esforço máximo e em one-shot. Nenhuma especificação de estilo, ritmo ou render.
- Para os nossos Reels: baixo — sem tema nem técnica explícita para reaproveitar.

### Motion designer résumé reel
- Criador: @RaphaelAubryy · Tipo: Prompt · Tags: Shapes, Particles · Data: 25/09/2026
- Página: https://prompt-motion.com/raphaelaubryy-4b137e · Post: https://x.com/RaphaelAubryy/status/2103416909857190360
- O que o vídeo mostra: showreel de 15 s com formas e partículas.
- Técnica: o brief padrão de showreel de currículo de 15 s, "vá com tudo", sem nenhuma especificação técnica.
- Para os nossos Reels: baixo — nada reaproveitável no prompt.
