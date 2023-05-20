import tkinter as tk
from tkinter import messagebox
import datetime

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Factura:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []
        self.total = 0
        self.fecha = datetime.datetime.now()

    def agregar_item(self, producto, cantidad):
        subtotal = producto.precio * cantidad
        self.items.append((producto, cantidad, subtotal))
        self.total += subtotal

    def generar_factura(self):
        factura_texto = "******** FACTURA ********\n"
        factura_texto += "Fecha: " + str(self.fecha) + "\n"
        factura_texto += "Cliente: " + self.cliente + "\n"
        factura_texto += "----------------------------\n"
        for item in self.items:
            producto, cantidad, subtotal = item
            factura_texto += f"{producto.nombre} x {cantidad}: ${subtotal}\n"
        factura_texto += "----------------------------\n"
        factura_texto += "Total: $" + str(self.total)

        messagebox.showinfo("Factura", factura_texto)

def agregar_producto():
    nombre = entry_producto.get()
    precio = float(entry_precio.get())
    cantidad = int(entry_cantidad.get())

    producto = Producto(nombre, precio)
    factura.agregar_item(producto, cantidad)

    entry_producto.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)

root = tk.Tk()
root.title("Sistema de Facturación")

label_producto = tk.Label(root, text="Producto:")
label_producto.pack()
entry_producto = tk.Entry(root)
entry_producto.pack()

label_precio = tk.Label(root, text="Precio:")
label_precio.pack()
entry_precio = tk.Entry(root)
entry_precio.pack()

label_cantidad = tk.Label(root, text="Cantidad:")
label_cantidad.pack()
entry_cantidad = tk.Entry(root)
entry_cantidad.pack()

boton_agregar = tk.Button(root, text="Agregar", command=agregar_producto)
boton_agregar.pack()

factura = Factura("Juan Pérez")

root.mainloop()
