---
name: biblioteca-motion
description: Biblioteca de técnicas de motion graphics tiradas das 240 entradas do prompt-motion.com (prompts e skills de vídeos feitos com Claude), destilada e adaptada aos Reels do @tiagoassessorxp. Use junto com a skill reels-motion-tiago sempre que for criar ou ajustar um Reels, um motion ou um vídeo animado. Serve para escolher uma técnica visual nova (abertura, transição, fio condutor, gráfico, tipografia), acertar o acabamento (easing, ritmo, som, o que evitar para não parecer feito por IA) e rodar a checagem antes de filmar. Use também quando o Tiago mandar um link ou vídeo do prompt-motion.com, ou pedir para "melhorar o motion" ou "deixar mais profissional".
---

# Biblioteca de motion (prompt-motion.com)

Esta pasta guarda o que aprendemos com a biblioteca pública prompt-motion.com: 240 vídeos de motion feitos com Claude, cada um com o prompt ou a skill que o gerou. Ela não substitui `_skill_reels_motion/SKILL.md`, que continua mandando no fluxo, no roteiro, no compliance e na aprovação. Esta skill entra no passo de **animar** e no de **conferir**.

- `catalogo.md`: as 240 entradas, com link, o que o vídeo mostra, a técnica descrita com as nossas palavras e quanto serve para nós (34 alto, 85 médio, 121 baixo).
- `guias.md`: os dois templates e os cinco artigos do site, com as regras de cada um e a adaptação ao nosso motor.
- `skills_externas.md`: as 6 skills instaláveis da biblioteca, com comando de instalação e o que já foi estudado.

Os prompts originais não estão copiados aqui: pertencem aos criadores, e o link de cada um está no catálogo. Use como referência de técnica e nunca reproduza o vídeo, a marca ou o texto de outra pessoa.

## Como usar em cada Reels

1. **Depois de escolher o formato** (A, B ou C, em `_skill_reels_motion/formatos.md`), abra a seção "Alto" do `catalogo.md` e escolha **uma** técnica que sirva ao assunto (tabela abaixo). Uma por vídeo basta. Se quiser ver o vídeo, o link está no bloco.
2. **Escreva o conceito em uma linha** no `roteiro.json` (`"conceito"`), por exemplo "o ponto dourado é o dinheiro; ele viaja de um país ao outro". Cada cena precisa nascer desse conceito.
3. **Monte a tabela de batidas** antes da página: para cada fala, o que aparece, o que se move e por que existe. Batida sem motivo sai.
4. **Anime seguindo o acabamento** (seção abaixo).
5. **Confira com a lista de checagem** antes de filmar.
6. Se a técnica funcionar e o Tiago aprovar, registre em `_skill_reels_motion/aprendizados.md` e, se for um jeito novo de estruturar, em `formatos.md`.

## Técnica por tipo de assunto

| Assunto | Técnica (entrada no catálogo) | Como fica no nosso |
|---|---|---|
| Fluxo de dinheiro, causa e efeito (formato B) | Orange dot motion system; White ball UI motion loop | Um ponto ou moeda dourada que nunca teletransporta: sai de um lugar, viaja e vira o número da cena seguinte |
| Abertura sobre bolsa ou mercado | Sahi trading terminal reveal (zoom de escala) | Começa num ponto, abre um painel fictício de cotações, a câmera recua e o painel vira um ponto de novo |
| Composição de algo (pesos, fatias) (formato A) | White Russian recipe animation | Um recipiente que se enche em camadas rotuladas, cada uma com o peso dito na fala (ex.: os grupos do IPCA) |
| Tempo longo, fases da vida | Cycle of life animation | Uma linha da vida com fases e persona genérica; o último quadro volta ao primeiro (loop) |
| Escala, "quanto acontece em X" | What happens in one second | Contadores dourados de um dado oficial por segundo ou por dia, com fonte na tela |
| Mecanismo técnico | Token bucket rate limiter; Animated business explainer | Diagrama que se monta peça por peça; roteiro problema → como funciona em 3 passos → prova → assinatura |
| Resumo da semana | Steam new releases news recap | Um card por fato, um destaque por card, janela de datas fixa |
| Frase de efeito, fechamento | Speech built as architecture; TechHalla kinetic type bumper | Cada palavra-chave vira uma peça que sustenta a próxima; nenhuma palavra sai antes de ser lida |
| Número que rompe um limite | Poster breaking its frame | O número ou a linha do gráfico estoura a moldura do card (ex.: dólar na máxima do ano) |
| Lista que para num item | NotchBrowser product teaser (roleta) | Uma roleta de temas que desacelera e para no assunto do vídeo |

