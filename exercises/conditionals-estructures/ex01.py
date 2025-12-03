"""
1 - verificando quais frutas venderam mais no comércio:
Use estruturas condicionais para determinar quais frutas 
venderam mais na banca no último dia.
"""

macas = 15
bananas = 3

# estrutura condicional tradicional
if macas >= bananas:
    vendeu_mais = "Maçãs venderam mais"
else:
    vendeu_mais = "Venderam mais bananas"


# operador ternário
#vendeu_mais = 'As maçãs venderam mais' if macas >= bananas else 'As bananas venderam mais'


# usando programação funcional
"""
def vendeu_mais():
    if macas > bananas:
        return ("Venderam mais Maçãs")
    else:
        return ("Venderam mais bananas")
"""

print(vendeu_mais)