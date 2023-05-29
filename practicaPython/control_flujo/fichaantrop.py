"""import tkinter as tk

def guardar_ficha():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    altura = entry_altura.get()
    peso = entry_peso.get()

    # Aquí puedes realizar las operaciones o guardar los datos como desees

    # Ejemplo: imprimir los datos en la consola
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Altura:", altura)
    print("Peso:", peso)

    # Puedes agregar aquí el código para guardar los datos en un archivo o base de datos

    # Limpiar los campos de entrada
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ficha Antropométrica")

# Crear etiquetas y campos de entrada
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_edad = tk.Label(ventana, text="Edad:")
label_edad.pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

label_altura = tk.Label(ventana, text="Altura:")
label_altura.pack()
entry_altura = tk.Entry(ventana)
entry_altura.pack()

label_peso = tk.Label(ventana, text="Peso:")
label_peso.pack()
entry_peso = tk.Entry(ventana)
entry_peso.pack()

# Botón para guardar la ficha
boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_ficha)
boton_guardar.pack()

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()

import tkinter as tk

def guardar_ficha():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    altura = entry_altura.get()
    peso = entry_peso.get()
    cintura = entry_cintura.get()

    # Aquí puedes agregar la lógica para guardar la ficha en una base de datos o archivo

    # Ejemplo de impresión de los datos
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Altura:", altura)
    print("Peso:", peso)
    print("Cintura:", cintura)

    # Limpia los campos después de guardar la ficha
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_cintura.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ficha Antropométrica")

# Etiquetas
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_edad = tk.Label(ventana, text="Edad:")
label_edad.pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

label_altura = tk.Label(ventana, text="Altura:")
label_altura.pack()
entry_altura = tk.Entry(ventana)
entry_altura.pack()

label_peso = tk.Label(ventana, text="Peso:")
label_peso.pack()
entry_peso = tk.Entry(ventana)
entry_peso.pack()

label_cintura = tk.Label(ventana, text="Cintura:")
label_cintura.pack()
entry_cintura = tk.Entry(ventana)
entry_cintura.pack()

# Botón Guardar
boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_ficha)
boton_guardar.pack()

# Ejecutar la aplicación
ventana.mainloop() """

# Definición de la clase para la ficha antropométrica
class FichaAntropometrica:
    def __init__(self, nombre, edad, sexo, altura, peso, circunferencia_cintura, circunferencia_cadera):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.altura = altura
        self.peso = peso
        self.circunferencia_cintura = circunferencia_cintura
        self.circunferencia_cadera = circunferencia_cadera

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc

    def calcular_relacion_cintura_cadera(self):
        relacion = self.circunferencia_cintura / self.circunferencia_cadera
        return relacion

    def mostrar_ficha(self):
        print("Ficha Antropométrica")
        print("====================")
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Sexo:", self.sexo)
        print("Altura:", self.altura)
        print("Peso:", self.peso)
        print("Circunferencia de la cintura:", self.circunferencia_cintura)
        print("Circunferencia de la cadera:", self.circunferencia_cadera)
        print("IMC:", self.calcular_imc())
        print("Relación cintura-cadera:", self.calcular_relacion_cintura_cadera())

# Crear una instancia de la ficha antropométrica
ficha = FichaAntropometrica("John Angulo", 46, "Masculino", 1.70, 69, 80, 90)

# Mostrar la ficha antropométrica
ficha.mostrar_ficha()

