tabela = [
    {
        "category": "Tipo de variável",
        "symbol": "int",
        "description": "tipo inteiro"
    },
    {
        "category": "Tipo de variável",
        "symbol": "bool",
        "description": "tipo booleano"
    },
    {
        "category": "Atribuição",
        "symbol": "=",
        "description": "atribuir valor à variável"
    },
    {
        "category": "Operações matemáticas",
        "symbol": "+",
        "description": "somar"
    },
    {
        "category": "Operações matemáticas",
        "symbol": "-",
        "description": "subtrair"
    },
    {
        "category": "Operações matemáticas",
        "symbol": "*",
        "description": "multiplicar"
    },
    {
        "category": "Operações matemáticas",
        "symbol": "/",
        "description": "dividir"
    },
    {
        "category": "Operações lógicas",
        "symbol": "==",
        "description": "igual"
    },
    {
        "category": "Operações lógicas",
        "symbol": "!=",
        "description": "diferente"
    },
    {
        "category": "Operações lógicas",
        "symbol": "<=",
        "description": "menor igual"
    },
    {
        "category": "Operações lógicas",
        "symbol": ">=",
        "description": "maior igual"
    },
    {
        "category": "Operações lógicas",
        "symbol": "<",
        "description": "menor"
    },
    {
        "category": "Operações lógicas",
        "symbol": ">",
        "description": "maior"
    },
    {
        "category": "Operações lógicas",
        "symbol": "&&",
        "description": "operador E"
    },
    {
        "category": "Operações lógicas",
        "symbol": "||",
        "description": "operador OU"
    },
    {
        "category": "Escopo",
        "symbol": "{",
        "description": "abertura de escopo"
    },
    {
        "category": "Escopo",
        "symbol": "}",
        "description": "fechamento de escopo"
    },
    {
        "category": "Escopo",
        "symbol": ";",
        "description": "fim de linha"
    },
    {
        "category": "Escopo",
        "symbol": "(",
        "description": "abertura de trecho"
    },
    {
        "category": "Escopo",
        "symbol": ")",
        "description": "fechamento de trecho"
    },
    {
        "category": "Palavras reservadas",
        "symbol": "if",
        "description": "estrutura condicional"
    },
    {
        "category": "Palavras reservadas",
        "symbol": "else",
        "description": "estrutura condicional"
    },
    {
        "category": "Palavras reservadas",
        "symbol": "while",
        "description": "estrutura de repetição"
    },
    {
        "category": "Valores de variáveis",
        "symbol": "true",
        "description": "valor booleano"
    },
    {
        "category": "Valores de variáveis",
        "symbol": "false",
        "description": "valor booleano"
    },
    {
        "category": "Valores de variáveis",
        "symbol": "sequência de números",
        "description": "ex: 122452862"
    },
    {
        "category": "Nome de variáveis",
        "symbol": "inicia com letra, pode conter letras e números",
        "description": "ex: var1"
    }
]

import re

def analise_lexica(entrada):
    padroes = [
        r'\bint\b', r'\bbool\b', r'\=', r'\+', r'\-', r'\*', r'\/',
        r'\==', r'\!=', r'\<=', r'\>=', r'\<', r'\>', r'\&\&', r'\|\|',
        r'\{', r'\}', r'\;', r'\(', r'\)',
        r'\bif\b', r'\belse\b', r'\bwhile\b',
        r'\btrue\b', r'\bfalse\b', r'\b\d+\b',
        r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
        r'\S+' 
    ]

    padrao = '|'.join(padroes)
    tokens = re.findall(padrao, entrada)
    resultado = []

    for token in tokens:
        token = token.strip()
        encontrado = False
        for simbolo in tabela:
            if token == simbolo["symbol"]:
                resultado.append({"token": token, "category": simbolo["category"], "description": simbolo["description"]})
                encontrado = True
                break

        if not encontrado:
            resultado.append({"token": token, "category": "Desconhecido", "description": "Token desconhecido"})

    return resultado

def extrair_variaveis_info(tokens):
    variaveis_info = []
    i = 0

    while i < len(tokens):
        if i + 3 < len(tokens) and tokens[i]["category"] == "Tipo de variável" and tokens[i + 2]["token"] == "=":
            tipo_variavel = tokens[i]["token"] 
            nome_variavel = tokens[i + 1]["token"]
            valor_variavel = tokens[i + 3]["token"]

            variaveis_info.append({
                "nome": nome_variavel,
                "valor": valor_variavel,
                "tipo": tipo_variavel
            })

            i += 4  
        else:
            i += 1

    return variaveis_info

def analisar_tokens_desconhecidos(tokens):
    for i, token in enumerate(tokens):
        if token["category"] == "Desconhecido":
            if token["token"].isnumeric():
                tokens[i]["category"] = "valores de variáveis"
                tokens[i]["description"] = "sequência de números"
            elif token["token"][0].isalpha():
                tokens[i]["category"] = "nomes de variáveis"
                tokens[i]["description"] = "nome de variável"

def verificar_tokens(tokens):
    for token in tokens:
        if token["category"] == "Desconhecido":
            print("rejeitada")
            return
    print("aceita")

entrada1 = "int var = 1234; var = 0; if(var > 1 && false){ var = var + 2; }"
entrada2 = "int var = 1234; var = ; fi(var > 1{ var = + 2; }"
entrada3 = "int var = 1234: var = 0; if(var > 1 & false){ var = var ^ 2; }"
entrada4 = "int teste}{var = 3 ; teste} 123 #"

tokens = analise_lexica(entrada4)
analisar_tokens_desconhecidos(tokens)

variaveis_info = extrair_variaveis_info(tokens)

for token in tokens:
    print(token)

print(variaveis_info)

verificar_tokens(tokens)