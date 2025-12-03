#6 - controle de acesso ao escritório

horario = input('Digite a hora atual(formato HH ou HH:HH): ')

# transforma a hora em formato HH:HH
if ':' in horario:
    partes = horario.split(':')
    horas = int(partes[0])
    minutos = int(partes[1])
    horario_decimal = horas + minutos / 60
else:
    horario_decimal = float(horario)
    
# validação
if horario_decimal < 0 or horario_decimal >= 24:
    print('O formato aceito pelo programa é de 24 horas (0 a 23:59).')
elif 8 <= horario_decimal <= 18:
    print('Acesso permitido.')
else:
    print('Acesso negado.')