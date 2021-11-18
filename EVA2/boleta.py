class Boleta:
    def __init__(self, numero, producto, cantidad, precio):
        self.numero = numero
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio

    def mostrarBoleta (self):
        txt = """
        Boleta Número {},
        Producto asociado: {}
        Cantidad: {}
        Precio : {}
        """.format(self.numero, self.producto, self.cantidad, self.precio)

        return txt

    def totalPagar(self):
        total = int(self.cantidad) + int(self.precio)
        return total



