---
name: reels-motion-tiago
description: Cria Reels de ~1 minuto em motion (vídeo animado com narração, legenda, trilha e efeitos sonoros) para o Instagram @tiagoassessorxp, do Tiago Acordi, assessor Alta Renda da XP. Use sempre que o Tiago pedir um Reels, um vídeo, um motion, um vídeo explicativo ou animado sobre mercado financeiro, quando mandar um vídeo de referência para "fazer igual" ou "treinar esse estilo", quando pedir ajuste em um Reels já feito (voz, ritmo, visual, legenda), e em toda rodada da tarefa agendada de Reels. Cobre a escolha do formato, o roteiro, a validação dos números, o compliance de assessor, a geração do vídeo e o pedido de aprovação.
---

# Reels em motion — @tiagoassessorxp

O Tiago atende empreendedores, produtores rurais e famílias com patrimônio consolidado no Oeste de SC e quer ser visto como assessor de padrão private. O Reels existe para isso: explicar um assunto do mercado em um minuto, de um jeito que a pessoa assista até o fim, entenda e comente. Um vídeo bonito que ninguém termina não serve, e um vídeo viral com número errado ou cara de recomendação é um risco para a carreira dele.

Esta skill mora no repositório `acordisemfronteiras-create/artesinstagram`:

- `_skill_reels_motion/` — esta pasta: o que aprendemos. Leia `formatos.md` para escolher a estrutura, `referencias/` para ver os vídeos que o Tiago gostou e por quê, `ideias.md` para pautas, `aprendizados.md` para o que ele já pediu.
- `_kit_reels/` — o motor: `voz.py` (narração e linha do tempo), `base.css` / `base.js` / `personas.js` (animação), `som.py` (trilha e efeitos), `render.py` (vídeo), `historico.md`.
- Pastas `NN_reels_...` — cada Reels, com `roteiro.json`, `pagina.html`, `timeline.json`, `legenda.txt` e `reels.mp4`. Os dois primeiros são os melhores exemplos de cada formato; abra o do formato escolhido antes de escrever.

## A regra que não dobra: aprovação

Reels só vai ao ar com o OK do Tiago, por escrito, na mesma conversa. Ele pediu isso em 12/11/2026 e ainda não liberou publicação direta para vídeo (só para os posts de notícia). Então o fim do trabalho é sempre: rascunho no HubPost (sem data), vídeo e legenda enviados, e parar. "Aprovado" → aí sim agendar. Se ele mudar essa regra, registre em `aprendizados.md` e atualize aqui.

## Fluxo

1. **Sincronize e leia.** `git fetch origin main && git reset --hard origin/main`. Leia esta pasta, `_kit_reels/historico.md` e o fim de `_kit_noticias/historico.md` para não repetir assunto dos últimos 10 dias.
2. **Escolha a pauta.** O que está em alta no mercado agora e interessa a quem tem patrimônio: um conceito por trás da notícia da semana, um dado que surpreende, uma regra que mudou. Pesquise em fontes de qualidade (BC, IBGE, Tesouro, CVM, B3, ANBIMA, Fed, Agência Brasil, InfoMoney, Valor, Estadão, Folha, Reuters, Bloomberg Línea, Exame, Canal Rural).
3. **Valide os números.** Cada número na tela ou na fala precisa de fonte primária oficial ou de duas fontes independentes que batem. Se divergirem, fique com a primária ou tire o dado. Guarde os links em `"fontes"` no `roteiro.json`. Conta derivada (ex.: 36 − 19 = 17) só quando a própria fonte confirma o resultado.
4. **Escolha o formato** em `formatos.md` pelo tipo de assunto: proporção ou distribuição pede o formato A (metáfora única); causa e efeito pede o B (personas); processo em etapas ou lista pede o C (texto cinético). Alterne quando der, e veja em `aprendizados.md` se há formato esperando estreia.
5. **Escreva o roteiro** (seção abaixo) e rode `python3 _kit_reels/voz.py PASTA --alinhar`. Mire em 50 a 62 s. Se passar, corte frases, não acelere a voz.
6. **Anime** em `PASTA/pagina.html`, com desenho novo para o tema.
7. **Confira antes de filmar:** `python3 _kit_reels/render.py PASTA --quadros t1,t2,...` em 8 a 14 instantes, incluindo os de troca de texto. Abra as imagens. Procure texto sobre texto, texto sobre desenho, corte nas bordas, número diferente do verificado. Corrija e repita. Filmar custa minutos; um quadro custa segundos.
8. **Filme:** `python3 _kit_reels/render.py PASTA` → `reels.mp4`. Confira duração, volume e um quadro do meio. Para mexer só no som: `--so-audio`.
9. **Legenda** em `PASTA/legenda.txt`, commit e push, rascunho no HubPost, pedido de aprovação (seção final).

