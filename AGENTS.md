# AGENTS.md — Instruções permanentes do projeto Jovem Parlamentar

## 1. Fluxo obrigatório de trabalho

Antes de realizar qualquer alteração que não seja trivial, o agente deverá
apresentar um plano de trabalho e executá-lo até a entrega integral, sem exigir
aprovação entre as etapas, salvo orientação diferente do usuário.

O plano deverá:

- dividir a atividade em etapas pequenas e independentes;
- indicar o objetivo de cada etapa;
- identificar os arquivos que serão alterados;
- apontar impactos e riscos;
- informar dúvidas ou premissas assumidas.

Ao concluir, o agente deverá:

- apresentar um resumo objetivo das alterações;
- informar os arquivos modificados;
- indicar as verificações executadas e seus resultados;
- sugerir uma mensagem de commit;
- apresentar o `git diff`.

Não realizar commits automaticamente, salvo solicitação expressa do usuário.

### Mostrar antes de aplicar

Mudanças visuais ou de comportamento perceptível pelo jogador deverão ser
feitas primeiro em uma **cópia** do jogo (por exemplo, `index_previa.html`) e
mostradas ao usuário com capturas de tela. Só depois da aprovação o agente
aplica a mudança em `index.html`.

Quando o usuário disser “não faça nada”, “só processe” ou “só quero dar
orientações”, o agente deverá apenas registrar e confirmar o entendimento,
sem alterar arquivos.

### Quando interromper

A execução contínua não autoriza prosseguir quando houver:

- ambiguidade que possa alterar o resultado esperado;
- decisão pedagógica ou de conteúdo ainda não definida;
- necessidade de ampliar o escopo;
- ação destrutiva não autorizada;
- conflito com alterações feitas pelo usuário.

Nesses casos, interrompa, explique o impedimento e peça orientação.

Melhorias percebidas fora do plano deverão ser registradas como sugestão ao
final, sem implementação.

## 2. Escopo

Limite-se ao que foi pedido. Não:

- refatore código não relacionado;
- renomeie funções, constantes ou classes CSS existentes;
- reorganize arquivos;
- altere perguntas, regras ou pontuação quando a tarefa for visual;
- altere o visual quando a tarefa for de conteúdo ou de lógica;
- reformate trechos sem relação com a tarefa.

Cada alerta relevante deverá ser apresentado uma única vez. Decisões já
confirmadas pelo usuário não deverão ser reabertas.

## 3. Leitura obrigatória

Antes de propor ou realizar alterações, leia:

- os ADRs relacionados em `doc/`;
- o `README.md`;
- o bloco de comentário da constante ou função que será alterada.

As decisões registradas em ADR aceito são obrigatórias. Não altere
arquitetura, tecnologias ou padrões sem autorização expressa.

## 4. Princípio central

Adote a solução de menor complexidade que não comprometa acessibilidade,
correção do conteúdo, manutenção, desempenho e funcionamento sem internet.
Não introduza abstrações ou dependências por hábito.

## 5. Arquitetura

- O jogo é um único `index.html` com HTML, CSS, JavaScript, conteúdo e
  ilustrações ([ADR-001](doc/ADR-001-arquivo-html-unico-sem-framework.md)),
  dividido em seis partes: ESTILOS, PÁGINA, CONTEÚDO, MOTOR, IMAGENS e
  APLICATIVO. Respeite essa ordem e os blocos de cada parte
  ([ADR-015](doc/ADR-015-codigo-enxuto-e-verificacao.md)).
- Não use React, Vue, Angular, Svelte, TypeScript, bundlers, Tailwind ou
  qualquer etapa de build.
- Não carregue scripts, estilos, fontes ou imagens de servidores externos.
- O estado da partida fica no objeto `G`; toda ação altera `G` e chama
  `render()`. Não manipule a tela fora desse ciclo.
- A caderneta `P` (chave `jv1` do `localStorage`) guarda somente recorde,
  leis aprovadas e nome (o tratamento Vereadora/Vereador não é guardado)
  ([ADR-009](doc/ADR-009-armazenamento-local-minimo.md)).

## 6. PWA e publicação

- A cada alteração em arquivo publicado, aumente a versão de `CACHE` em
  `sw.js` ([ADR-002](doc/ADR-002-pwa-com-cache-versionado.md)).
- Arquivo novo que precise funcionar sem internet deverá entrar na lista
  `FILES` do `sw.js`.
- Mantenha `theme_color` e `background_color` do manifesto coerentes com a
  identidade visual.

## 7. Conteúdo pedagógico

- Toda pergunta deverá ter base no Regimento Interno (RI) ou na Lei Orgânica
  (LOM) e citar o artigo na posição 6
  ([ADR-012](doc/ADR-012-fontes-normativas.md)).
- Toda alternativa errada deverá ter comentário próprio, que explique por que
  está errada sem revelar a resposta certa
  ([ADR-004](doc/ADR-004-instrucao-ramificada-de-crowder.md)).
- Não invente regra regimental. Em caso de dúvida, pergunte ao usuário.
- Mantenha pelo menos seis perguntas por etapa.
- Linguagem: português do Brasil, frases curtas, adequada a estudantes do
  ensino médio, sem gírias nem ironia com o jogador.

## 8. Regras do jogo

