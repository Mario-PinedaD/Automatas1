#Ejercicio_1
#Crear e implementar eun python un ER para validar lo siguiente:
#Correo Electrónico
#RFC (4 letras + 6 numeros (año - mes - dia) + 3 datos homoclave)
#CURP (4 letras + 6 numeros (año - mes - dia) + clave del estado + 3 letras + 3 caracteres )
import re

#Correo
#p = re.compile("^[a-zA-Z0-9\_\.]*[@]((hotmail|gmail|outlook|yahoo)+.com)$")

#RFC                4letras    año          mes             dia               3digitos
p = re.compile ("^([A-Z]{4})([0-9]{2})(0[1-9]|1[0-2])([0-2][0-9]|3[0-1])([A-Z0-9]{3})?$")

#CURP              4 letras    año            mes              dia              sexo                     estado                                                                                      Homoclave
#p = re.compile("^([A-Z]{4})([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])([HM])(AS|BC|BS|CC|CL|CM|CS|CH|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS)[^AEIOU]{3}[A-Z0-9]{2}$")

print("Introduce una cadena a comprobar:")
cadena = input()
#cadena = "CorreoPrueba_m4riopineda@gmail.com" #correo
#cadena = "PIDM030906HB9" #RFC PIDM030906HVZNMRA3
#cadena = "GOMA000101HDFRLR07" #CURP
res = p.match(cadena)

if res:
    print("Cadena ACEPTADA")
else:
    print("Cadena RECHAZADA")
    
#Cuenta 0112394962
#reporte 3021969