## Roteiro: o que faz a pessoa assistir até o fim

Estas regras vêm da referência que o Tiago mais gostou (`referencias/01_quadradinhos-ia.md`) e do que ele aprovou.

- **A primeira frase põe o espectador dentro do assunto.** "Esse quadradinho é você." "Na quinta, o dólar fechou a R$ 5,65." Nada de "olá" ou "hoje vamos falar".
- **Fale como quem conversa, e rápido.** Frases de 4 a 12 palavras, cerca de 2,5 a 2,8 palavras por segundo, expressões de fala ("presta atenção", "ou seja", "esses dois verdinhos aqui"). Tom de alta renda vem da precisão, não de palavra difícil.
- **Uma ideia por batida, um número grande por vez.** Se a tela precisa de um parágrafo, a batida está grande demais.
- **A fala aponta para a tela.** Dê nome ao que aparece (as cores, os personagens) e use esse nome.
- **Do geral para o raro**, com a câmera chegando mais perto a cada passo. O menor grupo é o clímax.
- **Vire o dado para o espectador** perto do fim ("ou seja, se você..."), e feche com o gancho do Tiago: para quem já tem patrimônio, a pergunta muda (como está organizado, protegido, sucedido). Efeito, nunca conselho.
- **Termine com uma pergunta de resposta curta**, ligada à metáfora do vídeo, para puxar comentário. O "fale comigo pelo link da bio" vai na legenda e no cartão final.
- **Não copie frase de outro criador.** Referência ensina estrutura; o texto é nosso.

`roteiro.json` (veja os exemplos): `titulo`, `kicker`, `formato`, `voz`, `fontes`, `cenas` → `falas` com `fala` (números por extenso, deixas `{nome}` antes da palavra que dispara algo na tela) e `legenda` (o texto que aparece, com algarismos), e `sfx`.

## Compliance de assessor (bloqueia)

Descreva o que aconteceu e o efeito; não diga o que fazer. Fica de fora: sugerir comprar, vender ou resgatar; citar produto ou emissor específico; prometer ou projetar rentabilidade; opinião sobre partido ou candidato. Categoria genérica pode ("poupança", "ações", "títulos públicos"), sem juízo de valor sobre quem escolhe cada uma. O cartão final traz "Conteúdo informativo. Não é recomendação de investimento." e a fonte. Sem pessoas, logos ou marcas reais no desenho. Na dúvida, mande com a dúvida explicada; ele decide.

## Visual

