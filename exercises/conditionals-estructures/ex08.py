#8 - Calculando pedágio

distancia_percorrida = input('Digite a distância percorrida(em KM): ')

distancia_percorrida = float(distancia_percorrida.replace(',','.'))

if distancia_percorrida <= 100:
    print('O valor a pagar será de R$ 10,00.')
elif distancia_percorrida > 100 and distancia_percorrida < 200:
    print('O valor a pagar será de R$ 20,00.')
else:
    print('O valor a ser pago é de R$ 30,00.')