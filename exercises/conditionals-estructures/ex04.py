#4 - calculando o IMC

peso = float(input('Digite o seu peso(em Kg): '))
altura = float(input('Digite a sua altura(em mt): '))

imc = peso / (altura**2)

print('O seu IMC é de {}')

if imc <= 18.5:
    print('Você está abaixo do peso.')
elif imc > 18.5 and imc < 25:
    print('Seu peso está normal. Parabéns!')
else:
    print('Você está acima do peso. Hora de buscar ajuda especializada.')