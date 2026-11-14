# Guias do prompt-motion.com (templates e blog)

Leitura feita em 14/11/2026 com WebFetch (um resumo por página, mais uma segunda passada em duas delas). Texto reescrito com nossas palavras; aspas só em expressões curtas. Quando uma página não trazia um parâmetro, isso está anotado como "não informado".

---

## 1. Template "showreel"

**Link:** https://prompt-motion.com/templates/showreel

**Ideia central:** pegar o prompt mais copiado do site (uma linha pedindo um showreel de 15 s, "vá com tudo") e reescrevê-lo com direção criativa e técnica completas, para que o modelo não decida tudo sozinho. A recomendação é rodar no Opus 5.5 com esforço máximo.

**Regras e técnicas:**
- **Um único conceito**, nomeado em uma linha antes de começar (exemplo do tipo "tinta vira tipo vira arquitetura"). Cada cena nasce da anterior, em vez de uma colagem de efeitos.
- **Transições por transformação:** formas, letras e cores viram a cena seguinte. Sem cortes secos e sem fades.
- **Tipografia:** uma família só (Geist, Inter ou uma display forte do Google Fonts).
- **Paleta:** no máximo 3 cores, além de preto e branco.
- **Câmera:** uma linguagem de câmera só, mantida do início ao fim.
- **Repertório obrigatório, com tempo igual para cada item:** tipografia cinética, morphing de formas, uma passagem de 2D para 3D, um momento de dados/UI e um título final.
- **Proibições:** explosões de partículas, glows, lens flare, tremor de câmera, separação RGB, crossfade, gradientes genéricos, easing "saltitante", qualquer quadro parado por mais de **0,5 s** e qualquer coisa com cara de template.
- **Estrutura de tempo:** 15 s a **120 BPM** (cerca de 30 batidas), com algo acontecendo em toda batida.
  - Compasso 1 = gancho.
  - Cada compasso seguinte = uma técnica, encadeada na anterior.
  - Último compasso completo = momento mais forte.
  - Meio compasso final = título; o último quadro é igual ao primeiro para fechar o loop.
  - (7 compassos de 2 s + meio compasso de 1 s = 15 s.)
- **Build:**
  1. Um HTML em 1920x1080; todo estilo é calculado a partir do tempo dentro de `window.seek(t)`. Sem animação CSS, sem timers, sem estado guardado entre quadros.
  2. Easings de mola e exponenciais escritos como funções do tempo. O desfoque acompanha velocidade e direção nos movimentos rápidos.
  3. Trilha gerada em código (Web Audio, OfflineAudioContext): kick em cada batida, riser antes do último compasso completo, impacto em cada troca de cena. Exporta WAV.
  4. Render com Playwright a 60 fps, **3 subquadros por quadro** misturados com ffmpeg `tmix` (motion blur), e depois o áudio entra no MP4.
  5. Revisão: um quadro por batida antes do render final, corrigindo o que estiver poluído, fora do tempo, sobreposto ou ilegível.
- **Fluxo pedido ao agente:** apresentar o conceito e um storyboard batida a batida, construir sem fazer perguntas e entregar o MP4.
- **Campos customizáveis:** conceito, fonte e paleta.
- **Não informado:** parâmetros numéricos das molas (rigidez/amortecimento), intensidade do blur, formato vertical.

---

## 2. Template "realtime" (3D)

**Link:** https://prompt-motion.com/templates/realtime

**Ideia central:** um prompt para peças 3D em three.js com cara de filme, e não de demo técnica. O prompt é dividido em cinco blocos: `direction` (estilo, câmera, luz, materiais, movimento, proibições), `structure` (lista de planos), `build` (requisitos técnicos), `gotchas` (armadilhas de render) e `start` (o que fazer primeiro).

