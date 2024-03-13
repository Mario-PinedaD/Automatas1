#diseñar una ER para verificar la robustez de una password
#1 minuscula
#1 mayuscula
#1 nmero
#1 caracter especial

import re

p = re.compile("^[a-zA-Z]{8,?}$")

cad = input('Introduzca la cadena: ')

res = p.match(cad)

if res:
    print("Contraseña GOD")
else:
    print("Contraseña no")
    
