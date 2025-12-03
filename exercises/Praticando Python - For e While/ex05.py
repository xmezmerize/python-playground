#5 - Organizando seu portfólio

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto == None:
        print('Projeto Ausente')
    else:
        print(projeto)