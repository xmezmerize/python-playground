from math import pow, sqrt, floor, ceil
from fractions import Fraction
from numpy import polyadd, polysub, polymul, polydiv
from sympy.abc import x
from sympy import factor

"""
Operações abordadas nesse arquivo:

- 1. adição, subtração, multiplicação e divisão;
- 2. potenciação e radiciação;
- 3. operações inteiras (piso - floor, teto - celing e arredondamento - round);
- 4. operações com frações;
- 5. operações com polinômios;
- 6. fatoração de polinômios

O python usa seguinte ordem para resolver expressões com várias operações:
- parênteses
- potenciação
- multiplicação
- divisão
- adição
- subtração
"""

# 1. operações básicas

a = 5
b = 2

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

# aqui você pode trabalhar com 'int' e 'float'
print(f"números escolhidos: {a}, {b}")
print(f"soma: {soma}")
print(f"subtração: {subtracao}")
print(f"multiplicação: {multiplicacao}")
print(f"divisão: {divisao}")
print("\n")

# 2. potenciação e radiciação

c = 5
d = 4

potenciacao = c ** 2 # ou a ** d (pra elevar ao quadrado)
elevar_ao_quadrado = pow(c, 2) # método usando lib externa
radiciacao = d ** (1/2) # forma pura de usar raíz quadrada
radiciacao_sqrt = sqrt(d)

print(f"números escolhidos:  {c}, {d}")
print(f"potenciação pura: {potenciacao}")
print(f"potenciação usando lib externa: {elevar_ao_quadrado}")
print(f"radiciação pura: {radiciacao}")
print(f"radiciação usando lib externa: {radiciacao_sqrt}")
print("\n")

# 3. operações inteiras

"""
em python temos 3 tipos de saídas para operações com números inteiros:

- piso (floor) => retorna o maior valor inteiro menor que 'e'
- teto (ceil) => retorna o menor valor inteiro menor que 'e'
- arredondamento (round) => retorna o valor inteiro mais próximo de 'e'
"""

e = 3.456

piso = floor(e)
teto = ceil(e)
arredondamento = round(e)

print(f"número escolhido: {e}")
print(f"número escolhido inteiro: {piso}")
print(f"número seguinte ao escolhido: {teto}")
print(f"arredondando o número pro inteiro mais próximo: {arredondamento}")
print("\n")

# 4. operações com frações

"""
Podemos fazer divisões em python desconsiderando a parte fracionária, usando (//).
Também podemos retornar o valor do resto da divisão usando (%)."""

f = 10
g = 3

divisao_inteira = f // g
resto = f % g

print(f"números escolhidos: {f}, {g}")
print(f"divisão inteira: {divisao_inteira}")
print(f"resto da divisão: {resto}")
print("\n")

"""
Podemos usar uma lib externa para declarar operações com frações, por exemplo
"""

h = Fraction(1, 4)
i = Fraction(2, 3)

soma_f = h + i
subtracao_f = h - i
multiplicacao_f = h * i
divisao_f = h / i

print(f"números escolhidos: {h}, {i}")
print(f"soma de fração: {soma_f}")
print(f"subtração de fração: {subtracao_f}")
print(f"multiplicação de fração: {multiplicacao_f}")
print(f"divisão de fração: {divisao_f}")
print("\n")

# 5. operações com polinômios

coeficiente_pol1 = [3, 2, -1] # define 3x**2 + 2x -1
coeficiente_pol2 = [4, -1, 3] # define 4x**2 -x + 3

soma_pol = polyadd(coeficiente_pol1, coeficiente_pol2)
subtracao_pol = polysub(coeficiente_pol1, coeficiente_pol2)
multi_pol = polymul(coeficiente_pol1, coeficiente_pol2)
div_pol = polydiv(coeficiente_pol1, coeficiente_pol2)

print(f"os números escolhidos foram: polinômio A ({coeficiente_pol1}) e polinômio B ({coeficiente_pol2})")
print(f"soma dos polinômios: {soma_pol}")
print(f"subtração dos polinômios: {subtracao_pol}")
print(f"multiplicação dos polinômios: {multi_pol}")
print(f"divisão dos polinômios: {div_pol}")
print("\n")

# 6. fatoração de polinômios

resultado = factor(x**2 + 3*x)
print(resultado)