## Acabamento (o que muda na página)

Estas regras vêm dos templates e artigos do site (detalhes em `guias.md`), já adaptadas ao vertical, aos 30 fps e à narração.

- **Transição é transformação.** A cena B nasce de um elemento da A, que sai, viaja e assume outro papel. Evite dissolver uma cena na outra. Um elemento-fio dourado (linha, ponto, barra) pode atravessar o vídeo inteiro.
- **Texto antigo sai antes do novo entrar** (já é regra nossa). Fade de texto com pelo menos 0,3 s, porque menos que isso parece "pipocar".
- **Nada surge do nada:** cresce, desliza de uma borda ou é revelado por máscara.
- **Molas com quase nenhum quique.** Assentamento suave; quique visível parece infantil. Nunca movimento linear em objeto.
- **Stagger variado:** elementos de um grupo entram com atraso e duração levemente diferentes, nunca todos iguais.
- **Câmera viva sem tranco:** zoom lento (1,00 → 1,04) dentro da cena; a cena seguinte começa no zoom em que a anterior terminou.
- **Sem tempo morto:** nenhum quadro totalmente parado por mais de ~0,5 s. Quando a fala pede leitura, segure o layout, mas mantenha um micro-movimento.
- **Um foco por quadro**, ocupando boa parte da largura. Melhor cortar na borda do que encolher.
- **Paleta travada:** fundo escuro, um dourado (sempre o mesmo tom), branco e cinzas, e no máximo uma cor de dado com significado (alta e baixa).
- **Tipografia em dois papéis:** Fraunces para títulos e números-herói, Inter para o resto. Texto de tela com pelo menos 44 px no vertical.
- **Determinismo:** tudo sai do tempo (`data-*` e `window.onSeek(t)`); nada de `Math.random` sem semente, timer ou relógio. Gráfico e ponto que o percorre saem da mesma função.
- **Som:** um efeito por evento visual (já é regra nossa); voz bem acima da trilha; riser antes do bloco mais forte.
- **Gancho no primeiro segundo**, e o momento mais forte no penúltimo bloco.

### O que evitar (cada item com a alternativa)

Glow e neon → acento chapado · partículas, lens flare, tremor de câmera, separação RGB → movimento com origem e destino · crossfade entre cenas → transformação · quique → mola amortecida · texto ou rótulo nos cantos → informação no centro de leitura · retângulo de "seleção" atrás de palavra → a palavra muda para dourado · flash branco → corte na batida · e, para fechar, nada com cara de template.

## Checagem antes de filmar

Além dos quadros de conferência do `render.py --quadros`:

- **Folha de contato:** um quadro no meio de cada fala, todos numa imagem só. Confira se há um foco claro, texto grande o bastante, cantos limpos e layout diferente do quadro anterior.
- **Tiras de transição:** em cada troca de cena, os quadros de 0,3 s antes a 0,3 s depois. Procure texto sobre texto, elemento que pisca por um quadro só e corte sem ligação.
- **Corrija uma coisa por vez,** dizendo o segundo exato e o que deveria acontecer. Não mexa no que já está bom.
- **O modelo não ouve nem "sente".** Diga ao Tiago quando um efeito ou ritmo for novidade, para ele assistir em velocidade normal e com som.

## Ainda não está no motor (candidatos)

- **Motion blur por subquadros:** renderizar 3 ou 4 subquadros por quadro e misturar com ffmpeg `tmix`. Deixa os movimentos rápidos mais cinematográficos e custa mais tempo de render. Teste num Reels antes de virar padrão.
- **Grade de batidas na trilha** (120 BPM = 15 quadros por batida a 30 fps), com trocas de cena na batida.
- **Mix com medição:** master em −14 LUFS e voz cerca de 9 dB acima da trilha.

Quando um desses entrar no `_kit_reels/`, mova a linha para o `README.md` do kit.

## Como atualizar a biblioteca

O site ganha vídeos novos toda semana. Para atualizar: leia `https://prompt-motion.com/sitemap.xml`, compare com os links do `catalogo.md` e, para cada entrada nova, abra a página e acrescente um bloco no mesmo formato, no nível certo. Nunca copie o prompt inteiro: escreva a técnica com as nossas palavras e mantenha o link. Registre a data da atualização no topo do catálogo.
