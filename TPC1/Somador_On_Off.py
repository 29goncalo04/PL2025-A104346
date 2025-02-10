def main():
    texto = input("> ").lower()
    soma  = 0
    soma_ativa = False
    numero_atual = ""
    i = 0

    while(i < len(texto)):
        if texto[i] == "o":
            if i+1<len(texto) and texto[i+1] == "n":    #corresponde a ON
                soma_ativa = True
                numero_atual = ""
                i+=1
            elif i+1<len(texto) and texto[i+1] == "f":
                if i+2<len(texto) and texto[i+2] == "f": #corresponde a OFF
                    soma_ativa = False
                    if numero_atual != "": soma += int(numero_atual)
                    numero_atual = ""
                    i+=2
        elif texto[i] == "=": 
            if numero_atual != "":
                soma += int(numero_atual)
                numero_atual = ""
            print ("Soma: " + str(soma))
        elif soma_ativa:
            if texto[i].isdigit():
                numero_atual += texto[i]
            elif numero_atual != "":
                soma += int(numero_atual)
                numero_atual = ""
        i+=1 

if __name__ == "__main__":
    main()