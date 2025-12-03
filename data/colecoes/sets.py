# Sets (Conjuntos)

"""
Conjuntos em qualquer linguagem de programação, faz referência à Teoria dos Conjuntos
da Matemática. Eles são estruturas não ordenadas, mutáveis e não indexadas.

Características de um Set:
- Sets não possuem valores ordenados: não existe uma ordem garantida dos elementos;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados (s[0] dá erro);
- Elementos únicos: duplicatas são automaticamente removidas.
- Mutável: você pode adicionar ou remover elementos (.add, .remove).
- Aceita tipos imutáveis: você pode colocar int, str, tuple, mas não listas nem outros sets (exceto frozenset).

Devemos utilizar conjuntos para armazenar elementos sem depender de ordenação.
Quando não utiliza-se chaves, valores e itens duplicados. Os conjuntos são
referenciados em Python com chaves {}.

Diferença entre Conjuntos (Set) e Dicionários (Maps) em Python:
- Um dicionário tem chave/valor;
- Um conjunto tem apenas valor;
"""

# ================================================================================================================== #

 # Matemática dos conjuntos aplicada à programação

"""
O set em Python foi inspirado diretamente na Teoria dos Conjuntos,
base da matemática moderna (Cantor, século XIX). Ele representa 
um conjunto de elementos distintos, sem ordem e sem repetição.
"""

# Na matemática, escrevemos:
# 𝐴 = {1, 2, 3, 4, 5}

# No Python, é praticamente a mesma coisa:
A = {1, 2, 3, 4, 5}

# Conexão matemática:
"""
Um set em Python é a implementação de um conjunto matemático.
Você pode fazer operações clássicas de conjuntos com ele:
"""

# União:
# 𝐴 ∪ 𝐵

# Interseção: 
# 𝐴 ∩ 𝐵

# Diferença: 
# 𝐴 − 𝐵

# Diferença simétrica: 
# 𝐴 Δ 𝐵

# Exemplo em Python:

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # união → {1, 2, 3, 4, 5, 6}
print(A & B)  # interseção → {3, 4}
print(A - B)  # diferença → {1, 2}
print(A ^ B)  # diferença simétrica → {1, 2, 5, 6}

# ================================================================================================================== #

# Definindo Sets

# Forma 1 -> referenciando que será um set usando "set"
s = set({1, 2, 3, 4, 5, 5,  6, 7, 2, 3})  # usa "set antes de passar os dados"
print(s)
print(type(s))

# Forma 2 -> forma direta (e mais usada)
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))
# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

"""
OBS: Ao criar um conjunto, caso seja adicionado um valor já existente,
o mesmo será ignorado sem gerar error e não fará parte do conjunto.
"""

conjunto = {1, 2, 3}
conjunto.add(3)   # tenta adicionar um 3 novamente
conjunto.add(4)   # adiciona o 4

print(conjunto) # 1, 2, 3, 4

# ================================================================================================================== #

# Diferenças entre as principais coleções em Python

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla}  com {len(tupla)} elementos')

# Dicionários não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario}  com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto}  com {len(conjunto)} elementos')

# ================================================================================================================== #

# Usando diferentes tipos de dados no mesmo conjunto

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# ================================================================================================================== #

# Usos interessantes com sets

# issubset / issuperset: verificar se um conjunto está contido em outro.
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))   # True
print(B.issuperset(A)) # True

# isdisjoint: verificar se dois conjuntos não têm elementos em comum.
X = {1, 2}
Y = {3, 4}
print(X.isdisjoint(Y)) # True

# Como converter entre lista ↔ conjunto para remover duplicatas rapidamente:

lista = [1, 2, 2, 3, 4, 4, 5]
conjunto = set(lista)
print(conjunto)  # {1, 2, 3, 4, 5}

# Adicionando elementos em um conjunto
s = {1, 2, 3}

# Agregação dos elementos

s = {1, 2, 3}

s.add(4)
s.add(4)  # Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado.
print(s)

# Soma 
print(sum(s)) # -> soma todos os elementos do conjunto (só funciona se forem numéricos).

# Valor Máximo
print(max(s)) # -> retorna o maior valor.

# Valor Mínimo
print(min(s)) # -> retorna o menor valor.

# Tamanho
print(len(s)) # -> retorna a cardinalidade, ou seja, quantos elementos únicos existem no conjunto.

# ================================================================================================================== #

# Remover elementos em um conjunto

s = {1, 2, 3}
print(s)

# Forma 1 -> NÃO é índice! Informamos o valor a ser removido.
s.remove(3)
print(s)
# OBS: Caso o valor não seja encontrado será gerado o erro KeyError. Nenhum valor é retornado.

# Forma 2
s.discard(22)
print(s)
# OBS: Se o valor não for encontrado, nenhum erro é gerado.

# Forma 3 -> Podemos remover todos os itens de um conjunto
s.clear()
print(s)

# ================================================================================================================== #

# Copiando um conjunto para outro...

# Forma 1 - Deep Copy
novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy
novo = s

novo.add(4)

print(novo)
print(s)

# ================================================================================================================== #

# União de conjuntos "|"

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}


# Forma 1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
# {'Pedro', 'Fernando', 'Ana', 'Julia', 'Guilherme', 'Patricia', 'Marcos', 'Ellen', 'Gustavo'}
print(unicos1)

unicos1_1 = estudantes_java.union(estudantes_python)
# {'Ana', 'Marcos', 'Gustavo', 'Fernando', 'Patricia', 'Guilherme', 'Pedro', 'Ellen', 'Julia'}
print(unicos1_1)

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)
# Veja que alguns alunos que estudam Python também estudam Java.

# ================================================================================================================== #

# Interseção de conjuntos "&"

# Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# ================================================================================================================== #

# Diferença "-"

"""
Imagine que temos dois conjuntos: Um contendo estudantes
do curso Python e um contendo estudantes do curso de Java.
"""

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# ================================================================================================================== #

# Diferença Simétrica "Δ"

"""
n(A∪B) = n(A) + n(B) - n(A∩B)

Vamos pegar os estudantes que estão matriculados em apenas
um curso por vez dos dois conjuntos (exclui a interseção).
"""

# Vamos gerar um conjunto de estudantes que não estão em dois cursos ao mesmo tempo
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

um_curso_apenas = estudantes_java | estudantes_python - (estudantes_java & estudantes_python)

print(um_curso_apenas)
print(len(um_curso_apenas))