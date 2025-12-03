import os
from helpers import voltar_ao_menu_principal, exibir_subtitulo

restaurantes = ['Pizza', 'Sushi']

def exibir_nome_do_programa():
    print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
""")
"""
função para exibir o nome do programa
fonte usada do site 'fsymbols'
"""

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')
"""
função para exibir as opções do programa
'\n' para dar espaço abaixo
"""

def finalizar_app():
    exibir_subtitulo('Finalizando app...')
    voltar_ao_menu_principal()
"""
função para finalizar o app
mostrar a mensagem 'Finalizando app...'
e retorna a função para voltar ao menu principal
"""

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()
    main() # chama o main e volta a executar as funções dentro de main() em ordem
"""
função para inputs inválidos
exibe 'Opção inválida!'
retorna a função para voltar ao menu principal
chama a função 'main()', principal do programa
"""

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # print(f'Você escolheu a opção {opcao_escolhida}')
        # if else elif
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
            print('Listar restaurante')
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            # print('Finalizando o app')
            finalizar_app() # substituindo print por uma função
        else:
            opcao_invalida()
    except:
        opcao_invalida()

"""
^ funções da aplicação ^
"""

def main(): # define as ações executadas pelo programa principal(define também a ordem de execução)
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__': # define esse como arquivo principal da aplicação(não pode ser importado)
    main()

"""
Quando pedimos para que um programa Python seja executado, o interpretador cria uma variável chamada __name__. 
Se o __name__ for __main__ (principal, em inglês), significa que esse código não será importado por outros 
scripts de código Python, e ele será o programa principal.
"""

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:\n')
    restaurantes.append(nome_do_restaurante) # para colocar dados em uma lista em python .append, em JS .push
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()
    main()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    for restaurante in restaurantes: # para cada restaurante da lista restaurantes
        print(f'.{restaurante}') # printa os restaurantes
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

"""
^ funções de ação da aplicação ^
"""