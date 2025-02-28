import re

def main():
    dentro_lista = False
    with open("conversor.md", "r", encoding="utf-8") as file, open("conversor.html", "w", encoding="utf-8") as output:
        for linha in file:
            #-------Lista_Numerada------
            p = re.compile(r'^\d+\.\s*(.*)')
            if p.search(linha):
                linha = re.sub(p, r'<li>\1</li>', linha)
                if dentro_lista == False: 
                    output.write("<ol>" + "\n")
                    dentro_lista = True
            elif dentro_lista: 
                output.write("</ol>" + "\n")
                dentro_lista = False
            #-----------Cabeçalhos-------------
            p = re.compile(r'^(#{1,3})\s*(.*)')
            search = p.search(linha)
            if search:
                hashtags = str(len(search.group(1)))
                texto = search.group(2)
                linha = re.sub(p, "<h" + hashtags + ">" + texto + "</h" + hashtags + ">", linha)
            #-----------Bold-------------
            p = re.compile(r'\*\*(.*?)\*\*')
            linha = re.sub(p, r'<b>\1</b>', linha)
            #-----------Itálico----------
            p = re.compile(r'\*(.*?)\*')
            linha = re.sub(p, r'<i>\1</i>', linha)
            #-----------Imagem----------
            p = re.compile(r'!\[(.*?)\]\((.*?)\)')
            linha = re.sub(p, r'<img src="\2" alt="\1"/>', linha)
            #------------Link-----------
            p = re.compile(r'\[(.*?)\]\((.*?)\)')
            linha = re.sub(p, r'<a href="\2">\1<a/>', linha)


            output.write(linha.strip() + "\n")

        if dentro_lista: output.write("</ol>" + "\n")

if __name__ == "__main__":
    main()