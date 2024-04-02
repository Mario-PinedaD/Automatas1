import re

# Definición de palabras reservadas
palabras_reservadas = {
    'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
    'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int',
    'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
    'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile',
    'while'
}

# Definición de tokens con expresiones regulares
tokens_regex = {
    'IDENTIFICADOR': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'NUMERO_ENTERO': r'\b\d+\b',
    'NUMERO_FLOTANTE': r'\b\d+\.\d+\b',
    'OPERADOR': r'[-+*/%&|=<>!^~?:]',
    'PARENTESIS_IZQUIERDO': r'\(',
    'PARENTESIS_DERECHO': r'\)',
    'LLAVE_IZQUIERDA': r'\{',
    'LLAVE_DERECHA': r'\}',
    'CORCHETE_IZQUIERDO': r'\[',
    'CORCHETE_DERECHO': r'\]',
    'PUNTO_Y_COMA': r';',
    'COMA': r',',
    'PUNTO': r'\.',
    'COMILLA_SIMPLE': r'\'',
    'COMILLA_DOBLE': r'\"',
    'ASIGNACION': r'=',
    'INCREMENTO': r'\+\+',
    'DECREMENTO': r'--',
    'MAYOR_QUE': r'>',
    'MENOR_QUE': r'<',
    'MAYOR_IGUAL_QUE': r'>=',
    'MENOR_IGUAL_QUE': r'<=',
    'IGUAL_QUE': r'==',
    'DIFERENTE_DE': r'!=',
    'AND_LOGICO': r'&&',
    'OR_LOGICO': r'\|\|',
    'NOT_LOGICO': r'!',
    'AND_BIT_A_BIT': r'&',
    'OR_BIT_A_BIT': r'\|',
    'XOR_BIT_A_BIT': r'\^',
    'NOT_BIT_A_BIT': r'~',
    'SHIFT_IZQUIERDA': r'<<',
    'SHIFT_DERECHA': r'>>',
    'COMENTARIO_UNA_LINEA': r'//.*?$',
    'COMENTARIO_MULTI_LINEA': r'/\*.*?\*/',
    'ESPACIO': r'\s+'
}

def lexer(codigo):
    tokens = []  # Lista para almacenar los tokens encontrados
    posicion = 0  # Posición actual en el código

    while codigo:
        codigo = codigo.lstrip()  # Eliminar espacios en blanco al principio
        if not codigo:
            break  # Salir si no hay más código después de los espacios en blanco

        coincidencia = None
        for tipo_token, patron in tokens_regex.items():
            regex = re.compile(patron)
            coincidencia = regex.match(codigo)
            if coincidencia:
                valor = coincidencia.group(0)
                if tipo_token == 'IDENTIFICADOR' and valor in palabras_reservadas:
                    tipo_token = 'PALABRA_RESERVADA'  # Cambiar el tipo a 'PALABRA_RESERVADA' si el identificador es una palabra reservada
                # Agregar el token a la lista con su tipo, valor y posición inicial y final
                tokens.append((tipo_token, valor, posicion + coincidencia.start(), posicion + coincidencia.end() - 1))
                posicion += coincidencia.end()  # Actualizar la posición para el próximo análisis
                codigo = codigo[coincidencia.end():]  # Actualizar el código restante
                break

        if not coincidencia:
            # Si no hay coincidencia, significa que hay un carácter inesperado
            raise SyntaxError(f"Error léxico: carácter inesperado '{codigo[0]}' en la posición {posicion}")

    return tokens

# Ejemplo de uso
codigo = """
int main() {
    printf("Hola Mundo!");
    return 0;
}
"""

tokens_encontrados = lexer(codigo)
for token in tokens_encontrados:
    print(token)

