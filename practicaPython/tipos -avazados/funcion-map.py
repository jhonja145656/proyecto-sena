usuarios = [["pedro", 2], ["carlo", 1], ["john", 4], ["tina", 5]]
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

# FILTRAR ELEMENTOS DE LA LISTA!
menosusuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosusuarios)
