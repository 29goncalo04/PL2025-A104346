# Conversor

## Autor
![Foto de Perfil](../Photo.jpeg)

Gonçalo Oliveira Cruz (A104346)

---

## Descrição

Este programa em Python lê um ficheiro Markdown (chamado `conversor.md`) e converte-o para HTML, criando o ficheiro `conversor.html`. O objetivo é:

1. **Converter Cabeçalhos**: Linhas que iniciam com 1 a 3 hashtags são transformadas em tags HTML correspondentes (`<h1>`, `<h2>`, `<h3>`).
2. **Converter Listas Numeradas**: Linhas que começam com um número seguido de um ponto são convertidas em itens de lista (`<li>`) contidos dentro de uma lista ordenada (`<ol>`).
3. **Converter Formatações de Texto**:
   - **Negrito**: `**texto**` → `<b>texto</b>`
   - *Itálico*: `*texto*` → `<i>texto</i>`
4. **Converter Imagens e Links**:
   - Imagem: `![alt](url)` → `<img src="url" alt="alt"/>`
   - Link: `[texto](url)` → `<a href="url">texto</a>`

---

## Enunciado

> Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:
> As transformações devem incluir:
> 1. Conversão de cabeçalhos para `<h1>`, `<h2>` ou `<h3>` de acordo com o número de hashtags.
> 2. Conversão de listas numeradas para `<li>` dentro de uma lista ordenada `<ol>`.
> 3. Conversão das formatações de negrito e itálico.
> 4. Conversão de imagens e links para as tags HTML correspondentes.

---

## Funcionamento do Código

1. **Abertura dos Ficheiros:**
   - O ficheiro `conversor.md` é aberto em modo leitura.
   - O ficheiro `conversor.html` é criado.

2. **Processamento Linha a Linha:**
   - **Listas Numeradas:**
     - Verifica se a linha inicia com um número seguido de um ponto usando expressões regulares.
     - Se identificado, a linha é convertida para um item de lista (`<li>`).
     - Ao detetar o início de uma lista, insere a tag `<ol>`; quando a lista termina, insere a tag `</ol>`.
   - **Cabeçalhos:**
     - Linhas que começam com 1 a 3 hashtags são substituídas pelas tags HTML correspondentes, de acordo com o número de hashtags.
   - **Formatações de Texto:**
     - Textos marcados como **negrito** (`**texto**`) são convertidos para `<b>texto</b>`.
     - Textos marcados como *itálico* (`*texto*`) são convertidos para `<i>texto</i>`.
   - **Imagens e Links:**
     - Imagens no formato `![alt](url)` são transformadas em `<img src="url" alt="alt"/>`.
     - Links no formato `[texto](url)` são transformados em `<a href="url">texto</a>`.

3. **Escrita do HTML:**
   - Cada linha processada é escrita no ficheiro `conversor.html` com a formatação HTML correta.
   - Se uma lista estiver aberta ao final do ficheiro, a tag `</ol>` é inserida.

4. **Execução do Programa:**
   - A função `main()` é executada quando o script é executado diretamente a partir do comando:
     ```
     python3 conversor.py
     ```

---

## Exemplo de Saída

Dado um ficheiro `conversor.md` com o seguinte conteúdo:
 ```
 # Exemplo1
 ## Exemplo2
 ### Exemplo3
 
 Este é um **exemplo** ...
 
 Este é um *exemplo* ...
 
 1. Primeiro item
 2. Segundo item
 3. Terceiro item
 
 Como pode ser consultado em [página da UC](http://www.uc.pt)
 
 Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com)
  ```

O respetivo ficheiro HTML será:
 ```
 <h1>Exemplo1</h1>
 <h2>Exemplo2</h2>
 <h3>Exemplo3</h3>
 
 Este é um <b>exemplo</b> ...
 
 Este é um <i>exemplo</i> ...
 
 <ol>
 <li>Primeiro item</li>
 <li>Segundo item</li>
 <li>Terceiro item</li>
 </ol>
 
 Como pode ser consultado em <a href="http://www.uc.pt">página da UC<a/>
 
 Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/>
  ```