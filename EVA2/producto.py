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

    def __str__(self):
        txt = """
                ID : {},
                Nombre: {},
                Precio: {},
                Stock: {}
        """.format(self.id, self.nombre, self.precio, self.stock)

        return txt

