import ply.yacc as yacc
from lexer import tokens

# Regras sintáticas
def p_program(p):
    '''program : statements'''
    p[0] = ('program', p[1])

def p_statements(p):
    '''statements : statement statements
                  | empty'''
    if len(p) == 3:
        p[0] = ('statements', p[1], p[2])
    else:
        p[0] = ('empty',)

def p_statement(p):
    '''statement : assignment
                 | if_statement
                 | while_statement'''
    p[0] = p[1]

def p_assignment(p):
    'assignment : ID ASSIGN expression SEMICOLON'
    p[0] = ('assignment', p[1], p[3])

def p_if_statement(p):
    'if_statement : IF LPAREN expression RPAREN SCOPE statements SCOPE else_block'
    p[0] = ('if_statement', p[3], p[6], p[8])

def p_else_block(p):
    '''else_block : ELSE SCOPE statements SCOPE
                  | empty'''
    if len(p) == 5:
        p[0] = ('else_block', p[3])
    else:
        p[0] = ('empty',)

def p_while_statement(p):
    'while_statement : WHILE LPAREN expression RPAREN SCOPE statements SCOPE'
    p[0] = ('while_statement', p[3], p[6])

def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | factor'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : INT
              | BOOL
              | ID
              | LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

# Tratamento para regra vazia
def p_empty(p):
    'empty :'
    pass

# Tratamento de erro
def p_error(p):
    print("Erro de sintaxe")

# Crie o analisador sintático
parser = yacc.yacc()