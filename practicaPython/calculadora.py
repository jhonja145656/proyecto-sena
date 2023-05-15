n1 = input("Ingresa Primer Numero")
n2 = input("Ingresa Segundo Numero")
n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
divi = n1 / n2
resto = n1 % n2
mensaje = f""" 
 Para los numero {n1} y {n2},
 Elresultado de la suma es {suma}.
 Elresultado de la resta es {resta}.
 Elresultado de la multiplicacion es {multi}.
 Elresultado de la divicion es {divi}.
 Elresultado de la resto es {resto}.


"""


print(mensaje)
