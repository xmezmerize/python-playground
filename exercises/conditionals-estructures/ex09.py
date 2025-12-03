#9 - verificando paridade de um número

num = int(input('Digite um número inteiro: '))

# ternário
resultado = 'O número é par' if num % 2 == 0 else 'O número é ímpar'
print(resultado)