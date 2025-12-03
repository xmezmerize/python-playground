# Lista de Exercícios – Estruturas de Controle, repetição, lógica e tratamentos

## 🔹 Loop for 

>1.
Uma empresa de energia deseja calcular o consumo mensal de 10 clientes.
As leituras estão armazenadas em uma lista [120, 340, 560, 45, 89, 230, 600, 780, 320, 150].
Percorra a lista com for e exiba: "Cliente X consumiu Y kWh", sendo X o índice (1 a 10) e Y o valor.

>2.
Um engenheiro precisa calcular a soma dos quadrados de todos os números pares entre 1 e 50.
Implemente com for e acumule o resultado em uma variável.

>3.
Um time de basquete tem jogadores numerados de 4 a 15.
Crie um programa que percorra esses números e exiba: "Jogador X em quadra".
Destacar o número 13 como "Jogador 13 – Armador principal".

>4.
Uma empresa de logística precisa converter preços em dólares para reais.
Os preços [10.5, 22.75, 7.30, 50.0] devem ser percorridos com for.
Para cada preço, exiba o valor convertido usando a cotação R$ 5.10.
Formato: "Produto Y: R$ <valor convertido com 2 casas decimais>".

>5.
Simule um sistema de provas: uma lista contém notas [7.5, 8.0, 6.3, 9.2, 5.0].
Percorra a lista com for e exiba a situação do aluno: "Aprovado" se nota ≥ 7, "Recuperação" se entre 5 e 6.9, e "Reprovado" caso contrário.

## 🔹 Loop while (5 exercícios)

>6.
Implemente uma contagem regressiva iniciando em 20 até 0, exibindo todos os números, seguida de "FIM!".

>7.
Um caixa eletrônico deve pedir ao usuário valores para saque até que seja digitado 0.
No final, exibir o total de dinheiro sacado.

>8.
Uma empresa coleta dados de temperatura ambiente.
O sistema deve pedir entradas até que seja digitado -999.
No final, calcular a média das temperaturas válidas.

>9.
Um jogo pede que o usuário digite senhas até acertar "python123".
Exiba a cada tentativa "Senha incorreta, tente novamente...".
Quando acertar, exibir "Acesso liberado!".

>10.
Simule o cálculo de juros compostos:
Enquanto o saldo de uma aplicação de R$ 1000 não ultrapassar R$ 2000, aplique juros de 5% ao mês.
Exibir mês a mês o saldo atualizado.

## 🔹 Uso do break (5 exercícios)

>11.
Um programa deve percorrer os números de 1 a 20.
Se encontrar um múltiplo de 7, deve parar imediatamente e exibir: "Primeiro múltiplo de 7 encontrado: X".

>12.
Simule um sistema de login: o usuário pode tentar até 3 vezes.
Se acertar "admin", interromper o loop e exibir "Login bem-sucedido".
Se passar das 3 tentativas, encerrar com "Acesso bloqueado".

>13.
Um restaurante possui mesas numeradas de 1 a 15.
Percorra com for, exibindo "Mesa X disponível".
Ao chegar na mesa 8, use break para encerrar e exibir: "Apenas mesas até 8 estão em operação hoje".

>14.
Um sistema de sorteio deve gerar números de 1 a 100.
Percorra com for, mas se encontrar o número 42, interrompa imediatamente e exiba "Número premiado encontrado!".

>15.
Implemente um laço while True que peça nomes de alunos.
Ao digitar "fim", use break para encerrar.
Exibir no final quantos nomes foram cadastrados.

## 🔹 Uso do range (5 exercícios)

>16.
Exiba todos os múltiplos de 4 no intervalo de 1 a 100 usando range.

>17.
Um professor deseja exibir todos os números pares de 2 a 200.
Use range(início, parada, passo) para resolver.

>18.
Um sistema precisa exibir números de 100 até 0, de 5 em 5.
Implemente usando range com passo negativo.

>19.
Crie um programa que exiba os quadrados perfeitos dos números de 1 a 10.
Use range e potências (**2).

>20.
Uma padaria deseja calcular a produção de pães ao longo do dia:
a cada 15 minutos são feitos 50 pães, das 6h até às 12h.
Simule usando range e exiba "Hora: XhYmin → Z pães produzidos".

## 🔹 Tratamento e Exceções (5 exercícios)

>21.
Solicite dois números do usuário e exiba a divisão.
Use try/except para tratar a divisão por zero.

>22.
Peça ao usuário para digitar um número inteiro.
Use try/except para garantir que a entrada é válida.
Se não for número, exibir "Entrada inválida, tente novamente".

>23.
Crie um programa que abra um arquivo dados.txt e leia seu conteúdo.
Trate a exceção caso o arquivo não exista.

>24.
Implemente uma calculadora simples que peça dois números e uma operação (+, -, *, /).
Use try/except para evitar erros de entrada e divisão por zero.

>25.
Crie um programa que receba uma lista de notas [8, 9, 'dez', 7].
Percorra a lista e tente somar os valores.
Use try/except para ignorar valores inválidos (não numéricos).
No final, exibir a média apenas dos valores válidos.