# Exercícios de Estruturas Condicionais e Operadores

## 🔹 Bloco 1 

>1.
Em uma competição escolar de matemática, dois alunos chegaram à final. O professor anotou as notas de cada um: João obteve 72 pontos e Maria 85.
Elabore um programa que receba duas notas inteiras e determine qual dos dois candidatos teve o melhor desempenho. Caso os dois tenham obtido a mesma nota, informe que houve empate.

>2.
Um aplicativo de cadastro exige que o usuário seja maior de idade para completar o registro.
Escreva um programa que receba a idade de uma pessoa e informe se ela já pode se cadastrar no sistema ou não.

>3.
Na organização de uma olimpíada esportiva, os participantes recebem um número de identificação. Para fins de logística, a coordenação precisa separar os números pares para alojamentos masculinos e os ímpares para alojamentos femininos.
Escreva um programa que, dado um número inteiro, classifique-o como “par” ou “ímpar”.

>4.
Um caixa eletrônico somente libera notas de R$ 10 em diante, e o valor solicitado precisa ser múltiplo de 10.
Escreva um programa que leia um valor inteiro solicitado pelo cliente e informe se o saque é válido. Se for válido, exiba “Saque liberado”, caso contrário, “Valor inválido”.

>5.
Uma pesquisa do IBGE classifica a população por faixas etárias.
Escreva um programa que, ao receber a idade de uma pessoa, classifique-a como:

- Criança (menor de 12 anos)
- Adolescente (12 a 17 anos)
- Adulto (18 a 59 anos)
- Idoso (60 anos ou mais).

## 🔹 Bloco 2 

>6.
Um vestibular exige que o candidato tenha idade mínima de 18 anos e tenha concluído o ensino médio.
Crie um programa que receba esses dois dados e verifique se o candidato pode ou não se inscrever no vestibular.

>7.
Um clube de esportes permite a entrada de associados de 18 a 35 anos. Porém, atletas profissionais podem entrar mesmo fora dessa faixa.
Elabore um programa que, dados a idade e a condição de atleta, informe se a pessoa pode se associar ou não.

>8.
Um sistema de reconhecimento de caracteres precisa diferenciar entradas de teclado.
Escreva um programa que leia um único caractere e informe se é:

- uma vogal,
- uma consoante,
- um número ou
- um símbolo.

>9.
Em um sistema de autenticação, duas senhas podem ter o mesmo valor, mas não serem o mesmo objeto na memória.
Crie um programa que leia duas senhas digitadas pelo usuário e verifique:

- Se possuem o mesmo conteúdo (==),
- Se são o mesmo objeto (is).

>10.
Uma plataforma de jogos online possui uma lista de nomes proibidos: ["admin", "root", "teste"].
Escreva um programa que leia o nome escolhido pelo jogador e verifique se está nessa lista. Se estiver, recuse o cadastro; caso contrário, permita.

## 🔹 Bloco 3 

>11.
Em uma escola, a aprovação é definida pela média de 3 provas.

- Se a média for maior ou igual a 7 → aprovado.
- Entre 5 e 6.9 → recuperação.
- Abaixo de 5 → reprovado.
- Escreva um programa que receba as três notas de um aluno e informe sua situação.

>12.
Um supermercado oferece descontos progressivos:

- Compras menores que R$ 100 → sem desconto.
- De R$ 100 a R$ 199 → 10% de desconto.
- A partir de R$ 200 → 20% de desconto.

Escreva um programa que leia o valor da compra e calcule o valor final a pagar.

>13.
Um professor propôs um desafio: dado um número inteiro, verificar se ele é múltiplo de 3 e de 5 ao mesmo tempo.
Escreva o programa que resolva esse desafio e exiba a mensagem correspondente.

>14.
Uma empresa de transportes cobra pelo peso da carga:

- Até 10 kg → R$ 10 fixo;
- Entre 11 e 20 kg → R$ 20 fixo;
- Acima de 20 kg → R$ 20 + R$ 2 por quilo extra.

Crie um programa que leia o peso da carga e calcule o valor do frete.

>15.
O calendário gregoriano define que um ano é bissexto se:

- É divisível por 4;
- Não é divisível por 100, exceto se também for divisível por 400.

Escreva um programa que receba um ano e determine se ele é ou não bissexto.

## 🔹 Bloco 4 

>16.
Uma universidade classifica os alunos com base na média final:

- ≥ 9 → Conceito A
- 7 a 8.9 → B
- 5 a 6.9 → C
- 3 a 4.9 → D
- < 3 → E

✦ Dica: use if/elif/else em cascata para organizar os intervalos.

>17.
Um estacionamento cobra:

- Primeira hora: R$ 5;
- Até 5 horas: R$ 5 + R$ 3 por hora extra;
- Acima de 5 horas: valor fixo de R$ 20.

✦ Dica: identifique primeiro se está acima de 5 horas para simplificar.

>18.
O vestibular de uma instituição funciona assim:

- Prova objetiva precisa ser ≥ 60;
- Redação precisa ser ≥ 50;
- Nota final (70% objetiva + 30% redação) precisa ser ≥ 70.

✦ Dica: calcule a média ponderada e combine as condições com and.

>19.
Uma loja online calcula o frete da seguinte forma:

- Sudeste: R$ 20;
- Sul/Nordeste: R$ 30;
- Norte/Centro-Oeste: R$ 40;
- Compras ≥ R$ 200 têm frete grátis.

✦ Dica: use in para verificar se o estado pertence a determinada região.

>20.
Um banco avalia pedidos de empréstimo com base em:

- Renda mensal ≥ R$ 3.000;
- Tempo de trabalho ≥ 2 anos;
- Nome limpo (sem restrição);
- Parcela ≤ 30% da renda.

Se todas as condições forem atendidas, o empréstimo é aprovado. Caso contrário, é negado.

✦ Dica: combine todas as regras com and. Para a parcela, use regra matemática → valor_parcela <= renda * 0.3.