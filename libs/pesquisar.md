📚 Bibliotecas de Matemática, Engenharia e Física em Python
1. Nível Fundamental – Matemática de Base
🔹 math (nativo)

Funções matemáticas elementares.

Principais:

math.sqrt(x) → raiz quadrada

math.factorial(n) → fatorial

math.gcd(a, b) / math.lcm(a, b) → MDC / MMC

math.sin, math.cos, math.tan, math.pi, math.e

math.log(x, base) → logaritmo

🔹 decimal

Números decimais com alta precisão (útil em finanças).

Ex.: Decimal('0.1') + Decimal('0.2') → 0.3 (exato).

🔹 fractions

Trabalha com frações exatas.

Ex.:

from fractions import Fraction
Fraction(3, 4) + Fraction(2, 3)  # 17/12

🔹 statistics (nativo)

Estatística descritiva.

Média, mediana, moda, variância, desvio padrão.

2. Nível Numérico – Computação Científica
🔹 NumPy

Base do Python científico.

Vetores, matrizes, álgebra linear.

Operações vetorizadas super rápidas.

Exemplos:

import numpy as np
A = np.array([[1, 2], [3, 4]])
np.linalg.inv(A)   # inversa da matriz
np.dot([1, 2], [3, 4])  # produto escalar

🔹 SciPy

Extensão do NumPy para engenharia e ciência.

Módulos principais:

scipy.integrate → integrais numéricas.

scipy.optimize → otimização (mínimos/máximos).

scipy.fft → transformadas de Fourier.

scipy.signal → processamento de sinais.

scipy.linalg → álgebra linear avançada.

scipy.stats → estatística avançada.

🔹 mpmath

Cálculo numérico com precisão arbitrária.

Ótimo para problemas com muitos dígitos.

3. Nível Simbólico – Matemática Exata
🔹 SymPy

Cálculo simbólico (manipulação algébrica, como no papel).

Exemplos:

from sympy import symbols, diff, integrate, solve, sin

x = symbols('x')
diff(x**2, x)         # derivada → 2x
integrate(sin(x), x)  # integral → -cos(x)
solve(x**2 - 4, x)    # equação → [-2, 2]


Pode gerar LaTeX, ótimo para relatórios.

Inclui módulo de física simbólica (SymPy.physics).

4. Engenharia – Aplicações Diretas
🔹 Matplotlib

Visualização de dados, gráficos 2D.

Ex.: funções matemáticas, gráficos de engenharia.

🔹 Pandas

Tabelas e séries temporais.

Útil para engenharia de dados e experimentos.

🔹 OpenCV

Processamento de imagens e visão computacional.

Muito usado em engenharia elétrica, automação e robótica.

🔹 PyDy

Dinâmica de sistemas mecânicos.

Baseado em SymPy + NumPy.

Simulação de corpos rígidos e sistemas dinâmicos.

🔹 FEniCS

Método dos Elementos Finitos (FEM).

Resolve PDEs (equações diferenciais parciais) em engenharia.

🔹 Abaqus / ANSYS Python APIs

Não são bibliotecas puras do Python, mas interfaces para softwares de simulação estrutural usados em engenharia.

5. Física – Modelagem e Simulação
🔹 Astropy

Voltada para astronomia e astrofísica.

Conversão de unidades, coordenadas, tempo astronômico, espectros.

🔹 Pint

Gerenciamento de unidades físicas (SI, CGS etc).

Ex.: 3 * u.meter / u.second → 3 m/s.

🔹 SymPy.physics

Submódulo de SymPy para fórmulas físicas.

Inclui mecânica quântica, ótica, eletromagnetismo.

🔹 Quantum Libraries

Qiskit (IBM) → computação quântica.

QuTiP → simulação de sistemas quânticos.

🔹 PlasmaPy

Biblioteca para física de plasmas.

🔹 EinsteinPy

Relatividade geral e cosmologia.

Tensores, geodésicas, buracos negros.

6. Avançado – Computação Numérica e IA
🔹 JAX

Da Google, focada em diferenciação automática.

Usa GPU/TPU para cálculos de álgebra linear.

🔹 TensorFlow / PyTorch

Inicialmente para IA, mas usados em cálculo numérico massivo.

Suportam tensores, autograd, otimização.

🔹 Theano (mais antigo, mas acadêmico)

Precursor dos frameworks modernos.

🚀 Linha de Estudo Recomendada

Começo (base matemática)
→ math, decimal, fractions, statistics.

Computação científica
→ NumPy → SciPy.

Matemática simbólica
→ SymPy.

Engenharia aplicada
→ Matplotlib, Pandas, PyDy, FEniCS.

Física aplicada
→ Astropy, Pint, SymPy.physics, EinsteinPy.

Avançado / Pesquisa
→ JAX, PyTorch, TensorFlow.

👉 Esse é o arsenal completo pra Matemática, Engenharia e Física com Python.
Com isso você consegue:

resolver exercícios de cálculo → SymPy,

simular sistemas mecânicos → PyDy,

trabalhar com unidades físicas → Pint,

estudar até relatividade → EinsteinPy.