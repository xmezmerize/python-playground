#3 - Temperatura dos servidores

temperatura = int(input('Digite a temperatura(ºC) atual: '))

if temperatura <= 25:
    print(f'Temperatura atual de {temperatura}ºC.')
else:
    print('Alerta! Temperatura acima do limite permitido.')