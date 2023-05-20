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
        print("******** FACTURA ********")
        print("Fecha:", self.fecha)
        print("Cliente:", self.cliente)
        print("----------------------------")
        for item in self.items:
            producto, cantidad, subtotal = item
            print(f"{producto.nombre} x {cantidad}: ${subtotal}")
        print("----------------------------")
        print("Total: $", self.total)

# Crear productos
producto1 = Producto("Camisa", 25.0)
producto2 = Producto("Pantalón", 40.0)
producto3 = Producto("Zapatos", 60.0)

# Crear factura
factura = Factura("Juan Pérez")

# Agregar items a la factura
factura.agregar_item(producto1, 2)
factura.agregar_item(producto2, 1)
factura.agregar_item(producto3, 1)

# Generar la factura
factura.generar_factura()
