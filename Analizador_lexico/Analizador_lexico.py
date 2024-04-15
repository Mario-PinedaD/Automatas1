import sys
import ply.lex as lex
import re

#Palabras reservadas
reservadas = ['await', 'break', 'case', 'catch', 'class','console','const', 'continue',
    'debugger', 'default', 'delete', 'do', 'else', 'enum', 'export',
    'extends', 'false', 'finally', 'for', 'function', 'if', 'implements',
    'import', 'in', 'instanceof', 'interface', 'let','log', 'new', 'null', 'package',
    'private', 'protected', 'public', 'return', 'super', 'switch', 'static',
    'this', 'throw', 'try', 'typeof', 'true', 'var', 'void', 'while', 'with', 'yield']

#Tokens
tokens = [
    'INT',
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
    'FLOAT',
    'STRING',
    'IDENTIFICADOR',
    'RESERVADAS',
    'CORCHETE_DER',
    'CORCHETE_IZQ',
    'LLAVE_IZQ',
    'LLAVE_DER',
    'OPERADOR',
    'COMA',
    'PUNTO_Y_COMA',
    'PUNTO',
    'COMENTARIO',
    'ERROR'
]

# \ Secuencia de escape
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_CORCHETE_DER = r'\]'
t_CORCHETE_IZQ = r'\['
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_COMA = r'\,'
t_PUNTO_Y_COMA = r'\;'
t_PUNTO = r'\.'
t_ignore = ' \t'

def t_COMENTARIO(t):
    #r"(//.*)"
    r'//.* | \/\*[\s\S]*?\*\/'
    t.type = "COMENTARIO"
    t.lexer.lineno += t.value.count('\n')
    pass
    #return t

def t_OPERADOR(t):
    r'[+\-*/%=><!&|^~?:]'
    t.type = 'OPERADOR'
    return t


def t_IDENTIFICADOR(t):
    r'[a-zA-Z_$][a-zA-Z_0-9$]*'
    if t.value.lower in reservadas:
        t.type = 'RESERVADAS'
    else:
        t.type = 'IDENTIFICADOR'
    return t

def t_STRING(t):
    r'\" ([^\"\n]*?) \" | \'([^\'\n]*?) \''
    t.value = t.value.strip('"').strip("'")
    return t

def t_FLOAT(t):
    r'\d+\.\d+ | \d*\.\d+'
    #t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    return t

def t_linea(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    t.type = "ERROR"
    print("Caracter invalido '%s'" % t.value + ", en la linea: " + str(t.lexer.lineno))
    t.lexer.lineno += len(t.value)
    t.lexer.skip(1)
    #sys.exit(1)

    # Encuentra el inicio de la palabra actual
    inicio_palabra = t.lexer.lexdata.rfind(" ", 0, t.lexpos) + 1
    # Encuentra el final de la palabra actual
    final_palabra = t.lexer.lexdata.find(" ", t.lexpos)
    if final_palabra == -1:
        final_palabra = len(t.lexer.lexdata)
    print("Error léxico en la palabra:\n", t.lexer.lexdata[inicio_palabra:final_palabra])
    # Omitir la palabra completa
    t.lexer.lexpos = final_palabra

def lexer_action(data):
    token_list = []
    lexer = lex.lex() #Instancia del analizador
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        token_list.append((tok.type, tok.value, tok.lineno))
    return token_list

def abrir_archivo(arch):
    try:
        with open(arch, 'r') as file:
            datos = file.read()
            tokens_encontrados = lexer_action(datos)
            print("Tokens encontrados en el archivo", arch, ":\n")
            # Impresion de los tokens_encontrados encontrados
            for token in tokens_encontrados:
                if token[0] != 'ERROR':
                    print(token)
                else:
                    print("Error encontrado en el token")
    except FileNotFoundError:
        print("El archivo no se encuentra =(")


if __name__ == "__main__":
    archivo = "arch_prueba.js"
    abrir_archivo(archivo)
