# Dicionários (dict)

"""
Também conhecidos como "Mapas", os dicionários são coleções de pares chave:valor,
onde: as chaves são únicas e imutáveis, os valores podem ser de qualquer tipo e
a ordem segue de acordo com a inserção(desde o Python 3.7).
Dicionários são representados por chaves {}.

Características de um Dict:
- Estrutura de pares chave:valor.
- Chaves únicas e imutáveis (int, str, tuple...).
- Valores podem se repetir e podem ser de qualquer tipo.
- Mutável: é possível adicionar, atualizar e remover pares.
- Ordenado (a partir do Python 3.7, mantém a ordem de inserção).
- Acesso rápido via chave, não via índice.
- Implementado com tabela hash (busca, inserção e remoção eficientes).
"""

print(type({}))

# ================================================================================================================== #

# Criação de dicionários

# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 (Menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
print(paises)
print(type(paises))

# ================================================================================================================== #

# Acessando elementos

# Acessando direto via chave, parecido com acesso por índice em listas/tuplas
print(paises['br'])
#print(paises['ru']) # KeyError

# Acessando via get (remomendada)
print(paises.get('br'))
print(paises.get('ru')) # None

# Buscando via Key
pais = paises.get('ru')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

# Podemos definir um valor padrão para caso não encontremos a chave informada
pais = paises.get('py', 'Não encontrado')
print(f'Encontrei o país {pais}')

# Podemos verificar se determinada chave se encontra em um dicionário
print('br' in paises) # True
print('ru' in paises) # True
print('Estados Unidos' in paises) # False

if 'ru' in paises:
    russia = paises['ru']
    print(russia) # o valor não existe para chave 'ru', porém não gera KeyError

"""
Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusice lista,
tupla dicionário, como chaves de dicionários.
Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionários,
pois as mesmas são imutáveis.
"""

localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}
print(localidades)
print(type(localidades))

# ================================================================================================================== #

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1 - atribuição direta
receita['abr'] = 350
print(receita)

# Forma 2 - .update()
novo_dado = {'mai': 500}
receita.update(novo_dado)  # receita.update({'mai': 500})
print(receita)

# ================================================================================================================== #

# Atualizando dados em um dicionário

# Forma 1 - atribuição direta
receita['mai'] = 550
print(receita)

# Forma 2 - .update()
receita.update({'mai': 600})
print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas.

# ================================================================================================================== #

# Remover dados de um dicionário

calendario = {'jan': 100, 'fev': 120, 'mar': 300}
print(calendario)

# Forma 1 - .pop(chave) -> remove pela chave, retorna valor, se a chave não existir - KeyError
ret = calendario.pop('mar')
print(ret)
print(calendario)

# Forma 2 - del dict[chave] -> remove pela chave, não retorna valor, se a chave não existir - KeyError
del calendario['fev']
print(calendario)

"""
Imagine que você tem um comércio eletrônico, onde temos
um carrinho de compras na qual adicionamos produtos.

Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;

Poderíamos utilizar uma lista para isso? A resposta é sim.
"""
carrinho = []

produto1 = ['Paystation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

"""
Teríamos que saber qual é o índice de cada informação no produto.
Poderíamos utilizar uma tupla para isso? De novo, sim.
"""
produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

"""
Teríamos que saber qual é o índice de cada informação no produto.
Poderíamos utilizar um dicionário para isso? Sim.
"""
carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# ================================================================================================================== #

# Métodos em dicionários

# Criando um dicionário
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Copiando um dicionário para outro

# Forma 1 # Deep Copy
novo = d.copy()
print(novo)

novo['d'] = 4
print(novo)

# Forma 2 # Shallow Copy
novo = d
print(novo)

novo['d'] = 4
print(novo)

# Limpar o dicionário
d.clear()
print(d)

# ================================================================================================================== #

# Criando dicionários com .fromkeys()

"""
O método fromkeys recebe dois parâmetros: um interável e um valor. Ele vai gerar para
cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.
"""

outro = {}.fromkeys('a', 'b') # {chave, valor}
print(outro) # {'a': 'b'}
print(type(outro)) # <class 'dict'>

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo') # cria chaves de 1 a 10 com o valor 'novo'
print(veja)