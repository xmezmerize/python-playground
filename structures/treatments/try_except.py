# bloco try/except

"""
Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Prevenindo
assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema
"""

# Exemplo 1 - Tratando um erro genérico

try:
    erro()
except:
    print("Deu erro") # -> a função não foi declarada
    
# Exemplo 2 - Tratando um erro genérico

try:
    len(5)
except:
    print('Deu algum problema') # -> eu não defini a variável ou tipo de dado para len

# Exemplo 3 - Tratando um erro específico

try:
    pedro()
except NameError:
    print('Você está utilizando uma função inexistente')

# Exemplo 4 - Tratando um erro específico

try:
    len(5)
except TypeError:
    print('Você está utilizando uma função inexistente')

# Exemplo 5 - Tratando um erro específico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Podemos efetuar diversos tratamentos de erros de uma vez.

try:
    pedro()
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')

# Tratando erro dentro da função

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {"nome": "Geek"}

print(pega_valor(dic, 8))

# Forma correta do pseudocódigo acima
"""
dic = {"nome": "Geek"}

def pega_valor(dic):
    try:
        return dic
    except KeyError:
        return KeyError
    except TypeError:
        return TypeError

print(pega_valor(dic))
"""