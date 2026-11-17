# Contexto de Continuidade — Jovem Parlamentar

**Última atualização:** 17/11/2026
**Finalidade:** dar contexto de transição entre computadores, chats e sessões
de agentes de IA.

## 1. Como utilizar este documento

Este arquivo é um resumo operacional e não substitui a documentação
normativa. Em caso de divergência, prevalecem, nesta ordem:

1. instruções expressas do usuário para a tarefa atual;
2. `AGENTS.md`;
3. ADRs aceitos em `doc/`;
4. `README.md`;
5. código e comentários de `index.html`;
6. este `CONTEXT.md`.

Antes de iniciar uma nova frente de trabalho, atualize este arquivo e confira o
estado do Git. Não registre aqui senhas, tokens ou dados pessoais.

## 2. Objetivo do projeto

Ensinar a estudantes, de forma lúdica, como um projeto de lei tramita na
Câmara Municipal de Campinas, do protocolo à sanção ou ao veto do Prefeito.

Público: estudantes do ensino médio e participantes do programa Jovem
Parlamentar, em sessões curtas, no celular ou no computador da escola.

Responsável: Anderson Bredda, Câmara Municipal de Campinas.

## 3. Publicação

- Repositório: `andersonbredda232-pixel/JogoJovemParlamentar` (público).
  Em 17/11/2026 o GitHub ainda tinha a versão de 22/10 (cache v1), com um
  `index.html` na raiz e outro na pasta `jovem_parlamentar_pwa/`.
- Hospedagem: GitHub Pages.
- Versão atual do cache do service worker: `jovem-parlamentar-v31`.

## 4. Decisões consolidadas

### Arquitetura

- Um único `index.html` com tudo embutido, sem framework nem build (ADR-001).
- PWA com service worker *stale-while-revalidate* e cache versionado (ADR-002).
- Conteúdo em constantes JavaScript comentadas (ADR-003).
- `localStorage` só para recorde, leis e nome, na chave `jv1`
  (ADR-009).

### Pedagogia

- Instrução programada ramificada de Norman Crowder (ADR-004): cada
  alternativa errada tem comentário próprio; o pop-up de erro só fecha no
  botão OK; o jogador tenta de novo a mesma pergunta, com a errada riscada; o
  peão só anda com acerto.
- Perguntas baseadas no RI e na LOM, sempre com o artigo citado (ADR-012).
- Ao final, a tela “Para rever” lista as perguntas erradas, a resposta certa e
  as alternativas descartadas.

### Regras do jogo (ADR-005, ADR-016 e ADR-017)

- 5 vidas; mandato de 48 meses; acerto gasta 1 mês e erro, 2.
- Estrelas por tentativa: 3, 2, 1 e depois 0; no máximo 1 se só restava uma
  alternativa.
- O primeiro erro de uma pergunta custa 1 vida; erro em imprevisto não tira
  vida (só meses). A cada etapa nova, +1 vida (até 5).
- 3 consultas grátis à Procuradoria; cada uma esconde uma errada.
- Veto em 1 de cada 3 partidas, derrubado com uma pergunta da lista `VETO`.
- Bônus na Sanção: +1 estrela por vida restante.
- Só duas derrotas: sem vidas ou errar com o mandato zerado. Acertos e
  cartas nunca encerram a partida.
- Cargos por estrelas: 0, 8, 18, 30, 42 e 52.

### Conteúdo atual

- 7 etapas: Protocolo, Procuradoria, Constituição e Legalidade, Comissões
  Temáticas, Finanças e Orçamento, Plenário e Prefeitura.
- 21 casas: perguntas, 3 imprevistos e 4 cartas de Sorte ou Azar.
- 76 perguntas de etapa (10 a 14 por etapa) e 20 perguntas de imprevisto,
  em 8 eventos, num total de 96.
- 10 cartas de Sorte ou Azar.

### Identidade visual

- Anil oficial `#323380`; chão `#f6f6fc`; amarelo de foco `#f2c300` (ADR-006).
- Bebas Neue (títulos) e Montserrat (texto), locais, sob OFL.
- Ícones da biblioteca Phosphor (MIT), embutidos, no lugar de emoji
  (ADR-007 e ADR-017). Etapas: carimbo, balança, pergaminho, grupo, moedas,
  mão levantada, prédio público e assinatura.
- Legis: pato amarelo de terno azul-marinho e gravata vermelha, parado nas
  cenas; ilustrações embutidas como data URI (ADR-008).
- Tela inicial com a cena do Legis na tribuna e as bandeiras do Brasil e de
  Campinas caídas.
