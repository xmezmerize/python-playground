def teste(teste):
    def encapsular():
        print("antes de alterar qualquer coisa")
        teste()
        print("depois de chamar o parâmetro teste")
    return(encapsular)

@teste # é um atalho para escrever vamos_testar = teste(vamos_testar)
def vamos_testar():
    print("o que vem aqui?")

vamos_testar()