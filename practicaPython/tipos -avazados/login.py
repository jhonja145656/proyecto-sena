def crear_cuenta():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    # Aquí puedes guardar los datos de la cuenta en una base de datos o archivo


def iniciar_sesion():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    # Aquí puedes verificar si los datos ingresados coinciden con los registrados


# Menú principal
while True:
    print("1. Crear cuenta")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_cuenta()
    elif opcion == "2":
        iniciar_sesion()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, seleccione nuevamente.")
