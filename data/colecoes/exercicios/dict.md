# Lista de exercícios - Dicionários

> 1. Frequência de caracteres em um texto

Um criptógrafo deseja analisar a ocorrência de letras em uma mensagem secreta:

    mensagem = "A matemática é a linguagem com que Deus escreveu o universo"


- Construa um dicionário onde cada chave é uma letra e o valor é a quantidade de vezes que ela aparece.
- Identifique a letra mais frequente.
- Compare se as vogais aparecem mais do que as consoantes.

---

> 2. Votos em uma eleição estudantil

Uma urna registrou os votos em uma lista de candidatos:

    votos = ["Ana", "Pedro", "Ana", "Carla", "Pedro", "Ana", "Carla", "Pedro", "Pedro"]

- Construa um dicionário com o total de votos de cada candidato.
- Determine o candidato vencedor.
- Exiba a porcentagem de cada candidato em relação ao total.

---

> 3. Dicionário de funções matemáticas

Um professor deseja armazenar funções em um dicionário:

    funcoes = {
        "quadrado": lambda x: x**2,
        "cubo": lambda x: x**3,
        "raiz": lambda x: x**0.5
    }

- Peça um número ao usuário e aplique todas as funções armazenadas.
- Gere uma tabela com o resultado de cada função para x = 1 a 10.

---

> 4. Frequência de palavras em um texto científico

Um pesquisador analisa um parágrafo:

    texto = "Python é usado em ciência de dados, ciência da computação, física e estatística"

- Construa um dicionário que mapeie cada palavra para o número de vezes que aparece.
- Liste as três palavras mais frequentes.
- Verifique se a palavra "ciência" aparece em mais de uma forma (ex.: com maiúscula e minúscula).

---

> 5. Banco de notas de uma turma

Um professor organiza as notas de alunos em um dicionário:

    notas = {
        "Ana": [7.5, 8.0, 6.0],
        "Pedro": [6.0, 5.5, 6.5],
        "Carla": [9.0, 8.5, 7.5]
    }

- Calcule a média de cada aluno.
- Determine o aluno com maior média.
- Gere um novo dicionário apenas com os aprovados (média ≥ 7).

---

> 6. Dicionário de coordenadas em Física

Um experimento registra posições de partículas em 3 instantes:

    dados = {
        "t1": (2, 3, 1),
        "t2": (4, 7, 2),
        "t3": (7, 13, 3)
    }

- Calcule a distância percorrida entre cada par consecutivo de tempos.
- Gere um dicionário com as velocidades médias entre os instantes.
- Determine se o movimento é acelerado ou uniforme.

---

> 7. Grafo representado por dicionários

Um sistema de transporte pode ser representado como grafo:

    rotas = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"]
    }

- Liste todos os vizinhos de cada vértice.
- Verifique se existe caminho entre "A" e "F".
- Encontre o vértice com maior grau (mais conexões).

---

> 8. Estoque de uma farmácia

Um sistema armazena os medicamentos e suas quantidades:

    estoque = {"dipirona": 20, "paracetamol": 15, "ibuprofeno": 10}

- Simule uma compra: peça ao usuário o nome do medicamento e a quantidade.
- Atualize o estoque, validando se há quantidade suficiente.
- Exiba os medicamentos que ficaram abaixo de 5 unidades (estoque crítico).

---

> 9. Análise de dicionário aninhado (dados experimentais)

Um laboratório registra resultados em estrutura aninhada:

    experimentos = {
        "ensaio1": {"temp": 20, "pressao": 1.2, "resultado": True},
        "ensaio2": {"temp": 25, "pressao": 1.5, "resultado": False},
        "ensaio3": {"temp": 22, "pressao": 1.3, "resultado": True}
    }

- Liste apenas os ensaios com resultado positivo.
- Calcule a média de temperatura dos ensaios válidos.
- Identifique o ensaio com maior pressão registrada.

---

> 10. Dicionário de polinômios

Um matemático deseja representar polinômios como dicionários, onde a chave é o grau e o valor é o coeficiente:

    p = {0: 2, 1: -3, 3: 5}   # 2 - 3x + 5x³

- Calcule o valor de p(x) para um dado x.
- Construa a derivada de p também como dicionário.
- Some dois polinômios representados dessa forma.