# ADR-005 — Pontuação por estrelas e duas formas de perder

- **Status:** Substituído em parte pelo ADR-016 (custos em meses, consulta,
  cartas, vida por etapa e formas de perder) e pelo ADR-017 (a consulta
  esconde uma errada)
- **Data:** 29/10/2026

## Contexto

A pontuação anterior misturava pontos, apoio político e várias condições de
derrota, o que confundia os estudantes e tinha erros de cálculo. Com o modelo
de Crowder (ADR-004), o jogador sempre acerta em algum momento; a pontuação
precisa medir **em quantas tentativas** ele acertou.

## Decisão

Os números ficam em `REGRAS` e `CARGOS`:

| Regra | Valor |
|---|---|
| Vidas | 5 |
| Mandato | 48 meses |
| Custo de cada tentativa | 2 meses |
| Estrelas por tentativa | 3, 2, 1 e depois 0 |
| Consultas à Procuradoria | 3, de 1 mês cada |
| Bônus na Sanção | +1 estrela por vida restante |

- O **primeiro** erro de uma pergunta de etapa custa 1 vida; os erros
  seguintes na mesma pergunta custam só os meses.
- Erro em imprevisto não tira vida; aplica o efeito do evento em meses.
- A consulta esconde até duas erradas não tentadas, deixando sempre uma.
- Só há **duas formas de perder**: ficar sem vidas ou terminar o mandato.
- Se o acerto leva à Sanção, a vitória vale mesmo com o mandato zerado.
- O cargo final depende das estrelas: Vereador(a) Iniciante (0), Experiente
  (8), Presidente de Comissão (18), Líder de Bancada (30), Presidente da
  Câmara (42) e Mestre(a) do Processo Legislativo (52).

## Consequências

Positivas:

- regra explicável em poucas linhas na tela Como jogar;
- tempo (meses) e erros (vidas) são recursos visíveis e diferentes;
- o bônus por vidas premia quem erra pouco até o fim.

Negativas:

- os limites dos cargos dependem do número de casas; acrescentar casas exige
  rever `CARGOS`.

## Alternativas consideradas

- **Pontos numéricos por acerto:** menos legíveis para o público jovem.
- **Derrota também por apoio político baixo:** acrescentava uma terceira
  barra e confundia o objetivo.
