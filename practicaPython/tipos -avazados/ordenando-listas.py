numeros = [1, 5, 45, 2, 3, 6, 8, 4, 9, 7, 12, 52, 45, 85, 32, 13, 1, 5,]
# numeros.sort()
# print(numeros)

# numeros.sort(reverse=True)  # orden inverso
# print(numeros)
print(numeros)

numeros2 = sorted(numeros)  # crea una nueva lista
print(numeros2)

usuarios = [["pedro", 2], ["carlo", 1], ["john", 4], ["tina", 5]]
usuarios.sort()  # lo ordena alfabeticamente por que son textos al principio
# print(usuarios)


def ordenar(elemento):
    return elemento[1]


usuarios.sort(key=ordenar)
print(usuarios)

# ordenar inverso
usuarios.sort(key=ordenar, reverse=True)

print(usuarios)
