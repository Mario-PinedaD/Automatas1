import ply.lex as lex

reservadas = ['if', 'then', 'function', 'and', 'elseif', 'nil', 'return', 'while', 'break', 'end', 'not', 'do',
            'false', 'in', 'true', 'else', 'for', 'local', 'repeat', 'until', 'type', 'print', 'require', 'or',
            'table']

tokens = (
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
    'COMENTARIO'
)

t_CORCHETE_DER = r'\]'
t_CORCHETE_IZQ = r'\['
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_COMA = r'\,'
t_PUNTO_Y_COMA=r'\;'
t_ignore = ' \t'


def t_COMENTARIO(t):
    r"//.*"
    t.type = "COMENTARIO"
    return t


def t_OPERADOR(t):
    r'[+\-*/=><~#%^\.:]'
    t.type = 'OPERADOR'
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value.lower() in reservadas:
        t.type = 'RESERVADAS'
    else:
        t.type = 'IDENTIFICADOR'
    return t


def t_STRING(t):
    r'\"([^\"\n]*?)(?<!\\)\"|\'([^\'\n]*?)(?<!\\)\'|"""([^"]*?)"""'
    t.value = t.value.strip('"').strip("'")
    return t


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+(?![\.\d])'
    t.value = int(t.value)
    return t

def t_linea(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Caracter invalido '%s'" % t.value[0] + ", en la linea: " + str(t.lexer.lineno))
    t.lexer.skip(1)

def lexer_action(data):
    token_list = []
    lexer = lex.lex()
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
            tokens = lexer_action(datos)
            print("Tokens encontrados en el archivo", archivo, ":\n")

            # Impresion de los tokens encontrados
            for token in tokens:
                print(token)
    except FileNotFoundError:
        print("El archivo no se encuentra =(")


if __name__ == "__main__":
    archivo = "arch_prueba.js"
    abrir_archivo(archivo)
