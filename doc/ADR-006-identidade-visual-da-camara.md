# ADR-006 — Identidade visual da Câmara Municipal de Campinas

- **Status:** Aceito
- **Data:** 29/10/2026

## Contexto

O jogo é um produto institucional da Câmara e precisa ser reconhecido como tal,
com a mesma aparência das peças de comunicação da Casa, como o informativo
Notícias da Casa.

## Decisão

- **Cor principal:** anil `#323380`, cor oficial da Câmara.
- **Chão da página:** `#f6f6fc`, o tom mais claro do anil.
- **Destaque e foco:** amarelo `#f2c300`, também usado no Legis.
- **Títulos:** Bebas Neue. **Texto:** Montserrat.
- As fontes ficam em `fontes/` em woff2, com as licenças OFL, e são
  declaradas com `@font-face`. Não se usa Google Fonts nem outro CDN.
- O logotipo da Câmara aparece no cabeçalho; no celular, fica à esquerda, e o
  botão Início, à direita.
- `theme_color` do manifesto é o anil e `background_color` é o chão.

O anil é uma exceção declarada à regra geral de evitar violeta e índigo da
skill de design (ADR-011).

## Consequências

Positivas:

- reconhecimento imediato como material da Câmara;
- fontes locais funcionam sem internet e não expõem o jogador a terceiros.

Negativas:

- as fontes somam cerca de 70 KB ao cache.

## Alternativas consideradas

- **Fontes do sistema:** mais leves, mas sem a identidade do informativo.
- **Google Fonts:** dependeria de internet e de serviço externo.
