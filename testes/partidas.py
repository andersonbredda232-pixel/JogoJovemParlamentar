"""Joga partidas automáticas do Jovem Parlamentar e confere as regras.

Uso (com o jogo servido em http://localhost:8000):
    python3 testes/partidas.py [quantidade]          # padrão: 30 partidas

O que confere em cada partida:
  - nenhum erro de JavaScript na página;
  - o peão nunca volta e só anda depois de um acerto;
  - o pop-up de erro só fecha pelo botão OK;
  - a partida sempre termina (vitória, sem vidas ou fim do mandato).
O sorteio é fixo por partida (semente), então duas versões do jogo podem
ser comparadas: o resumo impresso deve ser igual se as regras não mudaram.
"""
import sys, json, random, hashlib, os
from playwright.sync_api import sync_playwright

URL = os.environ.get('JOGO_URL', 'http://localhost:8000/index.html')
N = int(sys.argv[1]) if len(sys.argv) > 1 else 30
# sorteio previsível: troca o Math.random do jogo por um gerador com semente
SEMENTE = """(() => { let s = %d; Math.random = () => { s |= 0; s = s + 0x6D2B79F5 | 0;
  let t = Math.imul(s ^ s >>> 15, 1 | s); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
  return ((t ^ t >>> 14) >>> 0) / 4294967296; }; })();"""


def clica(p, sel):
    p.evaluate("s => document.querySelector(s).click()", sel)


def partida(navegador, semente):
    ctx = navegador.new_context(viewport={'width': 1280, 'height': 860}, service_workers='block')
    ctx.add_init_script(SEMENTE % semente)
    p = ctx.new_page()
    erros = []
    p.on('pageerror', lambda e: erros.append(str(e)))
    p.goto(URL)
    sorte = random.Random(semente)
    acerto = [0.55, 0.8, 0.95][semente % 3]  # chance de acertar de primeira
    clica(p, '[data-a=iniciar]')
    clica(p, f'[data-a=trat][data-v="{"ao"[semente % 2]}"]')
    p.evaluate("n => { const e = document.querySelector('#nome'); e.value = n; e.dispatchEvent(new Event('input', {bubbles: true})); }", f'Teste {semente}')
    clica(p, f'[data-a=exemplo][data-v="{semente % 3}"]')
    p.evaluate("() => document.querySelector('#fm').requestSubmit()")
    trilha = []
    for _ in range(900):
        st = p.evaluate('({t: G.tela, f: G.fase, c: !!G.corr, pos: G.pos, m: G.mes, v: G.vidas, e: G.estrelas})')
        if st['t'] == 'fim':
            r = p.evaluate("({vitoria: G.win, estrelas: G.estrelas, acertos: G.acertos, perguntas: G.perguntas, meses: G.mes, vidas: G.vidas, motivo: G.motivo && G.motivo[0], casa: G.pos})")
            r['passos'] = len(trilha)
            r['trilha'] = hashlib.md5(json.dumps(trilha).encode()).hexdigest()[:10]
            r['erros_js'] = erros
            ctx.close()
            return r
        trilha.append(st)
        if st['c']:
            p.keyboard.press('Escape')  # o Esc não pode fechar o pop-up
            assert p.evaluate('!!G.corr'), 'o pop-up fechou sem o OK'
            clica(p, '#okp')
            continue
        if st['f'] == 'q':
            if sorte.random() < 0.12 and p.evaluate('podeConsultar()'):
                clica(p, '[data-a=consultar]')
                continue
            livres = p.evaluate('G.q.ops.filter(i => !G.q.desc.includes(i) && !G.hid.includes(i))')
            escolha = 1 if sorte.random() < acerto else sorte.choice([i for i in livres if i != 1] or [1])
            clica(p, f'#o [data-v="{escolha}"]')
            if escolha != 1:
                assert p.evaluate('G.pos') == st['pos'], 'o peão andou depois de um erro'
            continue
        clica(p, '#app .st > .go')
        assert p.evaluate('G.pos') >= st['pos'], 'o peão voltou'
    raise AssertionError('a partida não terminou')


with sync_playwright() as pw:
    nav = pw.chromium.launch(executable_path=os.environ.get('CHROME') or None)
    res = [partida(nav, s) for s in range(N)]
    nav.close()
for r in res:
    print(json.dumps(r, ensure_ascii=False, sort_keys=True))
erros = sum(len(r['erros_js']) for r in res)
print(f"vitórias: {sum(r['vitoria'] for r in res)} de {len(res)} · erros de JavaScript: {erros}")
sys.exit(1 if erros else 0)
