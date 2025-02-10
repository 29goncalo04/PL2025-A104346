# Somador_On_Off

## Autor
Gonçalo Oliveira Cruz (A104346)

## Descrição

O "Somador_On_Off" é um programa em Python que analisa uma string fornecida e soma todas as sequências numéricas encontradas entre as marcações "on" e "off".  
O programa obedece às seguintes regras:

- **Início da Soma:**  
  Sempre que a string `"on"` (em qualquer combinação de maiúsculas e minúsculas) for encontrada, o modo de soma é ativado.

- **Fim da Soma:**  
  Sempre que a string `"off"` (em qualquer combinação de maiúsculas e minúsculas) for encontrada, o modo de soma é desativado.  
  Caso haja uma sequência numérica em construção no momento, ela é convertida para inteiro e somada ao valor da soma total.

- **Exibição do Resultado:**  
  Sempre que o caractere `"="` for encontrado, o programa imprime o resultado da soma acumulada até o momento.

## Enunciado

> **Somador on/off: criar o programa em Python**  
> Pretende-se um programa que some todas as sequências de dígitos que encontre num texto:
> - Sempre que encontrar a string `"off"` em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado.
> - Sempre que encontrar a string `"on"` em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado.
> - Sempre que encontrar o caractere `"="`, o resultado da soma é colocado na saída.

## Funcionamento do Código

O programa consiste na função `main()` que realiza as seguintes etapas:

1. **Leitura da Entrada:**  
   - Solicita uma string do usuário e converte-a para minúsculas com `.lower()`.

2. **Inicialização de Variáveis:**  
   - `soma`: Variável que acumula a soma total das sequências numéricas.
   - `soma_ativa`: Flag (booleano) que indica se o modo de soma está ativo (inicialmente `False`).
   - `numero_atual`: String que armazena os dígitos consecutivos, formando um número enquanto o modo de soma estiver ativo.
   - `i`: Índice para percorrer cada caractere do texto.

3. **Processamento do Texto (Loop `while`):**  
   - O loop percorre a string caractere por caractere.
   - Quando o caractere `"o"` é encontrado, o código verifica se a sequência subsequente é `"on"` ou `"off"`:
     - Se for `"on"`, ativa o modo de soma e reinicia a variável `numero_atual`.
     - Se for `"off"`, desativa o modo de soma e, caso `numero_atual` contenha um número, converte-o para inteiro e adiciona-o à soma.
   - Se o caractere atual for `"="`, o programa verifica se há algum número em construção (em `numero_atual`), soma-o se necessário e imprime o resultado da soma.
   - Enquanto o modo de soma estiver ativo e o caractere for um dígito, este é concatenado à variável `numero_atual`.  
     Se um caractere não numérico é encontrado e `numero_atual` não está vazia, o número acumulado é convertido para inteiro e adicionado à soma, e `numero_atual` é reiniciada.

4. **Exemplo de Execução:**  
   - **Entrada:**
     ```
     on123eveiber1erivenrv1off=
     ```
   - **Processamento:**  
     - Ativação com `"on"`; captura dos números: `123`, `1` e `1`.
     - Desativação com `"off"`: soma os números acumulados.
     - Impressão com `"="`: exibe `Soma: 125`.
   - **Saída:**  
     ```
     Soma: 125
     ```