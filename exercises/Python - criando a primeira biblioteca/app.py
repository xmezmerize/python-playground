import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Nona', 'categoria':'Brasileira', 'ativo':False}]

def exibir_nome_prg():
    ''' Exibe o nome estilizado do programa na tela '''

    print('''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█\n''')

def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar status do restaurante')
    print('4. Sair')

def finalizando_app():
    ''' Exibe a mensagem de finalização do app'''

    exibir_subtitulos('Finalizando o app...')

def voltar_menu():
    ''' Solicita uma tecla para retornar ao menu principal

        Outputs:
        - Retorna ao menu principal

    '''
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

# funções de criação da interface ^

def opcao_invalida():
    ''' Exibe uma mensagem de opção inválida

        Outputs:
        - Retorna ao menu principal

    '''
    print('Opção inválida!\n')
    voltar_menu()  

def exibir_subtitulos(texto):
    '''Exibe um subtítulo estilizado na tela

       Outputs:
       - texto: str - O texto do subtítulo

    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print() # pra validar e dar espaço

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante 
    
        Inputs:
        - Nome do restaurante
        - Categoria

        Outputs:
        - Adiciona um novo restaurante na lista

    ''' # docstring => torna o código mais acessível
    exibir_subtitulos('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante) # .append => coloca dentro da lista
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.\n')
    voltar_menu()

def listar_restaurantes():
    ''' Essa função é responsável por cadastrar um novo restaurante
        
        Inputs:
        - Nome do restaurante
        - Categoria

        Outputs:
        - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulos('Listando os restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    print('==========================================================')
    for restaurante in restaurantes:
        #aplicando dicionário
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        situacao = 'ativado' if restaurante['ativo'] else 'desativado' #ternário
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {situacao}')
        # .ljust => organiza o texto em espaços iguais
    voltar_menu()

def alterar_status_restaurante():
    ''' Altera o status ativo/desativo de um restaurante
    
        Outputs:
        - Exibe mensagem indicando o sucesso da operação

    '''
    exibir_subtitulos('Alternando o status...')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso' # Operador Ternário
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_menu()

# funções de refatoração e automação de processos ^

def escolher_opcao():
    ''' Executa a opção escolhida pelo usuário '''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizando_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

# O bloco `try` no código tenta converter a entrada do usuário em um inteiro. Se ocorrer um erro (como entrada inválida), o bloco `except` executa `opcao_invalida()` para lidar com a situação, assegurando que o programa continue funcionando sem interrupções, melhorando a experiência do usuário ao garantir robustez contra entradas inesperadas.

def main():
    ''' Função principal que inicia o programa '''
    
    os.system('cls')
    exibir_nome_prg()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()