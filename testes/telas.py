"""Tira capturas das telas principais e mede os alvos de toque.

Uso (com o jogo servido em http://localhost:8000):
    python3 testes/telas.py

Gera testes/capturas/<tela>_<largura>.png em 390 px (celular) e 1440 px
(computador) e lista:
  - botões e campos com menos de 44 × 44 px (ADR-010);
  - rolagem horizontal (a página não pode passar da largura da tela);
  - erros de JavaScript.
Termina com código 1 se encontrar algum problema.
"""
import os, sys
from playwright.sync_api import sync_playwright

URL = os.environ.get('JOGO_URL', 'http://localhost:8000/index.html')
PASTA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'capturas')
os.makedirs(PASTA, exist_ok=True)

MEDE = """() => [...document.querySelectorAll('#app button, #app input, #app textarea, #mn')]
  .filter(e => e.offsetParent && getComputedStyle(e).visibility != 'hidden')
  .map(e => { const r = e.getBoundingClientRect(); return [e.textContent.trim().slice(0, 30) || e.id, Math.round(r.width), Math.round(r.height)]; })
  .filter(([, w, h]) => w < 44 || h < 44)"""


def clica(p, sel):
    p.evaluate("s => document.querySelector(s).click()", sel)
    p.wait_for_timeout(350)


def telas(p):
    """Percorre o jogo e devolve (nome, função que leva até a tela)."""
    yield 'inicio', lambda: None
    yield 'como_jogar', lambda: clica(p, '[data-a=como]')
    yield 'gabinete', lambda: clica(p, '[data-a=iniciar]')

    def protocolar():
        clica(p, '[data-a=trat][data-v="a"]')
        p.evaluate("() => { const e = document.querySelector('#nome'); e.value = 'Ana Teste'; e.dispatchEvent(new Event('input', {bubbles: true})); }")
        clica(p, '[data-a=exemplo][data-v="0"]')
        p.evaluate("() => document.querySelector('#fm').requestSubmit()")
        p.wait_for_timeout(350)
    yield 'etapa', protocolar
    yield 'pergunta', lambda: clica(p, '[data-a=abrir]')
    yield 'popup_erro', lambda: clica(p, '#o [data-v="2"]')
    yield 'riscada', lambda: clica(p, '#okp')
    yield 'acerto', lambda: clica(p, '#o [data-v="1"]')

    def ate_o_fim():
        for _ in range(300):
            if p.evaluate("G.tela == 'fim'"):
                break
            if p.evaluate("G.fase == 'q'"):
                clica(p, '#o [data-v="1"]')
            else:
                clica(p, '#app .st > .go')
    yield 'tela_final', ate_o_fim


problemas = 0
with sync_playwright() as pw:
    nav = pw.chromium.launch(executable_path=os.environ.get('CHROME') or None)
    for largura, altura, celular in ((390, 844, True), (1440, 900, False)):
        ctx = nav.new_context(viewport={'width': largura, 'height': altura}, is_mobile=celular, has_touch=celular, service_workers='block')
        p = ctx.new_page()
        erros = []
        p.on('pageerror', lambda e: erros.append(str(e)))
        p.goto(URL)
        p.evaluate('localStorage.clear()')
        p.reload()
        p.wait_for_timeout(500)
        for nome, ir in telas(p):
            ir()
            p.screenshot(path=f'{PASTA}/{nome}_{largura}.png', full_page=True)
            pequenos = p.evaluate(MEDE)
            larga = p.evaluate('document.documentElement.scrollWidth > innerWidth')
            for x in pequenos:
                print(f'  {nome} {largura}px: alvo pequeno {x}')
            if larga:
                print(f'  {nome} {largura}px: rolagem horizontal!')
            problemas += len(pequenos) + int(larga)
        for e in erros:
            print(f'  erro de JavaScript ({largura}px): {e}')
        problemas += len(erros)
        ctx.close()
    nav.close()
print(f'capturas em {PASTA} · problemas: {problemas}')
sys.exit(1 if problemas else 0)
