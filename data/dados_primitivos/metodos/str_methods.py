# Métodos de Tratamento de String

# =================================================================================================================== #

# Limpeza e Espaçamento -> usados para remover espaços ou caracteres extras.

texto = "   Python   "
print(texto.strip())   # "Python"
print(texto.lstrip())  # "Python   "
print(texto.rstrip())  # "   Python"

# =================================================================================================================== #

# Caixa Alta e Baixa -> controle de maiúsculas/minúsculas.

nome = "pEdRo HeNriQuE"
print(nome.lower())      # "pedro henrique"
print(nome.upper())      # "PEDRO HENRIQUE"
print(nome.capitalize()) # "Pedro henrique"
print(nome.title())      # "Pedro Henrique"
print(nome.swapcase())   # "PeDrO hEnRIqUe"

# =================================================================================================================== #

# Busca e Substituição -> localizar e modificar partes do texto.

frase = "banana amarela"
print(frase.find("na"))     # 2 (primeira ocorrência)
print(frase.rfind("na"))    # 4 (última ocorrência)
print(frase.index("am"))    # 7 (igual ao find, mas erro se não achar)
print(frase.replace("amarela", "verde")) # "banana verde"
print(frase.count("a"))     # 5

# =================================================================================================================== #

# Verificação de Conteúdo (True/False) -> checar se a string segue certo padrão.

codigo = "12345"
print(codigo.isdigit())   # True
print(codigo.isalpha())   # False
print(codigo.isalnum())   # True
print("   ".isspace())    # True
print("python".startswith("py")) # True
print("script.py".endswith(".py")) # True

# =================================================================================================================== #

# Divisão e Junção -> separar e juntar strings.

frase = "um dois três"
print(frase.split())     # ['um', 'dois', 'três']

frutas = "maçã,banana,uva"
print(frutas.split(",")) # ['maçã', 'banana', 'uva']

nomes = ["Pedro", "Henrique"]
print(" ".join(nomes))   # "Pedro Henrique"

# =================================================================================================================== #

# Formatação e Alinhamento -> ajustar o texto em relação a um tamanho.

num = "42"
print(num.zfill(5))       # "00042"

titulo = "Python"
print(titulo.center(10, "-")) # "--Python--"
print(titulo.ljust(10, "."))  # "Python...."
print(titulo.rjust(10, "."))  # "....Python"