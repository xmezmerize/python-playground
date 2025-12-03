class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome} | {self.idade} anos | {self.profissao}'
    
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}!'

    def aniversario(self):
        self.idade += 1

pessoa1 = Pessoa(nome='Pedro', idade=21, profissao='Engenheiro')

pessoa1.aniversario() # => chamando o método aniversário pra dentro da instância criada

print(f'Parabéns pelos {pessoa1.idade} anos, {pessoa1.nome}! Você é nosso melhor {pessoa1.profissao}')
