# 1

nome = "   pedro   "

print(nome.strip().upper())

# 2

frase = "Python é poderoso"

qnt = frase.count("o")
verify = frase.endswith("so")

print(f"A frase tem {qnt} 'o's e é {verify} que termina com 'so'")

# 3

texto = "O experimento apresentou FALHAS graves"

novo_texto = texto.lower().replace("falhas", "ajustes").capitalize()

print(novo_texto)

# 4 -> pode alterar

palavras = ["  casa", "Carro ", "peDRo"]

novas_palavras = " ".join(palavras).lower().title()
print(type(novas_palavras))

novas_palavras.strip()

novas_palavras = novas_palavras.split()
print(novas_palavras)

# 5 -> complexo (pode alterar)

emails = ["ana@gmail.com", "pedro@yahoo.com", "joao@outlook.com"]

novos_emails = " ".join(emails)

novos_emails.split("@")
novos_emails = set({"ana@gmail.com", "pedro@yahoo.com", "joao@outlook.com"})
print(novos_emails)

# 6

