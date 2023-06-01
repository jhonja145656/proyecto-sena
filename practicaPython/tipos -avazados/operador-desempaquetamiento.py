usuarios = [
    {"id": 1, "nombre": "john"},
    {"id": 2, "nombre": "Emma"},
    {"id": 3, "nombre": "Tina"},
    {"id": 4, "nombre": "Yenny"}
]
print(*usuarios)

usuarios2 = [{"id": 5, "nombre": "Robert"},
             {"id": 6, "nombre": "Elsy"},
             {"id": 7, "nombre": "Dennis"},]
usuarioscombinados = [*usuarios, *usuarios2]
print(usuarioscombinados)
