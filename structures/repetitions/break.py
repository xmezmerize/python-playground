# Break

"""
Utilizamos o break para sair de loops de maneira projetada.
O break interrompe imediatamente a execução de um loop (for ou while).
Depois do break, o programa continua a execução do código que vem após o loop.
"""

# Exemplo 1

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Saindo do loop...')


# Exemplo 2

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break