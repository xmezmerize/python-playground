📘 Lista de Exercícios — Try / Except / Else / Finally
1. Captura de erro simples

Peça para o usuário digitar um número e tente convertê-lo com int().

Se der erro de conversão (ValueError), mostre "Digite apenas números!".

Caso contrário, mostre "Você digitou {num}".

2. Erro de divisão por zero

Crie uma função dividir(a, b) que retorna a / b.

Trate o erro de divisão por zero (ZeroDivisionError) e retorne uma mensagem amigável.

Teste com (10, 2) e (10, 0).

3. Vários excepts

Dado:

valores = ["10", "abc", None, 0]


Para cada valor, tente converter para inteiro e dividir 100 por ele.

Capture e trate separadamente ValueError, TypeError e ZeroDivisionError.

Exiba mensagens específicas para cada erro.

4. Usando else

Peça um número ao usuário.

Se a conversão para int for bem-sucedida, mostre "Número válido".

Se der erro (ValueError), mostre "Entrada inválida".

Use else para rodar o código apenas quando não houver exceção.

5. Usando finally

Implemente um programa que abre um arquivo chamado "dados.txt".

Se o arquivo não existir, capture o FileNotFoundError.

No bloco finally, mostre "Encerrando execução".

Mesmo com erro, o finally deve ser executado.

6. Tratamento genérico

Implemente uma função executar_codigo(codigo: str) que recebe um comando em string e tenta executar com eval(codigo).

Se ocorrer erro, capture de forma genérica (except:) e retorne "Erro ao executar".

Teste com "10+5" e "abc+2".

7. Função robusta

Crie a função pega_valor(dic, chave) que:

Retorna dic[chave] se a chave existir.

Se não existir, capture KeyError e retorne "Chave não encontrada".

Se dic não for um dicionário, capture TypeError e retorne "Tipo inválido".

Teste com:

dic = {"nome": "Pedro"}
print(pega_valor(dic, "nome"))
print(pega_valor(dic, "idade"))
print(pega_valor(123, "idade"))

8. Simulação de login

Um sistema pede usuário e senha:

usuarios = {"admin": "1234"}


Se o usuário não existir no dicionário, capture KeyError.

Se a senha não bater, levante (raise) um ValueError e trate.

Se tudo certo, mostre "Login bem-sucedido!".

9. Tratamento múltiplo semi-genérico

Crie a função dividir(a, b) que tenta converter os parâmetros para inteiro e dividir.

Trate especificamente ValueError e ZeroDivisionError.

Para qualquer outro erro, use um except genérico.

Exiba mensagens diferentes para cada caso.

10. Programa final — robusto

Monte um mini-calculador:

Peça dois números (input).

Peça a operação (+, -, *, /).

Trate todos os erros possíveis:

Entrada inválida (ValueError),

Divisão por zero,

Operador inválido.

Use else para exibir o resultado quando não houver erros.

Use finally para exibir "Programa finalizado".