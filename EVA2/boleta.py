class Boleta:

    def __init__(self, idboleta, numero, producto, cantidad):
        self.idboleta = idboleta
        self.numero = numero
        self.producto = producto
        self.cantidad = cantidad
        self.precio = producto.precio
        self.subtotal = self.cantidad * self.precio

    def mostrarBoleta (self):
        txt = """
        Boleta Número {},
        Producto Número {},
        Producto asociado: {}
        Cantidad: {}
        Precio : {:.0f}
        Subtotal: {}
        """.format(self.idboleta, self.numero,  self.producto, self.cantidad, self.precio, self.subtotal)

        return txt

    def mostrarDetalle (self):
        txt ="{} = {} * {:.0f} = {:.0f}\n".format(self.producto.nombre, self.cantidad, self.precio, self.subtotal)
        return txt

    def devolverSubtotal (self):
        return self.subtotal

    def totalPagar (self):
        total = int(self.cantidad) + int(self.precio)
        return total

    def mostrarCarrito(self):
        txt = "ID: {}, Producto: {} * {} = {}".format(self.numero, self.producto.nombre, self.cantidad, self.subtotal)
        return txt
    def __str__(self):
        txt = """
        Boleta Número {},
        Producto Numero {},
        Producto asociado: {}
        Cantidad: {}
        Precio : {:.0f}
        Subtotal: {}
        """.format(self.idboleta,self.numero,  self.producto, self.cantidad, self.precio, self.subtotal)

        return txt








