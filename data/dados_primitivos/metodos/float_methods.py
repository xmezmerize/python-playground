# Métodos e Funções para float

# =================================================================================================================== #

"""
Diferente de str ou list, o float não possui muitos métodos próprios.
A maior parte das operações é feita através de funções built-in ou do módulo math.
"""

# =================================================================================================================== #

# Funções built-in aplicáveis a float
x = -7.85
y = 3.14159

# abs(x) → valor absoluto

print(abs(x))   # 7.85

# round(x) → arredondamento

print(round(y))      # 3
print(round(y, 2))   # 3.14

# int(x) → converte float para inteiro (trunca a parte decimal)

print(int(y))   # 3

# float(x) → garante que o número seja float

print(float(7)) # 7.0

# =================================================================================================================== #

# Representações especiais

# Notação científica

n = 1.2e3
print(n)        # 1200.0


# is_integer() → verifica se o float representa um número inteiro

a = 5.0
b = 5.2
print(a.is_integer())  # True
print(b.is_integer())  # False

# =================================================================================================================== #

# Módulo math — operações matemáticas

import math

print(math.ceil(7.1))   # 8 (arredonda para cima)
print(math.floor(7.9))  # 7 (arredonda para baixo)
print(math.trunc(7.9))  # 7 (descarta decimais)
print(math.sqrt(16))    # 4.0 (raiz quadrada)
print(math.pow(2, 3))   # 8.0 (potência, float)
print(math.pi)          # 3.141592653589793
print(math.e)           # 2.718281828459045

# =================================================================================================================== #

# Módulo decimal — alta precisão

# O tipo float tem limitações de precisão. Para cálculos financeiros ou científicos, usamos Decimal.

from decimal import Decimal, getcontext

getcontext().prec = 6  # define precisão global
a = Decimal("0.1")
b = Decimal("0.2")

print(a + b)  # 0.3 (sem os erros do float normal)

# =================================================================================================================== #

# Funções adicionais úteis

"""
max() e min() → maior/menor número entre valores.
sum(lista) → soma de valores em lista.
divmod(a, b) → retorna (quociente, resto) mesmo com floats.
"""

print(max(2.3, 7.1, 4.5))   # 7.1
print(min(-3.5, 0.2))       # -3.5
print(sum([1.5, 2.5, 3.0])) # 7.0
print(divmod(7.5, 2))       # (3.0, 1.5)

# =================================================================================================================== #

# Tratamento de valores especiais (nan e inf)

print(float("inf"))   # infinito positivo
print(float("-inf"))  # infinito negativo
print(float("nan"))   # not a number

# Verificação:

math.isinf(float("inf"))  # True
math.isnan(float("nan"))  # True