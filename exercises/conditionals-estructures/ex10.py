#10 - aprovando empréstimo

renda_mensal = input('Digite sua renda mensal(R$): ')
valor_da_parcela = input('Digite o valor da parcela desejada(R$): ')

renda_mensal = float(renda_mensal.replace(',','.'))
valor_da_parcela = float(valor_da_parcela.replace(',','.'))

limite_parcela = renda_mensal * 0.3

if valor_da_parcela > limite_parcela:
    print('Empréstimo negado')
else:
    print('Empréstimo consebido. Parabéns!')