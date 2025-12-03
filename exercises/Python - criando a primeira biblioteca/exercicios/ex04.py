#1
#numeros = [1,2,3,4,5,6,7,8,9,10]
#nomes = ['Pedro', 'Dudu', 'Felipe', 'Miguel']
#anos = [2003, 2024]

#2
#for numero in numeros:
#    print(numero)

#3
#soma = 0

#for numero in range(1, 11):
#    soma += numero

#4
#for numero in range(10, 0, -1):
#    print(numero)

#5
#numero = int(input("Digite um número para ver a tabuada: "))

#for i in range(1, 11):
#    resultado = numero * i
#    print(f"{numero} x {i} = {resultado}")

#6
#try:
#    numeros = input("Digite uma lista de números separados por espaço: ").split()

#    numeros = [int(num) for num in numeros]

#    soma = 0

#    for numero in numeros:
#        soma += numero

#    print(f"A soma dos números é: {soma}")

#except ValueError:
#    print("Erro: Por favor, digite apenas números inteiros separados por espaço.")
#except Exception as e:
#    print(f"Ocorreu um erro inesperado: {e}")

#7
#lista_valores = [15, 20, 25, 30]
#soma_valores = 0

#try:
#    for valor in lista_valores:
#        soma_valores+= valor
#    media = soma_valores / len(lista_valores)
#    print(f'Média dos valores: {media}')
#except ZeroDivisionError:
#    print('A lista está vazia, não é possível calcular a média.')
#except Exception as e:
#    print(f'Ocorreu um erro: {e}')