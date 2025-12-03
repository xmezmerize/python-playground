# Métodos e Operações do int

# =================================================================================================================== #

# Operações Aritméticas Básicas

# Os inteiros suportam todas as operações matemáticas clássicas:

a = 15
b = 4

print(a + b)   # 19  (adição)
print(a - b)   # 11  (subtração)
print(a * b)   # 60  (multiplicação)
print(a / b)   # 3.75 (divisão normal → float)
print(a // b)  # 3   (divisão inteira)
print(a % b)   # 3   (resto da divisão)
print(a ** b)  # 50625 (potenciação)

# =================================================================================================================== #

# Comparações

# Os inteiros podem ser comparados com os operadores relacionais:

print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a <= b)  # False

# =================================================================================================================== #

# Conversão

# int(x) → converte valores de outros tipos para inteiro (quando possível).

print(int("42"))   # 42
print(int(9.8))    # 9 (trunca)
print(int(True))   # 1
print(int(False))  # 0

# =================================================================================================================== #

# Métodos Especiais (Dunder Methods)

# Esses métodos internos são atalhos para operadores.

# Exemplo com a = 5, b = 3:

a.__add__(b)   # 8  → equivale a (a + b)
a.__sub__(b)   # 2  → (a - b)
a.__mul__(b)   # 15 → (a * b)
a.__floordiv__(b) # 1 → (a // b)
a.__mod__(b)   # 2  → (a % b)
a.__pow__(b)   # 125 → (a ** b)

# Isso mostra que até operações simples como + são na verdade métodos da classe int.

# =================================================================================================================== #

# Métodos Úteis para Representação

# Além da aritmética, o int tem métodos para transformar sua forma de exibição:

num = 255

print(num.bit_length())   # 8 (quantos bits para representar em binário)
print(num.to_bytes(2, 'big'))  # b'\x00\xff' (representação em bytes)
print(num.to_bytes(2, 'little'))  # b'\xff\x00'
print(int.from_bytes(b'\x00\xff', 'big'))  # 255 (volta para int)

# =================================================================================================================== #

# Representações em Diferentes Bases

n = 42
print(bin(n))  # '0b101010' (binário)
print(oct(n))  # '0o52' (octal)
print(hex(n))  # '0x2a' (hexadecimal)

# =================================================================================================================== #

# Funções Matemáticas Extras (math)

# O módulo math expande as possibilidades de cálculo com inteiros:

import math

print(math.sqrt(16))     # 4.0 (raiz quadrada)
print(math.factorial(5)) # 120
print(math.gcd(24, 36))  # 12 (máximo divisor comum)
print(math.isqrt(17))    # 4 (raiz quadrada inteira)

# Vamos explorar mais sobre libs adiante!