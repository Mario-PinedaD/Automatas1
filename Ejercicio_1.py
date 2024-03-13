#Ejercicio_1
#Crear e implementar eun python un ER para validar lo siguiente:
#Correo Electrónico
#RFC (4 letras + 6 numeros (año - mes - dia) + 3 datos homoclave)
#CURP (4 letras + 6 numeros (año - mes - dia) + )
import re

#Correo
#p = re.compile("^[a-zA-Z0-9\_]*[@]((hotmail|gmail|outlook|yahoo)+\.com)$")

#RFC
#p = re.compile("^[A-Z]{4} + [1-9]{2}+([A-Z] + [0-9]){3}$")
#p = re.compile("^[(A-Z){4}]*[0-9]{2}(01|02|03|04|05|06|07|08|09|10|11|12)$") #
p = re.compile("^$")

print("Introduce una cadena a comprobar:")
cadena = input()
res = p.match(cadena)

if res:
    print("Cadena ACEPTADA")
else:
    print("Cadena RECHAZADA")
    
#Cuenta 0112394962
#reporte 3021969