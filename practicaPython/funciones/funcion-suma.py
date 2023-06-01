def sumar(a, b):
    suma = a + b
    return suma


numero_1 = float(input("Ingrese el primer Numero: "))
numero_2 = float(input("Ingrese el segundo Numero: "))

resultado = sumar(numero_1, numero_2)
print("la suma de {} y {} es igual a {}".format(numero_1, numero_2, resultado))
