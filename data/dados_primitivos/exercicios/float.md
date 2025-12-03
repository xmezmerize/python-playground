# Lista de exercícios - Ponto flutuante

> 1. Calibração de instrumentos de laboratório

Um laboratório de química fez 10 medições da densidade de uma mesma solução. Como os instrumentos possuem pequenas imprecisões, os valores variam levemente:

	densidades = [1.23, 1.25, 1.27, 1.22, 1.24, 1.26, 1.28, 1.21, 1.29, 1.24]


O pesquisador deseja saber:

- O valor médio das medições (média aritmética).
- O desvio padrão experimental (usando a fórmula manual, não statistics).
- Se alguma medição está fora do intervalo de confiança definido como média ± 2*desvio.

---

> 2. Estudo de crescimento populacional

Um biólogo modela o crescimento de uma população de bactérias. A cada hora, o número de indivíduos é multiplicado por 1.35 em relação à hora anterior. A população inicial é de 2.0e3 (2000).

- Gere os valores populacionais nas primeiras 12 horas.
- Armazene cada resultado em uma lista de float.
- Descubra em qual hora a população ultrapassa 1.0e6.

---

> 3. Análise de notas em uma turma

Uma turma de 12 alunos obteve as seguintes notas em uma prova:

	notas = [5.5, 7.0, 8.5, 6.0, 9.0, 7.5, 10.0, 4.0, 6.5, 8.0, 9.5, 3.5]

O professor deseja:

- Calcular média, mediana e variância das notas.
- Normalizar os valores entre 0 e 1 (para usar em um modelo de aprendizado de máquina).
- Produzir uma distribuição de frequência em 5 faixas (0–2, 2–4, …, 8–10).

---

> 4. Juros compostos e projeções financeiras

Um investidor aplica R$ 50.000,00 em um título com rendimento de 0,8% ao mês.

- Monte uma tabela mês a mês (até 24 meses) mostrando o saldo atualizado.
- Identifique o mês em que o saldo ultrapassa R$ 60.000,00.
- Calcule a diferença entre o saldo obtido e o saldo que teria sido gerado caso fossem juros simples.

---

> 5. Aproximação de π por séries infinitas

Um matemático utiliza a série de Leibniz para aproximar π:

	𝜋 ≈ 4 ⋅ ( 1 − 1/3 + 1/5 − 1/7 + 1/9 − ...)

- Implemente a série até 10.000 termos usando float.
- Compare o resultado com math.pi.
- Exiba o erro absoluto.
- Mostre como o erro diminui à medida que aumentamos o número de termos.

---

> 6. Cálculo de energia em física

Um objeto de 10 kg é lançado com velocidades distintas (em m/s) armazenadas em uma lista:

	velocidades = [5.0, 12.0, 20.0, 25.5, 30.0]

- Calcule a energia cinética para cada velocidade (Ec = 0.5 * m * v²).
- Gere uma lista com os valores de energia cinética.
- Descubra a velocidade mínima necessária para que a energia ultrapasse 3000 J.

---

> 7. Método numérico para raízes

Um engenheiro precisa calcular √7 com precisão de 6 casas decimais sem usar math.sqrt.

- Implemente o método de Newton-Raphson para calcular a raiz.
- Mostre as aproximações passo a passo até a convergência.
- Compare com o valor retornado por math.sqrt(7).

---

> 8. Temperatura em escala científica

Um físico registrou temperaturas em Fahrenheit de uma reação química:

	valores_f = [98.6, 120.5, 212.0, 32.0, 451.0]


- Converta todos os valores para Celsius.
- Converta todos os valores para Kelvin.
- Determine o valor médio em cada escala.

---

> 9. Integração numérica (regra do trapézio)

Um matemático quer aproximar a integral:

 	 1
	∫ 𝑒^𝑥 𝑑𝑥
 	 0

- Divida o intervalo [0,1] em 100 subintervalos.
- Aplique a regra do trapézio com floats.
- Compare com o valor real math.e - 1.

---

> 10. Simulação de queda livre

Um objeto é solto de uma altura de 100 metros, desprezando resistência do ar. A fórmula da posição em função do tempo é:

ℎ(𝑡) = ℎ − 1/2𝑔𝑡^2 
	   0​      

com g = 9.8 m/s².

- Calcule a altura do objeto a cada segundo até atingir o solo.
- Descubra em qual segundo ele toca o chão.
- Calcule a velocidade do objeto nesse instante.

---

> 11. Estatística de medições (float)

Um laboratório mediu a densidade de uma substância 8 vezes:

    valores = [1.23, 1.25, 1.27, 1.22, 1.24, 1.26, 1.28, 1.21]

- Calcule a média aritmética.
- Calcule a variância e o desvio padrão (fórmulas manuais).
- Determine se há algum valor fora do intervalo média ± 2*desvio.

---

> 12. Juros compostos (float)

Um investidor aplica R$ 10.000,00 a uma taxa de 1,2% ao mês.

- Calcule o valor acumulado após 12 meses.
- Gere uma lista com o saldo mês a mês.
- Determine em qual mês o valor ultrapassa R$ 12.000.

---

> 13. Distâncias em física (float)

Um carro percorre posições medidas a cada segundo:

	posicoes = [0.0, 2.5, 10.0, 22.5, 40.0]

- Calcule as velocidades médias entre cada par de pontos.
- Calcule as acelerações médias.
- Determine se o movimento é uniformemente acelerado.

---

> 14. Criptografia com inteiros (RSA simplificado)

Um professor introduz RSA com pequenos números:

	p = 17, q = 23.

	n = p * q.

	φ(n) = (p-1)*(q-1).

Escolha e = 3 tal que mdc(e, φ(n)) = 1.

- Calcule a chave pública (e, n).
- Encontre a chave privada d tal que (d*e) % φ(n) = 1.
- Encripte a mensagem m = 42 e depois descriptografe.

> 15. Aproximação de raízes (float, método numérico)

Um engenheiro deseja calcular a raiz quadrada de 2 sem usar math.sqrt.

- Implemente o método de Newton-Raphson para encontrar √2.
- Mostre as 10 primeiras aproximações.
- Compare o resultado com math.sqrt(2).

> 16. Distribuição de notas (float)

Uma turma teve as seguintes notas:

	notas = [5.5, 7.0, 8.5, 6.0, 9.0, 7.5, 10.0, 4.0, 6.5, 8.0]

- Calcule média, mediana e moda.
- Normalize as notas para ficarem entre 0 e 1.
- Gere um histograma textual (faixas de 0.0–0.2, 0.2–0.4, etc.) mostrando quantos alunos caem em cada intervalo.