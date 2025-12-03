# Tipo Booleano (bool)

# =================================================================================================================== #

# Definição

"""
Criado a partir da Álgebra Booleana de George Boole.
Possui apenas dois valores possíveis:

True → Verdadeiro
False → Falso

Sempre iniciam com letra maiúscula.
"""

ativo = True
print(ativo)       # True
print(type(ativo)) # <class 'bool'>

# Errado: true, false → gera erro em Python.

# =================================================================================================================== #

# Conversão para Booleano

# Qualquer valor pode ser convertido em bool:

print(bool(0))     # False
print(bool(1))     # True
print(bool(""))    # False (string vazia)
print(bool("a"))   # True  (string não-vazia)

"""
Regra prática:

Valores vazios/zero → False.
Valores não-vazios/diferentes de zero → True.
"""

# =================================================================================================================== #

#Operadores Lógicos

# Os booleanos são usados principalmente em expressões condicionais.

# Negação (not) -> Inverte o valor lógico:

ativo = False
print(not ativo)  # True

# Ou (or) -> Verdadeiro se pelo menos um for verdadeiro.

print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False

# E (and) -> Verdadeiro somente se ambos forem verdadeiros.

print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

# =================================================================================================================== #

# Tabelas Verdade

# Úteis para visualizar:

"""
NOT

A	    not A
True	False
False	True

OR

A	    B	    A or B
True	True	True
True	False	True
False	True	True
False	False	False

AND

A	    B	    A and B
True	True	True
True	False	False
False	True	False
False	False	False
"""

# =================================================================================================================== #

# Uso em Condições

# Os booleanos são base de estruturas de decisão:

idade = 20
maior = idade >= 18

if maior:
    print("É maior de idade")
else:
    print("É menor de idade")