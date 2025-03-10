from datetime import date
import json, re

def calcular_troco(valor):
    moedas = [(2, "2e"), (1, "1e"), (0.5, "50c"), (0.2, "20c"), (0.1, "10c"), (0.05, "5c"), (0.02, "2c"), (0.01, "1c")]
    troco = {}
    for moeda, expressao in moedas:
        quantidade = int(valor//moeda)
        if quantidade > 0:
            troco[expressao] = quantidade
            valor = round(valor - quantidade * moeda, 2)
    if not troco:
        return "Sem troco"
    partes = []
    for expressao, quantidade in troco.items():
        partes.append(f"{quantidade}x {expressao}")
    if len(partes) == 1:
        return f"Pode retirar o troco: {partes[0]}."
    return f"Pode retirar o troco: {', '.join(partes[:-1])} e {partes[-1]}."

def imprimir_saldo(valor):
    valor_euros = int(valor)
    valor_centimos = int(round((valor - valor_euros) * 100, 2))
    if valor_euros == 0:
        return f"{valor_centimos}c"
    if valor_centimos == 0:
        return f"{valor_euros}e"
    return f"{valor_euros}e{valor_centimos}c"

def main():
    with open('stock.json', 'r', encoding='utf-8') as file:
        dados = json.load(file)
    stock = dados["stock"]  #lista de produtos

    # Definir larguras fixas para cada coluna
    largura_cod = 6
    largura_nome = 25
    largura_quant = 12
    largura_preco = 8

    total = 0

    print(f"{date.today()}, Stock carregado, Estado atualizado.")
    print("Bom dia. Estou disponível para atender o seu pedido.")

    pedido_moeda = re.compile(r'MOEDA (.*)\.$')  #irá extrair as moedas inseridas
    pedido_selecao = re.compile(r'SELECIONAR (.*)$')  #extrai o código inserido

    while (True):
        pedido = input()

        if pedido == "LISTAR":
            print(f"    {"cod":<{largura_cod}} | {"nome":^{largura_nome}} | {"quantidade":^{largura_quant}} | {"preço":^{largura_preco}}")
            print("--------------------------------------------------------------")
            for produto in stock:
                print(f"    {produto["cod"]:<{largura_cod}}   {produto["nome"]:^{largura_nome}}   {produto["quant"]:^{largura_quant}}   {produto["preco"]:^{largura_preco}}")
            print()

        elif pedido_moeda.search(pedido):  #MOEDA 1e, 20c, 5c, 5c .
            moedas = pedido_moeda.search(pedido).group(1) #1e, 20c, 5c, 5c
            moedas_separadas = re.findall(r'(\d+)([ec])', moedas) #[(1,e), (20,c), (5,c), (5,c)]
            for valor, unidade in moedas_separadas:
                valor = int(valor)
                if unidade == "e":
                    if valor in [1, 2]:
                        total+=valor
                if unidade == "c":
                    if valor in [1, 2, 5, 10, 20, 50]:
                        total+=valor/100
            total = round(total,2)
            print (f"Saldo = {imprimir_saldo(total)}")
            print()
        
        elif pedido_selecao.search(pedido):   #SELECIONAR A23
            codigo = pedido_selecao.search(pedido).group(1)  #A23
            for produto in stock: 
                if produto["cod"] == codigo:
                    if total >= produto["preco"]:
                        total -= produto["preco"]
                        print(f'Pode retirar o produto dispensado "{produto["nome"]}"')
                        print(f"Saldo = {imprimir_saldo(total)}")
                        print()
                    else:
                        print("Saldo insufuciente para satisfazer o seu pedido")
                        print(f"Saldo = {imprimir_saldo(total)}; Pedido = {imprimir_saldo(produto["preco"])}")
                        print()
        
        elif pedido == "SAIR":
            print(calcular_troco(total))
            print("Até à próxima")
            break
                    



     

if __name__ == "__main__":
    main()