# Set significa grupo o conjunto
# los set en python elimina los elementos duplicados en este caso el 3
grupoUno = {1, 2, 3, 3, 4, 5}
grupoUno.add(5)
grupoUno.remove(1)

print(grupoUno)

grupoDos = [3, 4, 5, 6, 7, 7, 8]  # Lista
grupoDos = set(grupoDos)  # convierte lista a set
print(grupoDos)
print(grupoUno | grupoDos)  # "|" OPERADOR DE UNION
print(grupoUno & grupoDos)  # "|" OPERADOR DE INTERSECCION
print(grupoUno - grupoDos)  # "|" OPERADOR DE DIFERENCIA DEL PRIMER SET
print(grupoUno ^ grupoDos)  # "|" OPERADOR DE DIFERENCIA SIMETRICA
