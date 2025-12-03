# Exercícios — Tipo None

> 1. Inicialização de variável

- Crie uma variável resultado = None.
- Mostre seu valor e tipo.
- Depois atribua o valor 42 a ela e exiba novamente.

---

> 2. Checagem de valor

Dado:

x = None
y = 10

- Verifique com is None se x está vazio.
- Verifique com is not None se y já recebeu um valor.

---

> 3. Função sem retorno

- Crie uma função que apenas imprime "Olá, mundo!" sem usar return.
- Mostre o que aparece ao fazer print(funcao()).
- Explique por que o resultado é None.

---

> 4. Lista com espaços vazios

Crie uma lista de tamanho 5 inicializada só com None:

    valores = [None] * 5

- Substitua os elementos de índice par por seus próprios índices (0, 2, 4).
- Exiba a lista final.

---

> 5. Filtro de valores

Dada a lista:

     dados = [10, None, 20, None, 30]

- Gere uma nova lista contendo apenas os elementos que não são None.

Dica: use list comprehension com is not None.

---

> 6. Retorno condicional

Implemente uma função que recebe uma lista de números e retorna:

- A média dos valores, se a lista não estiver vazia.
- None, caso a lista esteja vazia.
- Teste com [] e [5, 10, 15].

---

> 7. Comparação com False

Verifique a diferença entre:

    print(None == False)
    print(None is False)
    print(bool(None))

- Explique por que os três casos dão resultados diferentes.