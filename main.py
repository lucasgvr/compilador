# main.py

from lexer import lexer  # Certifique-se de ter o arquivo lexer.py no mesmo diretório
from parser import parser  # Certifique-se de ter o arquivo parser.py no mesmo diretório

# Ler o código-fonte do arquivo de entrada
with open('input.txt', 'r') as file:
    source_code = file.read()

# Executar o analisador léxico
lexer.input(source_code)

# Executar o analisador sintático
result = parser.parse(source_code, lexer=lexer)

for token in lexer:
    print(token)
    
# Imprimir a árvore sintática resultante
print(result)
