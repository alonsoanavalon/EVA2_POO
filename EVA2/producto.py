from EVA2.precio import Precio

class Producto(Precio):
    def __init__(self, idproducto, nombre, stock, idprecio, preciolista, ganancia):
        super().__init__(idprecio, preciolista, ganancia)
        self.idproducto = idproducto
        self.nombre = nombre
        self.stock = stock
        self.ganancia = (ganancia / 100) + 1
        self.precio = self.ganancia * self.preciolista


    def mostrarProducto (self):
        txt = """
                ID : {},
                Nombre: {},
                Precio: {:.0f},
                Stock: {}
        """.format(self.idproducto, self.nombre, self.precio, self.stock)

        return txt

    def actualizarPrecio (self, nuevoPrecio, nuevaGanancia):
        if int(nuevoPrecio) and int(nuevoPrecio) > 0:
            ganancia = (nuevaGanancia/100) + 1
            self.precio = ganancia * nuevoPrecio
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

    def validarStock (self, cantidad):
        if int(cantidad) and int(cantidad) >= 1 and self.stock >= 1:
            if self.stock > cantidad:
                return True
            elif self.stock == cantidad:
                return self.stock
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
        """.format(self.idproducto, self.nombre, self.precio, self.stock)

        return txt


