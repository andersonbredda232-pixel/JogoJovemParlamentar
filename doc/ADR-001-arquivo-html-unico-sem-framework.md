# ADR-001 — Arquivo HTML único, sem framework nem build

- **Status:** Aceito
- **Data:** 29/10/2026
- **Complementado por:** ADR-015 (organização interna e verificação)

## Contexto

O jogo é mantido por uma pessoa e publicado no GitHub Pages, que serve apenas
arquivos estáticos. Ele precisa abrir rápido em celulares simples de
estudantes, funcionar sem internet e poder ser editado sem instalar
ferramentas de desenvolvimento.

## Decisão

Todo o jogo fica em um único `index.html`, com HTML, CSS e JavaScript nativos.
O conteúdo, os ícones e as ilustrações ficam embutidos no mesmo arquivo.

Ficam fora do `index.html` somente os arquivos que o navegador exige separados:
`sw.js`, `manifest.webmanifest`, os ícones do aplicativo e as fontes.

O código segue um ciclo simples: o estado da partida fica no objeto `G`; toda
ação altera `G` e chama `render()`, que redesenha a tela a partir dele.

## Consequências

Positivas:

- publicar é copiar arquivos; não há build que possa quebrar;
- qualquer editor de texto basta para alterar perguntas;
- poucos pedidos de rede, bom para o cache e para conexões lentas;
- nenhuma dependência para atualizar ou auditar.

Negativas:

- o arquivo é grande (cerca de 350 KB, a maior parte imagens embutidas), o
  que dificulta a leitura dos diffs;
- não há verificação de tipos nem módulos; a organização depende de
  comentários e da ordem das seções;
- conflitos de edição simultânea são mais prováveis.

## Alternativas consideradas

- **React, Vue ou Svelte com Vite:** exigiria Node e build a cada publicação,
  sem ganho para um jogo de telas simples.
- **Vários arquivos JS e CSS:** facilitaria a leitura, mas aumentaria a lista
  de cache do service worker e os pontos de falha sem internet. Pode ser
  revisto em novo ADR se o arquivo crescer demais.
