# Tipo ponto flutuante (Float)

# =================================================================================================================== #

"""
O que é um float?

- Representa números reais em ponto flutuante (decimal).
- Usa ponto (.) como separador decimal (não vírgula).
- Aproximação: nem sempre é exato, porque os computadores 
armazenam floats em binário, o que pode gerar arredondamentos.
"""

# =================================================================================================================== #

# Exemplo:

a = 1.44
print(a)         # 1.44
print(type(a))   # <class 'float'>

# =================================================================================================================== #

# Diferença entre vírgula e ponto

# Se usar vírgula, o Python entende como tupla:
x = 1, 44
print(x)        # (1, 44)
print(type(x))  # <class 'tuple'>

# Com ponto, é float:
y = 1.44
print(y)        # 1.44
print(type(y))  # <class 'float'>

# =================================================================================================================== #

# Dupla atribuição

# É possível atribuir vários valores em uma linha:

valor1, valor2 = 1, 44
print(valor1)  # 1 (int)
print(valor2)  # 44 (int)

# Aqui não é float: são dois inteiros atribuídos ao mesmo tempo.

# =================================================================================================================== #

# Conversão de tipos

# De float → int: trunca (descarta a parte decimal).
num = 1.99
print(int(num))   # 1

# De string → float:
print(float("3.14"))  # 3.14

# De int → float:
print(float(7))   # 7.0

# =================================================================================================================== #

# Precisão e arredondamento

# Devido ao armazenamento binário, alguns cálculos podem parecer "estranhos":

print(0.1 + 0.2)   # 0.30000000000000004

# Para lidar com isso:

# round(x, n) → arredonda para n casas decimais.
# decimal.Decimal → módulo para alta precisão.

# =================================================================================================================== #

# Operações básicas

a = 5.5
b = 2.0

print(a + b)  # 7.5
print(a - b)  # 3.5
print(a * b)  # 11.0
print(a / b)  # 2.75
print(a ** b) # 30.25

# =================================================================================================================== #

# Números complexos

# Em Python, j representa a unidade imaginária:

z = 5j
print(z)          # 5j
print(type(z))    # <class 'complex'>

# Um número complexo pode ser escrito como a + bj, onde a é a parte real e b a parte imaginária.

# =================================================================================================================== #

# Características importantes

"""
Sempre usa ponto como separador decimal.
Pode representar valores muito grandes ou muito pequenos usando notação científica:
"""

n = 1.5e3   # 1.5 × 10³ = 1500.0
m = 2.5e-4  # 2.5 × 10⁻⁴ = 0.00025

# É imutável: uma vez criado, não muda, só gera novos objetos.