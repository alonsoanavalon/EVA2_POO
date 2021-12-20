from EVA2.precio import Precio

class Producto(Precio):


    def __init__(self, idproducto, nombre, stock, idprecio, preciolista, ganancia, proveedor, categoria):
        super().__init__(idprecio, preciolista, ganancia)
        self.idproducto = idproducto
        self.nombre = nombre
        self.stock = stock
        self.proveedor = proveedor
        self.categoria = categoria
        self.ganancia = (ganancia / 100) + 1
        self.precio = self.ganancia * self.preciolista



    def mostrarProducto (self):
        txt = """
                ID : {},
                Nombre: {},
                Precio: {:,.0f},
                Stock: {},
                Proveedor: {},
                Categoría: {}
        """.format(self.idproducto, self.nombre, self.precio, self.stock, self.proveedor, self.categoria).replace(',','.')

        return txt


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
                Precio: {:.0f},
                Stock: {},
                Proveedor: {},
                Categoría: {}
        """.format(self.idproducto, self.nombre, self.precio, self.stock, self.proveedor, self.categoria).replace(',','.')

        return txt

    # CRUD PRODUCTOS
    # Create

    def crearProducto(idproducto, nombre, stock, idprecio, preciolista, ganancia, proveedor, categoria, listaProductos):
        producto = Producto(idproducto, nombre, stock, idprecio, preciolista, ganancia, proveedor, categoria)
        listaProductos.append(producto)
        return producto

    def traerProducto(idproducto, listaProductos):
        idBuscar = idproducto
        for producto in listaProductos:
            if producto.idproducto == idBuscar:
                return print(producto.mostrarProducto())

    def traerProductos(listaProductos):
        for producto in listaProductos:
            print(producto.mostrarProducto())

    def actualizarProducto(idproducto, nombre, stock, preciolista, ganancia, proveedor,
                           categoria, listaProductos):
        idBuscar = idproducto
        for producto in listaProductos:
            if producto.idproducto == idBuscar:
                producto.nombre = nombre
                producto.stock = stock
                producto.preciolista = preciolista
                producto.ganancia = (ganancia / 100) + 1
                producto.precio = producto.ganancia * producto.preciolista
                producto.proveedor = proveedor
                producto.categoria = categoria
                return producto.mostrarProducto()

    def actualizarProductoPorNombre(nombreBuscar, nombre, stock, preciolista, ganancia, proveedor,
                           categoria, listaProductos):
        for producto in listaProductos:
            if producto.nombre == nombreBuscar:
                producto.nombre = nombre
                producto.stock = stock
                producto.preciolista = preciolista
                producto.ganancia = (ganancia / 100) + 1
                producto.precio = producto.ganancia * producto.preciolista
                producto.proveedor = proveedor
                producto.categoria = categoria
                return producto.mostrarProducto()

    def eliminarProducto(idproducto, listaProductos):
        idBuscar = idproducto
        for producto in listaProductos:
            if producto.idproducto == idBuscar:
                listaProductos.pop(idBuscar-1)
                print("Se ha eliminado el producto con id {}".format(producto.idproducto))
                return listaProductos
                break


