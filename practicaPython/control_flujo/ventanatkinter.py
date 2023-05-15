import tkinter as tk
from tkinter import messagebox

def calcular_total():
    # Lógica para calcular el total de la factura
    precio_unitario = float(entry_precio.get())
    cantidad = int(entry_cantidad.get())
    total = precio_unitario * cantidad
    messagebox.showinfo("Total", f"El total es: {total}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Facturación")

# Etiqueta y campo de entrada para el precio unitario
label_precio = tk.Label(ventana, text="Precio unitario:")
label_precio.pack()
entry_precio = tk.Entry(ventana)
entry_precio.pack()

# Etiqueta y campo de entrada para la cantidad
label_cantidad = tk.Label(ventana, text="Cantidad:")
label_cantidad.pack()
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack()

# Botón para calcular el total
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_total)
boton_calcular.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
