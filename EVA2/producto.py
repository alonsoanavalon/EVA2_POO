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
            return "El precio ha sido actualizado con éxito"
        else:



    def __str__(self):
        txt = """
                ID : {},
                Nombre: {},
                Precio: {},
                Stock: {}
        """.format(self.id, self.nombre, self.precio, self.stock)

        return txt


productito = Producto(20, "Pan", 2000, 10)

print(productito.mostrarProducto())

productito.actualizarPrecio(0)

print(productito.mostrarProducto())