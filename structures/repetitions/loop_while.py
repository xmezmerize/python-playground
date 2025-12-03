# Loop - while

"""
Sintaxe:

while expressão_booleana:
    //execução do loop


O bloco do while será repetido enquanto a expressão booleana for verdadeira.
"""

# Exemplo 1

numero = 1

while numero < 11:
    print(numero)
    numero = numero + 1
# OBS: Em um loop while, é importante que cuidemos do critério de parada para não causar um loop infinito.

# Exemplo 2

resposta = ''
aceitos = {'sim', 'ss', 's'}
while resposta.strip().lower() not in aceitos:
    resposta = input('Já acabou? ')