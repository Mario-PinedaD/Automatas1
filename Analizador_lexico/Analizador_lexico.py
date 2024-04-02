import re

# Definición de palabras reservadas de JavaScript
palabras_reservadas = {
    'await', 'break', 'case', 'catch', 'class', 'const', 'continue', 'debugger',
    'default', 'delete', 'do', 'else', 'enum', 'export', 'extends', 'finally',
    'for', 'function', 'if', 'implements', 'import', 'in', 'instanceof', 'interface',
    'let', 'new', 'package', 'private', 'protected', 'public', 'return', 'static',
    'super', 'switch', 'this', 'throw', 'try', 'typeof', 'var', 'void', 'while', 'with', 'yield'
}

# Definición de tokens con expresiones regulares para JavaScript
tokens_regex = {
    'IDENTIFICADOR': r'[a-zA-Z_]\w*',
    'NUMERO': r'\b\d+(\.\d+)?\b',
    'OPERADOR': r'[-+*/%&|=<>!^~?:]',
    'PARENTESIS': r'[()\[\]{}]',
    'PUNTO_Y_COMA': r';',
    'COMA': r',',
    'PUNTO': r'\.',
    'COMILLA_SIMPLE': r'\'',
    'COMILLA_DOBLE': r'\"',
    'ASIGNACION': r'=',
    'INCREMENTO': r'\+\+',
    'DECREMENTO': r'--',
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
let x = 10;
if (x === 10) {
    console.log("El valor de x es 10");
} else {
    console.log("El valor de x no es 10");
}
"""

tokens_encontrados = lexer(codigo)
for token in tokens_encontrados:
    print(token)

