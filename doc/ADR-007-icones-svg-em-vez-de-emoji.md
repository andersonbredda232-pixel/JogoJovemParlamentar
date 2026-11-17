# ADR-007 — Ícones SVG em vez de emoji

- **Status:** Aceito; substituído em parte pelo ADR-017 (os desenhos agora
  são da biblioteca Phosphor, embutidos no arquivo)
- **Data:** 29/10/2026

## Contexto

A interface usava emoji em 38 lugares (corações, estrela, ampulheta, ícones das
etapas e das cartas). Cada sistema desenha emoji de um jeito: no Android, a
estrela e o coração saíam diferentes do computador, e a interface perdia
unidade.

## Decisão

- Usar um conjunto único de ícones em traço, em SVG, guardado no objeto
  `ICONES` e inserido com a função `ico(nome, classe)`.
- Tamanhos entre 16 e 24 px, na cor do texto ou em anil.
- Ícones decorativos recebem `aria-hidden="true"`; quando o ícone sozinho
  carrega sentido, o botão ou elemento tem rótulo textual.
- O campo `ic` de `ETAPAS`, `EVENTOS` e `CARTAS` guarda o **nome** do ícone, não
  um emoji.

## Consequências

Positivas:

- aparência igual em todos os aparelhos;
- ícones herdam a cor do tema e podem ser ajustados por CSS.

Negativas:

- ícone novo precisa ser desenhado em SVG e acrescentado a `ICONES`.

## Alternativas consideradas

- **Biblioteca de ícones por CDN:** dependeria de internet.
- **Manter emoji:** sem custo, mas com aparência inconsistente.
