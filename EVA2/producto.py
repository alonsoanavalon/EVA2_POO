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
        if int(nuevoPrecio) and int(nuevoPrecio) > 0:
            self.precio = nuevoPrecio
            return print("El precio ha sido actualizado con éxito")
        else:
            error = print("El producto no ha podido ser actualizado")
            return error

    def restarStock (self, cantidad):
        if int(cantidad) and int(cantidad) > 0:
            self.stock -= cantidad
            return print ("El stock ha sido actualizado con éxito")
        else:
            error = print("El producto no ha podido ser actualizado")
            return error

    def validarStock(self, cantidad):
        if int(cantidad) and int(cantidad) >= 1 and self.stock >= 1:
            if self.stock > cantidad:
                return True
            elif self.stock < cantidad:
                return self.stock
        else:
            error = print("No hay stock para {}".format(self.nombre))
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

productito.restarStock(5)

print(type(productito.validarStock(10)))


print(productito.mostrarProducto())