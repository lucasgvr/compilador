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
    'IF',
    'ELSE',
    'WHILE'
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
    keywords = {
        'if': 'IF', 
        'else': 'ELSE',
        'while': 'WHILE',
        'int': 'INT',
        'true': 'BOOL',
        'false': 'BOOL',
        'bool': 'BOOL'
    }
    t.type = keywords.get(t.value, 'ID')  # Usar o tipo correto se for uma palavra-chave
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

# Testar o analisador léxico
entrada1 = "int var = 1234; var = 0; if(var > 1 && false){ var = var + 2; } while for true"
entrada2 = "int var = 1234; var = ; fi(var > 1{ var = + 2; }"
entrada3 = "int var = 1234: var = 0; if(var > 1 & false){ var = var ^ 2; }"
entrada4 = "int teste}{var = 3 ; teste} 123 #"