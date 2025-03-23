# Recursivo_Desc

## Autor
![Foto de Perfil](../Photo.jpeg)

Gonçalo Oliveira Cruz (A104346)

---

## Descrição

Este programa em Python implementa um parser LL(1) recursivo-descendente para reconhecer expressões aritméticas e calcular os respetivos valores. Utilizando os módulos `ply.lex` e `ply.yacc`, o código:
1. Tokeniza números, parêntesis e operadores (`+`, `-`, `*`);
2. Reconhece e avalia expressões aritméticas com a devida precedência;
3. Processa expressões, realizando o cálculo dos valores.

---

## Enunciado

> Baseado nos materiais fornecidos na aula, cria um parser LL(1) recursivo descendente que reconheça expressões > aritméticas e calcule o respetivo valor.
> Exemplos de algumas frases:
> ```
> 2+3
> 67-(2+3*4)
> (9-2)*(13-4)
> ```

## Funcionamento do Código

1. **Análise Léxica:**
   - Utiliza o módulo `ply.lex` para definir os tokens:
     - `NUM`: representa números, convertendo o valor para inteiro;
     - `PA` e `PF`: representam os parêntesis de abertura e fecho, respetivamente;
     - `PLUS`, `MINUS` e `TIMES`: representam os operadores de adição, subtração e multiplicação.
   - Ignora espaços e tabulações e atualiza a contagem de linhas conforme necessário.
   - Em caso de caractere desconhecido, exibe uma mensagem de erro indicando o caractere e a linha onde ocorreu o problema.

2. **Análise Sintática:**
   - Utiliza o módulo `ply.yacc` para definir a gramática das expressões aritméticas:
     - Regras para operações de soma e subtração, tratando a precedência com expressões e termos;
     - Regras para operações de multiplicação, permitindo o reconhecimento de fatores compostos;
     - Suporte para agrupamento com parêntesis.
   - Se ocorrer um erro sintático, o parser exibe a mensagem "Erro sintático no input!".

3. **Cálculo das Expressões:**
   - Após o reconhecimento, o parser avalia a expressão e calcula o valor final.
   - Um loop interativo com o prompt `calc >` permite a entrada de expressões pelo usuário, e o resultado é exibido logo após o processamento.

---

## Exemplo de Saída

calc > 67-(2+3*4)
 ```
53
 ```

calc > (9-2)*(13-4)
 ```
63
 ```