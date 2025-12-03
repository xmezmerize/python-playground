# Estruturas Lógicas: and (e), or (ou), not (não), is (é)

"""
Na matemática, implica-se nos estudos de lógica.

Estruturas lógicas servem para combinar ou inverter condições em expressões 
booleanas (True/False).

Onde são usadas?

- Controle de fluxo → em if, while, for (com if dentro).
- Validação de regras de negócio → ex: só libera saque se saldo > 0 e cliente ativo.
- Segurança e autenticação → usuário precisa estar logado ou ser administrador.
- Filtros e pesquisas → ex: encontrar itens que não sejam vazios.
- Comparações de objetos → verificar se duas variáveis são o mesmo objeto na memória.

Características de cada operador:

1. and (e)

-Binário (compara 2 lados).
- Retorna True se ambos os lados forem verdadeiros.
- Se o primeiro for False, nem olha o segundo (curto-circuito).

2. or (ou)

- Binário.
- Retorna True se pelo menos um dos lados for verdadeiro.
- Se o primeiro já for True, ignora o segundo (curto-circuito).

3. not (não)

- Unário (atua sobre um único valor).
- Inverte o valor booleano.

4. is (é)

- Binário.
- Verifica identidade do objeto, não só valor.

Outras características importantes:

- Curto-circuito: and e or param a avaliação cedo quando já sabem o resultado.
- Truthiness: não só True/False contam — listas vazias, 0, strings vazias,
None também são tratados como False.
- Legibilidade: em Python, boas práticas recomendam escrever expressões simples
e claras, sem exagerar em combinações muito grandes.
"""
ativo = True
logado = False

if ativo:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')


# ativo é verdadeiro?
print(ativo is True)
print(logado is True)
print(logado is not True)