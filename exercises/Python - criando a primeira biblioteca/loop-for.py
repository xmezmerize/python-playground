#Loop for => usado quando se conhece previamente o númeo de iterações. Usadas em elementos de sequência como listas, tuplas, strings ou ranges.

# Ex.
numero = -1
for _ in range(3): # número máximo de tentativas = 3
    numero = int(input('Digite um número positivo: '))
    if numero > 0:
        break

print('Você digitou: ', numero)

# Dessa forma, ele terá um limite arbitrário definido.