**Regras e técnicas:**
- **Plano-chave:** existe um momento-assinatura (no exemplo, um recuo de câmera que revela um desenho visto de cima), e todo o resto prepara esse momento.
- **Estilo:** luz de dia suave, muito espaço livre, preto e branco com **um único acento** de cor, uma fonte.
- **Câmera de cinema:** cada plano tem **um movimento nomeado** (dolly, crane, orbit, push-in, rack focus), com aceleração e desaceleração suaves. Nada de controles de órbita livres, e a câmera nunca atravessa geometria.
- **Luz:** três pontos (key, fill, rim) com sombras suaves; mapa de ambiente para reflexos; névoa para dar profundidade; tone mapping ACES.
- **Materiais:** físicos (PBR), com rugosidades diferentes entre si; nada pode parecer material padrão.
- **Movimento:** os elementos reagem uns aos outros (o que é tocado se mexe, o que está perto acende). Molas ou física simples, nunca interpolação linear.
- **Proibições:** luz e material padrão, rótulos de texto flutuando, brilho em tudo, "um objeto girando devagar" como ideia central e qualquer cara de demo.
- **Estrutura:** planos de **cerca de 3 s** cada (exemplo: macro com rack focus → dolly para trás revelando a repetição → crane por cima → um elemento se solta e vem até a câmera "com peso" → plano-assinatura → fechamento com marca/URL). Pede um MP4 de 20 s.
- **Build:** um HTML, three.js via CDN, sem build; tudo modelado em código, sem modelos ou texturas baixados; profundidade de campo só onde precisa; meta de 60 fps em laptop; modo `?render`, em que cada quadro sai do tempo, sem relógio e com aleatoriedade semeada, capturado por Playwright em 1920x1080.
- **Revisão:** um quadro por plano, corrigindo o que estiver chapado, serrilhado, com clipping ou ilegível.
- **Armadilhas:** ajustar o shadow bias (evita "acne" listrado); manter near/far da câmera justos (evita tremulação ao longe); semear todo número aleatório para o render bater com a prévia.
- **Início:** descrever o plano de cenas em poucas linhas e construir direto, sem perguntas.
- **Não informado:** BPM, valores de easing/mola, bias, near/far.

---

## 3. Página "customize"

**Link:** https://prompt-motion.com/customize

**Ideia central:** partir de um prompt que já deu certo e adaptá-lo (objetivo do vídeo, formato, cores etc.) em vez de escrever do zero. Os templates expõem como campos tudo o que faz sentido trocar.

**Regras e técnicas:**
- Reaproveitar um prompt comprovado e trocar só os campos: assunto, objetivo, formato, cores.
- Templates disponíveis: showreel e 3D. Explicativo, filme de produto e curta estão anunciados para depois.
- Categorias da galeria que servem de referência: UI de produto, telefone, **gráficos (charts)**, **diagramas**, **tipografia cinética**, formas, partículas, personagens, fotos, música e código.
- **Não informado:** durações, easings, BPM, fontes, paletas, fps, resolução. A página não traz regras técnicas.

---

## 4. Página "about"

**Link:** https://prompt-motion.com/about

**Ideia central:** biblioteca gratuita e com curadoria humana de vídeos de motion feitos com IA (Claude). Cada vídeo vem acompanhado do prompt ou skill que o gerou e do crédito ao criador. Em novembro de 2026 eram 240 vídeos.

**Regras e técnicas:**
- Cada entrada passa por revisão manual e credita o criador, com link para a postagem original.
- Vídeos e prompts pertencem aos criadores, não ao site. Para nós: estudar as técnicas, não reproduzir os vídeos.
- **Não informado:** nenhum parâmetro técnico.

---

## 5. Blog: "Fix AI motion graphics with Claude"

**Link:** https://prompt-motion.com/blog/fix-ai-motion-graphics-with-claude

**Ideia central:** um bom prompt não basta, porque mesmo revisando os próprios quadros o modelo deixa passar quadros vazios, textos pequenos e pausas longas. A saída é um ciclo em etapas (planejar → checar stills → checar movimento → corrigir uma coisa por vez), que acha os problemas enquanto ainda são baratos.

**Etapa 1: planejar antes de codar**
- Três ideias **realmente diferentes**, cada uma com um still (três variações da mesma ideia não contam).
- Lista de assets com a origem de cada um. O que faltar vira pergunta, nunca invenção.
- **Tabela de batidas:** uma linha por batida, com tempo, o que aparece, o que se mexe e **por que a batida existe**. Se não houver justificativa, a batida sai.

