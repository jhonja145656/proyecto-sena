mascotas = ["Goya", "Rocket", "linux", "shury", "cayo", "rayito"]
# se indica el indice donde queremos agregar  el valor o nombre
mascotas.insert(1, "chory")
print(mascotas)
mascotas.append("pollito")  # agrega "pollito" al final de la lista
print(mascotas)

mascotas.remove("chory")  # se indica el valor o nombre del elemento a eliminar
print(mascotas)

mascotas.pop()  # elimina el ultimo elemento
print(mascotas)
mascotas.append("pollitos")
print(mascotas)
del mascotas[2]
mascotas.append("linux")

print(mascotas)
