import ply.lex as lex

# Lista de tokens
tokens = [
    'ID',       # Nome de variáveis
    'INT',      # Valor inteiro
    'BOOL',     # Valor booleano
    'ASSIGN',   # Atribuição
    'PLUS',     # Operador de soma
    'MINUS',    # Operador de subtração
    'TIMES',    # Operador de multiplicação
    'DIVIDE',   # Operador de divisão
    'EQ',       # Operador de igualdade
    'NEQ',      # Operador de desigualdade
    'LE',       # Operador menor ou igual
    'GE',       # Operador maior ou igual
    'LT',       # Operador menor que
    'GT',       # Operador maior que
    'AND',      # Operador lógico E
    'OR',       # Operador lógico OU
    'SCOPE',    # Abertura e fechamento de escopo {}
    'SEMICOLON',# Fim de linha ;
    'LPAREN',   # Abertura de parênteses (
    'RPAREN',   # Fechamento de parênteses )
    'IF'
]

# Regras léxicas
t_INT = r'\d+'                  # Valor inteiro
t_BOOL = r'true|false'          # Valor booleano
t_ASSIGN = r'='                 # Atribuição
t_PLUS = r'\+'                  # Operador de soma
t_MINUS = r'-'                  # Operador de subtração
t_TIMES = r'\*'                 # Operador de multiplicação
t_DIVIDE = r'/'                # Operador de divisão
t_EQ = r'=='                   # Operador de igualdade
t_NEQ = r'!='                  # Operador de desigualdade
t_LE = r'<='                   # Operador menor ou igual
t_GE = r'>='                   # Operador maior ou igual
t_LT = r'<'                    # Operador menor que
t_GT = r'>'                    # Operador maior que
t_AND = r'&&'                  # Operador lógico E
t_OR = r'\|\|'                 # Operador lógico OU
t_SCOPE = r'\{|\}'             # Abertura e fechamento de escopo {}
t_SEMICOLON = r';'             # Fim de linha ;
t_LPAREN = r'\('               # Abertura de parênteses (
t_RPAREN = r'\)'               # Fechamento de parênteses )

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value == 'if':
        t.type = 'IF'
    return t

# Tratamento de quebra de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erro
def t_error(t):
    print(f"Caractere ilegal: '{t.value[0]}'")
    t.lexer.skip(1)

# Criar um analisador léxico
lexer = lex.lex()

# Teste o analisador léxico
data = '''
int var1;
bool flag;
var1 = 42;
flag = true;
'''

entrada1 = "int var = 1234; var = 0; if(var > 1 && false){ var = var + 2; } while for"
entrada2 = "int var = 1234; var = ; fi(var > 1{ var = + 2; }"
entrada3 = "int var = 1234: var = 0; if(var > 1 & false){ var = var ^ 2; }"
entrada4 = "int teste}{var = 3 ; teste} 123 #"

lexer.input(entrada1)

for token in lexer:
    print(token)

import ply.yacc as yacc

# Defina a precedência dos operadores
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'EQ', 'NEQ', 'LE', 'GE', 'LT', 'GT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Regras de produção da gramática
def p_statement_assign(p):
    'statement : ID ASSIGN expression SEMICOLON'
    print(f'Assign: {p[1]} = {p[3]}')

def p_statement_if(p):
    'statement : IF LPAREN expression RPAREN SCOPE statements SCOPE'
    print(f'If Statement: if ({p[3]}) {{ {p[6]} }}')

def p_statements(p):
    '''
    statements : statement
               | statements statement
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + '\n' + p[2]

def p_expression_binop(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression EQ expression
               | expression NEQ expression
               | expression LE expression
               | expression GE expression
               | expression LT expression
               | expression GT expression
               | expression AND expression
               | expression OR expression
    '''
    p[0] = f'{p[1]} {p[2]} {p[3]}'

def p_expression_unary(p):
    '''
    expression : MINUS expression %prec MINUS
    '''
    p[0] = f'-{p[2]}'

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_id(p):
    'expression : ID'
    p[0] = p[1]

def p_expression_int(p):
    'expression : INT'
    p[0] = p[1]

def p_expression_bool(p):
    'expression : BOOL'
    p[0] = p[1]

# Lida com erros de sintaxe
def p_error(p):
    print(f'Erro de sintaxe: {p}')

# Criar um analisador sintático
parser = yacc.yacc()


# Código-fonte para análise sintática
source_code = 'int var = 1234; var = 0; if(var > 1 && false){ var = var + 2; }'

# Analise o código-fonte
result = parser.parse(source_code)

print(result)