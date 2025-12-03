# Bloco With

"""
O With é uma construção de contexto do Python (chamada Python context manager).
Ela server para abrir e fechar recursos automaticamente, sem precisar chamar
close() no final.

Recursos como:
- arquivos,
- conexões de banco de dados,
- sockets,
- locks de thread/processos,
- streams de rede, etc.

Passo para se trabalhar com arquivos:

# 1 - Abrimos o arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo

"""

with open('read/texto.txt') as arquivo:
    print(arquivo.readlines())
    # se eu não usar arquivo.closed aparece apenas o texto
#    print(arquivo.closed) # dentro do bloco retorna (False) o arquivo ainda não foi fechado

#print(arquivo.closed) # fora do bloco retorna (True) o arquivo já foi fechado
"""
1. Abre o arquivo (open("texto.txt")) e associa o objeto à variável arquivo.
2. Você faz qualquer manipulação (ler, escrever, etc.) dentro do bloco indentado.
3. Quando o bloco acaba, o Python automaticamente chama arquivo.close() — mesmo que tenha ocorrido um erro no meio.
"""