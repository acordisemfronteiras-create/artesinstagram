# Referência 02 — texto cinético com etapas e "barra de status"

- **Enviada pelo Tiago em:** 12/11/2026 ("gostei desse vídeo aqui também... pra você estudar")
- **Origem:** vídeo de terceiro (iamjeff.ia aparece no canto). O arquivo tem os primeiros 60 s de um vídeo de 2min40 (há um cronômetro regressivo no canto: 2:40 → 1:41). Só vimos as etapas 1 a 3 de 5.
- **Assunto dele:** uma equipe de agentes de IA que produz vídeos, em 5 etapas. O assunto não nos interessa; o jeito de animar, sim.
- **O vídeo em si não fica no repositório.** Aqui fica só a análise.

## O que acontece

| Tempo | Narração (resumo) | Tela |
|---|---|---|
| 0–3 s | "Cara, imagina ter uma equipe inteira de agentes..." | fundo preto; a frase entra **palavra por palavra no centro**, no ritmo da fala; "agentes" em serifa itálica rosa |
| 3–6 s | "...trabalhando pra você, cada um com a sua própria função..." | **o fundo vira claro** de uma vez; um avatar de personagem por frase ao lado do texto; desfoque de movimento na troca |
| 6–8 s | "...e sem pagar por nenhuma ferramenta a mais." | volta ao preto; **"R$ 0" enorme em vermelho**, que depois gira e sai |
| 8–11 s | "Pra fazer vídeos cada vez mais profissionais..." | fundo claro; 2 ou 3 palavras por vez, uma colorida |
| 11–17 s | "eu desenvolvi... que roda dentro do..." | preto; palavra-chave **sublinhada à mão**; depois fundo claro com o nome do produto e cartões entrando em pilha |
| 17–23 s | "Ele instala toda uma cadeia de produção..." | surge embaixo uma **barra de status** (pílula com avatar, uma linha de texto e pontinhos), com brilho colorido atrás; em cima, uma lista 01–09 em que o destaque desce item por item; depois um mosaico de miniaturas se multiplica |
| 23–27 s | "A gente segue a metodologia..., que se divide em 5 etapas." | frase pequena em cima, nome grande embaixo, depois **"5 etapas"** com o 5 gigante |
| 27–37 s | "1. Descobrir qual estilo de vídeo..." | **número 1 gigante entra voando**; balão de pergunta; três opções aparecem uma a uma; um **cursor clica** em uma; a barra de status mostra "etapa 1 de 5" |
| 37–52 s | "2. O roteiro. ... não pode delegar 100% pra IA, senão sai genérico..." | "2" gigante → "2 Roteiro" no canto; cartões de documento com texto sendo digitado, viram em 3D; "100% pra IA"; "genérico" em cinza apagado; a barra muda de avatar e de cor: "etapa 2 de 5" |
| 52–60 s | "3. Pesquisar referências. E aqui começa a ficar mais autônomo." | "3" gigante; outro avatar, outra cor de brilho; cartões e uma pílula "trabalhando sozinho" |

## Por que funciona (o que levar para os nossos)

1. **O texto É o vídeo.** Não há cenário. A frase aparece no centro, 2 a 5 palavras por vez, cada palavra entrando no instante em que é dita. É legenda e animação ao mesmo tempo.
2. **Uma palavra de destaque por frase**, em outra cor e outra fonte (serifa itálica). O olho sabe onde pousar.
3. **Troca de fundo como pontuação.** Preto → claro → preto, de uma vez, a cada mudança de ideia. Dá ritmo sem precisar de desenho novo.
4. **Número gigante para marcar etapa.** O "1", "2", "3" entram enormes, depois encolhem para o canto com o título. O espectador sempre sabe onde está.
5. **Barra de status fixa embaixo.** Uma pílula com avatar, o que está acontecendo ("etapa 2 de 5") e um brilho que muda de cor a cada etapa. É o fio que costura o vídeo e dá sensação de progresso.
6. **Um personagem por etapa.** Avatares simples e simpáticos; cada um com sua cor.
7. **Interface de mentira para explicar processo.** Balão de pergunta, opções que aparecem, cursor que clica, documento sendo digitado. Mostra o "como" sem falar muito.
8. **Um número enorme quando o número é o argumento** ("R$ 0", "100%").
9. **Movimento com desfoque e sobra.** Tudo entra com um borrão curto e assenta; cartões têm leve inclinação 3D. Nada fica parado mais de 2 s.
10. **Fala em primeira pessoa, de conversa.** "Cara, imagina...", "Pois é", "aqui você não pode, de maneira nenhuma...". Ritmo perto de 2,7 palavras por segundo.
11. **Lista que se percorre.** Itens 01–09 na tela, o destaque descendo um a um enquanto a fala resume.

## Diferenças para a referência 01

| | 01 (quadradinhos) | 02 (texto cinético) |
|---|---|---|
| O que carrega o vídeo | um desenho só (grade) e a câmera | o texto e a troca de fundo |
| Melhor para | proporção, distribuição, ranking | processo em etapas, lista, opinião, "como funciona" |
| Texto na tela | etiqueta + número grande + 1 linha | a própria fala, palavra por palavra |
| Fio condutor | a câmera | a barra de status e os números de etapa |

## Como fazer no nosso motor

- **Frase palavra por palavra:** `<div class="cin" data-cin="L2">imagina uma equipe inteira de <em>agentes</em></div>` (classe `.cin` em `base.css`, lógica em `base.js`). `L2` = 2ª fala da cena; `<em>` = palavra de destaque; `data-cin-hold` segura na tela; `.cin.claro` para fundo claro. Quebre a fala em pedaços curtos no `roteiro.json` (uma `fala` por linha de tela, 2 a 7 palavras), porque cada bloco `.cin` mostra uma fala.
- **Sem legenda embaixo:** `"legenda_na_tela": false` no `roteiro.json`, já que o texto central faz esse papel.
- **Troca de fundo:** um `<div>` de tela cheia claro (`#efe9dc`) com `data-in="fade" data-dur=".12"` e `data-out` na deixa seguinte, atrás dos textos.
- **Número de etapa:** `.num-etapa` com `data-in="zoom"`, e depois uma versão pequena no canto com o título.
- **Barra de status:** uma pílula fixa em y≈1180–1260 (acima da área que o Instagram cobre), com persona pequena, texto que troca por etapa (`data-in`/`data-out`) e um brilho radial cuja cor muda em `window.onSeek`.
- **Interface de mentira:** cartões `.card`, opções com `data-in="fade-up"` em sequência, um cursor (SVG) movido em `onSeek`, texto "digitado" com `.cin`.
- **Som:** `tique` em cada palavra de destaque é demais; use `pop` na entrada de cartão, `whoosh` na troca de fundo, `impacto` no número gigante, `contagem` na lista.

## O que mudamos de propósito

- Paleta do Tiago (preto, creme e dourado) no lugar de preto, branco e rosa. O destaque é dourado, em Fraunces itálico.
- Sem logos de empresas reais (a referência mostra marcas de ferramentas).
- Personas nossas (`personas.js`) no lugar dos avatares 3D.
- 50 a 60 s, com fim claro e pergunta para comentário; a referência é um vídeo longo.
- Fonte dos dados e o aviso "Conteúdo informativo. Não é recomendação de investimento." no cartão final.
