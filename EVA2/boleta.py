class Boleta:

    def __init__(self, numero, producto, cantidad):
        self.numero = numero
        self.producto = producto
        self.cantidad = cantidad
        self.precio = producto.precio
        self.subtotal = self.cantidad * self.precio

    def mostrarBoleta (self):
        txt = """
        Boleta Número {},
        Producto asociado: {}
        Cantidad: {}
        Precio : {:.0f}
        Subtotal: {}
        """.format(self.numero, self.producto, self.cantidad, self.precio, self.subtotal)

        return txt

    def mostrarDetalle (self):
        txt ="{} = {} * {:.0f} = {:.0f}\n".format(self.producto.nombre, self.cantidad, self.precio, self.subtotal)
        return txt

    def devolverSubtotal (self):
        return self.subtotal

    def totalPagar (self):
        total = int(self.cantidad) + int(self.precio)
        return total







