# Lista de exercícios - Conjuntos

> 1. Conjunto de Divisores em Engenharia Estrutural

Um engenheiro precisa calcular os pontos de apoio possíveis para uma viga metálica de 60 metros.
Os apoios só podem ser posicionados em divisões exatas do comprimento da viga (ex.: 2, 3, 4, 5…).

a. Crie um conjunto com todos os divisores de 60.

b. Agora, outro engenheiro sugere usar uma viga de 84 metros.
- Monte o conjunto de divisores de 84.

c.Determine:
- Quais divisores são comuns aos dois comprimentos (apoios viáveis para ambos os projetos).
- O maior divisor comum (MDC).
- Se os divisores de 60 estão contidos nos de 84 (subconjunto).

---

> 2. Conjuntos Numéricos em Modelagem Matemática

Um pesquisador estuda padrões em três conjuntos de números dentro do intervalo de 1 a 100:

A: todos os números pares.
B: todos os múltiplos de 3.
C: todos os quadrados perfeitos.

Ele precisa responder:

- Quais números estão ao mesmo tempo em A e B?
- Quais múltiplos de 3 não são pares?
- Quais quadrados perfeitos pertencem também a A ou a B?

---

> 3. Vocabulário de Textos Científicos

Dois alunos escrevem relatórios sobre “Computação e Matemática”.

O texto 1 contém as palavras:
    "ciência, computação, matemática, álgebra, conjuntos, probabilidade, dados".

O texto 2 contém as palavras:
    "ciência, conjuntos, lógica, análise, estatística, computação, modelos".

Perguntas:

- Quais palavras são comuns aos dois textos (interseção)?
- Quais são exclusivas de cada texto?
- Qual o conjunto total de palavras diferentes usadas pelos dois alunos?
- Quantas palavras únicas cada aluno utilizou?

---

> 4. Teorema de De Morgan Aplicado

Em um estudo de biologia, o conjunto universal U representa 1 a 50 espécies de plantas catalogadas.

Dois grupos foram observados:

A: espécies que vivem em solos úmidos.
B: espécies que vivem em solos arenosos.

O biólogo deseja verificar computacionalmente as Leis de De Morgan:

- O complemento da união (¬(A ∪ B)) é igual à interseção dos complementos (¬A ∩ ¬B)?
- O complemento da interseção (¬(A ∩ B)) é igual à união dos complementos (¬A ∪ ¬B)?

Monte conjuntos aleatórios para A e B (subconjuntos de 1 a 50) e teste essas propriedades.

---

> 5. Frequência de Caracteres em Genômica

Um biólogo recebe a sequência de DNA:

"ATCGATCGAACCTGGAATTCCG"

Ele deseja identificar:

- O conjunto das bases nitrogenadas distintas presentes na sequência.
- Quantas vezes cada base aparece.
- Se todas as bases possíveis (A, T, C, G) estão representadas.
- Qual base ocorre com maior frequência.

---

> 6. Probabilidade em Jogos de Dados

Um cientista da computação quer simular o lançamento de 1000 dados de 6 faces.

Com base na simulação:

- Construa o conjunto de valores distintos que apareceram.
- Verifique se todos os elementos de {1, 2, 3, 4, 5, 6} apareceram ao menos uma vez.
- Exiba quais valores não apareceram.
- Calcule a frequência relativa de cada valor (probabilidade empírica).

> 7. Conjuntos de Sensores Climáticos

Três sensores de temperatura registraram medidas em diferentes horários:

sensor1 = {21.5, 22.0, 23.1, 24.0}
sensor2 = {22.0, 23.1, 25.2}
sensor3 = {20.9, 21.5, 23.1, 26.3}


Responda:

- Quais temperaturas foram captadas por todos os sensores?
- Quais foram captadas por pelo menos um sensor (união)?
- Quais foram exclusivas do sensor 3?

> 8. Análise de Plágio em Textos

Dois alunos entregaram trabalhos.
Monte conjuntos com as palavras de cada texto e calcule o índice de semelhança:

Índice = |A ∩ B| ÷ |A ∪ B|

- Se o índice ≥ 0.7 → “Plágio suspeito”.
- Se 0.4 ≤ índice < 0.7 → “Alto nível de similaridade”.
- Se índice < 0.4 → “Textos distintos”.

> 9. Crivo de Eratóstenes (Versão com Sets)

Implemente o algoritmo clássico para encontrar números primos até 100:

- Construa o conjunto U = {2, 3, 4, ..., 100}.
- Iterativamente, selecione o menor número do conjunto, adicione-o aos primos e remova seus múltiplos de U.
- Ao final, exiba o conjunto dos primos encontrados.

>10. Álgebra Relacional com Sets

Dois bancos de dados simplificados estão representados como conjuntos:

alunos = {("João", "Engenharia"), ("Maria", "Medicina"), ("Ana", "Engenharia")}
cursos = {("Engenharia", "Sala 101"), ("Medicina", "Sala 202")}


Perguntas:

- Quais alunos têm correspondência de curso e sala?
- Algum aluno está matriculado em curso sem sala definida?
- Gere uma visão final com pares (Aluno, Curso, Sala).