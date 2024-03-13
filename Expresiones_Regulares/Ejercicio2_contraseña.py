#diseñar una ER para verificar la robustez de una password
#1 minuscula
#1 mayuscula
#1 nmero
#1 caracter especial

import re
#                Min-may dig caracteres {minimo, max}
p = re.compile("^[A-Za-z\d@$!%*?&]{8,}$")

cadena = input('Introduce la contraseña: ')
res = p.match(cadena)

if res:
    print("Cadena ACEPTADA")
else:
    print("Cadena RECHAZADA")
