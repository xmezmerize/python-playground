#5 - controlando o orçamento mensal

gastos_mensais = input('Digite os seus gastos: ')

# .replace() - substitui o (.) por uma (,)
gastos_mensais = float(gastos_mensais.replace(',','.'))

if gastos_mensais > 3000:
    print('Atenção! Você ultrapassou o limite do orçamento.')
elif gastos_mensais < 0:
    print('O programa não aceita valores negativos.')
else:
    print('Parabéns, você está dentro da meta!')