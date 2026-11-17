# Documentação do Jovem Parlamentar

## Architecture Decision Records (ADRs)

Cada ADR registra uma decisão, o contexto em que foi tomada, suas
consequências e as alternativas descartadas.

| ADR | Decisão | Status |
|---|---|---|
| [ADR-001](ADR-001-arquivo-html-unico-sem-framework.md) | Arquivo HTML único, sem framework nem build | Aceito |
| [ADR-002](ADR-002-pwa-com-cache-versionado.md) | PWA com service worker e cache versionado | Aceito |
| [ADR-003](ADR-003-conteudo-embutido-no-codigo.md) | Conteúdo pedagógico embutido no código | Aceito |
| [ADR-004](ADR-004-instrucao-ramificada-de-crowder.md) | Instrução programada ramificada de Crowder | Aceito |
| [ADR-005](ADR-005-pontuacao-por-estrelas.md) | Pontuação por estrelas e duas formas de perder | Substituído em parte pelos ADRs 016 e 017 |
| [ADR-006](ADR-006-identidade-visual-da-camara.md) | Identidade visual da Câmara | Aceito |
| [ADR-007](ADR-007-icones-svg-em-vez-de-emoji.md) | Ícones SVG em vez de emoji | Substituído em parte pelo ADR-017 |
| [ADR-008](ADR-008-ilustracoes-embutidas-e-legis.md) | Ilustrações embutidas e o mascote Legis | Aceito |
| [ADR-009](ADR-009-armazenamento-local-minimo.md) | Armazenamento local mínimo | Aceito |
| [ADR-010](ADR-010-acessibilidade-e-areas-de-toque.md) | Acessibilidade e áreas de toque | Aceito |
| [ADR-011](ADR-011-regras-de-acabamento-visual.md) | Regras de acabamento visual | Aceito |
| [ADR-012](ADR-012-fontes-normativas.md) | Fontes normativas das perguntas | Aceito |
| [ADR-013](ADR-013-botoes-teclas-de-votacao.md) | Botões no formato de “teclas de votação” | Aceito |
| [ADR-014](ADR-014-privacidade-e-lgpd.md) | Aviso de privacidade (LGPD) e “Apagar meus dados” | Aceito |
| [ADR-015](ADR-015-codigo-enxuto-e-verificacao.md) | Código enxuto, comentado por blocos e verificado por comparação | Aceito |
| [ADR-016](ADR-016-ajustes-de-jogabilidade.md) | Ajustes de jogabilidade para o público leigo | Substituído em parte pelo ADR-017 |
| [ADR-017](ADR-017-textos-consulta-e-icones-phosphor.md) | Textos mais simples, consulta menor e ícones Phosphor | Aceito |

## Como criar um novo ADR

1. Copie [`ADR-000-modelo.md`](ADR-000-modelo.md) com o próximo número livre e
   um nome curto, sem acentos: `ADR-018-salvar-partida.md`.
2. Preencha com status **Proposto**.
3. Depois da aprovação, mude para **Aceito** e acrescente a linha nesta
   tabela.
4. Se ele substituir uma decisão anterior, não apague o ADR antigo: mude o
   status dele para **Substituído por ADR-NNN**.
