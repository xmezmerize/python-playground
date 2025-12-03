# List Comprehension

# ================================================================================================================== #

"""
Utilizando List Comprehension, podemos gerar novas
listas com dados processados a partir de outro iterável.

Para entender o que está acontecendo devemos dividir a expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10
"""

# ================================================================================================================== #

# Sintaxe -> [ dado for dado in iterável ]

# Exemplos

numeros = [1, 2, 3, 4, 5]

# 1 -> multiplica cada número da lista por 10
res = [numero * 10 for numero in numeros] 
print(res)

# 2 -> divide cada número da lista por 2
res = [numero / 2 for numero in numeros] 
print(res)

# 3 -> multiplica cada número da lista, por ele mesmo
def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros ] 
print(res)

# ================================================================================================================== #

# List Comprehension x Loop

# Loop
numeros_dobrados = []

for numero in [1, 2, 3, 4, 5]:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in [1, 2, 3, 4, 5]])

# ================================================================================================================== #

# Mais exemplos

# 1 -> coloca todas as letras do nome em maiúscula, separadas como lista
nome = 'Pedro Henrique'

print([letra.upper() for letra in nome])

# 2 -> coloca a primeira letra de cada nome em maiúscula
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([caixa_alta(amigo) for amigo in amigos])

# 3 -> multiplica por 3 cada número de 1 a 10
print([numero * 3 for numero in range(1, 11)])

# 4 -> verifica se cada elemento da lista é verdadeiro ou falso
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5 -> transforma todos os elementos da lista em string
print([str(numero) for numero in [1, 2, 3, 4, 5]])

# ================================================================================================================== #

# Podemos adicionar estruturas condicionais lógicas às nossas List Comprehension

# Exemplos

numeros = [1, 2, 3, 4, 5, 6]

# 1 -> Verifica quais números da lista são ímpares e quais são pares
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# 2 -> Refatorar

# Qualquer número par módulo de 2 é 0 e 0 em Python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]

# Qualquer número ímpar módulo de 2 é 1, e 1 em Python é True
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# 3 -> divide cada número da lista cujo o índice é ímpar por 2 e multiplica os pares por 2
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)