**Etapa 2: checar stills (contact sheet)**
- Um still do meio de cada batida, todos numa folha só (mais rápido de revisar e deixa a sessão menor).
- Critérios:
  - um elemento focal por quadro, com pelo menos **metade da largura**;
  - texto legível no celular, com no mínimo **32 px em 1080p**;
  - nada nos cantos (timecodes, rótulos, colchetes);
  - espaçamento uniforme dentro de grupos;
  - layout diferente do quadro anterior.

**Etapa 3: checar o movimento**
- Para cada transição, uma tira com **todos os quadros de 0,3 s antes até 0,3 s depois**.
- Varrer o vídeo atrás de "pops" de um quadro só (exceto em sequências rápidas planejadas).
- Assistir a uma prévia leve, em velocidade normal, antes do render final.

**Etapa 4: corrigir**
- Apontar o **segundo exato** e descrever o que deveria acontecer. Exemplo forte: "em 18,3 s corta de X direto para Y sem ligação; o texto deveria subir, fazer um arco e pousar crescendo até o tamanho do destino". Exemplo fraco: "a transição está estranha".
- **Uma mudança por vez.**
- **Proteger o que funciona** (do tipo "não mexa nada depois de 2,9 s").
- **Pedir evidência:** os quadros de 18,0 a 19,0 s e medições, não apenas um "corrigido".

**Tabela de problemas e correções:**

| Sintoma | Correção |
|---|---|
| Elementos pequenos boiando em quadro vazio | Focal com ≥ 60% da largura; cortar na borda em vez de encolher |
| Dois textos sobrepostos por alguns quadros | O texto antigo sai **antes** de o novo entrar |
| Cenas que só cortam ou dissolvem | Um elemento sai de A, viaja e assume um papel novo em B |
| Tudo se mexe junto | Variar duração, atraso e velocidade; nunca stagger idêntico |
| Bounce em tudo | Assentamento suave, sem quique nem overshoot |
| Coisas surgindo do nada | Crescer, deslizar de uma borda ou revelar com máscara |
| Trepidação ou render diferente a cada vez | Cada quadro sai do tempo; sem CSS animation, timers ou `Math.random` sem semente |
| Corte fora do tempo | Mapear as batidas do áudio e cortar em batida ou meia batida |

**Custo e sessão:** um vídeo de 30 s custou cerca de US$ 14–15 e 1,5–2 h. As rodadas de polimento numa mesma sessão foram ficando mais caras (5,83 → 9,69 → 13,48), então a recomendação é abrir uma sessão nova por rodada e manter plano, tabela de batidas e decisões em arquivos.

**Limites do modelo:** ele mede loudness e batidas, mas não ouve se a música combina ou se um efeito incomoda (ouça de olhos fechados). Também vê se o movimento é suave, mas não se ele "parece certo": num teste com 13 vídeos, concordou só moderadamente com um motion designer. Um humano precisa assistir em velocidade normal.

**As 4 linhas para colar em qualquer prompt:** planejar primeiro e esperar aprovação; checar contact sheet e tiras antes do render, mostrando evidências; guardar decisões em arquivos; corrigir uma coisa por vez, com quadros como prova.

