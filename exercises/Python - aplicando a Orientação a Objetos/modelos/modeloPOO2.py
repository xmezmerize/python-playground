class Pessoa: # classe
    contagem = 0  # Atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância
        self.idade = idade  # Atributo de instância
        Pessoa.contagem += 1

    def dizer_ola(self):
        return f"Olá, meu nome é {self.nome}."

    @classmethod
    def obter_contagem(cls):
        return cls.contagem

    @staticmethod
    def saudacao_geral():
        return "Olá a todos!"

# Criar instâncias
pessoa1 = Pessoa("Ana", 30)
pessoa2 = Pessoa("João", 25)

# Usar métodos de instância
print(pessoa1.dizer_ola())  # Saída: Olá, meu nome é Ana.

# Usar métodos de classe
print(Pessoa.obter_contagem())  # Saída: 2

# Usar métodos estáticos
print(Pessoa.saudacao_geral())  # Saída: Olá a todos!


# Métodos de Instância: São métodos que atuam sobre uma instância específica da classe e podem acessar e modificar os atributos dessa instância.
# Métodos de Classe: São métodos que atuam sobre a classe em si e não sobre uma instância específica. Usam o decorador @classmethod.
# Métodos Estáticos: Não agem sobre a instância ou a classe. Usam o decorador @staticmethod e são usados para funções que não precisam acessar atributos da classe ou da instância.
