import datetime
ahora = datetime.datetime.now()
print("La fecha y hora actual es : ", ahora)
# formatear fecha y hora como cadena de caracteres
horactual_formateada = ahora.strftime("%H:%M:%S %d-%m-%y")
print(horactual_formateada)
