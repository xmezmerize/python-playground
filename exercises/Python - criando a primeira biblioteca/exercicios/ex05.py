#1
pessoa = [{'nome': 'Pedro', 'idade': '21', 'cidade': 'itaguara'}]

#2
pessoa[0]['idade'] = '19'

pessoa[0]['profissão'] = 'T.I'


del pessoa[0]['cidade']

print(pessoa)

#3
numeros_quadrados = {x: x**2 for x in range(1,6)}
print(numeros_quadrados)

#4
pessoa2 = [{'nome': 'Felipe', 'idade': '30', 'cidade': 'cláudio'}]
if 'nome' in pessoa2[0]:
    print("A chave 'nome' existe")
else:
    print("A chave 'nome' não existe")

#5
frase = 'Python se tornou uma das linguagens mais populares do mundo nos últimos tempos'
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)