# Lista de Exercícios — Tipo Booleano (bool)

--- 

> 1. Valores lógicos simples

Crie variáveis com os valores True e False.

- Exiba o tipo de cada uma.
- Converta para inteiro (int(True), int(False)).
- Some dois True e veja o resultado.

---

> 2. Conversão para bool

Converta para booleano usando bool():

- O número 0.
- O número -5.
- A string "".
- A string "Python".

Explique os resultados.

---

> 3. Negação

Dado ativo = False, use not para inverter o valor.
Exiba o resultado antes e depois.

---

> 4. Tabelas verdade

Implemente em código as tabelas verdade de not, or e and.
Exiba cada resultado no formato:

    A   B   A and B   A or B   not A

> 5. Expressões compostas

Avalie e explique o resultado das expressões:

    True or False and False
    not True or True
    (False and True) or (not False)

---

> 6. Operadores aritméticos com bool

Mostre o resultado de:

    True + False
    True * 10
    False * 100
    sum([True, True, False, True])

---

> 7. Verificação de idade

- Crie uma variável idade = 20.
- Crie uma variável maior = idade >= 18.
- Exiba True se for maior de idade, senão False.

---

> 8. Login simples

Dados:

    usuario_cadastrado = "admin"
    senha_cadastrada = "1234"

    usuario_digitado = "admin"
    senha_digitada = "1234"


- Verifique com and se o login é válido.
- Teste mudando senha ou usuário para valores errados.

> 9. Sistema de acesso

Dado:

    ativo = True
    admin = False

Mostre a mensagem:

- "Acesso permitido" se o usuário estiver ativo e for admin.

- "Acesso negado" caso contrário.

---

> 10. Validação de formulário

Um formulário é válido se:

- O nome não está vazio,
- A idade é maior que 0.

Teste com:

    nome = "Pedro"
    idade = 25

e depois altere para valores inválidos.

---

> 11. Filtro de lista com bool

Dada a lista:

    numeros = [0, 1, 2, 3, 4, 5, 6]

- Use uma list comprehension para gerar apenas os números pares (n % 2 == 0).
- Use outra para gerar apenas os ímpares.

---

> 12. Verificação de senha forte

Uma senha é considerada forte se:

- Tem pelo menos 8 caracteres,
- Contém pelo menos 1 número.

Teste com:

    "Python123"
    "senha"

---

> 13. Any e All

Dada a lista:

    checks = [True, True, False, True]

- Use any() para verificar se pelo menos um é verdadeiro.
- Use all() para verificar se todos são verdadeiros.

---

> 14. Controle de acesso em empresa

Um funcionário só pode entrar no prédio se:

- Estiver ativo (ativo = True),
- Não estiver suspenso (suspenso = False),
- For admin ou tiver crachá válido (admin or cracha_valido).

Monte diferentes cenários e teste os resultados.

---

> 15. Validação de CPF simplificada

Um CPF digitado é válido se:

- Tem 11 caracteres,
- Todos os caracteres são dígitos.

Use:

    cpf = "12345678901"   # válido
    cpf = "1234abc8901"   # inválido