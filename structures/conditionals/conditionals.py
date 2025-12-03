# Estruturas condicionais -> if (Se), else (então), elif (else if - então, se)

"""
Dentro de estruturas em Python, podemos usar diversos tipos
de operadores para relacionar situações e condições
"""

# 1. Usando operadores relacionais (comparam valores)
idade = 18

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade')
    
# 2. Operadores lógicos (combinam condições)
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")
if idade < 18 or not tem_carteira:
    print("Não pode dirigir") 
    
# 3. Operadores de pertencimento (verifica se um valor está ou não em uma coleção)
fruta = "laranja"
frutas = ["maçã", "uva", "laranja"]

if fruta in frutas:
    print("Tem na lista")

if "uva" in frutas:
    print("Não tem uva")

# 4. Operadores de identidade (checam se duas variáveis apontam para o mesmo objeto na memória)
x = None

if x is None:
    print("x não definido")

y = []
if y is not None:
    print("y existe")
    
# 5. Operadores Bitwise (trabalham no nível dos bits)
a = 6 # 110 em binário
b = 3 # 011 em binário

if a & b: # 110 & 011 = 010 => 2 (True) 
    print("a e b têm bits em comum")

if a | b: # 110 | 011 = 111 -> 7 (True)
    print("pelo menos um bit é 1")
    
# 6. Bitwise com booleanos
x = True
y = False

if x & y:   # AND bit a bit -> False
    print("ambos verdadeiros")

if x | y:   # OR bit a bit -> True
    print("pelo menos um verdadeiro")

if x ^ y:   # XOR -> True (um ou outro, mas não os dois)
    print("um é verdadeiro, outro é falso")
    
# 7. Operador ternário
idade = 17
status = "Maior" if idade >= 18 else "Menor"
print(status)

# 8. Match case - Python 3.10+ (usado como o switch em outras linguagens)
idade = 26

match idade:
    case 18:
        print("Tem 18 anos")
    case 26:
        print("Tem 26 anos")
    case _:
        print("Outra idade")