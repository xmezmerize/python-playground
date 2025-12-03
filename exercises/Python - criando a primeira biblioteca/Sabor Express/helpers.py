import os

def voltar_ao_menu_principal():
    os.system('cls') # função para limpar o terminal usando a biblioteca os
    print('\nDigite qualquer tecla para voltar ao menu: ')

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
