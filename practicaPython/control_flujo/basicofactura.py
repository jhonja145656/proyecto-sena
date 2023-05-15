import tkinter as tk

class FacturacionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Facturación")

        # Crear widgets
        self.label_producto = tk.Label(root, text="Producto:")
        self.label_producto.pack()
        self.entry_producto = tk.Entry(root)
        self.entry_producto.pack()

        self.label_precio = tk.Label(root, text="Precio:")
        self.label_precio.pack()
        self.entry_precio = tk.Entry(root)
        self.entry_precio.pack()

        self.boton_agregar = tk.Button(root, text="Agregar", command=self.agregar_producto)
        self.boton_agregar.pack()

        self.textarea_factura = tk.Text(root)
        self.textarea_factura.pack()

        self.total = 0

    def agregar_producto(self):
        producto = self.entry_producto.get()
        precio = float(self.entry_precio.get())

        self.textarea_factura.insert(tk.END, f"{producto}: ${precio}\n")
        self.total += precio

        self.entry_producto.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)

        self.actualizar_total()

    def actualizar_total(self):
        self.textarea_factura.insert(tk.END, f"Total: ${self.total}\n")

root = tk.Tk()
app = FacturacionApp(root)
root.mainloop()
