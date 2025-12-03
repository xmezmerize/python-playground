# Tipo String 

# =================================================================================================================== #

# O que é uma string -> Um dado é do tipo string quando está entre aspas simples, duplas ou triplas

'uma string'
"outra string"
'''string com múltiplas linhas'''

# =================================================================================================================== #

# Declaração e exibição

nome = 'Pedrinho'
print(nome)         # Pedrinho
print(type(nome))   # <class 'str'>

# =================================================================================================================== #

# Caracteres especiais (escape sequences)

"""
\n → quebra de linha
\" → aspas literais dentro da string
"""

# Exemplo:

nome = "Pedro \nHenrique"
print(nome)

nome = "Pedro \"Henrique\""
print(nome)

# =================================================================================================================== #

# Métodos úteis para manipulação

nome = "Pedro Henrique"

print(nome.upper())   # PEDRO HENRIQUE
print(nome.lower())   # pedro henrique
print(nome.split())   # ['Pedro', 'Henrique']
print(nome[0:5])      # Pedro
print(nome[6:])       # Henrique

# =================================================================================================================== #

# Índices e slices

"""
Cada caractere tem um índice:

 P   e   d   r   o       H   e   n   r   i   q   u   e
[0] [1] [2] [3] [4] [5] [6] ...
"""

print(nome[0])   # P
print(nome[6:9]) # Hen

# =================================================================================================================== #

# Inversão e substituição

print(nome[::-1])                # euqirneH ordeP
print(nome.replace("e", "i"))    # Pidro Hinriqui

# =================================================================================================================== #

# Palíndromos → palavra/frase que pode ser lida de trás para frente:

texto = 'socorram me em marrocos'
print(texto == texto[::-1])  # True

nome = 'ana'
print(nome == nome[::-1])    # True