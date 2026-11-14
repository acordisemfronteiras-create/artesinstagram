# Skills externas listadas no prompt-motion.com

Seis entradas da biblioteca são skills instaláveis, e não prompts. Os comandos abaixo vêm das páginas do prompt-motion.com. Este ambiente (a sessão na nuvem) não instala skills na conta do Tiago. Quem instala é ele, no Claude Code ou no Cowork, quando quiser. Por enquanto, a ideia é **absorver as regras no nosso motor**, que já é HTML + Playwright + ffmpeg.

| Skill | Para que serve | Instalação | Repo | Estudo |
|---|---|---|---|---|
| design-taste-frontend (taste-skill), @LexnLin | Direção de arte para sites, dashboards e telas de app | `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"` | https://github.com/Leonxlnx/taste-skill | Lido em 14/11 (resumo abaixo) |
| cinetic, @LexnLin | Motion e tipografia cinética para agentes | `npx skills add Leonxlnx/cinetic` | https://github.com/Leonxlnx/cinetic | Pendente: o GitHub pediu autorização e o pedido expirou |
| html-demo, @MengTo | Demos animadas em HTML | `npx skills add MengTo/Skills --skill html-demo` | https://github.com/MengTo/Skills/tree/main/agent-skills/web-design/html-demo | Pendente (mesmo motivo) |
| product-film, @anthonyriera | Filmes de produto | `/plugin marketplace add Rieranthony/product-film-skill` e `/plugin install product-film@product-film-skill` | https://github.com/Rieranthony/product-film-skill | Pendente (mesmo motivo) |
| session-story (HyperFrames), @jake11moran | Vídeo a partir de uma sessão de trabalho, no motor HyperFrames | `npx skills add heygen-com/hyperframes-community-skills --skill session-story` | https://github.com/heygen-com/hyperframes-community-skills/tree/master/skills/session-story | Bloqueado: o GitHub não permite leitura automática desta pasta (robots) |
| generative-film-skill, @BuildFastWithAI | Tema → MP4 desenhado em código, trilha sintetizada na batida | `npx skills@latest add https://github.com/buildfastwithai/buildfast-skills` | https://github.com/buildfastwithai/buildfast-skills/tree/main/generative-film-skill | Pendente (mesmo motivo) |

## design-taste-frontend (lido)

- **Licença:** MIT. **Exige:** Node 22+ e Chrome/Chromium; ffmpeg é opcional.
- **O que faz:** antes do HTML, classifica o tipo de negócio, planeja a página tela a tela, escolhe paleta e par de fontes e um layout de abertura testado. No fim, confere o resultado no navegador em várias larguras e repete a correção até três rodadas.
- **Regras que servem para nós:**
  - Um único sistema de design do começo ao fim.
  - Margens esquerda e direita iguais.
  - Sem texto de exemplo e sem dado inventado.
  - Movimento com uma entrada forte e um ou dois "momentos", e o resto discreto.
  - Conferência visual em rodadas, com uma lista fixa do que procurar: área vazia, contraste baixo, coluna desalinhada, texto de exemplo esquecido.
- **O que não serve:** é feita para sites, não para vídeo. Também usa fotos e ícones de marcas reais em páginas de tecnologia, o que nós não fazemos.
- **Vale instalar?** Só se o Tiago quiser montar sites ou landing pages. Para os Reels, as regras acima bastam.

## Para terminar o estudo das pendentes

Basta autorizar o acesso ao github.com quando o pedido de permissão aparecer, ou colar os links dos repositórios numa mensagem. Na próxima rodada eu leio os READMEs e os SKILL.md, anoto licença, dependências e regras aqui, e digo se vale instalar. As candidatas mais promissoras para o nosso caso são a **generative-film-skill** (é o nosso pipeline: código → quadros → trilha na batida) e a **product-film**.
