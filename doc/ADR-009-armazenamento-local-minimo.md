# ADR-009 — Armazenamento local mínimo

- **Status:** Aceito
- **Data:** 29/10/2026
- **Complementado por:** ADR-016 (o tratamento deixou de ser guardado) e ADR-014 (aviso de privacidade e “Apagar meus dados”)

## Contexto

O jogo é usado por estudantes, muitas vezes em aparelhos compartilhados da
escola. Não há servidor nem conta de usuário, e não se deve coletar dados
pessoais.

## Decisão

- A caderneta `P` guarda somente: recorde de estrelas (`best`), leis
  aprovadas (`leis`), último nome digitado (`nome`) e tratamento
  (`trat`, vereador ou vereadora).
- Ela é gravada no `localStorage` na chave `jv1`, dentro de `try/catch`, para
  que o jogo funcione mesmo com o armazenamento bloqueado.
- Nenhum dado sai do aparelho. Não há analytics, cookies de terceiros ou
  envio a servidor.
- A partida em andamento (`G`) não é gravada.

## Consequências

Positivas:

- nada a proteger além do próprio aparelho;
- funciona em janela anônima, só sem lembrar o recorde.

Negativas:

- fechar a página no meio da partida perde o progresso;
- não há placar entre aparelhos ou turmas.

## Alternativas consideradas

- **Salvar a partida em andamento:** sugerida como melhoria (lei de UX da
  tolerância a interrupções); exigirá novo ADR se aprovada.
- **Placar on-line:** exigiria servidor, contas e tratamento de dados de
  menores.
