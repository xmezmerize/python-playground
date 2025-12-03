# Leitura de Arquivos

"""
Para ler o conteúdo de um arquivo em Python, utilizamos a 
função integrada open(), que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização, passamos apenas um parâmetro
de entrada, que neste caso é o caminho para o arquivo a ser lido. Essa função 
retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

Por padrão, a função open() abre o arquivo para leitura. Este arquivo
deve existir, ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>
mode r -> Modo de Leitura. r -> read() -> ler
"""

# Exemplo (forma errada)

arquivo = open('read/texto.txt')
conteudo = arquivo.read() # lê tudo de uma vez
print(type(conteudo))
print(conteudo)
arquivo.close()

# Exemplo (forma Pythônica)

# with garante que o arquivo será fechado automaticamente
with open("texto.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Lendo por partes

# Lendo linha a linha com readlines()
with open("texto.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    print(linhas)  # retorna uma lista de strings

# Controle de cursor

with open("texto.txt", "r", encoding="utf-8") as arquivo:
    print("Primeira leitura:")
    print(arquivo.read())

    arquivo.seek(0)  # move o cursor de volta ao início

    print("\nSegunda leitura:")
    print(arquivo.read())