**Parâmetros do prompt de exemplo (lançamento, com narração), muito úteis para nós:**
- 1440x1440, 60 fps, 22 s, fundo branco com tinta preta e uma tipografia.
- **Roteiro de locução:** 9 linhas; tags de emoção usadas com moderação (calmas nas frases tranquilas, entusiasmo só no verbo), **nenhuma tag na abertura** (uma tag "calorosa" pode soar sussurrada, e "excited" pode soar falso).
- **Voz:** gerar 4 takes completos e regenerar cada linha ruim até 4 vezes; encurtar pausas **> 0,28 s para 0,2 s**; nivelar cada frase em direção à mediana (85% do caminho), mexendo no ganho só nas pausas.
- **Alinhamento:** cortar a leitura em silêncios de **≥ 100 ms**, transcrever cada trecho separado e ancorar a primeira palavra no onset medido (uma transcrição única pode atrasar palavras em até meio segundo).
- **Câmera:** zoom lento de **1,0 a 1,04** por cena; a cena seguinte começa no zoom em que a anterior terminou (voltar a 1,0 na transição dá um tranco).
- **Entradas:** fades de no mínimo **0,3 s** (um fade de 0,05 s parece pop-in); trocas rápidas de imagem em semicolcheia, com um clique por troca.
- **Destaque de palavra:** gradiente nas cores da marca com brilho sutil atrás. **Proibido o retângulo atrás da palavra**, que parece seleção de texto.
- **Vidro líquido:** blur de ~14 px no corpo, faixa de 12 px na borda com lupa de 1,06x, brilho no topo, borda luminosa e sombra suave.
- **Música:** 129,83 BPM, com o drop alinhado à frase do verbo.
- **Render:** Playwright a 60 fps com **8 subquadros** de motion blur, depois ffmpeg.
- **Mix:** sidechain em 3 bandas (graves 30%, médios 85%, agudos 55%; hold 0,3 s, antecipação de 50 ms, release de 0,5 s); voz **~9 dB acima da música entre 300 Hz e 4 kHz**; master em **−14 LUFS**; **um efeito sonoro por evento** (clique, tecla, pouso, whoosh, impacto); fade da música em curva de dB no final.
- **Proibições do exemplo:** caixa de seleção, "slams" batendo em cada beat, flashes brancos, 3D, templates, ponto final em texto na tela.
- **Verificação final:** contact sheet, varredura de diferença entre quadros (só as sequências rápidas podem saltar) e checagem da razão voz/música frase a frase.

---

## 6. Blog: "AI explainer video prompts"

**Link:** https://prompt-motion.com/blog/ai-explainer-video-prompts

**Ideia central:** os explicativos que funcionam mostram um **processo com começo, meio e fim** (ex.: um drinque montado do copo vazio até pronto), não um tema solto. E quase ninguém pede checagem de fatos.

**Regras e técnicas:**
- Transformar tema abstrato em sequência visível: uma requisição atravessando um sistema, **um número que muda conforme as entradas mudam**, uma linha do tempo com paradas fixas.
- **Definir as cenas.** Template de explicativo de negócio em 30 s com 5 cenas (~6 s cada): problema do cliente → o que a empresa faz → como funciona em 3 passos → prova → nome no final.
- Texto em destaque, transições suaves, cores da marca.
- O próprio conceito pode virar estrutura (ex.: recursão contada de forma recursiva).
- **Público:** dizer para quem é ("alguém sem experiência com computadores") define vocabulário, ritmo e o que precisa ser explicado.
- **Fatos:** mandar pesquisar antes e **não inventar números, nomes ou citações**; revisar à mão depois.
- **Som:** se houver narração, dizer como (um prompt usa TTS gratuito).
- **Checklist do explicativo:** tema + público; sequência de etapas em ordem; duração (**~5 s por ideia** como ponto de partida); estilo e paleta; precisão (pesquisar, não inventar); som (música, narração ou nada).
- O que os prompts mais esquecem: duração, estilo, som, público e, principalmente, checagem de fatos (0 de 27).
- Prompt genérico ("vídeo explicativo profissional") não rendeu nada.

---

## 7. Blog: "AI launch video prompts"

**Link:** https://prompt-motion.com/blog/ai-launch-video-prompts

**Ideia central:** os lançamentos curtos que só repetem o prompt viral de showreel transformam o produto em pano de fundo. Os que dão certo dizem **o que mostrar e como**. O tamanho do prompt não é o fator; o que conta é responder às perguntas que o prompt curto deixa abertas.

