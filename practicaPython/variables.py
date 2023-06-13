nombreCurso = "python ultimate"
descripcionCurso = """"Este curso contempla todo los detalles 
necesarios para aprender y trabajar como programador"""

alumno = 5000
puntaje = 9.8
publicado = True

print(descripcionCurso, alumno, puntaje, publicado)

# longitud de cadenas de caracteres
len(nombreCurso)
print(len(nombreCurso))

# acceder a un caracter o porcion de la cadena
print(nombreCurso[3])
print(nombreCurso[6:14])
print(nombreCurso[0:6])
print(nombreCurso[6:])
print(nombreCurso[:])

# formatear
# Format string PY:
print(nombreCurso.upper())
print(nombreCurso.lower())
print(casa.lower())


# coloca la primera letra en mayuscula
print(nombreCurso.capitalize())
# coloca la primera letra de cada palabra en mayuscula
print(nombreCurso.title())
# si arroja un numero positivo es por que si se encuentra el o los caracteres,
# pero si es negativo significa que no se encuentra.*/
print(nombreCurso.replace("ul", "pu"))  # remplaza cadenas o cracter
