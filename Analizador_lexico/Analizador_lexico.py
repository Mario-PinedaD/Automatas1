import re

class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def __str__(self):
        return f'Token({self.tipo}, {self.valor})'

class Lexer:
    def __init__(self, texto):
        self.texto = texto
        self.posicion = 0
        self.tokens = []

    def obtener_tokens(self):
        while self.posicion < len(self.texto):
            caracter_actual = self.texto[self.posicion]

            if caracter_actual.isdigit():
                self.tokens.append(self.obtener_numero())
            elif caracter_actual in ['+', '-', '*', '/', '(', ')']:
                self.tokens.append(Token('OPERADOR', caracter_actual))
                self.posicion += 1
            elif caracter_actual.isspace():
                self.posicion += 1
            else:
                raise Exception(f'Caracter inesperado: {caracter_actual}')

        self.tokens.append(Token('FIN', None))
        return self.tokens

    def obtener_numero(self):
        numero = ''
        punto_decimal = False

        while self.posicion < len(self.texto) and (self.texto[self.posicion].isdigit() or self.texto[self.posicion] == '.'):
            if self.texto[self.posicion] == '.':
                if punto_decimal:
                    break
                punto_decimal = True
                numero += '.'
            else:
                numero += self.texto[self.posicion]
            self.posicion += 1

        if punto_decimal:
            return Token('NUMERO', float(numero))
        else:
            return Token('NUMERO', int(numero))

# Ejemplo de uso
texto = "public void setFuncion()"
lexer = Lexer(texto)
tokens = lexer.obtener_tokens()

for token in tokens:
    print(token)
