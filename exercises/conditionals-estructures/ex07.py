#7 - classificando estudantes por média

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print(media)

if media >= 7:
    print('Aprovado!')
elif media >= 5 and media < 7:
    print('Recuperação')
elif media < 5:
    print('Reprovado')
else:
    raise ValueError