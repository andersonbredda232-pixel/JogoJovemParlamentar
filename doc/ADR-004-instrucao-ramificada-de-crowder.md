# ADR-004 — Instrução programada ramificada de Crowder

- **Status:** Aceito
- **Data:** 29/10/2026

## Contexto

Na primeira versão, o erro só tirava pontos e passava para a próxima pergunta.
O estudante não sabia por que tinha errado e não tinha chance de corrigir o
raciocínio. O objetivo do jogo é ensinar, não apenas avaliar.

## Decisão

Adotar o modelo de instrução programada ramificada de Norman Crowder:

1. Cada alternativa errada tem um comentário próprio (posições 7, 8 e 9 da
   pergunta), que explica o equívoco sem entregar a resposta.
2. Ao errar, abre-se um pop-up com esse comentário. Ele **só fecha pelo botão
   OK** (não fecha com Esc nem clicando fora), e o foco vai para o OK.
3. Depois do OK, o jogador volta à **mesma pergunta**, com a alternativa
   errada riscada e desabilitada.
4. O peão **só avança com acerto**, sempre para a frente.
5. Depois do acerto, aparece a explicação (posição 5) e a fonte legal
   (posição 6).
6. Ao fim da partida, a seção “Para rever” lista cada pergunta errada, a
   resposta certa, a fonte e as alternativas descartadas.

## Consequências

Positivas:

- o erro vira momento de aprendizagem;
- o estudante sempre chega à resposta certa antes de seguir;
- “Para rever” serve de material de estudo depois da partida.

Negativas:

- cada pergunta exige quatro textos de explicação, o que dá mais trabalho
  para escrever e revisar;
- partidas ficam um pouco mais longas.

## Alternativas consideradas

- **Instrução linear de Skinner** (só certo ou errado e passa): mais rápida,
  mas sem retorno sobre o erro.
- **Mostrar a resposta certa logo após o erro:** ensina menos, porque o
  estudante não refaz o raciocínio.
