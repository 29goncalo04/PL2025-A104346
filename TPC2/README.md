# Obras

## Autor
Gonçalo Oliveira Cruz (A104346)

---

## Descrição

Este programa em Python lê um ficheiro CSV (chamado `obras.csv`) **sem recorrer ao módulo `csv`**. O objetivo é:

1. **Extrair e listar** os compositores de forma ordenada (alfabeticamente).  
2. **Distribuir as obras por período**, apresentando a contagem de obras em cada período.  
3. **Criar um dicionário** que, para cada período, guarde uma lista alfabética dos títulos das obras correspondentes.

---

## Enunciado

> É proibido usar o módulo CSV do Python;  
> Deverá ler o dataset, processá-lo e criar os seguintes resultados:  
> 1. Lista ordenada alfabeticamente dos compositores musicais;  
> 2. Distribuição das obras por período (quantas obras catalogadas em cada período);  
> 3. Dicionário em que a cada período está associada uma lista alfabética dos títulos das obras desse período.

---

## Funcionamento do Código

O programa está estruturado em duas partes principais: a função `processa_dados()` e a função `main()`.

1. **Função `processa_dados(dados_obra, campo_pretendido)`:**  
   - Recebe como entrada uma lista de linhas (`dados_obra`) que formam uma única obra, e o índice do campo (`campo_pretendido`) que se pretende extrair.  
   - Concatena todas as linhas numa única string e percorre cada caractere para separar corretamente os campos, tendo em conta que alguns campos podem estar entre aspas (`" "`).  
   - Sempre que encontra um ponto e vírgula (`;`) **fora** de aspas, encerra o campo atual e inicia outro.  
   - No final, devolve o conteúdo do campo selecionado (`campo_pretendido`).

2. **Função `main()`:**  
   - **Abertura e Leitura do Ficheiro:** Abre o ficheiro `obras.csv` com codificação `utf-8`.  
   - **Ignora a Primeira Linha:** Chama `next(ficheiro)` para saltar o cabeçalho.  
   - **Processamento das Linhas:**  
     - Percorre cada linha e conta quantos pontos e vírgulas (`;`) aparecem **fora** de aspas.  
     - Assim que identifica que foram lidos 6 pontos e vírgulas, interpreta essas linhas como uma única obra completa.  
     - Extrai os campos pretendidos:  
       - Índice 0: **Título da Obra**  
       - Índice 3: **Período**  
       - Índice 4: **Compositor**  
     - Armazena o compositor numa lista de compositores.  
     - Armazena o título no dicionário `periodos`, usando o período como chave. Se o período já existir, incrementa a contagem e adiciona o título na lista. Caso contrário, cria uma nova entrada para esse período.  
   - **Ordenação:**  
     - Ordena alfabeticamente a lista de compositores.  
     - Para cada período, ordena também a lista de títulos.  
   - **Impressão dos Resultados:**  
     - Lista de compositores.  
     - Quantidade de obras por período.  
     - Títulos das obras, agrupados por período.  

3. **Dicionário `periodos`:**  
   - Estrutura-se como um mapeamento de **Período** → `{"quantidade": x, "titulos": [lista_de_titulos]}`.  
   - Permite facilmente manter e exibir a contagem de obras e a lista dos seus títulos.

4. **Exemplo de Saída:**  
   - Lista ordenada de compositores.  
   - Quantidade de obras por período.  
   - Títulos das obras por período, também ordenados.
     ```
     Lista ordenada dos compositores musicais:
        Alessandro Stradella
        Antonio Maria Abbatini
        Bach, Johann Christoph
        Bach, Johann Michael
        ...

     Quantidade de obras catalogadas em cada período:
        Barroco: 26
        Clássico: 15
        Medieval: 48
        Renascimento: 41
        Século XX: 18
        Romântico: 19
        Contemporâneo: 7

     Títulos das obras de cada período:
        Barroco:
           Ab Irato
           Die Ideale, S.106
           Fantasy No. 2
           Hungarian Rhapsody No. 16
           Hungarian Rhapsody No. 5
           ...
        Clássico:
           Bamboula, Op. 2
           Capriccio Italien
           Czech Suite
           French Overture
           Hungarian Rhapsody No. 14
           ...
        Medieval:
           Adagio in B minor
           Ballade No.1
           Ballades, Op. 10
           Barcarole Op. 60
           Coriolan Overture
           ...
        Renascimento:
           Bagatelles, Opus 119
           Bagatelles, Opus 33
           Cantatas, BWV 141-150
           Carnival Overture
           Estampes
           ...
     ```