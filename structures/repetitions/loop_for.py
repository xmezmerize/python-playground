# Loop - for

"""
Loop -> Estrutura de repetição.
For -> Uma dessas estruturas, usada para iterar sobre objetos iteráveis.

Sintaxe:

for item in interavel:
    # execução do loop

Serve para iterar (repetir ações) sobre uma sequência ou objeto iterável.
Iteráveis comuns: string, lista, tupla, dicionário, set, range.
"""

# Exemplos de iteráveis:

# 1. String
nome = 'Pedro Henrique'

for letra in nome:
    print(letra)
    
# 2. Lista
lista = [1, 3, 5, 7, 9]

for numero in lista:
    print(numero)
    
# 3. Range
numeros = range(1, 10)

for numero in range(1, 11):
    print(numero)

# 4. Enumerate: retorna pares (índice, valor)
nome = 'Pedro Silva'

for indice, letra in enumerate(nome):
    print(indice, letra)

for _, letra in enumerate(nome): # descartando o indice
    print(letra)

# 5. Somatório em Loop
qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input('Informe o primeiro valor: '))
    num2 = int(input('Informe o segundo valor: '))
    soma = soma + (num + num2)
print(f'A soma é {soma}')

# 6. Controle de saída com end
nome = 'Pedrinho'
for letra in nome:
    print(letra, end='')

# 7. Loops aninhados
for _ in range(2):
    for num in range(1, 11):
        print('\U0001F605' * num)
        
# Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode

# Original: U+1F605
# Modificado: U0001F605