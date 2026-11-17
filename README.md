# Jovem Parlamentar

Jogo sobre o processo legislativo da Câmara Municipal de Campinas, para
ensinar estudantes como uma lei é feita.

O jogador assume um mandato de vereador ou vereadora, protocola um projeto de
lei e o acompanha pelas sete etapas da tramitação, do Protocolo à Sanção do
Prefeito, respondendo a perguntas baseadas no Regimento Interno e na Lei
Orgânica do Município. O mascote **Legis** guia o percurso.

O jogo é um aplicativo web progressivo (PWA): abre no navegador, funciona sem
internet depois da primeira visita e pode ser instalado no celular ou no
computador. Não coleta nem envia dados pessoais (veja [Privacidade](#privacidade-e-lgpd)).

## Estrutura do repositório

```text
jovem_parlamentar_pwa/
├── AGENTS.md                instruções permanentes para agentes de IA
├── CONTEXT.md               contexto de continuidade entre sessões
├── LICENSE                  licença do projeto
├── README.md                este arquivo
├── index.html               o jogo inteiro: estilos, conteúdo, motor e imagens
├── sw.js                    service worker (funcionamento sem internet)
├── manifest.webmanifest     dados de instalação do PWA
├── icon-*.png, apple-touch-icon.png, favicon-32.png
├── fontes/                  Bebas Neue e Montserrat (woff2) e licenças (OFL e Phosphor)
├── imagens/                 desenhos originais do Legis (referência; o jogo não os carrega)
├── conteudo-extra/          perguntas de cidadania, prontas para colar no jogo
├── testes/                  testes automáticos (Python + Playwright)
└── doc/                     ADRs (decisões do projeto)
```

## Documentação de referência

Antes de alterar o jogo, consulte, nesta ordem:

1. `AGENTS.md`;
2. os ADRs em `doc/` (lista em [`doc/README.md`](doc/README.md));
3. este `README.md`;
4. `CONTEXT.md`.

## Tecnologias

- HTML, CSS e JavaScript nativos, em um único arquivo, sem framework e sem
  etapa de build;
- Service Worker e Web App Manifest;
- `localStorage` só para recorde, leis sancionadas e último nome;
- fontes locais em woff2;
- GitHub Pages para a publicação.

## Como o `index.html` está organizado

O arquivo é dividido em seis partes, cada uma com um título em MAIÚSCULAS e
um comentário que explica o que ela faz:

| Parte | O que tem | Quando mexer |
|---|---|---|
| 1. ESTILOS | aparência de todas as telas, em blocos por tela; as cores ficam no bloco **CORES, FONTES E MEDIDAS** no topo | para mudar o visual |
| 2. PÁGINA | cabeçalho com o logo, área `#app` e rodapé | raramente |
| 3. CONTEÚDO | etapas, casas, perguntas, imprevistos, cartas, cargos, regras e textos | **para mudar o conteúdo** |
| 4. MOTOR | regras, telas e botões, em 8 blocos numerados | para mudar o funcionamento |
| 5. IMAGENS | Legis, cenas, faixas das etapas, ícones e logo | não editar à mão |
| 6. APLICATIVO | registra o `sw.js` | não editar |

## Executar localmente

O service worker só funciona por HTTP, não abrindo o arquivo com duplo clique.
A partir da pasta do jogo:

```bash
python3 -m http.server 8000
```

Abra `http://localhost:8000/`. Para testar sem o cache do service worker, use
uma janela anônima ou, nas ferramentas do desenvolvedor, **Application →
Service Workers → Unregister**.

## Publicar no GitHub Pages

1. Rode os testes (veja abaixo).
2. Aumente a versão do cache em `sw.js` (`v31` → `v32`).
3. Faça o commit em `main` e envie com `git push`.
4. Em **Settings → Pages**, a origem deve ser a branch `main` e a pasta onde
   está `index.html`.
5. Aguarde a publicação. Quem já tinha o jogo recebe a versão nova na
   abertura seguinte.

### Versão do cache (obrigatório a cada publicação)

```js
const CACHE = 'jovem-parlamentar-v31';
```

Sempre que qualquer arquivo publicado mudar, troque o número. Sem isso,
aparelhos que já abriram o jogo continuam com a versão antiga. Se um arquivo
novo precisar funcionar sem internet, inclua-o também na lista `FILES`.

## Como editar o conteúdo

Todo o conteúdo fica na parte **3. CONTEÚDO** do `index.html`. Cada lista tem,
acima dela, um comentário com os campos.

| Lista | O que guarda |
|---|---|
| `ETAPAS` | as 7 etapas da tramitação, com nome, ícone, o que acontece nela (`local`) e fala do Legis |
| `CASAS` | as 21 casas do tabuleiro (pergunta, imprevisto ou carta) |
| `Q` | o banco de perguntas, uma lista por etapa |
| `EVENTOS` | os imprevistos sorteados e suas perguntas |
| `CARTAS` | as cartas de Sorte ou Azar |
| `CARGOS` | os cargos alcançados conforme as estrelas |
| `REGRAS` | vidas, meses de mandato, custos e estrelas por tentativa |
| `VETO` | perguntas usadas quando o Prefeito veta |
| `COMO_JOGAR` | os 4 cartões da tela Como jogar (ícone, faixa ilustrada, título e texto) |
| `EXEMPLOS` | sugestões de nome de projeto |

### Trocar ou acrescentar um ícone

Os ícones ficam em `ICONES`, na parte 5. IMAGENS, e são da biblioteca
Phosphor (peso regular). Para trocar um, copie de phosphoricons.com (ou do
pacote `@phosphor-icons/core`, pasta `assets/regular`) só o conteúdo de
dentro do `<svg>` e cole no lugar do desenho antigo. Use o nome da chave no
campo `ic` das listas ou em `ico('nome')`.

### Acrescentar uma pergunta

Cada pergunta é uma lista de 10 textos:

| Posição | Conteúdo |
|---|---|
| 0 | enunciado |
| 1 | resposta **certa** |
| 2, 3, 4 | alternativas erradas |
| 5 | explicação mostrada depois do acerto |
| 6 | fonte legal (por exemplo, `RI, art. 128, VI`) |
| 7, 8, 9 | comentário de cada errada (posições 2, 3 e 4), mostrado no pop-up |

Copie uma linha existente da etapa, cole logo abaixo e troque os textos. O
jogo embaralha as alternativas; a certa é sempre a da posição 1. Mantenha pelo
menos seis perguntas por etapa e cite o artigo. Veja o
[ADR-003](doc/ADR-003-conteudo-embutido-no-codigo.md) e o
[ADR-004](doc/ADR-004-instrucao-ramificada-de-crowder.md).

### Perguntas de cidadania

A pasta `conteudo-extra/` tem 40 perguntas sobre cidadania (quem faz qual lei,
para que servem os órgãos públicos, direitos, participação), no mesmo formato:

- `perguntas_cidadania.js`: pronto para copiar e colar em `Q`;
- `perguntas_cidadania.xlsx`: a mesma lista em planilha, para revisão.

Os artigos foram citados de memória: confira cada fonte no texto oficial
antes de publicar.

### Conferir depois de editar

- abra o jogo e jogue até a parte alterada;
- erre de propósito para ver o comentário de cada alternativa;
- confira o console do navegador (F12): não pode haver erro;
- rode `python3 testes/partidas.py`;
- aumente a versão do cache antes de publicar.

## Testes

A pasta [`testes/`](testes/README.md) tem dois roteiros:

```bash
python3 testes/partidas.py   # 30 partidas automáticas: regras e erros de JavaScript
python3 testes/telas.py      # capturas de tela, botões de 44 px e rolagem horizontal
```

## Regras do jogo (resumo)

- 5 vidas e um mandato de 48 meses (a legislatura real dura 4 anos);
- cada acerto gasta 1 mês e cada erro, 2;
- acerto na 1ª tentativa vale 3 estrelas, na 2ª vale 2, na 3ª vale 1;
  se só restava uma alternativa, vale no máximo 1;
- o primeiro erro de uma pergunta custa 1 vida (nos imprevistos, não), e o
  jogador tenta de novo a mesma pergunta, com a errada riscada;
- a cada etapa nova, o jogador recupera 1 vida;
- 3 consultas grátis à Procuradoria; cada uma esconde uma alternativa errada;
- em 1 de cada 3 partidas o Prefeito veta, e a Câmara derruba o veto
  respondendo uma pergunta;
- na Sanção, cada vida restante vale +1 estrela;
- só há duas formas de perder: ficar sem vidas ou errar com o mandato zerado.
  Acertos e cartas nunca encerram a partida.

Detalhes no [ADR-005](doc/ADR-005-pontuacao-por-estrelas.md), no
[ADR-016](doc/ADR-016-ajustes-de-jogabilidade.md) e no
[ADR-017](doc/ADR-017-textos-consulta-e-icones-phosphor.md).

## Privacidade e LGPD

O jogo não coleta nem envia dados pessoais. Só o recorde de estrelas, as leis
sancionadas e o último nome digitado ficam guardados **no próprio aparelho**
(`localStorage`, chave `jv1`). A tela inicial mostra esse aviso e o botão
**Apagar meus dados**. Não há analytics, cookies de terceiros nem servidor.
Veja o [ADR-009](doc/ADR-009-armazenamento-local-minimo.md) e o
[ADR-014](doc/ADR-014-privacidade-e-lgpd.md).

## Fontes normativas

- **RI**: Regimento Interno da Câmara Municipal de Campinas (Resolução
  nº 842/2009, texto compilado até a Resolução nº 1.028/2025);
- **LOM**: Lei Orgânica do Município de Campinas.

## Licenças de terceiros

As fontes Bebas Neue e Montserrat são distribuídas sob a SIL Open Font License
1.1. Os ícones são da biblioteca [Phosphor](https://phosphoricons.com),
sob licença MIT, copiados para dentro do `index.html`. Os textos das licenças
estão em `fontes/`.