**Regras e técnicas:**
- **Nomear os momentos na tela:** 3 a 5 momentos reais, em ordem.
- **Bloco de entradas:** listar o que o modelo deve pedir antes de começar (nome e promessa em uma linha, 3–5 momentos, uma cor de acento, clipes próprios, música livre com "drop" claro). Assim o prompt fica reutilizável sem edição.
- **Aparência:** dar cores (em hex), uma fonte e modo claro/escuro. Mandar estudar referências em suavidade, timing, duração dos planos e fontes, **emprestando técnicas sem copiar o design**, e garantir que cada morph saia perfeito.
- Ideias de repertório: SVG limpo e variado, imagens em escalas diferentes e várias ao mesmo tempo, texto com morph, zooms. Sem rótulos pequenos acima dos títulos e sem estética "artística bege".
- **Ritmo:** "algo acontece a cada batida", que é o que separa um lançamento de um slideshow.
- **Formato:** para feed de celular, escrever "9:16 vertical" com o tamanho em pixels, para o layout nascer vertical desde o primeiro quadro (só 12 de 94 lançamentos eram verticais).
- **Lista do que evitar** como lista de exclusão: glows, explosões de partículas, crossfades, ícones com cara de banco de imagens.
- **Checklist curto (6 itens):** produto/promessa em 1 linha; 3–5 momentos; visual (hex, uma fonte, claro/escuro); tempo (duração, andamento, mudança por batida); o que evitar; final (logo, URL ou uma frase).
- Durações citadas: 10–15 s (mais perto de 15) e final com o logo.

---

## 8. Blog: "AI motion graphics prompts"

**Link:** https://prompt-motion.com/blog/ai-motion-graphics-prompts

**Ideia central:** o mesmo prompt curto ("vá com tudo") dá resultados muito dispersos, porque deixa assunto, estilo, ritmo e proibições a cargo do modelo. Os prompts longos que funcionam tomam essas decisões por ele em **cinco elementos**.

**Os cinco elementos:**
1. **Conceito único** que justifica cada cena.
2. **Lista de proibições.**
3. **Tempo em batidas** (BPM e número de compassos) no lugar de adjetivos como "dinâmico".
4. **Método de construção:** quadro a quadro, a partir do tempo.
5. **Etapa de revisão:** um quadro por batida, corrigindo o que estiver fora do ritmo, pesado ou ilegível.

Ajustar só configurações fora do prompt (esforço máximo) não resolveu a dispersão.

**Prompt de exemplo (motion de UI, 474 palavras):**
- **Entradas pedidas antes:** 8–12 estados de UI, paleta (P&B ou um acento), música livre de direitos em torno de 120 BPM.
- **Direção:** uma forma única que muda de tamanho, raio e cor; conteúdo que troca com um blur curto; um cursor que motiva cada mudança; fundo cinza quente claro; componentes em P&B; uma fonte; **molas em tudo, com overshoot mínimo**; câmera que aproxima cada estado; último quadro igual ao primeiro.
- **Proibições:** easing com quique, partículas, glows, gradiente na UI, traço de ícone inconsistente, tempo morto, cara de template.
- **Tempo:** 120 BPM, 7 compassos, algo por batida.
- **Build:**
  - um HTML 1440x1440 com estilo calculado em `seek`, sem CSS transitions, timers ou estado;
  - **molas como resposta ao degrau em forma fechada, somando uma mola por mudança de alvo** (isso dá continuidade de velocidade quando o alvo muda no meio);
  - bordas de um indicador em molas diferentes (a da frente estica primeiro);
  - arrasto com manipulação direta e retorno em mola;
  - **análise do áudio com numpy para achar a grade de batidas** e começar num downbeat, com cada som posicionado pelo pico medido;
  - Playwright com **4 subquadros** mesclados por `tmix`, a 60 fps.
- **Armadilhas:** não usar `will-change` em elementos que a câmera escala (o texto fica borrado); texto que troca dentro de um container animado precisa de timing próprio de entrada e saída; para o loop, o último quadro precisa bater com o primeiro, inclusive em posição e velocidade.
- **Início:** pedir as entradas e mostrar os estados na grade de batidas antes de escrever código.

**Faça:** conceito e forma principal; andamento e compassos; dizer como renderizar; checar um quadro por batida; molas em vez de quique; loop idêntico; deixar o modelo pedir as entradas.
**Não faça:** "vá com tudo"/"dinâmico" como única direção; glows, partículas, crossfades, gradiente na UI; `will-change` em elemento escalado; textos sobrepostos na troca; tempo morto; cara de template.

---

