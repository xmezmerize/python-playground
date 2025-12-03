"""
Sintaxe:
O primeiro ponto que diferencia esses dois arranjos é a sintaxe de cada um. 
Como vimos, as listas são definidas utilizando colchetes [ ], enquanto as 
tuplas são definidas utilizando parênteses ( )

Mutabilidade:
A maior diferença entre essas duas configurações são suas propriedades de mutabilidade!
As listas são estruturas mutáveis, o que significa que é possível modificar seus elementos, 
adicionar novos itens ou remover existentes após a criação da lista, podendo inclusive 
utilizar funções próprias para isso como append(), remove(), pop(), e insert().
Ao contrário das listas, tuplas são imutáveis. Uma vez que uma tupla é criada, 
seus elementos não podem ser alterados, adicionados ou removidos.

Desempenho:
Devido à sua imutabilidade, as tuplas têm um desempenho melhor do que listas para algumas operações. 
Elas são mais eficientes em termos de espaço e processamento em determinados cenários.
Sendo assim, listas podem ser menos eficientes em termos de desempenho para operações específicas, 
especialmente quando se trata de manipulação de grandes conjuntos de dados, devido à sua mutabilidade.
"""

# Exemplo lista
lista_de_compras = ["Maçã", "Banana", "Leite", "Pão", "Queijo"]

# Adicionando um item à lista
lista_de_compras.append("Ovos")

# Removendo um item da lista
lista_de_compras.remove("Banana")

# Exibindo a lista
print("Lista de Compras:")
for item in lista_de_compras:
    print("- " + item)

# Exemplo tuplas
coordenadas_gps = (40.7128, -74.0060)

# Exibindo as coordenadas
print("Coordenadas GPS:")
print("Latitude:", coordenadas_gps[0])
print("Longitude:", coordenadas_gps[1])