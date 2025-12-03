# print('Sabor Express\n')
> \n - pula uma linha em relação ao texto que virá abaixo.

# fsymbols.com
> textos personalizados para py

# print(f'Você escolheu a opção {opcao_escolhida}')
> f {} - interpolação de str => coloca f antes das aspas e a variável dentro das chaves

# def
> para definir uma função em py é usado 'def(definir)'

# os
> para usar code 'import os'
> ex. def finalizar_app():
> os.system('cls) => limpar terminal
> print('Finalizando o app')

# match | case

opcao_escolhida = int(input('Escolha uma opção: '))
match opcao_escolhida:
case 1:
print('ação 1')
case 2:
print('ação 2')
case _:
print('outra opção/saída')

# if/else

idade = 18

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# tuplas x listas

> Tuplas são estruturas imutáveis.
> Listas podem ser alteradas ao longo do programa usando diversas funções como: append(), delete(), pop() e insert().