# el parametro (*numeros) nos permite iterar varios argumentos numeros etc.
def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 7)
suma(2, 5, )
suma(2, 5, 45, 32)
