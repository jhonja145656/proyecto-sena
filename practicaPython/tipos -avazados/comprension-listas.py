"""obtener listado de nombres sin el indice o numero de la derecha"""
usuarios = [["pedro", 2], ["carlo", 1], ["john", 4], ["tina", 5]]

"""nombres = []
for usuario in usuarios:
    nombres.append(usuario[0])
print(nombres)"""

# otra forma de utilizar for de forma mas elegante
nombres = [usuario[0] for usuario in usuarios]
print(nombres)
