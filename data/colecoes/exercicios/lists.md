# Lista de exercícios - Listas

> 1. Sequência de temperaturas diárias

Um meteorologista registrou, durante 7 dias consecutivos, as temperaturas médias:

    [21.5, 22.0, 19.8, 23.1, 24.5, 20.0, 18.7]

- Exiba a maior e a menor temperatura da semana.
- Calcule a média semanal.
- Identifique em quais dias a temperatura ficou abaixo da média.

---

> 2. Produção em uma linha de fábrica

Uma indústria produz peças ao longo do dia e armazena a produção horária em uma lista:

    [120, 135, 150, 200, 175, 160, 190, 210]


- Calcule o total produzido no dia.
- Determine o horário de maior produção.
- Gere uma nova lista com a produção acumulada (somatório progressivo).

> 3. Notas e classificação de alunos

Um professor tem a lista de notas dos alunos:

    [6.5, 8.0, 7.2, 5.9, 9.1, 4.5, 6.0]


- Calcule a média da turma.
- Separe em três listas: aprovados (≥7), recuperação (≥5 e <7) e reprovados (<5).
- Exiba a porcentagem de cada grupo em relação ao total.

---

> 4. Análise de série temporal (valores de ações)

Uma corretora tem a série de preços de uma ação ao longo de 10 dias:

    [10.5, 10.7, 10.6, 10.8, 11.0, 10.9, 11.3, 11.5, 11.4, 11.8]

- Calcule a variação absoluta entre o menor e o maior preço.
- Gere uma nova lista com as variações diárias (diferença entre o dia atual e o anterior).
- Verifique se houve 3 dias seguidos de alta.

---

> 5. Matrizes com listas aninhadas

Uma universidade armazena as notas de 3 provas para 4 alunos em forma de lista de listas:

    notas = [
        [7.5, 8.0, 6.0],  
        [5.0, 6.5, 7.0],  
        [9.0, 8.5, 7.5],  
        [6.0, 5.5, 6.5]
    ]

- Calcule a média de cada aluno.
- Calcule a média de cada prova.
- Identifique o aluno com maior desempenho global.

---

> 6. Vetores em física

Considere dois vetores representados por listas:

    v1 = [2, 3, -1]  
    v2 = [1, 0, 4]

- Calcule o produto escalar (v1 · v2).
- Gere um novo vetor correspondente à soma v1 + v2.
- Calcule o módulo (norma euclidiana) de cada vetor.

---

> 7. Polinômios representados por listas

Um polinômio pode ser representado como lista de coeficientes, onde o índice é a potência de x.
Exemplo:

    p = [2, -3, 0, 5]  # Representa 2 - 3x + 0x² + 5x³

- Escreva uma função que, dado p e um valor de x, calcule o valor do polinômio.
- Escreva outra função que retorne a derivada de p como nova lista de coeficientes.

---

> 8. Estatística de dados experimentais

Um laboratório mediu a massa (em gramas) de 12 amostras:

    [1.23, 1.20, 1.25, 1.19, 1.30, 1.27, 1.22, 1.18, 1.26, 1.21, 1.24, 1.28]

- Calcule a média e o desvio padrão (fórmula manual, não usar statistics).
- Identifique se alguma amostra está fora do intervalo média ± 2*desvio.
- Gere uma lista apenas com os valores dentro do intervalo aceitável.

---

> 9. Compressão de dados com listas

Implemente uma versão simplificada do Run-Length Encoding (RLE):
Dada uma lista com elementos repetidos, como:

    [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]

Transforme-a em:

    [(1,3), (2,2), (3,4), (4,1)]

Ou seja, cada tupla representa (valor, quantidade de repetições).

---

> 10. Simulação científica (crescimento populacional)

Um biólogo modela o crescimento de uma população de bactérias que dobra a cada hora.
O valor inicial é 100 indivíduos.

- Gere uma lista com a população nas primeiras 12 horas.
- Identifique a hora em que a população ultrapassa 10.000.
- Transforme essa lista em uma lista de razões entre populações sucessivas (para verificar a taxa de crescimento).