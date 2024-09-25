class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad
    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad
    def actualizar_precio(self, precio):
        self.precio = precio
    def mostrar_informacion(self):
        return f"Producto: {self.nombre},Categoría: {self.categoria}, Precio: {self.precio}, Cantidad: {self.cantidad}"