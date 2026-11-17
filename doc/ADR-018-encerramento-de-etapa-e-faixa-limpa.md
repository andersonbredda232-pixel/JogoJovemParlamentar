# ADR-018 — Encerramento de etapa, faixa sem contadores e nova tela inicial

- **Status:** Aceito
- **Data:** 17/11/2026

## Contexto

Ao testar a v31, Anderson pediu:

- trocar a imagem da tela inicial por uma nova ilustração do Legis na
  tribuna;
- tirar “Etapa X de 7” e “Casa X de 21” da faixa, que pareciam
  mecânicos demais;
- trocar o botão “Entrar” por “Prosseguir”;
- mostrar um resumo ao fim de cada etapa. Na primeira tentativa, o resumo
  da etapa anterior aparecia na mesma tela da etapa nova e misturava as
  duas; ele escolheu separá-las em duas telas.

## Decisão

- **Tela inicial:** nova imagem (`CENA_INICIO`), com o amarelo do Legis
  clareado para igualar o das outras telas.
- **Faixa da etapa:** mostra o que acontece na etapa (`local`), o nome da
  etapa e o tipo da casa (Pergunta, Imprevisto, Sorte ou Azar), sem
  contadores.
- **Botão:** “Prosseguir” na apresentação da etapa (a 1ª continua
  “Começar a tramitação”).
- **Encerramento de etapa:** ao passar da última casa de uma etapa, a fase
  `fimEtapa` mostra a faixa da etapa que terminou (“Etapa concluída”), a
  frase do campo `feito` de `ETAPAS`, a próxima etapa e o caminho do
  projeto (etapas feitas, atual e futuras). Só depois vem a apresentação da
  etapa nova.
- **Glossário:** ficou pronto, mas fora do jogo até a troca das perguntas.

## Consequências

Positivas:

- cada tela fala de uma etapa só; o aluno vê o caminho da lei ao fim de
  cada fase;
- faixa mais limpa.

Negativas:

- um toque a mais entre as etapas;
- sem contadores na faixa, o progresso aparece só no tabuleiro.

## Alternativas consideradas

- **Resumo e etapa nova na mesma tela, com títulos separados:** descartada
  por deixar a tela cheia.
