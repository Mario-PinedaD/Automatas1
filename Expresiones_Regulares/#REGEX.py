#REGEX
import re

#Cuantificador
#Consideando que unicamente queremos que acepte n longitud (cuantificiador): ^[palabras]{n}$
#Palabras de 2 a 5 caracteres ^[abc]{2,5}*$
#p = re.compile("^[abc]{2,5}$") 

#Acepta la A, B o C
#p = re.compile("^(a|b|c)$")

#Considerando que queremos que se acepten n cantidades de a o b o c
#p = re.compile("^(a|b|c)*$")

#Consideerando que aceptamos abc de 0 a 2 de longitud o de 8 a 10 de longitud
#p = re.compile("^([abc]{0,2}|[abc]{8,10})$")

#Negación
#p = re.compile("^[^abc]$")

#Union
#p = re.compile("^[0-9]{1,2}$")

#Digitos
#p = re.compile("^[/d]{1,2}$")

#Letras
#p = re.compile("^[0-9]{1,2}$")
#Cualquier simbolo de n longitud (con puntos)
#p = re.compile("^...$")

#Espacios en blanco
#p = re.compile("^\s$")

#Acepte puntos
#p = re.compile("^\.$")

#Ejemplo: Que acepte un ejemplo como miserver.favorito.
p = re.compile("^([a-zA-Z]+\.)+(com|mx|org)$")


print("Introduce una cadena a comprobar:")
cadena = input()
res = p.match(cadena)

if res:
    print("Cadena ACEPTADA")
else:
    print("Cadena RECHAZADA")