# Escopo de variáveis

"""
Dois casos de escopo:

- Variáveis globais;
    Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o o programa.
    
- Variáveis locais;
    Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, 
    seu escopo está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel (snake case)

Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuírmos o valor a mesma.

Exemplo em C:
int numero = 42;

Exemplo em Python:
numero = 42
"""

# Exemplo de variável global
numero = 40
print(numero)
print(type(numero))
print(id(numero))

numero = 'Pedro'
"""
acima, eu reescrevo a mesma variável como outro
tipo de dado, porém ela é alocada em outro espaço
na memória, isso acontece devido a dinamicidade do
python, que ao invés de atribuir um espaço na memória 
para guardar as variáveis, ele serve como ponteiro
para indicar as variáveis na memória.
"""
print(numero)
print(type(numero))
print(id(numero))

# Exemplo de variável local
def teste():
    numero = 15
    print(numero)
    print(id(numero))

print(teste())