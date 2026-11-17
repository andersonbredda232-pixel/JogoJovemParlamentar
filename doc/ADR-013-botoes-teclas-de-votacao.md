# ADR-013 — Botões no formato de “teclas de votação”

- **Status:** Aceito
- **Data:** 04/11/2026
- **Complementa:** ADR-010 e ADR-011

## Contexto

Depois da revisão visual (ADR-011), os botões ficaram limpos, mas genéricos:
o principal, o secundário e as alternativas pareciam da mesma família de
qualquer aplicativo. O jogo precisava de botões com “jeito próprio”, ligados
à Câmara, e que seguissem as leis de UX usadas no projeto:

- **Fitts:** alvos grandes e fáceis de acertar com o polegar;
- **Hick:** poucas escolhas por tela, com uma ação principal clara;
- **Jakob:** comportamento que o jogador já conhece de outros aplicativos;
- **Von Restorff:** a ação principal se destaca das demais.

## Decisão

Os botões imitam as **teclas do painel de votação do Plenário**:

- uma borda inferior mais grossa (`--tecla: 4px`) dá volume ao botão; ao
  apertar, a tecla “afunda” (a borda diminui e o botão desce);
- **principal** (`.go`): anil cheio, uma por tela;
- **secundário** (`.sec2` e botões de saída): branco com borda anil;
- **alternativas** (`#o button`): cada uma recebe uma letra (A, B, C, D) num
  selo à esquerda, como as opções de uma cédula; a errada fica riscada e a
  certa fica verde;
- **realce do ponteiro** só em aparelhos com mouse (`@media (hover: hover)`),
  para não ficar “preso” no celular;
- **foco do teclado** em amarelo (`#f2c300`, o amarelo do Legis), bem visível
  sobre o anil;
- **alturas mínimas:** principal 52 px, alternativas 56 px, escolha
  Vereadora/Vereador 48 px e os demais 44 px.

## Consequências

Positivas:

- identidade própria, ligada ao Plenário, sem perder a clareza;
- 0 alvos abaixo de 44 px nas medições em 320, 390 e 1.440 px;
- o jogador sabe qual é a ação principal em cada tela.

Negativas:

- as letras A–D são geradas pelo CSS (contador); se a ordem das
  alternativas mudar no motor, as letras acompanham sozinhas, mas não são
  lidas pelos leitores de tela.

## Alternativas consideradas

- **Bloco “Design Premium V2”:** sombras e degradês fortes; quebrava o layout
  e contrariava o ADR-011.
- **Manter os botões da revisão anterior:** corretos, mas sem identidade.
