#1
class Carro:
    # construtor
    def __init__(self, cor, modelo, ano):
        # atributos
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

# instâncias
carro1 = Carro('Amarelo', 'Fusca', '1976')
carro2 = Carro('Vermelho', 'Siena', '2009')

# exibindo informações
print(f'Carro 1: {carro1.modelo} | {carro1.cor} | {carro1.ano}\nCarro2: {carro2.modelo} | {carro2.cor} | {carro2.ano}')


#2 & 3
class Restaurante:
    def __init__(self, nome, categoria, ativo=False, capacidade=None, avaliacao=None):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.avaliacao = avaliacao

#4
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo} | {self.capacidade} | {self.avaliacao}'

restaurante1 = Restaurante('Le Plastique', 'Frenchise Food', False, capacidade='100', avaliacao='4.5 estrelas')

print(restaurante1)


#5
class Cliente:
    def __init__(self, nome, idade, genero, nacionalidade):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.nacionalidade = nacionalidade

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.genero} | {self.nacionalidade}'

cliente1 = Cliente('Pedro', '21', 'masc', 'brasileiro')

print(f'Perfil do cliente: {cliente1}')