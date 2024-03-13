#Ejercicio_1
#Crear e implementar eun python un ER para validar lo siguiente:
#Correo Electrónico
#RFC (4 letras + 6 numeros (año - mes - dia) + 3 datos homoclave)
#CURP (4 letras + 6 numeros (año - mes - dia) + )
import re

#Correo
#p = re.compile("^[a-zA-Z0-9\_]*[@]((hotmail|gmail|outlook|yahoo)+\.com)$")

#RFC
#p = re.compile ("^([A-Z]{4})([0-9]{2})(0[1-9]|1[0-2])([0-2][0-9]|3[0-1])([A-Z0-9]{3})$")

#CURP
p = re.compile(
    r"^([A-Z]{4})"                # Primer grupo de 4 letras
    r"([0-9]{2})"                 # Segundo grupo de 2 números
    r"(0[1-9]|1[0-2])"            # Tercer grupo para el mes (01-12)
    r"(0[1-9]|[1-2][0-9]|3[0-1])" # Cuarto grupo para el día (01-31)
    r"([HM])"                     # Quinto grupo para el género (H o M)
    r"(AS|BC|BS|CC|CL|CM|CS|CH|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS)"  # Séptimo grupo para el estado
    r"[^AEIOU0-9]{3}"
    r"[A-Z0-9]{2}$"
)


print("Introduce una cadena a comprobar:")
cadena = input()
#cadena = "GOMA000101HDFRLR07"
res = p.match(cadena)

if res:
    print("Cadena ACEPTADA")
else:
    print("Cadena RECHAZADA")
    
#Cuenta 0112394962
#reporte 3021969