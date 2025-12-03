# Métodos e usos de bool

# =================================================================================================================== #

# Como números (int)

print(int(True))   # 1
print(int(False))  # 0
print(True + True) # 2
print(True * 10)   # 10

# Ou seja, qualquer método/operador que funcione com int, também funciona com bool:

print(True.__add__(False))  # 1
print(True.__mul__(5))      # 5

# =================================================================================================================== #

# Funções built-in aplicáveis

"""
bool(x) → conversão para booleano.
abs(True) → 1
abs(False) → 0
sum([True, False, True]) → 2 (conta quantos True existem).
any(lista) → retorna True se algum elemento for verdadeiro.
all(lista) → retorna True se todos forem verdadeiros.
"""

# Exemplo:

valores = [True, False, True]
print(any(valores))  # True
print(all(valores))  # False

# =================================================================================================================== #

# Métodos herdados (internos — dunder methods)

# Por ser um subtipo de int, bool possui métodos especiais:

print(True.__and__(True))   # True  (equivale a True and True)
print(True.__or__(False))   # True  (equivale a True or False)
print(True.__xor__(True))   # False (XOR: exclusivo)

# Isso mostra que até and, or, xor são implementados como métodos internos.

# =================================================================================================================== #

# Comparações

# Como bool é int, dá pra comparar diretamente:

print(True > False)   # True
print(False < True)   # True
print(True == 1)      # True
print(False == 0)     # True