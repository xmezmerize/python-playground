# Tipo None (NoneType)

"""
Definição: None é um tipo especial em Python que representa ausência de valor.
Pertence à classe NoneType. Usado quando queremos indicar que uma variável existe,
mas ainda não tem valor definido.

Correto: None (com N maiúsculo)
Errado: none, NONE, null (gera erro).
"""

# =================================================================================================================== #

# Definição

x = None
print(x)          # None
print(type(x))    # <class 'NoneType'>

# =================================================================================================================== #

# Características

"""
Não é zero, nem string vazia, nem False.
É um objeto único → sempre aponta para a mesma instância na memória.
"""

print(bool(None))   # False
print(None == 0)    # False
print(None == "")   # False
print(None == False) # False
print(None == None) # True

# =================================================================================================================== #


# Comparações:

# x is None → usado para verificar se algo é None

# Exemplo:

a = None
b = None
print(a == b)   # True
print(a is b)   # True (mesmo objeto)

# =================================================================================================================== #

# Uso comum

# Inicialização de variáveis. Quando ainda não sabemos qual valor atribuir:

resultado = None
# ... depois de algum cálculo
resultado = 42

# =================================================================================================================== #

# Funções que não retornam nada

# Se uma função não tiver return, ela retorna None por padrão:

def saudacao():
    print("Olá!")

print(saudacao())   # Olá! \n None

# =================================================================================================================== #

# Condicionais

# Em contexto booleano, None é considerado falso:

if None:
    print("Entrou")
else:
    print("Não entrou")  # executa

# =================================================================================================================== #

# Diferença entre None e False

print(bool(None))   # False
print(None == False) # False
print(None is False) # False

"""
Ou seja: ambos são tratados como "falsos" em condicionais.
Mas não são a mesma coisa.
"""

# =================================================================================================================== #

# Comparações recomendadas

# Sempre use is None ou is not None para verificar None:

x = None

if x is None:
    print("x não tem valor definido")