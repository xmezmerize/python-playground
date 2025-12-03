# Lista Progressiva de Exercícios com String

> 1. Limpeza de entrada de usuário

Um formulário recebe:

    nome = "   seu_nome   "

- Remova espaços extras.
- Converta para maiúsculo.
- Exiba "NOME" type <str> .

Dica: use .strip() e .upper().

---

> 2. Contagem de letras específicas

Dada a frase:

    frase = "Python é poderoso"

- Conte quantas vezes aparece a letra "o".
- Verifique se a frase termina com "so".

Dica: .count() e .endswith().

---

> 3. Relatório resumido

    texto = "O experimento apresentou FALHAS graves"

- Coloque tudo em minúsculo.
- Troque "falhas" por "ajustes".
- Capitalize o resultado.

---

> 4. Normalização de lista de palavras

    palavras = ["  casa", "Carro ", "peDRo"]

- Limpe espaços.
- Coloque todas no formato .title().
- Gere nova lista.

---

> 5. Extração de domínio de e-mails

    emails = ["ana@gmail.com", "pedro@yahoo.com", "joao@outlook.com"]

- Extraia apenas o domínio (gmail.com, yahoo.com, …).
- Exiba uma lista com os domínios únicos.

Dica: .split("@"), set().

---

> 6. Senha forte

Valide se "P@ssword123" atende:

- ≥ 8 caracteres,
- Tem maiúsculas, minúsculas, dígitos e caractere especial.

Exiba mensagens de erro específicas caso falte algo.

---

> 7. Mutação genética

    dna = "ATCGTAGCTAGGCTAATCG"

- Conte quantas vezes aparece "ATC".
- Substitua "TAG" por "XXX".
- Exiba em blocos de 3 caracteres.

Dica: use range(0, len(dna), 3).

---

> 8. Palíndromos múltiplos

Escreva uma função que receba:

    ["radar", "ana", "python", "osso"]

E retorne apenas os palíndromos.

> 9. Tabela de dados formatada

    dados = ["Aluno1: 7.5", "Aluno2: 9.3", "Aluno3: 5.75"]

- Separe nome e valor.
- Formate as notas com 2 casas decimais.
- Exiba em tabela alinhada:

    Aluno1  |  7.50
    Aluno2  |  9.30
    Aluno3  |  5.75

---

> 10. Logs de servidor

    log = "2025-09-30 14:05:22 | ERROR | Falha no sistema"

- Separe em: data, hora, nível, mensagem.
- Converta data para 30/09/2025.
- Exiba em linhas com rótulos.

---

> 11. Dicionário de frequência

    texto = "Dados são o novo petróleo, mas dados limpos são ouro."

- Conte a frequência de cada palavra (ignorando maiúsculas/minúsculas).
- Exiba o dicionário ordenado por frequência.

Dica: use .lower(), .split(), dict().

---

> 12. Encriptador personalizado

Transforme "seguranca" substituindo:

- a→@, e→3, i→!, o→0, u→#.

Resultado esperado: "s3g#r@nc@".

---

> 13. Colorindo saída no terminal

Use a biblioteca colorama para exibir:

- "ERRO" em vermelho,
- "AVISO" em amarelo,
- "SUCESSO" em verde.

Exemplo esperado:

    [ERRO] Falha no sistema
    [AVISO] Atenção ao limite
    [SUCESSO] Operação concluída

---

> 14. Mini parser de CSV (texto)

Dado:

    csv = "nome,idade\nAna,20\nPedro,25\nJoão,22"

- Separe em linhas.
- Crie lista de dicionários:

    [{"nome": "Ana", "idade": "20"}, ...]

- Exiba cada linha formatada: "Ana tem 20 anos."

---

> 15. Relatório Inteligente (final)

Receba um parágrafo:

    texto = "O experimento com amostras foi bem-sucedido, mas apresentou falhas em alguns casos."

- Limpe e padronize em minúsculo.
- Conte frequência de palavras.
- Mostre as 3 mais usadas.
- Exiba o texto original justificado em 50 caracteres.
- Mostre um resumo colorido com colorama:
    - Palavras mais usadas em amarelo,
    - Texto final em verde.