- 1080×1920, 30 fps. Paleta escura com dourado `#c9a45c`, Fraunces para números e títulos, Inter para o resto: a mesma identidade dos posts. Cores extras só para categorias.
- Zonas: cabeçalho até y≈230; texto principal em y≈285–600; desenho em y≈600–1250; legenda da fala em y≈1345–1470. Abaixo disso o Instagram cobre.
- Quando o desenho passa por trás do texto, use véus (gradientes escuros) no alto e embaixo, como no exemplo do formato A.
- Um bloco de texto sai antes de o próximo entrar (`data-out` uns 0,3 s antes da deixa seguinte). É o defeito mais comum; os quadros de conferência pegam.
- Mantemos a legenda da fala, menor, mesmo quando a referência não usa: boa parte do público assiste sem som.
- Texto palavra por palavra no centro (formato C): `<div class="cin" data-cin="L2">... <em>destaque</em></div>`; com ele, desligue a legenda de baixo (`"legenda_na_tela": false`).
- Animação: `data-in`, `data-at` (`"1.2"`, `"L2+0.3"` ou `"@deixa+0.2"`), `data-out`, `data-count`; para movimento contínuo (câmera, grade), `window.onSeek(t)` com `cue('nome')` e `ease()`. Detalhes no topo de `base.js`.

## Som

- **Voz:** uma só por estilo, sempre a mesma. Estilo atual: Kokoro `pm_alex`, velocidade 1,06 (`"voz"` no roteiro). O Tiago aprovou a demo com essa voz em 12/11/2026; o piloto do mesmo dia usou Piper `faber`. Trocar de voz é decisão dele.
- **Efeitos** no campo `"sfx"`, presos às deixas: `whoosh` em movimento de câmera, `impacto` em número forte, `riser` antes dele, `pop` quando algo aparece, `varredura` e `contagem` em ondas e contadores, `brilho` em conclusão, `bip` em "presta atenção". Um efeito por batida basta; som demais cansa e briga com a voz.
- Trilha e efeitos são sintetizados em `som.py`. Não baixe música nem efeito de terceiros.
- Você não ouve o resultado. Confira o que dá: transcreva a narração de volta para checar se as palavras saíram certas (números e siglas são onde a voz erra), e meça o volume. Diga isso ao Tiago quando o som for novidade.

## Entrega para aprovação

1. `legenda.txt`: título em uma linha; 3 a 5 parágrafos curtos, sem emojis; "Se quiser entender como isso afeta o seu patrimônio ou o caixa da sua empresa, fale comigo pelo link da bio."; "Conteúdo informativo. Não é recomendação de investimento."; 6 a 9 hashtags.
2. Commit da pasta e push na `main`.
3. HubPost: `get_upload_url` (video/mp4, tamanho exato) → `curl -X PUT --data-binary` → `confirm_upload` → `create_post` **sem** `scheduledAt`, conta Instagram @tiagoassessorxp, `{"kind":"REEL","aiGenerated":false,"shareToFeed":true}`. Se o HubPost falhar, diga o que falhou e pare; não use outro caminho.
4. Envie o vídeo. Em seguida, uma mensagem que começa com "Legenda do Reels (pronta para aprovar):" e traz a legenda exata, com hashtags. Depois, curto: tema e motivo, duração, fontes com link, o que ficou de fora, e "Responda 'aprovado' (e o horário, se quiser) ou diga o que ajustar."
5. Linha em `_kit_reels/historico.md`. Depois do OK: `edit_post` com `scheduledAt`, e atualize a linha.

## Quando o Tiago manda uma referência nova

É assim que esta skill melhora. Assista de verdade: extraia quadros (1 por segundo, em folhas de contato), transcreva a narração, leia o que aparecer de texto na tela. Escreva a análise em `referencias/NN_nome.md` no modelo da 01: o que acontece segundo a segundo, por que funciona, o que adaptamos e o que mudamos de propósito. Se trouxer uma estrutura nova, acrescente em `formatos.md`; se trouxer pautas, em `ideias.md`; registre o pedido em `aprendizados.md`. Se o motor não faz o que a referência faz, acrescente a peça que falta em `_kit_reels/` e teste com quadros. Depois mostre que aprendeu: se ele pedir, um Reels de demonstração na hora; se só pediu para estudar, anote em `aprendizados.md` ("Em aberto") que o formato espera estreia e use-o no próximo Reels em que o assunto couber. O vídeo de terceiro não entra no repositório.