## 9. Blog: "Make AI motion graphics look less AI"

**Link:** https://prompt-motion.com/blog/make-ai-motion-graphics-look-less-ai

**Ideia central:** a "cara de IA" vem de defaults que o modelo usa quando ninguém proíbe. Uma lista curta de proibições, **cada uma dizendo o que fazer no lugar**, é o que mais diferencia os prompts bem recebidos.

**Itens mais banidos (por frequência):** glows/neon; "qualquer coisa com cara de template"; rajadas de partículas; pausas longas, quadros congelados e tempo morto; crossfades; easing saltitante; gradientes; efeitos 3D; imagens ou kits de UI de banco; texto nos cantos; `Math.random`. Também citados: anéis de choque, separação RGB, camera shake, lens flare, grade no chão, fundo piscando.

**Sinais e correções:**
- **Glow/partícula/flare:** só com motivo narrativo. Todo movimento sai de um elemento em tela e chega a algum lugar; movimento sem origem é enchimento.
- **Crossfade/blur-in:** transformar o mesmo elemento de um estado no outro, ou ter um elemento-fio que atravessa todas as cenas. A transição passa a fazer parte da ideia.
- **Easing saltitante:** manter molas, mas com overshoot mínimo (bounce exagerado parece infantil).
- **Texto nos cantos (estética HUD):** remover, ou manter só se informar algo.
- **Tempo morto:** quadro parado por mais de **~1 s** sem motivo arrasta o vídeo. Segurar só quando o espectador precisa de tempo para ler.
- **Cara de template:** fechar a lista com um padrão geral de exigência, para cobrir também o que não foi listado.
- **`Math.random`:** proibir (ou semear), para que um quadro aprovado não mude no render seguinte.

**Como montar a lista:**
1. Começar pelos clássicos: glow, partícula, crossfade, quique, texto nos cantos.
2. Rodar uma vez e anotar o que apareceu sem ser pedido.
3. Para cada proibição, dizer a alternativa ("sem crossfade: cada cena nasce da anterior").
4. Fechar com "nada com cara de template".
5. Manter curta: uma linha com **5 a 9 itens**.

**Build do exemplo (~15 s, 1920x1080, 60 fps):**
- `seek(t)` puro, sem CSS transitions, timers ou estado.
- Molas em forma fechada para toggle, ponto e gráfico; **o gráfico é desenhado pela mesma função que move o ponto** (evita descompasso).
- Letras animadas individualmente quando uma palavra vira outra.
- Várias formas na verdade são **estados de uma mesma forma**, que conserva posição e movimento.
- Uma forma que "preenche a tela" precisa cobrir os 4 cantos de verdade.
- Clique, pouso, pico do gráfico, trocas de forma e título sincronizados com batidas medidas; um quadro por batida conferido antes de exportar.
- Erros a evitar: gráfico e ponto fora de sincronia, acento de cor inconsistente, texto saindo e entrando ao mesmo tempo, primeiro e último quadros diferentes.
- Paleta do exemplo: off-white quente, quase-preto e **um único acento** vivo. Uma mudança visual a cada batida principal.

---

## 10. Blog: "Remotion vs HyperFrames"

**Link:** https://prompt-motion.com/blog/remotion-vs-hyperframes

**Ideia central:** os três caminhos (Remotion, HyperFrames e HTML puro com Playwright) usam o mesmo princípio: navegador headless vai a um instante exato, tira um screenshot e o ffmpeg junta tudo. Como cada quadro é **função pura do tempo**, máquina lenta não perde quadro nem sai do tempo.

