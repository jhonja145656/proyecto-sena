usuarios = [["pedro", 2], ["carlo", 1], ["john", 4], ["tina", 5]]
usuarios.sort(key=lambda argumento: argumento[1])
print(usuarios)

# ordena al inverso
usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
