# ADR-016 — Ajustes de jogabilidade para o público leigo

- **Status:** Aceito; substituído em parte pelo ADR-017 (consulta, texto do
  imprevisto e Como jogar)
- **Data:** 13/11/2026
- **Substitui em parte:** ADR-005 (custos em meses, consulta, cartas,
  formas de perder) e ADR-008 (onde o Legis aparece)

## Contexto

Uma revisão lenta do jogo (09/11/2026), com partidas jogadas tela a tela e
milhares de partidas simuladas, encontrou problemas que o público notaria:

- o Legis aparecia duas ou três vezes na mesma tela, com e sem terno;
- “Vereadora” vinha marcada por padrão (“Vereadora Lucas”);
- o jogador podia perder logo depois de um “Isso mesmo!”;
- uma carta de azar podia encerrar a partida sozinha;
- depois do OK, a moldura de foco caía na alternativa que sobrava,
  parecendo dica;
- o jogo era difícil demais para quem não conhece o Regimento: quem
  acertava metade das perguntas de primeira vencia só 7% das vezes;
- várias regras não eram explicadas, e alguns textos se contradiziam.

## Decisão

**Legis e telas**
- Um Legis só, sempre de terno. Na partida, o balão de fala fica só com o
  texto (o Legis já está na faixa da etapa); o peão do tabuleiro é a cabeça
  do Legis de terno; a tela final usa o Legis de terno. A imagem do Legis
  sem terno (MIMG) saiu do jogo.
- Vereadora/Vereador sem opção marcada; a escolha é obrigatória e deixou
  de ser guardada no aparelho.
- Depois do OK do pop-up, o foco vai para o enunciado, não para uma
  alternativa.
- No computador, as casas de imprevisto e de carta também mostram o número.

**Regras** (`REGRAS`)
- Cada acerto gasta 1 mês (`custoAcerto`) e cada erro, 2 (`custoErro`). O
  mandato continua com 48 meses, a legislatura de 4 anos.
- Acertar nunca faz perder. Com o mandato zerado, o jogador segue enquanto
  acertar; o primeiro erro encerra a partida.
- Cartas nunca encerram a partida, não movem o peão e não tiram estrela.
  “Manchete negativa” passou a tirar 2 meses; “Parecer favorável” passou a
  dar 2 meses (antes avançava 2 casas).
- A cada etapa nova, a partir da 2ª, o jogador recupera 1 vida (até 5).
- A consulta à Procuradoria é grátis (`custoConsulta: 0`), continua com 3
  por partida e o botão desativado diz o motivo.
- Quando só resta uma alternativa, o acerto vale no máximo 1 estrela.
- Erro em imprevisto continua sem tirar vida, agora explicado na tela.

**Veto**
- Em 1 de cada 3 partidas, sorteado no início, o Prefeito veta o projeto
  depois da última casa. A Câmara derruba o veto respondendo uma pergunta da
  lista `VETO` (hoje, as perguntas da Prefeitura que falam de veto). O erro
  segue as regras comuns. Na vitória, o certificado mostra “PROMULGADA” e
  “Veto derrubado pela Câmara”.

**Textos**
- Casas com nomes genéricos (Pergunta, Imprevisto, Sorte ou Azar), porque o
  conteúdo de cada uma é sorteado.
- Nova fala da etapa Finanças, válida para qualquer projeto.
- Carta Recesso: “o projeto fica parado, mas o mandato continua correndo”.
- Como jogar com 5 cartões: inclui o mandato, os custos, as formas de
  perder, a vida por etapa, os imprevistos, a consulta e o bônus da Sanção.
- “O Legis só anda”, “Toque em OK”, “7 etapas da tramitação” e “Fonte da
  pergunta” no pop-up.
- A tela final mostra só números simples: estrelas, vidas que sobraram e
  meses restantes. As frações (“15/17 acertos”, “21/21 casas”) saíram,
  porque confundiam.

## Consequências

Simulação de 1.000 partidas por perfil (acertos na 1ª tentativa):

| Acerta de primeira | Vencia (v28) | Vence (v29) |
|---|---|---|
| 70% | 42% | cerca de 98% |
| 50% | 7% | cerca de 76% |
| 35% | 1% | cerca de 37% |

Positivas:

- o público leigo chega ao Plenário e à Sanção na maioria das partidas;
- ninguém perde logo depois de acertar nem por pura sorte;
- o Legis é um personagem só, coerente em todas as telas;
- o veto mostra uma parte real do processo que antes nunca acontecia.

Negativas:

- quem domina o conteúdo vence quase sempre; o desafio para essas pessoas
  passa a ser as estrelas e o cargo final;
- a lista `VETO` depende das perguntas da Prefeitura: ao trocar as
  perguntas, mantenha algumas sobre veto (ou crie uma lista própria).

## Alternativas consideradas

- **60 meses de mandato:** descartada para manter a relação com a
  legislatura real de 4 anos.
- **1 mês por resposta, certa ou errada:** fácil demais (94% de vitórias
  para quem acerta metade) e sem tensão.
- **Erro em imprevisto tirar vida:** descartada; o imprevisto continua sendo
  um momento de aprendizado sem punição de vida.
