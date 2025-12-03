# app.py 
> posso usar '' ou "" e também """ """ para quebrar linha no lugar de \n

> """ """ - usar print() com várias linhas

> fsymbols - site para fontes em python

> interpolação de strings : 
f'{1º} maneira'
'{2º} maneira'.format
'3º', 'maneira'
'4º' + 'maneira'

> python é uma linguagem fortemente tipada (Não conseguimos comparar variáveis de tipos diferentes.)

> o python tem algumas funções imbutidas(int, print) mas também permite baixar bibliotecas(import os, math)

> atalho para ajustar mais de 1 linha de código => CTRL + colchete

# usando match
a partir do python 3.10 temos uma nova funcionalidade como alternatica ao if/elif/else, a função condicional match.
Ex. de código:

opcao_escolhida = int(input('Escolha uma opção: '))
match opcao_escolhida:
    case 1: # if opcao_escolhida == 1:
        print('Adicionar restaurante')
    case 2: # if opcao_escolhida == 2:
        print('Listar restaurantes')
    case 3: # if opcao_escolhida == 3:
        print('Ativar restaurante')
    case 4: # if opcao_escolhida == 4:
        print('Finalizar app')
    case _: # else:
        print('Opção inválida!')

> para mais: https://docs.python.org/pt-br/3/tutorial/controlflow.html#match-statements