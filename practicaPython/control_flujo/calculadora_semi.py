print("Bienvenidos a la calculadora")
print("para salir escribe: salir")
print("Las operaciones son: suma, resta, divi, multi y Residuo")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("ingrese operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa el siguiente Numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "divi":
        resultado /= n2
    elif op.lower() == "residuo":
        resultado %= n2
    else:
        print("Ingresa una operacion valida")
        break
    print(f"El resultado es {resultado}")
    break
