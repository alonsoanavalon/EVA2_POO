class Producto:
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrarProducto (self):
        txt = """
                ID : {},
                Nombre: {},
                Precio: {},
                Stock: {}
        """.format(self.id, self.nombre, self.precio, self.stock)

        return txt

    def actualizarPrecio (self, nuevoPrecio):
        if int(self.precio) and int(nuevoPrecio) > 0:
            self.precio = nuevoPrecio
            return print("El precio ha sido actualizado con éxito")
        else:
            error = print("El producto no ha podido ser actualizado")
            return error

    def restarStock (self, cantidad):
        if int(self.precio) and int(cantidad) > 0:
            self.stock -= cantidad
            return "El stock ha sido actualizado con éxito"
        else:
            error = print("El producto no ha podido ser actualizado")
            return error




    def __str__(self):
        txt = """
                ID : {},
                Nombre: {},
                Precio: {},
                Stock: {}
        """.format(self.id, self.nombre, self.precio, self.stock)

        return txt


productito = Producto(20, "Pan", 2000, 10)

productito.actualizarPrecio(0)
productito.restarStock(2)

print(productito.mostrarProducto())