Os números ficam em `REGRAS` e `CARGOS`. Não os altere sem pedido expresso.
Mudança na pontuação ou nas formas de perder exige novo ADR que substitua o
[ADR-005](doc/ADR-005-pontuacao-por-estrelas.md), o
[ADR-016](doc/ADR-016-ajustes-de-jogabilidade.md) e o
[ADR-017](doc/ADR-017-textos-consulta-e-icones-phosphor.md).

Ao trocar perguntas: o comentário de cada errada explica o erro sem dizer
qual é a certa, e o enunciado não supõe o tema do projeto do jogador.
Mantenha perguntas sobre veto na Prefeitura (lista `VETO`).

## 9. Interface

- Respeite a identidade visual da Câmara
  ([ADR-006](doc/ADR-006-identidade-visual-da-camara.md)): anil `#323380`,
  Bebas Neue nos títulos e Montserrat no texto.
- Use ícones do conjunto `ICONES` com `ico(nome)`; não use emoji como
  elemento de interface ([ADR-007](doc/ADR-007-icones-svg-em-vez-de-emoji.md)).
  Ícone novo vem da biblioteca Phosphor, peso regular, copiado para dentro
  do arquivo ([ADR-017](doc/ADR-017-textos-consulta-e-icones-phosphor.md)).
- Siga as regras de acabamento do
  [ADR-011](doc/ADR-011-regras-de-acabamento-visual.md): sem gradientes, sombra
  apenas no que flutua, rótulos em caixa normal, anil cheio só em ações e
  estados.
- Os botões seguem o formato de “teclas de votação”
  ([ADR-013](doc/ADR-013-botoes-teclas-de-votacao.md)).
- Cores, fontes e medidas ficam só nas variáveis do bloco **CORES, FONTES E
  MEDIDAS** (`--anil`, `--texto2`...). Não espalhe cores soltas pelo CSS.
- Cada seletor aparece uma vez por contexto (base, celular, computador).
  Antes de criar uma regra, procure se ela já existe no bloco da tela.
- O Legis não pode ser deformado, duplicado nem trocado por outro personagem
  ([ADR-008](doc/ADR-008-ilustracoes-embutidas-e-legis.md)).
- Não use animações decorativas longas, carrossel automático ou som sem
  ação do jogador.

## 10. Acessibilidade

Toda tela deve
([ADR-010](doc/ADR-010-acessibilidade-e-areas-de-toque.md)):

- funcionar por teclado, com foco visível;
- usar HTML semântico e rótulos nos botões;
- ter texto alternativo nas imagens com conteúdo;
- manter contraste mínimo de 4,5:1 no texto;
- não depender só de cor (erro também é riscado e comentado);
- ter alvos de toque de pelo menos 44 × 44 px;
- funcionar de 320 px a 1.440 px de largura, sem rolagem horizontal.

## 11. Segurança e privacidade

- Escape todo texto exibido com `esc()` antes de inserir em HTML.
- Não colete dados pessoais além do nome digitado, que fica só no aparelho.
- Não envie dados a servidores, não use analytics nem cookies de terceiros.
- Mantenha o aviso de privacidade e o botão “Apagar meus dados” da tela
  inicial verdadeiros: se o que fica guardado mudar, mude o texto também
  ([ADR-014](doc/ADR-014-privacidade-e-lgpd.md)).

## 12. Verificações

Antes de concluir uma tarefa, execute as verificações pertinentes:

- abrir o jogo por HTTP local, sem erros no console;
- `python3 testes/partidas.py` (regras e erros de JavaScript);
- `python3 testes/telas.py` (capturas, alvos de 44 px, rolagem horizontal);
- conferir telas em 390 px (celular) e 1.440 px (computador);
- confirmar que o service worker instala com a nova versão de cache.

Em limpezas e reorganizações que não devem mudar nada na tela, compare a
versão antiga e a nova: as saídas de `testes/partidas.py` devem ser iguais e
as capturas, idênticas ([ADR-015](doc/ADR-015-codigo-enxuto-e-verificacao.md)).

Testes automatizados com Playwright estão autorizados, em servidor local e com
dados descartáveis.

## 13. Dependências

Antes de acrescentar qualquer arquivo de terceiros (fonte, imagem, biblioteca):

- verifique se é realmente necessário;
- confira a licença e registre-a no repositório;
- guarde o arquivo localmente, nunca por link externo;
- registre a justificativa em ADR.

## 14. Documentação

Atualize a documentação quando a alteração mudar comportamento, regras,
conteúdo, publicação ou decisão de arquitetura.

Não modifique ADR aceito para esconder mudança de decisão. Proponha novo ADR
que o substitua e marque o anterior como “Substituído por ADR-NNN”.

Comentários por blocos: cada bloco do CSS e do JavaScript começa com um
título em MAIÚSCULAS e uma explicação curta, em português simples, do que faz
e de como se liga ao resto. Comentários de linha só onde a regra não é óbvia.
Código que não é usado em nenhuma tela deve ser removido, não comentado.

## 15. Comunicação com o usuário

- Responda em português do Brasil.
- Comece cada resposta com uma correção sucinta, gramatical e de pontuação,
  da mensagem do usuário.
- Ao mostrar alternativas visuais, numere-as e mostre imagens, não só texto.

## 16. Incerteza

Quando houver ambiguidade:

- não invente regra de jogo nem regra regimental;
- não escolha tecnologia nova;
- não suponha comportamento silenciosamente;
- identifique objetivamente a decisão pendente.
