# Lista de exercícios - Tuplas

> 1. Coordenadas no plano cartesiano

Um geógrafo registra as coordenadas de duas cidades em forma de tuplas:

    cidadeA = (2, 5)  
    cidadeB = (8, 12)

- Calcule a distância euclidiana entre as cidades.
- Determine o ponto médio entre elas.
- Verifique em qual quadrante cada cidade se encontra.

---

> 2. Vetores 3D em Física

Um físico representa dois vetores no espaço como tuplas:

    v1 = (3, -2, 5)  
    v2 = (1, 4, -2)

- Calcule o produto escalar (v1 · v2).
- Calcule o vetor resultante da soma v1 + v2.
- Determine o módulo de cada vetor.

---

> 3. Sistema de equações lineares

Um economista modela um sistema linear com duas equações e duas incógnitas:

    2x + 3y = 8  
    x - y = 2

Armazene os coeficientes em tuplas:

    eq1 = (2, 3, 8)  
    eq2 = (1, -1, 2)

- Resolva o sistema pelo método da substituição ou determinantes (Cramer).
- Exiba o par ordenado (x, y) como tupla solução.

---

> 4. Movimentos em um tabuleiro (interpretação lógica)

Um jogo de tabuleiro define movimentos como deslocamentos (dx, dy).
Exemplo:

    movimentos = [(0,1), (1,0), (0,-1), (-1,0)]

Eles representam cima, direita, baixo e esquerda.

- Dada a posição inicial (2,2), aplique uma sequência de movimentos.
- Exiba a posição final.
- Verifique se o jogador voltou à posição inicial.

---

> 5. Tuplas em estatística

Um pesquisador coleta pares (idade, altura) de 8 pessoas:

    dados = [(15, 1.60), (16, 1.62), (17, 1.65), (18, 1.70),  
        (19, 1.72), (20, 1.74), (21, 1.75), (22, 1.76)]

- Calcule a média das alturas.
- Encontre a idade da pessoa mais alta.
- Transforme os dados em duas listas separadas: uma de idades e outra de alturas.

---

> 6. Distâncias entre pontos (aplicação científica)

Um drone captou quatro pontos no espaço representados por tuplas 3D:

    pontos = [(1,2,3), (4,5,6), (7,8,9), (2,3,4)]

- Calcule a distância entre cada par de pontos.
- Determine o par mais próximo entre si.
- Determine o par mais distante.

---

> 7. Função polinomial como tuplas de coeficientes

Um polinômio é representado pela tupla:

    p = (2, -3, 0, 5)  # 2 - 3x + 0x² + 5x³

- Calcule o valor de p(x) para x = 2.
- Construa uma função que receba a tupla e devolva sua derivada também em forma de tupla.
Exemplo: (2, -3, 0, 5) → (-3, 0, 15).

---

> 8. Compressão de imagens (modelagem simplificada)

Uma imagem em preto e branco pode ser representada como uma lista de tuplas (x, y) onde 1 indica pixel ligado.
Exemplo:

    pixels = [(0,0), (0,1), (1,0), (1,1)]

- Armazene os pixels ligados de uma figura simples (ex.: quadrado 3x3).
- Calcule o conjunto de vizinhos ativos de cada pixel.
- Determine se a figura é conexa (se todos os pixels estão interligados por vizinhos).

---

> 9. Tuplas em registros experimentais

Um laboratório armazena resultados de ensaios em tuplas:

    ensaios = [
        ("amostra1", 3.45, True),
        ("amostra2", 2.98, False),
        ("amostra3", 3.10, True),
        ("amostra4", 3.60, True)
    ]

Cada tupla representa (nome, valor, aprovado).

- Liste apenas as amostras aprovadas.
- Calcule a média dos valores das aprovadas.
- Verifique qual amostra possui o maior valor e exiba seus dados.

---

> 10. Trajetória em movimento uniformemente acelerado

Um físico registrou posições (tempo, posição) de um corpo:

    dados = [(0, 0), (1, 5), (2, 20), (3, 45), (4, 80)]

- Calcule as velocidades médias entre intervalos consecutivos.
- Calcule as acelerações médias entre intervalos.
- Determine se o movimento é uniformemente acelerado.