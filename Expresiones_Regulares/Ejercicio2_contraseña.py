#diseñar una ER para verificar la robustez de una password
#1 minuscula
#1 mayuscula
#1 nmero
#1 caracter especial

import re
#                   
p = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[¡@#$%&^()*+=,.;:/¿?_-])[A-Za-z\d¡@#$%&^()*+=,.;:/¿?_-]{8,}$')
#p = re.compile('^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!\#$%&()*+,-./:;<=>?@[\\]^_`{|}~-])[A-Za-z\d!\#$%&()*+,-./:;<=>?@[\\]^_`{|}~-]{8,}$')

#cadena = input('Introduce la contraseña:')
cadena = "Tr@nixito7v7|"
#cadena = "Parangaricutirim¡cuaro77_pedritosol@"
#cadena = "nosedeberíadeaceptar"
#cadena = "contraseña1113_77"
print(f"Su cadena es {cadena}")
res = p.match(cadena)

if res:
    print("Cadena ACEPTADA")
else:
    print("Cadena RECHAZADA")
