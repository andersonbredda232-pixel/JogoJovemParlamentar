# Testes automáticos

Dois roteiros em Python que abrem o jogo num navegador sem janela
(Playwright) e conferem se tudo continua funcionando. Use-os antes de
publicar uma versão nova.

## Preparar (uma vez só)

```bash
pip install playwright
python3 -m playwright install chromium
```

## Rodar

Em um terminal, sirva o jogo a partir da pasta dele:

```bash
python3 -m http.server 8000
```

Em outro terminal, na mesma pasta:

```bash
python3 testes/partidas.py      # 30 partidas automáticas
python3 testes/telas.py         # capturas de tela e medida dos botões
```

## O que cada um confere

| Roteiro | Confere |
|---|---|
| `partidas.py` | regras do jogo: o peão nunca volta, só anda com acerto, o pop-up só fecha no OK, toda partida termina, nenhum erro de JavaScript |
| `telas.py` | botões e campos com pelo menos 44 × 44 px, nenhuma rolagem horizontal, nenhum erro de JavaScript; salva capturas em `testes/capturas/` para olhar |

Os dois terminam com código 1 quando encontram problema.

## Comparar duas versões

O sorteio de `partidas.py` usa sementes fixas. Se você mudou só o visual ou
os comentários, rode o roteiro na versão antiga e na nova e compare as
saídas: elas precisam ser iguais.

```bash
python3 testes/partidas.py > antes.txt    # versão antiga
python3 testes/partidas.py > depois.txt   # versão nova
diff antes.txt depois.txt
```

Para usar outro endereço, defina `JOGO_URL`, por exemplo
`JOGO_URL=http://localhost:8080/index.html python3 testes/partidas.py`.
