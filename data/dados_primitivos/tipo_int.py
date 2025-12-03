# Tipo Inteiro (int)

# =================================================================================================================== #

"""
O que é um número inteiro

Em matemática, um número inteiro pertence ao conjunto dos ℤ (inteiros):

𝑍 = {...,-3,-2,-1,0,1,2,3,...}

Em Python, qualquer valor desse conjunto é representado pelo tipo int.
Diferente de linguagens como C ou Java, em Python o inteiro não tem 
tamanho fixo (32 bits, 64 bits, etc.): o limite é a memória disponível da máquina.
"""

# =================================================================================================================== #

# Formas de escrita -> Inteiros podem ser escritos diretamente:

x = 42
y = -17
z = 0

# Para melhorar a leitura, é permitido usar underscores (_) como separador:

num = 1_000_000   # equivalente a 1000000

# Inteiros podem ser representados em outros sistemas numéricos:

# Decimal(padrão): 42

# Binário: 0b101010

# Octal: 0o52

# Hexadecimal: 0x2A

# =================================================================================================================== #

# Armazenamento em memória

"""
Em Python, todo dado é um objeto. O int também é um objeto da classe int.
Isso significa que: Ele tem um identificador único na memória (id() mostra isso).
Ele possui atributos e comportamentos herdados da classe int.
"""

# =================================================================================================================== #

# Características importantes

"""
Não possui casas decimais → se precisar de decimais, use float ou Decimal.
Suporta valores negativos e positivos, incluindo zero.
Não tem limite fixo → pode armazenar números enormes (ex.: 10**1000).
É imutável → uma vez criado, não pode ser alterado, apenas substituído.
"""

# Exemplo de imutabilidade:

a = 5
print(id(a))  # endereço na memória
a = a + 1
print(id(a))  # endereço muda, porque criou um novo objeto

# =================================================================================================================== #

# Conversão para inteiro

"""
Podemos transformar outros tipos em inteiros:
De string numérica: int("42") → 42
De float: int(3.9) → 3 (trunca, não arredonda)
De booleano: int(True) → 1, int(False) → 0
"""