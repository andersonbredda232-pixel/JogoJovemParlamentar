# ADR-011 — Regras de acabamento visual

- **Status:** Aceito
- **Data:** 29/10/2026
- **Complementado por:** ADR-013 (botões) e ADR-015 (organização do CSS)

## Contexto

A revisão com a skill de design (*design-taste-frontend*, telas de aplicativo)
encontrou 43 falhas: gradientes, sombras em painéis parados, faixas inteiras
de anil sólido, rótulos em maiúsculas espaçadas e emoji. A interface parecia
genérica e pesada.

## Decisão

Adotar o estilo *accent ladder* (escada de tons) sobre o anil da Câmara:

- anil cheio só em pequenas marcas de ação e estado: botão principal, casas
  concluídas, barras de vidas e mandato;
- tons claros do anil nas áreas: balões, casa atual, chips;
- cartões brancos com borda de 1 px sobre o chão `#f6f6fc`;
- **sem gradientes**;
- **sombra só no que flutua** (pop-up, menus), nunca em painel parado;
- rótulos em caixa normal (*sentence case*), sem maiúsculas espaçadas;
- títulos que cabem na largura com unidades de contêiner, sem estourar;
- rodapé sempre no pé da tela.

Cada tela responde a uma pergunta do jogador, e o maior bloco é a resposta:

| Tela | Pergunta | Ação |
|---|---|---|
| Início | O que é isto e como começo? | Iniciar |
| Gabinete | Quem sou e qual é o meu projeto? | Protocolar |
| Partida | Qual é a pergunta e como respondo? | escolher alternativa |
| Pop-up | Por que errei? | OK |
| Fim | Quanto fui bem e o que revisar? | Novo mandato |

O lint e o inspetor da skill devem terminar sem falhas antes da publicação de
mudanças visuais.

## Consequências

Positivas:

- aparência profissional e coerente com a Câmara;
- regra verificável por ferramenta, não só por gosto.

Negativas:

- propostas visuais externas (por exemplo, blocos de CSS prontos) precisam
  ser adaptadas a estas regras antes de entrar no jogo.

## Alternativas consideradas

- **Bloco “Design Premium V2”:** testado numa cópia; quebrava o layout (ícones
  gigantes, tela inicial ilegível, título do pop-up invisível). Não aplicado.
