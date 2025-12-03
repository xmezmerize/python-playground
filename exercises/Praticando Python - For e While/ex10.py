#10 - Validação de entrada para login

while True:
    usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')

    if len(usuario) < 5:
        print('O nome de usuário deve ter pelo menos 5 caracteres.')
        continue

    if len(senha) < 8:
        print('A senha do usuário deve ter pelo menos 8 caracteres.')
        continue

    else:
        print('Cadastro realizado com sucesso!')
    break