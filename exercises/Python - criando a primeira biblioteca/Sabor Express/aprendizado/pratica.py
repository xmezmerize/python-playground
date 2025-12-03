# 1 - Imprima a frase: Python na Escola de Programação da Alura.
print('Python na Escola de Programação da Alura')

# 2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
nome = 'Pedro'
idade = 21
print(f'Meu nome é {nome} e tenho {idade} anos.')

# 3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha
print('A\nL\nU\nR\nA')

# 4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais.
pi_arredondado = 3.14159
print(f'O valor arredondado de pi é: {pi_arredondado:.2f}')

# 5 - Crie uma lista para cada informação a seguir:
#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    print(numero)

nomes = ['Pedro', 'Felipe', 'Dudu', 'Angelita']
for nome in nomes:
    print(nome)

ano = [2003, 2024]
for ano in ano:
    print(ano)

# 6 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
# Feito acima ^

# 7 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
for numero in numeros:
    if numero % 2 != 0:
        print(numero)

# 8 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
numeros_decrescente = sorted(numeros, reverse=True)

for numero in numeros_decrescente:
    print(numero)

# 9 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
num = int(input('Digite um número inteiro: '))
for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')

# 10 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.


# 11 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.