**Regras e técnicas:**
- **Remotion:** cenas como componentes React que leem o número do quadro, com studio de prévia. Bom quando o produto já é React. Exige React e pode exigir licença comercial paga, conforme a empresa.
- **HyperFrames:** HTML com atributos de dados, compatível com GSAP, pensado para agentes escreverem, Apache 2.0, sem React.
- **HTML + Playwright (o nosso caso):** uma página com `seek(t)` que define posição, tamanho e cor de cada elemento em `t`; Playwright percorre os tempos; ffmpeg monta. Só precisa de Playwright e ffmpeg; aceita CSS, SVG, canvas e WebGL. É o método mais usado na galeria, **mas o prompt precisa descrever o método**.
- **Escolha:** React → Remotion; agente sem React → HyperFrames; o mais simples → HTML + Playwright; 3D real → three.js capturado igual; matemática → Manim.
- **Sempre nomear a ferramenta/método no prompt**, senão o modelo escolhe a cada vez e o resultado fica difícil de repetir.
- **Subquadros:** vários prompts renderizam N subquadros por quadro e mesclam com ffmpeg para ter motion blur em movimentos rápidos.
- Não escolher a ferramenta por curtidas (amostras pequenas, com viés de audiência).
- **Não informado:** fps, resolução, tempo de render, pipeline de áudio.

---

## Como aplicar no nosso motor

Adaptações para Reels verticais de ~60 s, 1080x1920, 30 fps, narração TTS, paleta escura + dourado, Fraunces + Inter, tema mercado financeiro. Os números marcados "(nosso)" são escala ou adaptação nossa, não vêm do site.

1. **Conceito único e fio condutor.** Cada Reel tem um conceito declarado em uma linha (ex.: "a linha dourada é o patrimônio") e **um elemento-fio** (uma linha, um ponto ou uma barra dourada) que atravessa todas as cenas e muda de papel: vira gráfico, sublinhado, divisor, número. Nada de cena desconectada.

2. **Transição = transformação, nunca dissolve.** Proibido crossfade e blur-in entre cenas. A cena B nasce de um elemento da cena A, que sai, viaja e assume outro papel. Pops só em sequências rápidas planejadas.

3. **Grade de tempo explícita.** Trilha a **120 BPM** (nosso: 1 batida = 0,5 s = **15 quadros exatos** a 30 fps; 60 s = 30 compassos). Trocas de cena em downbeat ou meia batida; o início de cada frase da narração é ancorado no onset medido e a mudança visual mais próxima vai para a batida vizinha. O drop/impacto coincide com a frase-chave (o "verbo" do roteiro).

4. **Tabela de batidas antes do código.** Gerar e salvar em arquivo uma tabela (tempo, frase da narração, o que aparece, o que se move, **por que existe**). Batida sem justificativa sai. Estrutura de 60 s (nosso): gancho em 0–3 s; 4 a 6 ideias de **~8–10 s** (o site sugere ~5 s por ideia sem narração; a fala alonga); momento mais forte no penúltimo bloco; CTA/assinatura nos últimos 3–4 s.

5. **Easing: molas em forma fechada com overshoot mínimo, mais exponenciais.** Somar uma mola por mudança de alvo, para manter a velocidade contínua. Proibido bounce visível, `linear` em movimento de objeto e animações CSS, transitions ou timers. Tudo sai de `window.onSeek(t)`, sem estado entre quadros.

6. **Determinismo total.** Sem `Math.random` (usar PRNG semeado); sem `Date.now`/`performance.now`. Gráficos e o ponto que os percorre são desenhados pela **mesma função** de t. O mesmo t precisa gerar o mesmo pixel em qualquer render.

7. **Motion blur por subquadros.** Nosso: renderizar 3–4 subquadros por quadro de 30 fps e mesclar com ffmpeg `tmix` (ou aplicar blur direcional proporcional à velocidade só nos movimentos rápidos). Nunca blur estático "de enfeite".

8. **Paleta travada.** Fundo escuro + **um único acento dourado** + no máximo uma cor de dado (ex.: verde/vermelho dessaturados para alta/baixa), além de branco/cinzas. Nada de gradiente genérico, neon ou glow. O dourado aparece sempre com o mesmo tom, sem variar entre cenas.

9. **Tipografia em dois papéis fixos.** Fraunces só para títulos e números-herói; Inter para rótulos, dados e legendas. O site recomenda uma família, então duas é o nosso teto, cada uma com papel fixo. Texto mínimo (nosso: 32 px em 1080p → **≥ 44 px** de corpo e **≥ 96 px** de título no vertical). Sem ponto final nos textos de tela e sem rótulos pequenos acima de títulos.

