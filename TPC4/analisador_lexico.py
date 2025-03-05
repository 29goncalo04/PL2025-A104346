import sys
import re

linha = 1

def tokenize(code):
    global linha
    token_specification = [
        ('TYPE', r'\w+(?=:)'), # dbo
        ('SUFIX', r'(?<=:)\w+'), # MusicalArtist
        ('NUM', r'\d+'), # 1000
        ('SPECIAL', r'\w+'),  # select  where  a   LIMIT
        ('COMMENT', r'^#.*'),  # comentários
        ('VARIABLE', r'\?\w+'), # variáveis
        ('LBRACE', r'{'),  # {
        ('RBRACE', r'}'),  # }
        ('COLON', r':'), # :
        ('POINT', r'\.'), # .
        ('STRING', r'"[\w\s]*"'), # "Chuck Berry"
        ('TAG', r'@\w+'), # @en
        ('NEWLINE', r'\n'), # Line endings
        ('SKIP', r'[ \t]+'), # Skip over spaces and tabs
        ('ERRO', r'.'), # Any other character
    ]
    
    tok_regex = '|'.join([f'(?P<{id}>{expreg})' for (id, expreg) in token_specification])
    reconhecidos = []
    mo = re.finditer(tok_regex, code)
    for m in mo:
        dic = m.groupdict()
        if dic['SPECIAL']:
            t = ("SPECIAL", dic['SPECIAL'], linha, m.span())
        elif dic['COMMENT']:
            t = ("COMMENT", dic['COMMENT'], linha, m.span())
        elif dic['VARIABLE']:
            t = ("VARIABLE", dic['VARIABLE'], linha, m.span())
        elif dic['LBRACE']:
            t = ("LBRACE", dic['LBRACE'], linha, m.span())
        elif dic['RBRACE']:
            t = ("RBRACE", dic['RBRACE'], linha, m.span())
        elif dic['TYPE']:
            t = ("TYPE", dic['TYPE'], linha, m.span())
        elif dic['COLON']:
            t = ("COLON", dic['COLON'], linha, m.span())
        elif dic['SUFIX']:
            t = ("SUFIX", dic['SUFIX'], linha, m.span())
        elif dic['POINT']:
            t = ("POINT", dic['POINT'], linha, m.span())
        elif dic['STRING']:
            t = ("STRING", dic['STRING'], linha, m.span())
        elif dic['TAG']:
            t = ("TAG", dic['TAG'], linha, m.span())
        elif dic['NUM']:
            t = ("NUM", int(dic['NUM']), linha, m.span())
        elif dic['NEWLINE']:
            t = ("NEWLINE", dic['NEWLINE'], linha, m.span())
            linha += 1
        elif dic['SKIP']:
            pass
        else:
            t = ("ERRO", m.group(), linha, m.span())
        if not dic['SKIP']: reconhecidos.append(t)
    return reconhecidos


for line in sys.stdin:
   for tok in tokenize(line):
       print(tok)