# Kit de posts de notícia — @tiagoassessorxp

Padrão aprovado pelo Tiago em 04/11/2026 (referência: `referencia_selic_04-11.png`).

## Visual
- Formato feed 1080x1350 (4:5).
- Fundo: ilustração desenhada em SVG sobre o tema da notícia (ex.: prédio do Banco Central para Copom; pregão/telão com gráfico para Ibovespa; nota de dólar ou mapa para câmbio; silo e lavoura para agro; Capitólio ou prédio do Fed para juros nos EUA; barril para petróleo). A metade de cima mostra a ilustração; a de baixo termina em preto #0a0a0a, onde vai o texto. Paleta escura com dourado #c9a45c. Nada de logos ou marcas reais, nem rostos de pessoas reais.
- Tipografia: Fraunces (títulos e números) + Inter (texto). Dourado só para o número-chave do título (`<em>`).
- Estrutura: kicker + data no topo · selo opcional ("Urgente" só para decisão ou evento do dia) · título curto · uma linha de contexto · grade de 2 ou 4 dados · rodapé com nome, "Assessor Alta Renda da XP Investimentos", @tiagoassessorxp e fonte.

## Como gerar
1. Escreva o fundo como script Python que gera `bg.svg` (veja `exemplo_bg_banco_central.py`). Crie um desenho novo por tema; capriche.
2. Escreva o `spec.json` (veja `exemplo_spec_selic.json` e o topo de `render.py`).
3. `python3 render.py spec.json bg.svg saida.png` (precisa de `playwright`; usa o Chrome do sistema se existir).
4. Abra o PNG e confira: nada sobreposto, título em até 3 linhas, sub em até 2 linhas.

## Legenda
- Tom profissional, sofisticado e direto, sem emojis. 4 a 6 parágrafos curtos: o fato, o contexto, o que muda na prática para investidor, empresa ou produtor rural (sem recomendar produto ou ativo específico), o próximo evento a acompanhar e o convite "fale comigo pelo link da bio".
- 6 a 9 hashtags no fim.
- Política: só fatos, sem opinião sobre partidos ou candidatos.

## Publicação
- Arte em `NN_dia_dd-mm_HHh_tema/arquivo.jpg` (JPG qualidade 94), commit e push na `main`.
- Publicação no Instagram (@tiagoassessorxp) pelo **HubPost**: upload do JPG (get_upload_url → PUT → confirm_upload) e create_post na conta Instagram, tipo POST, fuso America/Sao_Paulo.
- Desde 12/11/2026 o Tiago deu **aprovação permanente** para os posts da tarefa de notícias: publicar direto, sem esperar resposta, desde que a validação de fontes e o compliance passem. Se algum dos dois falhar, não publicar: mandar como rascunho e explicar.
