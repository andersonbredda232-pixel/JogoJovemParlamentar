# ADR-003 — Conteúdo pedagógico embutido no código

- **Status:** Aceito
- **Data:** 29/10/2026

## Contexto

As perguntas, etapas, imprevistos e cartas mudam com mais frequência que a
lógica do jogo. O conteúdo precisa funcionar sem internet e ser editável por
quem não programa, sem banco de dados nem painel administrativo.

## Decisão

O conteúdo fica em constantes JavaScript no início de `index.html`:
`ETAPAS`, `CASAS`, `Q`, `EVENTOS`, `CARTAS`, `CARGOS`, `REGRAS`, `COMO_JOGAR` e
`EXEMPLOS`. Cada constante tem, acima dela, um bloco de comentário com
finalidade, estrutura, campos e como interage com o motor.

Cada pergunta de `Q` é uma lista de 10 textos:

| Posição | Conteúdo |
|---|---|
| 0 | enunciado |
| 1 | resposta certa |
| 2, 3, 4 | erradas |
| 5 | explicação após o acerto |
| 6 | fonte legal |
| 7, 8, 9 | comentário das erradas 2, 3 e 4 |

A certa é sempre a posição 1; o jogo embaralha as alternativas na tela. As
perguntas de imprevisto seguem o mesmo formato, dentro de `EVENTOS[n].qs`.

## Consequências

Positivas:

- editar é copiar uma linha e trocar textos;
- o conteúdo vai junto no cache e funciona sem internet;
- o formato fixo permite exportar as perguntas para planilha de revisão.

Negativas:

- um erro de vírgula ou aspas quebra o jogo inteiro; é preciso abrir o jogo
  e conferir o console depois de editar;
- a posição dos campos precisa ser decorada ou consultada no comentário.

## Alternativas consideradas

- **Arquivo JSON separado:** mais limpo, mas exigiria pedido de rede extra e
  cuidado no cache; o ganho é pequeno para o volume atual.
- **Planilha on-line lida em tempo real:** dependeria de internet e de serviço
  externo.
