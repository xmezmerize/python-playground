# Modos de Abertura de Arquivo

"""
r → leitura (padrão). O arquivo deve existir.
w → escrita. Cria ou sobrescreve o arquivo (apaga tudo que já tinha).
x → escrita exclusiva. Cria somente se não existir (senão gera FileExistsError).
a → escrita em modo append. Adiciona ao final sem apagar o conteúdo existente.
+ → atualização (permite leitura + escrita no mesmo arquivo, controlando o cursor).

Obs:
'a' → se o arquivo não existir, ele é criado.
'a' não permite movimentar o cursor para escrever no meio; sempre escreve no final.
'r+' ou 'w+' → permitem ler e escrever com movimentação do cursor (seek()).
"""

# Exemplo com x (cria somente se não existir)

try:
    with open("university.txt", "x") as arquivo:
        arquivo.write("Teste de conteúdo 2.\n")
except FileExistsError:
    print("Arquivo já existe")

# Exemplo com a (append → adiciona ao final)

with open("frutas.txt", "a", encoding="utf-8") as arquivo:
    while True:
        fruta = input("Informe uma fruta ou digite 'sair': ").strip()
        
        if fruta.lower() == "sair":
            print("Finalizando...")
            break

        if fruta:  # evita salvar vazio
            arquivo.write(fruta + "\n")

# Executando várias vezes, o arquivo vai acumulando frutas sem perder as anteriores.

# Exemplo com r+ (leitura + escrita, com cursor)
with open("outro.txt", "r+", encoding="utf-8") as arquivo:
    arquivo.write("Adicionada\n")        # escreve no começo
    arquivo.seek(11)                     # move o cursor
    arquivo.write("Nova linha.\n")       # escreve a partir da posição 11
    arquivo.seek(32)                     # move de novo
    arquivo.write("Mais uma linha.\n")   # escreve na posição 32

# Aqui, como temos controle do cursor (seek), conseguimos sobrescrever no meio do arquivo.