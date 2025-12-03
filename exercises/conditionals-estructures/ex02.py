"""
2 - calculando o tempo total do trajeto
Use variáveis para criar 3 inputs para o usuário
digitar o número de dias gastos para atividades.
Depois use estruturas condicionais para validar 
o tempo total gasto para realizar as 3 tarefas.
Obs. Não existe tempo negativo.
"""

atv_a = int(input('Digite o número de dias para a atividade A: '))
atv_b = int(input('Digite o número de dias para a atividade B: '))
atv_c = int(input('Digite o número de dias para a atividade C: '))

"""
if atv_a <= 0 or atv_b <= 0 or atv_c <= 0:
    print('Erro! Não é possível ter valores negativos ou nulos.')
else:
    total_dias = atv_a + atv_b + atv_c
    print(f'O total de dias é de {total_dias} dias para realizar as 3 tarefas.')
"""

# usando ternário
total_dias = (
    'Erro! Não é possível ter valores negativos ou nulos'
    if atv_a <= 0 or atv_b <= 0 or atv_c <= 0
    else f'O total de dias é de {atv_a + atv_b + atv_c} dias para realizar as 3 tarefas.'
)

print(total_dias)