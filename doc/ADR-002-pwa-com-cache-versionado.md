# ADR-002 — PWA com service worker e cache versionado

- **Status:** Aceito
- **Data:** 29/10/2026

## Contexto

Escolas costumam ter internet instável. O jogo precisa abrir sem conexão
depois da primeira visita e poder ser instalado na tela inicial do celular.
Ao mesmo tempo, correções publicadas precisam chegar a quem já instalou.

## Decisão

- O jogo é um PWA com `manifest.webmanifest` e `sw.js`.
- O service worker usa a estratégia *stale-while-revalidate*: responde na hora
  com a cópia guardada e busca a versão nova para a próxima abertura.
- Só arquivos da mesma origem e pedidos `GET` passam pelo cache.
- Na instalação, os arquivos da lista `FILES` são guardados de uma vez.
- O nome do cache tem versão (`jovem-parlamentar-vNN`). **Toda publicação que
  altere arquivo publicado deve aumentar esse número.** Na ativação, caches de
  outras versões são apagados.
- A tela inicial oferece um link discreto de instalação, sem bloquear o jogo.

## Consequências

Positivas:

- o jogo abre instantaneamente e funciona sem internet;
- a troca de versão limpa o cache antigo sem ação do usuário.

Negativas:

- a versão nova aparece só na segunda abertura depois da publicação;
- esquecer de aumentar a versão deixa aparelhos presos na versão antiga;
- testes locais precisam desregistrar o service worker ou usar janela anônima.

## Alternativas consideradas

- **Cache first sem revalidação:** mais simples, mas exigiria sempre uma ação
  manual para atualizar.
- **Network first:** ficaria lento ou travaria em redes ruins.
