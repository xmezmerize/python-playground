class Carro: # => classe

    def __init__(self, cor, modelo):
        self.cor = cor # => atributo da instância
        self.modelo = modelo # => atributo da instância
    # => objeto == tudo que foi criado dentro da classe se torna um objeto Ex. cor = vermelho, modelo = fusca
    
    def ligar(self): # => método
        print("O carro está ligado.")
    
    def desligar(self): # => método
        print("O carro está desligado.")


carro1 = Carro("vermelho", "Fusca") # => objeto da classe Carro
carro2 = Carro("azul", "Civic") # => objeto da classe Carro

print(carro1.cor)  # Saída: vermelho (atributo do objeto carro1 que pertence à classe Carro)

carro1.ligar()  # Saída: O carro está ligado. (método definindo o comportamento do objeto na classe)

def __init__(self, cor, modelo): # => definindo os parâmetros e os tipos de dados que eles usam
    self.cor = cor
    self.modelo = modelo


# Classe => Uma classe é como um molde ou uma receita para criar objetos. Define atributos e métodos que os objetos dessa classe terão.
# Objeto => Um objeto é uma instância de uma classe. É um item específico criado a partir da classe. Cada objeto pode ter valores diferentes para os atributos definidos na classe.
# Atributos => Atributos são variáveis que pertencem a uma classe e armazenam dados sobre o objeto. São como propriedades do objeto.
# Método => Métodos são funções definidas dentro de uma classe que descrevem comportamentos dos objetos daquela classe.
# Parâmetros => Parâmetros são valores que você passa para um método ou função quando a chama. Eles permitem que o método ou função use diferentes dados.

