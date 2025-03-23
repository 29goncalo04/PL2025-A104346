import ply.lex as lex
import ply.yacc as yacc

# Analisador Léxico

tokens = ('NUM', 'PA', 'PF', 'PLUS', 'MINUS', 'TIMES')

t_PA = r'\('
t_PF = r'\)'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = '\t '

def t_error(t):
    print('Caractere desconhecido:', t.value[0], 'Linha:', t.lexer.lineno)
    t.lexer.skip(1)

lexer = lex.lex()




# Analisador Sintático

def p_expr_plus(p):
    'expressao : expressao PLUS termo'
    p[0] = p[1] + p[3]

def p_expr_minus(p):
    'expressao : expressao MINUS termo'
    p[0] = p[1] - p[3]

def p_expr_termo(p):
    'expressao : termo'
    p[0] = p[1]

def p_termo_times(p):
    'termo : termo TIMES fator'
    p[0] = p[1] * p[3]

def p_termo_fator(p):
    'termo : fator'
    p[0] = p[1]

def p_fator_num(p):
    'fator : NUM'
    p[0] = p[1]

def p_fator_expr(p):
    'fator : PA expressao PF'
    p[0] = p[2]

def p_error(p):
    print("Erro sintático no input!")



# expressao : termo
#           | expressao MAIS termo
#           | expressao MINUS termo
# termo : termo VEZES fator
#       | fator
# fator : NUM
#       | PA expressao PF


parser = yacc.yacc()

while s := input('calc > '):
   result = parser.parse(s)
   print(result)