- Gabinete com a placa fixa “VER. LEGIS” e bandeiras de mesa.
- Faixas ilustradas para as 7 etapas.
- Acabamento *accent ladder*: sem gradientes, sombra só no que flutua, rótulos
  em caixa normal (ADR-011).
- Botões no formato de “teclas de votação”, com letras A–D nas alternativas e
  foco amarelo (ADR-013).
- Aviso de privacidade (LGPD) e botão “Apagar meus dados” na tela inicial
  (ADR-014).
- No celular, logotipo da Câmara à esquerda e botão Início à direita.

### Acessibilidade (ADR-010)

- Alvos de toque de pelo menos 44 px; foco visível; contraste mínimo 4,5:1.
- Teclado do celular é fechado antes de rolar até o palco.

## 5. Trabalho concluído

- Correção da pontuação e simplificação das regras.
- Tela de boas-vindas com Iniciar acima de Como jogar e link discreto de
  instalação do PWA.
- Pop-up de erro com botão OK e comentário de Crowder; correção do
  travamento no celular.
- Imprevistos de Comissão e de Emenda acrescentados.
- Identidade visual da Câmara, Legis e cenas ilustradas.
- Revisão com a skill de design: lint de 43 falhas para 0.
- Correções de celular: nome do projeto cortado, faixa preta no rodapé e
  borrões pretos em volta do Legis.
- Documentação: `README.md`, `AGENTS.md`, `CONTEXT.md`, `LICENSE` e ADRs 001
  a 015.
- Revisão completa de 03–04/11/2026 (ADR-015):
  - CSS de 76 KB e 3.050 linhas para 44 KB e 2.100 linhas, uma camada só,
    organizado por tela, com variáveis em português;
  - motor reescrito em 8 blocos comentados, sem código morto (fotos de
    cenário vazias, cena antiga da tribuna, ramos de “voltar casa”);
  - motor de 60 KB para 38 KB; Legis dos balões recomprimido (−5 KB);
  - `index.html` de 460 KB e 4.770 linhas para 350 KB e 3.270 linhas;
  - comparação automática: 285 capturas idênticas, estilos calculados iguais
    e 30 partidas com resultado idêntico ao da versão anterior;
  - pente fino dos botões aplicado (ADR-013) e aviso de LGPD (ADR-014);
  - testes automáticos em `testes/`;
  - 40 perguntas de cidadania em `conteudo-extra/` (JS e planilha).

- Ajustes de jogabilidade de 13/11/2026 (ADR-016), decididos por Anderson
  a partir da revisão lenta de 09/11: Legis único de terno, escolha
  obrigatória de Vereadora/Vereador, acerto nunca faz perder, cartas não
  encerram a partida, +1 vida por etapa, acerto 1 mês e erro 2, consulta
  grátis com motivo, 1 estrela quando só resta uma alternativa, veto em 1
  de cada 3 partidas, casas com nomes genéricos, Como jogar com 5 cartões e
  textos corrigidos.
- Revisão de 17/11/2026 (ADR-017), pedida por Anderson: tela final só com
  estrelas, vidas e meses (sem frações); texto da etapa diz o que acontece
  nela; imprevisto com um quadro só; Como jogar com 4 cartões curtos e
  ilustrados; consulta esconde uma errada; “Jogo” no lugar de “Jogo
  educativo”; link de instalação só no celular; ícones Phosphor.
- Bandeira de Campinas na mesa do gabinete redesenhada (texto inteiro,
  “SÃO PAULO”, escudo e fênix) e brasão entalhado da tribuna refeito a
  partir do brasão oficial, com “DE CAMPINAS” corrigido (v31, ADR-017).

## 6. Pendências


- **80 perguntas:** definir se a meta conta só perguntas de etapa (hoje 76)
  ou também as de imprevisto (hoje 96).
- **Novas perguntas:** Anderson vai trocar as perguntas do jogo. As 40
  perguntas de cidadania (`conteudo-extra/`) precisam ter os artigos
  conferidos no texto oficial antes de entrar no jogo.
- **Planilha de revisão pedagógica:** exportar as perguntas atuais do jogo
  para planilha (as de cidadania já têm a sua).
- **Leis de UX:** salvar a partida em andamento; revisão ao fim de cada etapa.
- **Perguntas novas:** o comentário de cada errada não pode entregar a
  resposta certa (hoje cerca de 45 das 96 entregam), e o texto não deve
  supor o tema do projeto do jogador (“Seu projeto trata de saúde…”).
  Manter perguntas sobre veto, usadas pela lista `VETO`.
