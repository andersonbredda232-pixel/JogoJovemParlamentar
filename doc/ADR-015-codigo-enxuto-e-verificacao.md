# ADR-015 — Código enxuto, comentado por blocos e verificado por comparação

- **Status:** Aceito
- **Data:** 04/11/2026
- **Complementa:** ADR-001

## Contexto

Depois de muitas rodadas de ajustes visuais, o `index.html` acumulou
camadas: o mesmo botão tinha regras de CSS em três ou quatro lugares, cada
uma desfazendo parte da anterior, e o JavaScript guardava trechos que nenhuma
tela usava mais (fotos de cenário vazias, uma cena antiga da tribuna, ramos
para “voltar casa” que nenhuma carta aciona). Os comentários repetiam a
mesma explicação em vários formatos. Ficou difícil para uma pessoa entender
o arquivo e arriscado mexer nele.

## Decisão

1. **CSS em uma camada só.** Cada seletor aparece uma vez por contexto
   (base, celular, computador...). As regras ficam agrupadas por tela ou
   peça, na ordem: cores e medidas → base → cabeçalho → botões → peças
   comuns → Legis → boas-vindas → Como jogar → gabinete → partida → cartas →
   pop-up → tela final → ajustes de celular e de computador → animações.
2. **Variáveis com nomes em português** (`--anil`, `--vermelho`,
   `--texto2`...), explicadas no bloco de cores.
3. **Sem código morto.** Declaração, regra, função ou imagem que não muda
   nada em nenhuma tela é removida.
4. **Comentários por blocos.** Cada bloco do CSS e do JavaScript começa com
   um título e uma explicação curta do que faz; comentários de linha só onde
   a regra não é óbvia.
5. **Nenhuma mudança visível sem pedido.** Uma limpeza só é aceita se o
   resultado for igual ao anterior, conferido por máquina:
   - os estilos calculados de todos os elementos, em 34 situações do jogo
     (telas, pop-ups, cartas, imprevistos, final), em 8 larguras de tela,
     com o mouse em cima, com foco do teclado e com botão apertado;
   - capturas de tela comparadas pixel a pixel;
   - 30 partidas automáticas com sorteio fixo, que precisam terminar
     exatamente iguais (`testes/partidas.py`).

## Consequências

Positivas:

- CSS cerca de 40% menor (de 76 KB para 44 KB) e legível de cima para baixo;
- quem edita encontra cada coisa em um só lugar;
- a comparação automática dá segurança para limpar sem medo.

Negativas:

- a comparação completa leva alguns minutos e exige Python e Playwright;
- mudar a ordem das regras exige cuidado: duas regras de mesmo peso que
  disputam a mesma propriedade dependem da ordem (a de baixo vence).

## Alternativas consideradas

- **Reescrever o CSS do zero:** mais rápido, mas sem garantia de que o
  visual aprovado continuaria igual.
- **Ferramentas de minificação:** reduzem o tamanho, mas tiram os
  comentários e não resolvem as camadas repetidas.
