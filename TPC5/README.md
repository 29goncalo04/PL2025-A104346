# Maquina_vendas

## Autor
![Foto de Perfil](../Photo.jpeg)

Gonçalo Oliveira Cruz (A104346)

---

## Descrição

Este programa em Python implementa um sistema interativo para o controlo de stock e processamento de pagamentos. O programa:
1. Lê os produtos de um ficheiro JSON (`stock.json`);
2. Permite listar os produtos disponíveis com uma tabela formatada;
3. Aceita a inserção de moedas através do comando `MOEDA` (ex.: `MOEDA 2e, 1e, 50c, 20c, 10c, 5c, 2c, 1c.`), somando o valor inserido;
4. Permite a seleção de um produto com o comando `SELECIONAR <código>` e efetua a compra se o saldo for suficiente;
5. Exibe o saldo atualizado e, ao sair, calcula e exibe o troco a ser devolvido.

---

## Enunciado

> Pediram-te para construir um programa que simule uma máquina de vending.
> A máquina tem um stock de produtos: uma lista de triplos, nome do produto, quantidade e preço.
> ```
>stock = [
>   {"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco": 0.7},
>   ...
>]
> ```
> Podes persistir essa lista num ficheiro em JSON que é carregado no arranque do programa e é atulizado
> quando o programa termina.
> A seguir apresenta-se um exemplo de uma interação com a máquina, assim que esta é ligada, para que
> possas perceber o tipo de comandos que a máquina aceita (as linhas iniciadas marcadas com >>
> representam o input do utilizador):
> ```
> maq: 2024-03-08, Stock carregado, Estado atualizado.
> maq: Bom dia. Estou disponível para atender o seu pedido.
> >> LISTAR
> maq:
> cod  | nome      | quantidade | preço
> ---------------------------------
> A23    água 0.5L   8            0.7
> ...
> >> MOEDA 1e, 20c, 5c, 5c .
> maq: Saldo = 1e30c
> >> SELECIONAR A23
> maq: Pode retirar o produto dispensado "água 0.5L"
> maq: Saldo = 60c
> >> SELECIONAR A23
> maq: Saldo insufuciente para satisfazer o seu pedido
> maq: Saldo = 60c; Pedido = 70c
> >> ...
> ...
> maq: Saldo = 74c
> >> SAIR
> maq: Pode retirar o troco: 1x 50c, 1x 20c e 2x 2c.
> maq: Até à próxima
> ```
> O stock encontra-se inicialmente armazenado num ficheiro JSON de nome "stock.json" que é carregado
> em memória quando o programa arranca. Quando o programa termina, o stock é gravado no mesmo
> ficheiro, mantendo assim o estado da aplicação entre interações.
> Use a imaginação e criatividade e tente contemplar todos os cenários, por exemplo, produto inexistente ou
> stock vazio.
> Como extra pode adicionar um comando para adicionar alguns produtos ao stock existente (produtos
> novos ou já existentes).

---

## Funcionamento do Código

1. **Leitura do Stock:**
   - O programa abre o ficheiro `stock.json` e carrega os dados dos produtos numa lista.
   - Cada produto é representado por um dicionário com as chaves: `"cod"`, `"nome"`, `"quant"` e `"preco"`.

2. **Interface Interativa:**
   - O programa exibe uma mensagem com a data atual e informa que o stock foi carregado.
   - Um loop interativo aguarda comandos do usuário.
   - Comandos disponíveis:
     - **LISTAR:** Exibe uma tabela com os produtos com larguras fixas para cada coluna.
     - **MOEDA:** Permite a inserção de moedas, utilizando uma expressão regular para extrair os valores. As moedas aceites são: 1e e 2e (euros) e 1c, 2c, 5c, 10c, 20c, 50c (cêntimos). O saldo é atualizado conforme o valor inserido.
     - **SELECIONAR \<código\>:** Procura o produto com o código especificado. Se o saldo for suficiente para pagar o preço do produto, este é dispensado e o saldo é reduzido.
     - **SAIR:** Exibe o troco a ser devolvido (calculado com base no saldo restante) e encerra o programa.

3. **Cálculo do Saldo e Troco:**
   - A função `imprimir_saldo` formata o saldo, separando a parte dos euros e dos cêntimos.
   - A função `calcular_troco` determina, a partir do saldo restante, a quantidade mínima de moedas a ser devolvida, exibindo o resultado num formato legível (por exemplo, "1x 50c, 1x 20c e 2x 2c").

4. **Processamento dos Comandos:**
   - **LISTAR:** Mostra uma tabela com os produtos, alinhando os dados de forma consistente.
   - **MOEDA:** Utiliza regex para extrair e somar os valores das moedas inseridas.
   - **SELECIONAR:** Verifica se há saldo suficiente para a compra do produto especificado. Se houver, atualiza o saldo e exibe uma mensagem confirmando a dispensação do produto.
   - **SAIR:** Calcula o troco, exibe o resultado e finaliza o programa.

---

## Exemplo de Saída

LISTAR
 ```
    cod    |           nome            |  quantidade  |  preço  
--------------------------------------------------------------
    A23              água 0.5L                8           0.7   
    B12            coca cola 1L               15          1.5   
    C45         sumo laranja 0.33L            20          1.2   
    D78                café                   30          0.8   
    E90                 chá                   12          1.0   
    F34          sandes de frango             10          2.5   
    G56            sandes mista               9           2.2   
    H67           croissant misto             7           1.8   
    I89          bolo de chocolate            5           2.0   
    J91           pastel de nata              12          1.2   
    K14        batata frita pequena           20          1.5   
    L28         batata frita grande           15          2.5   
    M39         hambúrguer simples            10          3.5   
    N50          hambúrguer duplo             8           5.0   
    O61               hot dog                 14          2.8   
    P72             pizza fatia               18          3.0   
    Q83            pizza inteira              5           12.0  
    R94            salada mista               6           3.5   
    S05            fruta fresca               10          1.5   
    T16           iogurte natural             8           1.2   
    U27         leite achocolatado            12          1.3
 ```

MOEDA 2e, 1e, 50c, 10c.
 ```
Saldo = 3e60c
 ```

SELECIONAR L28
 ```
Pode retirar o produto dispensado "batata frita grande"
Saldo = 1e10c
 ```

SELECIONAR C45
 ```
Saldo insufuciente para satisfazer o seu pedido
Saldo = 1e10c; Pedido = 1e20c
 ```

SAIR
 ```
Pode retirar o troco: 1x 1e e 1x 10c.
Até à próxima
 ```