# ADR-014 — Aviso de privacidade (LGPD) e “Apagar meus dados”

- **Status:** Aceito
- **Data:** 04/11/2026
- **Complementa:** ADR-009

## Contexto

O jogo é usado por estudantes, muitos deles menores de idade, em aparelhos
próprios ou da escola. Pais, escolas e a própria Câmara precisam saber, de
forma clara e visível, o que o jogo faz com dados pessoais. O ADR-009 já
limitou o armazenamento ao mínimo, mas isso não aparecia para o jogador.

A Lei Geral de Proteção de Dados (Lei nº 13.709/2018) pede transparência
sobre o tratamento de dados e garante ao titular o direito de pedir a
eliminação deles.

## Decisão

1. A tela de boas-vindas mostra, junto ao link de instalação, o aviso:

   > Este jogo não coleta nem envia dados pessoais. Só o seu recorde e o seu
   > nome ficam guardados neste aparelho, e você pode apagá-los quando
   > quiser. Respeitamos a LGPD (Lei nº 13.709/2018).

   O aviso aparece também quando o jogo já está instalado.

2. Quando há algo guardado, aparece o botão **Apagar meus dados**. Ele remove
   a chave `jv1` do `localStorage`, zera a caderneta `P` e limpa o nome do
   formulário. Uma frase confirma: “Pronto: os dados deste aparelho foram
   apagados.”

3. O texto diz exatamente o que acontece. Ele **não** afirma que “nada é
   salvo”, porque o recorde e o nome ficam no aparelho.

4. Continua valendo o ADR-009: nenhum dado sai do aparelho; sem analytics,
   cookies de terceiros ou servidor.

## Consequências

Positivas:

- transparência visível para estudantes, pais e escolas;
- o jogador exerce sozinho o direito de eliminação, sem precisar pedir a
  ninguém;
- em aparelho compartilhado, o próximo aluno não vê o nome do anterior.

Negativas:

- mais um elemento na tela de boas-vindas (texto pequeno, abaixo das
  ações, para não competir com o botão Iniciar).

## Alternativas consideradas

- **Página separada de política de privacidade:** mais completa, mas pouca
  gente abriria; o aviso curto na própria tela é mais eficaz. Uma política
  formal da Câmara pode ser acrescentada depois, com link a partir do aviso.
- **Não guardar nada:** perderia o recorde, que motiva o jogador a voltar.
- **Afirmar que “não salva dados”:** seria impreciso e contrário à LGPD.
