import re
from rules import TokenClass, Token

with open('teste1.c', 'r', encoding='utf-8') as f:
   code = f.read()

code = re.sub(r'/\*[\s\S]*?\*/', '', code)
code = re.sub(r'//\s*[^\n]*', '', code, flags=re.DOTALL)

lines = code.split('\n')

tokens = []
token_id = 1

for line in lines:
    line = re.sub(r'\s+', ' ', line.strip()) 

    while line:
        match = None
        for token_class in TokenClass:
            regex = token_class.value
            match = re.match(regex, line)
            if match:
                break
        if match:
            lexema = match.group(0)
            token = Token(token_class, lexema, token_id)
            tokens.append(token)
            line = line[len(lexema):].lstrip() 
            token_id += 1
        else:
            raise ValueError(f"Erro léxico: caractere inesperado: {line[0]}")

for token in tokens:
    print(token)
    #with open("result/token1.txt", "a") as file:
        #file.write(str(token))
        #file.write("\n")