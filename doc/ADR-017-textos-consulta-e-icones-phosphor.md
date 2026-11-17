# ADR-017 — Textos mais simples, consulta menor e ícones Phosphor

- **Status:** Aceito
- **Data:** 17/11/2026
- **Substitui em parte:** ADR-007 (desenho dos ícones), ADR-016 (consulta,
  texto do imprevisto e Como jogar) e ADR-005 (consulta)

## Contexto

Ao testar a v29 (17/11/2026), Anderson apontou pontos que confundiam o
público ou pareciam malfeitos:

- o “local” da etapa (“Fachada da Câmara”, “Corredores da Câmara”, “Sala de
  comissão” três vezes) não ensinava nada e se repetia;
- na casa de imprevisto, a palavra “Imprevisto” aparecia duas vezes seguidas
  (no quadro e no balão do Legis);
- o “Como jogar” tinha 5 cartões com textos longos e fundo liso;
- a consulta à Procuradoria escondia duas erradas, o que facilitava demais;
- “Jogo educativo” no topo e no rodapé;
- o link “Instalar o jogo no celular” aparecia também no computador;
- alguns ícones das etapas não comunicavam a ideia (o do Plenário parecia
  uma impressora; Prefeitura e Sanção eram prédios parecidos).

## Decisão

**Etapas.** O texto ao lado de “Etapa X de 7” passa a dizer o que acontece
na etapa: Entrada do projeto, Parecer jurídico, Análise da
constitucionalidade, Análise do mérito, Impacto no orçamento, Votação dos
vereadores e Sanção ou veto (campo `local` de `ETAPAS`).

**Imprevisto.** Um quadro só: “Casa de imprevisto: <nome>”, a situação e
“Aqui, errar não tira vida.” Sem balão do Legis nessa casa (o balão volta
só para avisar das alternativas descartadas ou do mandato zerado).

**Como jogar.** 4 cartões curtos (Leve sua lei até o fim, Acerte para andar,
Estrelas e vidas, O tempo corre), cada um com uma faixa ilustrada de uma
etapa, com o Legis, e o ícone por cima (campo `img` de `COMO_JOGAR`).

**Consulta à Procuradoria.** Esconde **uma** alternativa errada ainda não
tentada. Continua grátis, 3 por partida, uma por pergunta, e só funciona
quando restam pelo menos duas erradas, para nunca entregar a resposta.

**Textos da tela inicial.** “Jogo” no lugar de “Jogo educativo”, no topo e
no rodapé (“Câmara Municipal de Campinas · Jogo”).

**Instalação.** O link “Instalar o jogo no celular” só aparece em celular e
tablet (função `celular()`).

**Ícones.** Todos os ícones passam a ser da biblioteca Phosphor
(phosphoricons.com, licença MIT, em `fontes/LICENSE-Phosphor.txt`), copiados
para dentro do `index.html`, sem carregar nada da internet:

- peso regular; fechar, alerta (!) e certo no peso bold;
- coração das vidas e estrela no peso cheio (fill); a vida perdida fica só
  no contorno;
- etapas: Protocolo = carimbo, Procuradoria = balança, Constituição e
  Legalidade = pergaminho, Comissões Temáticas = grupo de pessoas, Finanças
  e Orçamento = moedas, Plenário = mão levantada, Prefeitura = prédio
  público, Sanção do Prefeito = assinatura.

O formato de uso não mudou: `ICONES` guarda os desenhos e `ico(nome, classe)`
os insere. Os nomes antigos foram mantidos; entraram `carimbo`, `assinatura`
e `celular`, e o objeto `ICONES_CHEIOS` (coração e estrela cheios).

## Consequências

Positivas:

- telas mais limpas, sem textos repetidos, e Como jogar lido em segundos;
- os ícones das etapas comunicam a ideia de cada fase;
- um conjunto de ícones coerente, mantido por uma biblioteca conhecida.

Negativas:

- a consulta ajuda menos: em 2.000 partidas simuladas, quem acerta metade
  das perguntas na tentativa vence cerca de 6 pontos percentuais menos (de
  54% para 48% nesse modelo de simulação);
- ícone novo deve vir da Phosphor (pasta `assets/regular` do pacote
  `@phosphor-icons/core`), copiando só o conteúdo do `<svg>`.

## Alternativas consideradas

- **Lugar real da etapa (Protocolo Geral, Sala das Comissões…):** descartada;
  repetia nas comissões e no Plenário.
- **Pontos extras no imprevisto:** descartada; mudaria a pontuação.
- **Phosphor por CDN:** descartada; o jogo precisa funcionar sem internet.
- **Trocar só os ícones das etapas:** descartada; misturaria dois estilos.

## Pendências registradas

- Bandeira de Campinas e fênix do brasão (na cena inicial): redesenhar a
  partir de uma referência oficial.
