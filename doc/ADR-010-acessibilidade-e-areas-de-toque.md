# ADR-010 — Acessibilidade e áreas de toque

- **Status:** Aceito
- **Data:** 29/10/2026

## Contexto

O jogo é usado em celulares, em sala de aula, por estudantes com diferentes
necessidades. Alvos pequenos e informações só por cor causavam toques errados
e dúvidas.

## Decisão

- Alvos de toque de pelo menos **44 × 44 px** (lei de Fitts); o botão
  principal e as alternativas são maiores.
- Foco visível em todos os elementos interativos.
- Contraste mínimo de 4,5:1 no texto.
- Erro não é sinalizado só pela cor: a alternativa é riscada e o pop-up
  explica.
- Ao abrir o pop-up, o foco vai para o botão OK; ao fechá-lo, volta à pergunta.
- Botões com rótulo textual; ícones decorativos com `aria-hidden`.
- Layout de 320 px a 1.440 px, sem rolagem horizontal; textos longos, como o
  nome do projeto, quebram linha em vez de serem cortados.
- No celular, o teclado virtual é fechado antes de rolar até o palco.
- Poucas opções por tela (lei de Hick): uma ação principal por tela.

## Consequências

Positivas:

- menos toques errados e uso possível por teclado;
- verificação objetiva: medir os alvos com Playwright.

Negativas:

- telas pequenas comportam menos informação de uma vez.

## Alternativas consideradas

- **Alvos de 32 px**, como em interfaces de mesa: reprovados nos testes em
  celular.
