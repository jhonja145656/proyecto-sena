# LAS TUPLAS SON PARENTESIS () Y NO SE PUEDEN MODIFICAR PERO SI CREAR NUEVAS DE UNA EXIXTENTE
# LAS LISTAS SON CORCHETES CUADRADOS [] ESTAS SI SE PUEDEN MODIFICAR
numeros = (1, 2, 3,)+(4, 5, 6,)
print(numeros)

punto = tuple([1, 2])
print(punto)
menosnumeros = numeros[:2]
print(menosnumeros)

# MODIFICAR LA LISTA EN BASE A LA TUPLA LO IDEAL ES NO HACERLO.
listaNumeros = list(numeros)
listaNumeros[0] = "Goya"

print(listaNumeros)
