def processa_dados(dados_obra, campo_pretendido):
    dados = "".join(dados_obra)
    campos = []
    campo_atual = ""
    dentro_aspas = False
    for caractere in dados:
        if caractere == '"':
            dentro_aspas = not dentro_aspas
        elif caractere == ";" and dentro_aspas == False:
            campos.append(campo_atual)
            campo_atual = ""
        else:
            campo_atual += caractere
    if campo_atual:
        campos.append(campo_atual)
    return campos[campo_pretendido]

def main():
    compositores = []
    periodos = {}
    with open("./TPC2/obras.csv", "r", encoding="utf-8") as ficheiro:
        next(ficheiro)    #ignora a primeira linha
        dados_obra = []
        contador_ponto_virgula = 0
        dentro_aspas = False
        for linha in ficheiro:  
            for caractere in linha:
                if caractere == '"' and dentro_aspas == False:
                    dentro_aspas = True
                elif caractere == '"' and dentro_aspas == True:
                    dentro_aspas = False
                elif dentro_aspas == False and caractere == ";": 
                    contador_ponto_virgula += 1
            dados_obra.append(linha)
            if contador_ponto_virgula == 6:
                compositores.append(processa_dados(dados_obra, 4))   # o 4 corresponde ao compositor
                periodo = processa_dados(dados_obra, 3)              # o 3 corresponde ao período
                titulo = processa_dados(dados_obra, 0)               # o 0 corresponde ao título da obra
                if periodo in periodos:
                    periodos[periodo]["quantidade"] += 1
                    periodos[periodo]["titulos"].append(titulo)
                else:
                    periodos[periodo] = {"quantidade": 1, "titulos": [titulo]}
                dados_obra = []
                contador_ponto_virgula = 0
    compositores.sort()
    for periodo, info in periodos.items():
        info["titulos"].sort()
        
    print("Lista ordenada dos compositores musicais:")
    for compositor in compositores:
        print("   " + compositor)

    print("\n\n\n")

    print("Quantidade de obras catalogadas em cada período:")
    for periodo, info in periodos.items():
        print("   " + periodo + ": " + str(info["quantidade"]))

    print("\n\n\n")


    print("Títulos das obras de cada período:")
    for periodo, info in periodos.items():
        print("   " + periodo + ":")
        for titulo in info["titulos"]:
            print("      " + titulo)



if __name__ == "__main__":
    main()