class Restaurante:
    restaurantes = []

    # método especial
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self) # todo objeto criado vai pra dentro da lista

    # método especial
    def __str__(self):
        return f'{self._nome} | {self.categoria}'

    # métodos próprios/da classe (não precisou criar instâncias, é um método da classe)
    @classmethod
    def listar_restaurantes(cls): # uso do cls => pra indicar que é um método da classe
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Estado'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    # método para o objeto ativo
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza express', 'Italiana')

Restaurante.listar_restaurantes()

# vars => retorna o dicionário da classe
# __init__ => O método __init__ é um método especial em Python que atua como um construtor para uma classe. O objetivo deste método é inicializar os atributos da instância com valores específicos, com base nos argumentos passados durante a criação da instância. Portanto, ele é chamado ao aut. ao criar uma classe.
# self => O self em Python é uma convenção que representa a instância da própria classe. Ele é usado como o primeiro parâmetro em métodos de instância (métodos pertencentes a objetos específicos da classe).
# property => Usamos property quando precisamos encapsular informações que serão cruzadas com outras para gerar uma visualização diferente.
# coolsymbol.com
