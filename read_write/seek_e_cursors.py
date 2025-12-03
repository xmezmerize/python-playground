# Seek e Cursors

"""
Seek e Cursors

- O que é o cursor?

Quando abrimos um arquivo, o Python mantém um cursor (ponteiro) 
que indica a posição atual de leitura/escrita.
Toda vez que você usa read(), o cursor avança.

Para reposicionar, usamos seek(posição).
"""

# Movimentando o cursor (seek)

arquivo = open("texto.txt", "r", encoding="utf-8")

print("Primeira leitura:")
print(arquivo.read())  # lê tudo, cursor vai para o final

arquivo.seek(0)        # reposiciona para o início
print("\nSegunda leitura:")
print(arquivo.read())  # lê novamente desde o começo

arquivo.seek(22)       # move o cursor para o caractere 22
print("\nA partir da posição 22:")
print(arquivo.read())

arquivo.close()

# Lendo linha a linha

# readline() → lê apenas uma linha por vez
arquivo = open("texto.txt", "r", encoding="utf-8")

linha = arquivo.readline()
print(type(linha))   # str
print(linha)
print(linha.split(" "))  # divide a linha em palavras

arquivo.close()

# readlines() → lê todas as linhas e devolve uma lista
arquivo = open("texto.txt", "r", encoding="utf-8")

linhas = arquivo.readlines()
print(len(linhas))   # quantidade de linhas
print(linhas)        # lista com cada linha como item

arquivo.close()

# Iterando sobre o arquivo (forma mais eficiente)
with open("texto.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())  # strip remove o \n

# Fechando arquivos

"""
Quando abrimos com open(), criamos uma conexão (streaming) com o arquivo no disco.
É importante fechar para liberar o recurso.
"""

arquivo = open("texto.txt", "r", encoding="utf-8")

print(arquivo.read())
print(arquivo.closed)  # False → ainda aberto

arquivo.close()
print(arquivo.closed)  # True → agora fechado

# Se você tentar ler após fechar:

print(arquivo.read())  # ValueError

# Limitando a leitura

# Você pode passar um número para read(n) para limitar a quantidade de caracteres.

arquivo = open("texto.txt", "r", encoding="utf-8")

print(arquivo.read(50))  # lê só os 50 primeiros caracteres

arquivo.close()

"""
Passos corretos para trabalhar com arquivos:

Abrir → open()
Trabalhar → ler ou escrever (read, write, etc.)
Fechar → close()
"""

#Ou simplesmente usar o with (mais seguro e pythônico):

with open("texto.txt", "r", encoding="utf-8") as arquivo:
    print(arquivo.read())
# aqui o arquivo já foi fechado automaticamente