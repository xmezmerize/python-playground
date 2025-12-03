#1

num = input("digite um número de 1 a 10: ")
num = int(num)

if num in (2, 4, 6, 8):
    print('Esse número é par')
else:
    print('Esse número é ímpar')

#2

idade = int(input('Quantos anos você tem? '))
idade = int(idade)

if idade in (0,1,2,3,4,5,6,7,8,9,10,11,12):
    print('Criança')
elif idade in (13,14,15,16,17):
    print('Adolescente')
else:
    print('Você já é um adulto')

#3

nome = input('Digite seu nome: ')
senha = input('Digite uma senha: ')

if not nome.isalpha(): # isalpha verifica se o nome possui apenas letras
    print('Use apenas letras para o nome de usuário.')
elif len(senha) < 6: # len verifica a quantidade de caracteres
    print('Digite uma senha com pelo menos 6 caracteres.')
else:
    print('Usuário cadastrado com sucesso.')

#4

x = int(input('Digite a coordenada x: '))
y = int(input('Digite a coordenada y: '))

# Verifica em qual quadrante o ponto se encontra
if x > 0 and y > 0:
    print('O ponto está no Primeiro Quadrante.')
elif x < 0 and y > 0:
    print('O ponto está no Segundo Quadrante.')
elif x < 0 and y < 0:
    print('O ponto está no Terceiro Quadrante.')
elif x > 0 and y < 0:
    print('O ponto está no Quarto Quadrante.')
else:
    print('O ponto está no eixo ou na origem.')