# Fluxos (Entrada, processamento, saída)

"""
Assim como na matemática onde usamos da linguagem formal para descrever padrões, 
na programação usamos a linguagem formal para conversar com a máquina e seus 
vários componentes.
 
Fluxos (assinatura) são a espinha dorsal de qualquer processo computacional. Esse é um processo
básico durante o aprendizado de lógica de programação. Durante o fluxo definimos 3 processos 
essenciais de qualquer algoritmo.

- Entrada -> é solicitado algum dado do usuário para interagir com o programa;
- Processamento -> onde acontece a lógica e onde o algoritmo executa sua 
função dentro do programa;
- Saída -> retorna os dados esperados para o usuário.
"""

# ================================================================================================================== #

#  Entrada

#input() retorna sempre string
nome = input('Qual seu nome? ')
print(nome)

# definindo o tipo de dado para o input
idade = int(input('Qual sua idade? '))
print(idade)

# ================================================================================================================== #

# Processamento

print(f'O/A {nome} nasceu em {2025 - idade}')

# Outra forma de processar
data_nasc = 2025 - idade
print(data_nasc)

# ================================================================================================================== #

# Saída (formatos)

# Exemplo de print 'antigo' 2.x
print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')

# Exemplo de print 'antigo' 2.x
print('O/A %s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
print('O/A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'O/A {nome} tem {idade} anos')

print("\n")

# ================================================================================================================== #

"""
De forma análoga à matemática, na programação usamos da teoria da assinatura para
descrever funções
"""

funcao = lambda x: 3 * x + 1 # processamento (f(x) = y -> variável dependente)

resultado = funcao(10) # valor de entrada (variável independente)

print(resultado)
