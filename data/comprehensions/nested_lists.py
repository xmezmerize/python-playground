# Listas Aninhadas (Nested Lists)

"""
Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamadas de arrays:
- Unidimensionais (Arrays/Vetores);
- Multidimensionais (Matrizes);

Em Python usamos listas dentro de listas para representar
estruturas semelhantes
"""

# ================================================================================================================== #

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3

[[print(valor) for valor in lista] for lista in listas]

# Gerando um tabuleiro/matrix 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valor iniciais
print([['*' for i in range(1, 4)] for i in range(1, 4)])