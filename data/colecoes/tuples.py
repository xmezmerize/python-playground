# Tuplas (tuple)

"""
Tuplas são coleções ordenadas, indexadas e imutável de elementos,
são representadas por "()".

Tuplas são bastante parecidas com listas. Existem basicamente duas diferenças básicas:

- As tuplas são representdas por parênteses ()
- As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda.
Toda operação em uma tupla gera uma nova tupla.

Porque usar tuplas?
- Mais rápidas que listas (ótimo para performance).
- Mais seguras, já que não podem ser alteradas acidentalmente.
- Excelentes para dados fixos (como meses do ano, coordenadas, etc.).
"""

# ================================================================================================================== #

# Usando tuplas

# CUIDADO 1: As tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6,)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6,
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento
tupla3 = (5)  # Isso não é uma tupla!
print(tupla3)
print(type(tupla3)) # <class 'int'>

tupla4 = (10,)  # Isso é uma tupla!
print(tupla4)
print(type(tupla4))

tupla5 = 15,
print(tupla5)
print(type(tupla5))

# CONCLUSÃO: Podemos concluir que tuplas são definidas pela vírtula e não pelo uso do parênteses

# (4)  -> Não é tupla
# (4,) -> É tupla
#  4,  -> É tupla

# Podemos gerar uma tupla dinamicamente com range(inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# ================================================================================================================== #

# Desempacotamento de tupla

tupla = ('Pedro Henrique', 'Programação em Python')

estudante, curso = tupla

print(estudante)
print(curso)

# ================================================================================================================== #

# Agregações em tuplas

# OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos para desenpacotar.
# Métodos para adição e remoção de elementos nas tuplas são existem, dado o fato das tuplas serem imutáveis.

tupla = (1, 2, 3, 4, 5, 6)

# * Se os valores forem todos inteiros ou reais
print(sum(tupla))  # soma → 21
print(max(tupla))  # máximo → 6
print(min(tupla))  # mínimo → 1
print(len(tupla))  # tamanho → 6

# ================================================================================================================== #

# Concatenação de tuplas

tupla1 = (1, 2, 3)

tupla2 = (4, 5, 6)

print(tupla1 + tupla2)  # Tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3) # Tuplas são imutáveis, mas podemos sobrescrever seus valores
print(tupla1)
print(tupla2)

# ================================================================================================================== #

# Verificação de elementos

tupla = (1, 2, 3)
print(3 in tupla) #True

# ================================================================================================================== #

# Iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

i = 0
while i < len(tupla):
    print(tupla[i])
    i += 1

# ================================================================================================================== #

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('c')) #1

user = tuple('Pedro Henrique')
print(user)

print(user.count('e'))

# ================================================================================================================== #

# Slicing

meses = (
    'Janeiro', 
    'Fevereiro', 
    'Março', 
    'Abril', 
    'Maio', 
    'Junho', 
    'Junho', 
    'Agosto', 
    'Setembro', 
    'Outubro', 
    'Novembro', 
    'Dezembro'
        )

# O acesso a elementos de uma tupla também é semelhante a de uma lista
print(meses[5])

# tupla[inicio:fim:passo]
print(meses[5:9])

# Localizando índices
print(meses.index('Junho'))  # 5
# OBS: Se o elemento não existir, gera ValueError.

# ================================================================================================================== #

# Cópia de tuplas

tupla = (1, 2, 3)
nova = tupla

print(nova)  # (1, 2, 3)

outra = (4, 5, 6)
nova = nova + outra

print(nova)  # (1, 2, 3, 4, 5, 6)
print(tupla) # (1, 2, 3)

# Na tupla não temos o problema de Shallow Copy