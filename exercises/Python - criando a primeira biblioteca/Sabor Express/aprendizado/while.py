#ex. com for
#numero = -1
#for _ in range(3):  # Supondo um número máximo de tentativas (3) arbitrário
#    numero = int(input("Digite um número positivo: "))
#    if numero > 0:
#        break

#print("Você digitou:", numero)

# range == número de tentativas

"""
O loop while, diferente do for, é utilizado quando o número de iterações não é 
conhecido de antemão, mas ainda assim depende de uma condição específica para 
manter o bloco de código em repetição. Ele continua a executar o bloco de código 
enquanto a condição fornecida for avaliada como verdadeira.
"""

#ex. com while
numero = -1
while numero <= 0:
    numero = int(input("Digite um número positivo: "))

print("Você digitou:", numero)