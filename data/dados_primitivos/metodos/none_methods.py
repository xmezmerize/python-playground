# Métodos com NoneType

"""
O None em Python é um singleton (objeto único da classe NoneType)
e não possui métodos próprios como str, int, float ou list.
"""

# Isso significa que, se você fizer:

print(dir(None))

#Vai ver apenas os métodos herdados de object, por exemplo:

"""
['__bool__', '__class__', '__delattr__', '__dir__', '__doc__', 
 '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
 '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
 '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
"""

# =================================================================================================================== #

# Representação

# __str__() → usado quando imprimimos (print(None) → "None").
# __repr__() → representação oficial ("None").

# =================================================================================================================== #

# Comparação

#__eq__() → permite verificar None == None.
# __ne__() → diferente de.
# Operadores relacionais (<, >, >=, <=) não fazem sentido com None → dão erro se usados.

# =================================================================================================================== #

# Identidade

# Como None é único, o recomendado é usar:
"""
if x is None:
    ...
"""

# Isso usa __eq__ + identidade (is).

# =================================================================================================================== #

# Booleano

# __bool__() → sempre retorna False.

print(bool(None))  # False

# =================================================================================================================== #

# Herdados de object

# Métodos como __class__, __doc__, __hash__, __sizeof__ etc.

# Exemplo:

print(None.__class__)   # <class 'NoneType'>
print(None.__sizeof__()) # tamanho em memória