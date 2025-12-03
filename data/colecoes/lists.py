# Listas (List)

"""
Listas funcionam como vetores/matrizes (arrays). É uma estrutura ordenada, mutável 
e indexada.

Características principais de listas em Python:
- Mutáveis → você pode alterar, inserir e remover elementos após a criação.
- Indexadas → cada elemento tem uma posição (índice) começando do zero.
- Ordenadas → preservam a ordem em que foram criadas/adicionadas.
- Aceitam duplicatas → elementos iguais podem existir mais de uma vez.
- Heterogêneas → aceitam diferentes tipos de dados na mesma lista.
- Dinâmicas → não têm tamanho fixo, crescem e diminuem conforme adiciona ou remove valores.
- Métodos úteis → .append(), .insert(), .remove(), .pop(), .sort(), .reverse(), .extend(), .count(), .index().

Diferenças de listas em Python:

Linguagens como C/Java:
- Possuem tamanho e tipo de dado fixo - ou seja, nessas linguagens se você criar 
um array do tipo int e com tamanho 5, este array será SEMPRE do tipo inteiro e
poderá ter SEMPRE no máximo 5 valores.

Já em Python:
- Dinâmico: Não possuem tamanho fixo - podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo - suporta qualquer tipo de dado;

As listas em Python são representadas por colchetes: []
"""

# ================================================================================================================== #

# Criando Listas

print(type([])) # <class 'list'>

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['P', 'e', 'd', 'r', 'o', ' ', 'H', 'e', 'n', 'r', 'i', 'q', 'u', 'e']
lista3 = []
lista4 = list(range(11))
lista5 = list('Pedro Henrique')

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista3)

# ================================================================================================================== #

# Acesso e Verificação

# Checar se um valor está na lista
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# ================================================================================================================== #

# Ordenação e Contagem

# Ordenar
lista1.sort()
print(lista1)

# Contar ocorrências
print(lista1.count(1))
print(lista5.count('e'))

# ================================================================================================================== #

# Inserção de Elementos

# Adicionar no final
lista1.append(42) # OBS: Com append, nós só conseguimos adicionar 1 elemento por vez

# Adicionar sublista como elemento único
lista1.append([8, 3, 1])

# Adicionar múltiplos elementos
lista1.extend([123, 44, 67])

# Inserir em posição específica
lista1.insert(2, 'Novo Valor')

print(lista1)

# ================================================================================================================== #

# Concatenação de Listas

# Forma 1
lista_soma = lista1 + lista2

# Forma 2
lista1.extend(lista2)

print(lista_soma)

# ================================================================================================================== #

# Inversão da Lista

# Forma 1 - reverse()
lista1.reverse()
print(lista1)

# Forma 2 - slicing
print(lista2[::-1])

# ================================================================================================================== #

# Cópias

lista6 = lista3.copy()
print(lista6)

# ================================================================================================================== #

# Quantidade de Elementos (contagem)

print(len(lista5))

# ================================================================================================================== #

# Remoção de Elementos

# Remover último elemento
lista5.pop()

# Remover por índice
lista5.pop(2)

# Zerar lista
lista5.clear()

print(lista5)

# ================================================================================================================== #

# Repetição de Elementos

nova = [1, 2, 3]
nova = nova * 3
print(nova)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# ================================================================================================================== #

# Conversões (String ↔ Lista)

# String para lista
curso = 'Programação em Python'
curso = curso.split()  # separa por espaço
print(curso)

curso = 'Programação,em,Python'
curso = curso.split(',')  # separa por vírgula
print(curso)

# Lista para string
lista6 = ['Programação', 'em', 'Python']
curso = ' '.join(lista6)   # junta com espaço
print(curso)

# ================================================================================================================== #

#Listas Heterogêneas

lista6 = [1, 2.34, True, 'Pedrinho', 'd', [1, 2, 3], 45345345345]
print(lista6)

# ================================================================================================================== #

# Iterando sobre listas

# Exemplo 1 – usando for
soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(f"A soma dos elementos da lista 4 é igual a: {soma}")

"""
# Exemplo 2 – usando while
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
"""

# ================================================================================================================== #

# Utilizando variáveis dentro de listas

numeros = [1, 2, 3, 4, 5]
print(numeros)

num1, num2, num3, num4, num5 = 1, 2, 3, 4, 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)

# ================================================================================================================== #

# Acesso indexado

cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# ================================================================================================================== #

# Índices negativos

print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde

# ================================================================================================================== #

# Iteração com índices

for cor in cores:
    print(f"\n{cor}\n")
    
"""
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

for indice, cor in enumerate(cores):
    print(indice, cor)
"""

# ================================================================================================================== #

# Listas aceitam valores repetidos

lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)
print(lista)

# ================================================================================================================== #

# Buscando o índice de elementos

numeros = [5, 6, 7, 5, 8, 9, 10]

print(numeros.index(6))   # posição do 6
print(numeros.index(9))   # posição do 9
print(numeros.index(5))   # como está repetido, busca a primeira ocorrência do 5

print(numeros.index(5, 1))  # busca a partir do índice 1
print(numeros.index(5, 2))  # busca a partir do índice 2
print(numeros.index(8, 3, 6)) # busca o 8 no intervalo [3,6)

# ================================================================================================================== #

# Slicing (Fatiamento)

lista = [1, 2, 3, 4, 5, 6, 7, 8]

print(lista[1:])    # do índice 1 em diante
print(lista[:2])    # do início até o índice 1
print(lista[1:3])   # do 1 até 2
print(lista[::2])   # de 2 em 2
print(lista[1::2])  # a partir do índice 1, de 2 em 2
print(lista[2:6:2]) # do índice 2 até o 5, pulando de 2 em 2 → [3, 5]

# ================================================================================================================== #

# Invertendo valores em listas 

nomes = ['Pedro', 'Henrique']

# troca manual
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

# reverse()
nomes = ['Pedrinho', 'Silva']
nomes.reverse()
print(nomes)

# ================================================================================================================== #

# Agregações em listas númericas

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # soma
print(max(lista))  # maior valor
print(min(lista))  # menor valor
print(len(lista))  # quantidade de elementos

# ================================================================================================================== #

# Convertendo listas em tuplas

lista = [1, 2, 3, 4, 5, 6]
tupla = tuple(lista)
print(lista, type(lista))
print(tupla, type(tupla))

# ================================================================================================================== #

# Desempacotamento

lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1, num2, num3)

# ================================================================================================================== #

# Cópia de listas

# Deep Copy
lista = [1, 2, 3]
nova = lista.copy()
nova.append(4)
print(lista)  # [1, 2, 3]
print(nova)   # [1, 2, 3, 4]

# Shallow Copy
lista = [1, 2, 3]
nova = lista
nova.append(4)
print(lista)  # [1, 2, 3, 4]
print(nova)   # [1, 2, 3, 4]