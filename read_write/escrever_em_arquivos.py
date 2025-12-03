# Escrevendo em arquivos

# Exemplo 1 - Forma tradicional (NÃO recomendada em Python, mas funciona)
arquivo = open("mais.txt", "w")

arquivo.write("Um texto qualquer.\n")
arquivo.write("Mais um texto.")
arquivo.close()  # Sempre precisa fechar manualmente

# Exemplo 2 - Forma pythônica (recomendada)
with open("read/novo.txt", "w") as arquivo:
    arquivo.write("Novos dados.\n")
    arquivo.write("Outros podemos colocar quantas linhas quisermos.\n")
    arquivo.write("Mais Esta é a última linha.\n")

# Exemplo 3 - Escrita repetitiva
with open("read/teste.txt", "w") as arquivo:
    arquivo.write("Pedro " * 1000)

# Exemplo 4 - Recebendo entradas do usuário e salvando em arquivo
with open("read/frutas.txt", "a") as arquivo:
# o "a"(append) no lugar de "w"(write), evita sobrescrever a cada execução
# para persistir e consultar o que já existe, use p "a+"
    while True:
        fruta = input("Informe uma fruta ou digite 'sair': ").strip()
        
        if fruta.lower() == "sair":
            print("Finalizando...")
            break
        
        if fruta:  # evita salvar linhas vazias
            arquivo.write(fruta + "\n")