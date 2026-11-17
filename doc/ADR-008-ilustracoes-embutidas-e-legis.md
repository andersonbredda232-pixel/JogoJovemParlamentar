# ADR-008 — Ilustrações embutidas e o mascote Legis

- **Status:** Aceito; onde o Legis aparece foi atualizado pelo ADR-016
  (um Legis só, sempre de terno)
- **Data:** 29/10/2026

## Contexto

O jogo precisa de um personagem que guie o estudante e de cenários que
mostrem os lugares da tramitação. As imagens precisam funcionar sem internet
e ficar coerentes entre si.

## Decisão

- **Legis** é o mascote oficial: pato amarelo, de terno azul-marinho e gravata
  vermelha. Fica **parado** nas cenas (sem animação de caminhada) e não pode
  ser deformado, duplicado ou recortado.
- As ilustrações ficam embutidas em `index.html` como data URI (webp para as
  cenas, SVG para desenhos vetoriais):
  - `CENA_INICIO`: Legis na tribuna, com as bandeiras do Brasil e de
    Campinas caídas;
  - `GAB_FUNDO` e `GAB_FRENTE`: o gabinete, com bandeiras de mesa e a placa
    fixa “VER. LEGIS”;
  - `FAIXAS`: as 7 faixas ilustradas das etapas;
  - `PATO_TERNO`: o Legis de terno usado nos balões.
- A bandeira de Campinas segue o desenho oficial (escudo azul com a fênix
  amarela).
- As imagens de origem do Legis ficam em `imagens/`, só como referência.
- Pixels transparentes em volta do Legis são preenchidos com a cor vizinha
  antes da compressão, para não surgir contorno preto.

## Consequências

Positivas:

- nenhuma imagem a mais na lista de cache;
- o Legis dá unidade e voz às explicações.

Negativas:

- as imagens aumentam o tamanho do `index.html`;
- trocar uma ilustração exige gerar o data URI de novo.

## Alternativas consideradas

- **Arquivos de imagem separados:** diffs menores, mas mais itens no cache
  e risco de imagem faltando sem internet.
- **Fotos reais da Câmara:** foram usadas antes, mas não combinavam com o
  personagem desenhado.
