punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])  # mustra el valor de X
# if "goya" in punto:
# si existe mustra el valor del string o llave.
# print("encontre a goya", punto["goya"])

print(punto.get("y"))  # si existe mustra el valor del string o llave.
# mustra el valor del string o llave por defecto asi no exista
print(punto.get("goya", 3))
del punto["x"]
del punto["y"]
punto["x"] = 30
punto["y"] = 35


print(punto)
for valor in punto:
    print(valor, punto[valor])
    # otra forma de acceder a los valores :
for valor in punto.items():
    print(valor)
    # para desempaquetar:
    for llave, valor in punto.items():
        print(llave, valor)

    # vamos a darle un uso mas real:

usuarios = [
    {"id": 1, "nombre": "john"},
    {"id": 2, "nombre": "Emma"},
    {"id": 3, "nombre": "Tina"},
    {"id": 4, "nombre": "Yenny"}
]

for usuario in usuarios:
    print(usuario["nombre"])
