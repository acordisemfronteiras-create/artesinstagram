# Kit de Stories de notícia: @tiagoassessorxp

Padrão aprovado pelo Tiago em 23/11/2026 (referência: `referencia_dolar_23-11.jpg`, Stories "Dólar encosta em R$ 6").

## Ideia
Um Stories por dia, em formato de notícia curta e informativa, sobre o fato mais atípico ou urgente do dia no mercado: um nível simbólico rompido (dólar, Ibovespa, juros), decisão ou comunicado inesperado (BC, Fed, governo, Congresso), intervenção no câmbio, recorde, choque de commodity que pega o agro, dado que surpreende o consenso. Publicado automaticamente desde 24/11/2026 (com aprovação só em caso de dúvida).

## Visual
- 1080x1920. Mesma linguagem dos posts de notícia: paleta escura com dourado #c9a45c, Fraunces (títulos e números) + Inter (texto), dourado só no número-chave (`<em>`).
- Fundo: ilustração em SVG desenhada para o tema, entre y≈380 e y≈900 (ex.: gráfico de linha batendo num nível tracejado para câmbio ou bolsa; prédio do BC para comunicado do Copom; Capitólio/Fed para juros nos EUA; silo e lavoura para agro; barril para petróleo). Abaixo de y≈960 o fundo termina em #0a0a0a. Sem logos, marcas ou pessoas reais.
- Estrutura: kicker + data · selo "Urgente" (só para evento do dia) · título de até 3 linhas · subtítulo de até 3 linhas · grade de 2 ou 4 dados · rodapé com nome, cargo, @ e fonte. O texto é ancorado de baixo para cima; se o título ficar longo, confira se não encosta na ilustração.
- Zonas seguras: nada importante acima de y=230 nem abaixo de y=1745.

## Como gerar
1. Script Python novo que gera `bg.svg` (exemplo: `exemplo_bg_linha_6.py`).
2. `spec.json` (exemplo: `exemplo_spec_dolar.json`; formato no topo de `render_story.py`).
3. `python3 _kit_stories/render_story.py spec.json bg.svg saida.png`, depois JPG qualidade 94.

## Regras
- Todo número com fonte primária oficial ou duas fontes independentes que batem. Se o fato não está confirmado (ex.: "passou de R$ 6"), use a formulação que está confirmada ("encosta em R$ 6") e explique ao Tiago.
- Compliance de assessor: descrever, nunca recomendar; sem produto, emissor ou rentabilidade projetada; política só com fatos.
- Publicação automática (decisão do Tiago em 24/11/2026: "pode postar automático, não precisa pedir mais aprovação"), no HubPost, como STORY (sem legenda), agora + 3 min. Depois de publicar, avisar o Tiago com a arte, os dados e as fontes.
- Exceção: se a validação ou o compliance deixarem QUALQUER dúvida, não publicar. Deixar rascunho no HubPost e pedir o OK dele.

## Histórico
Ver `historico.md`.

## Aprendizados
- 24/11/2026: Tiago aprovou o Stories "Dólar chega a cair 2%" (99) e liberou a publicação automática dos próximos.
- Título de 2 linhas é mais seguro: com 3 linhas o título encostou na ilustração; ilustração até y≈860.
- Para fato intradiário, prefira dados que não mudam mais (PTAX do BC, fechamento anterior, "chegou a cair X%") a uma cotação do momento com fonte única.