10. **Composição vertical forte.** Um elemento focal por quadro ocupando **≥ 60% da largura** (≥ 650 px); cortar na borda em vez de encolher. Nada nos cantos (sem HUD, timecode ou colchetes); layout diferente da cena anterior; formas que "enchem a tela" cobrem os 4 cantos. Nosso: respeitar as zonas seguras do Reels (topo e base ocupados pela interface do app).

11. **Sem tempo morto, mas com tempo de leitura.** Nenhum quadro totalmente parado por mais de **0,5 s**. Quando a narração pede leitura (um número, uma frase-chave), segurar o layout, mas com micro-movimento de câmera: zoom lento **1,00 → 1,04** por cena, e a cena seguinte começa no zoom em que a anterior terminou (nunca reset para 1,0).

12. **Entradas e saídas com origem.** Nada surge do nada: crescer, deslizar de uma borda ou revelar por máscara. Fades de texto com **≥ 0,3 s** (fade curto parece pop-in). Na troca de texto, o antigo sai **antes** de o novo entrar. Staggers com duração e atraso variados, nunca idênticos.

13. **Lista de proibições do motor (5–9 itens, cada um com alternativa).** Sem glow/neon → acento chapado; sem partículas/flare/shake/RGB split → movimento com origem e destino; sem crossfade → morph; sem bounce → mola amortecida; sem texto em canto → informação no centro de leitura; sem retângulo de seleção atrás de palavra → destaque em dourado com brilho sutil; sem flash branco; e, por fim, "nada com cara de template".

14. **Destaque de palavra-chave sincronizado à fala.** A palavra enfatizada da narração muda para dourado (ou recebe sublinhado do fio condutor) no onset medido da palavra, nunca com caixa de seleção.

15. **Narração TTS tratada.** Gerar vários takes e regenerar frases ruins; encurtar pausas **> 0,28 s para ~0,2 s**; nivelar volume entre frases; cortar em silêncios ≥ 100 ms e alinhar cada trecho separadamente (evita atraso de até 0,5 s). Tags de emoção com parcimônia e nunca na abertura.

16. **Mix de áudio.** Voz **~9 dB acima da trilha na faixa de 300 Hz–4 kHz**, com sidechain (ducking com antecipação de ~50 ms, hold de ~0,3 s e release de ~0,5 s); master em **−14 LUFS**; **um SFX sintetizado por evento visual** (clique, tick de número, pouso, whoosh, impacto), sem SFX em cada batida; kick/pulso na grade, riser antes do bloco mais forte e fade da trilha em curva de dB no fim.

17. **Checagem quadro a quadro antes do render final.** (a) Contact sheet com um still do meio de cada batida, conferindo focal, tamanho de texto, cantos, espaçamento e layout novo; (b) tiras de transição com todos os quadros de **0,3 s antes até 0,3 s depois** de cada corte (no nosso caso, 9 + 9 quadros); (c) varredura de diferença entre quadros para achar pops de 1 quadro; (d) prévia leve em velocidade normal; (e) razão voz/trilha medida frase a frase.

18. **Ciclo de correção disciplinado.** Pedidos de ajuste sempre com segundo exato + comportamento desejado; uma mudança por rodada; congelar trechos aprovados ("não mexer após X s"); exigir quadros como prova. Plano, tabela de batidas e decisões ficam em arquivos, para uma sessão nova continuar sem reprocessar o histórico.

19. **Fatos e conformidade.** Explicativo financeiro = processo visível (um valor que cresce com aportes e tempo, um caminho do dinheiro, uma linha do tempo). **Não inventar números, taxas, índices nem citações**: todo dado vem de fonte informada ou é marcado como ilustrativo na tela. Sem logos, marcas ou pessoas reais, e o público-alvo fica declarado no roteiro (ex.: "investidor iniciante").

20. **Loop e fechamento.** Assinatura final curta (frase + CTA). Opcional: o último quadro igual ao primeiro, inclusive em posição e velocidade do elemento-fio, para o replay do Reels parecer contínuo. Um humano assiste ao render final em velocidade normal e ouve de olhos fechados, porque o modelo não julga "sensação" nem som.
