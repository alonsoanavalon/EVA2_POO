from EVA2.producto import Producto
from EVA2.boleta import Boleta



#Antes de agregarlo deberíamos hacer las comprobaciones correspondientes

def validarNumero(pregunta):
    while True:
        try:
            numero = int(input(pregunta))
        except ValueError:
            print("Debes escribir un número.")
            continue

        if type(numero) == float:
            print("Debes escribir un numero entero")
            continue

        if numero < 0:
            print("Debes escribir un número positivo.")
            continue

        else:
            break
    return numero

def mostrarProductos(listaProductos):
    for producto in listaProductos:
        print(producto.mostrarProducto())

def generarBoletaVenta(numBoleta):
    txt = "\nBoleta N°{}\n".format(numBoleta)
    txt += "Detalle de compra:\n"
    total = 0
    contadorProducto = 1
    for boleta in listaBoleta:
        if boleta.numero == numBoleta:
            txt += "{}. ".format(contadorProducto)
            txt += boleta.mostrarDetalle()
            total += boleta.devolverSubtotal()
            contadorProducto += 1

    txt += "El total de la compra es = ${:.0f}".format(total)
    return txt

# CRUD PRODUCTOS
# Create

def crearProducto(idproducto, nombre, stock, idprecio, preciolista, ganancia, proveedor, categoria):
    producto = Producto(idproducto,nombre,stock,idprecio,preciolista, ganancia, proveedor, categoria)
    listaProductos.append(producto)
    return producto

def traerProducto(idproducto, listaProductos):
    idBuscar = idproducto
    for producto in listaProductos:
        if producto.idproducto == idBuscar:
            return producto.mostrarProducto()

def actualizarProducto(idproducto, nombre, stock, idprecio, preciolista, ganancia, listaProductos, proveedor, categoria):
    idBuscar = idproducto
    for producto in listaProductos:
        if producto.idproducto == idBuscar:
            producto.nombre = nombre
            producto.stock = stock
            producto.idprecio = idprecio
            producto.preciolista = preciolista
            producto.ganancia = (ganancia / 100) + 1
            producto.precio = producto.ganancia * producto.preciolista
            producto.proveedor = proveedor
            producto.categoria = categoria
            return producto.mostrarProducto()

def eliminarProducto(idproducto, listaProductos):
    idBuscar = idproducto
    contador = 0
    for producto in listaProductos:
        print("Vuelta n°{}".format(contador))
        if producto.idproducto == idBuscar:
            listaProductos.pop(contador)
            print("Se ha eliminado el producto con id {}, contador {}, nombre {}".format(producto.idproducto, contador, producto.nombre))
            return listaProductos
            break
        else:
            contador += 1





listaProductos = []

martillo = crearProducto(1, "martillo", 50, 2, 8000, 20, "makita", "herramientas")
taladro = crearProducto(2, "taladro", 50, 3, 30000, 15, "B&D", "herramientas")
cemento = crearProducto(3, "cemento", 40, 4, 40000, 15, "polpaico", "herramientas")
clavos = crearProducto(4, "clavos", 50, 5, 3000, 30, "genericos", "insumos")
tornillos = crearProducto(5, "tornillos", 100, 6, 2500, 50, "genericos", "insumos")
tuboPvc = crearProducto(6, "tubo pvc", 60, 7, 4000, 40, "makita", "herramientas")
pintura = crearProducto(7, "pintura", 50, 8, 6000, 30, "ceresita", "pinturas")
pastaMuro = crearProducto(8, "pasta muro", 60, 9, 10000, 35, "tajamar", "materiales")
desatornillador = crearProducto(9, "desatornillador", 30, 10, 4000, 35, "stanley", "herramientas")
diablo = crearProducto(10, "diablo", 20, 11, 8000, 20, "makita", "herramientas")
espatula = crearProducto(11, "espatula", 10, 1, 1000, 10, "makita", "herramientas")

#Prueba eliminando producto OK, Prueba traerProducto OK, actualizarProducto OK
#eliminarProducto(10, listaProductos)
#print(traerProducto(10, listaProductos))
#actualizarProducto(10,"test", 100, 11, 1000, 20, listaProductos)


listaBoleta = []

numBoleta = 1
productoEncontrado = False

mostrarProductos(listaProductos)

while True:
    productoEncontrado = False
    print("\nMenú de Opciones")
    print("1. Agregar producto (nuevo)")
    print("2. Actualizar precio producto")
    print("3. Generar boleta (venta)")
    print("4. Registro de boletas emitidas")
    print("5. Mostrar listado de productos")
    print("6. Salir/Finalizar")
    # MODIFICAR DESPUÉS AL 2
    print("7. Mantenedor de precios")
    opcion = validarNumero("Ingrese una opción (1-7): ")

    while opcion < 1 or opcion > 7:
        opcion = validarNumero("Ingrese una opción (1-7): ")

# 1. Mantenedor de productos
    # 1.1 Agregar producto (nuevo)
    # 1.2 Mostrar producto por ID
    # 1.3 Mostrar listado completo de productos
    # 1.4 Actualizar un producto (Nombre - Stock - Proveedor - Categoria)
    # 1.5 Eliminar un producto
# 2. Mantenedor de precios --- LISTO...?
    # 2.1 Mostrar precio por ID de producto --- LISTO...?
    # 2.2 Actualizar precio por ID de producto (Precio - Precio ganancia) --- LISTO...?
# 3. Generar boleta (venta)
# 4. Registro de boletas emitidas

    if opcion==1:
        print("\nAgregando producto...")
        nuevoProductoId = len(listaProductos)+1
        print("\nID nuevo producto: ", nuevoProductoId)
        nombre = input("\nIngrese nombre del producto: ")
        nombre = nombre.lower()
        preciolista = int(input("Ingrese precio: "))
        while preciolista < 1:
            preciolista = int(input("Ingrese precio: "))
        ganancia = int(input("Ingrese porcentaje de ganancia %: "))
        while ganancia < 1:
            ganancia = int(input("Ingrese porcentaje de ganancia %: "))
        stock = int(input("Ingrese stock: "))
        while stock < 1:
            stock = int(input("Ingrese stock: "))
        proveedor = input("Ingrese proveedor: ")
        categoria = input("Ingrese categoría: ")

        nuevoProducto = crearProducto(nuevoProductoId, nombre, stock, nuevoProductoId, preciolista, ganancia, proveedor, categoria)
        print("\nNuevo producto agregado: ", nuevoProducto)

# MODIFICAR/REEMPLAZAR MENU 2  "ACTUALIZANDO PRECIO" POR EL MENU 7 "MANTENEDOR DE PRECIOS" (ESTÁ MAS ABAJO)

    elif opcion==2:
        mostrarProductos(listaProductos)
        print("\nActualizando precio...")
        print("1. Buscar por ID")
        print("2. Buscar por Nombre")
        buscar =  validarNumero("Ingrese opción (1-2): ")
        while buscar > 2 or buscar < 1:
            buscar = validarNumero("Ingrese opción (1-2): ")

        if buscar == 1:
            idBuscar = validarNumero("Ingrese ID:")
            while idBuscar > len(listaProductos):
                idBuscar = validarNumero("Ingrese un ID entre {} y {}:".format(1, len(listaProductos)))
            for articulo in listaProductos:
                if articulo.idproducto == idBuscar:

                    print("Precio a modificar: ", articulo)
                    nuevoPrecio = validarNumero("Ingrese nuevo precio: ")
                    nuevaGanancia = validarNumero("Ingrese un nuevo porcentaje de ganancia en número: ")
                    articulo.actualizarPrecio(nuevoPrecio, nuevaGanancia)
                    print("Precio modificado: ", articulo)

        if buscar == 2:
            nombreBuscar = input("Ingrese nombre: ")
            nombreBuscar = nombreBuscar.lower()
            while type(nombreBuscar) != str:
                nombreBuscar = input("Ingrese nombre: ")
            for articulo in listaProductos:
                if articulo.nombre == nombreBuscar:
                    print("Precio a modificar: ", articulo)
                    nuevoPrecio = validarNumero("Ingrese nuevo precio: ")
                    articulo.actualizarPrecio(nuevoPrecio)
                    print("Precio modificado: ", articulo)

    elif opcion==3:

        print("\nGenerando boleta N°{}".format(numBoleta))
        print("1. Seleccionar producto por ID")
        print("2. Seleccionar producto por Nombre")
        buscar = validarNumero("Ingrese opción (1-2): ")
        while buscar > 2 or buscar < 1:
            buscar = validarNumero("Ingrese opción (1-2): ")



        mostrarProductos(listaProductos)

        respuesta = True

        while respuesta == True:

            if buscar == 1:
                productoEncontrado = False
                mostrarProductos(listaProductos)
                idBuscar = validarNumero("Ingrese ID:")

                while idBuscar > len(listaProductos) or idBuscar < 1:
                    idBuscar = validarNumero("Ingrese ID válido entre {} y {}:".format(1, len(listaProductos)))

                for articulo in listaProductos:
                    if articulo.idproducto == idBuscar:
                        productoEncontrado = True
                        if articulo.stock < 1 or articulo.stock == 0:
                            print("No hay stock de {}".format(articulo.nombre))
                            continue

                        print("Producto seleccionado", articulo)
                        cantidad = validarNumero("Ingrese cantidad: ")
                        while cantidad < 1:
                            cantidad = validarNumero("Ingrese cantidad mayor a 0: ")
                        cantidadStock = articulo.validarStock(cantidad)
                        if cantidadStock == True or cantidadStock == cantidad:
                            articulo.restarStock(cantidad)
                            boletaGenerada = Boleta(numBoleta, articulo, cantidad)
                            listaBoleta.append(boletaGenerada)
                            print(boletaGenerada.mostrarBoleta())
                        elif cantidadStock < cantidad:
                            res = input(
                                "{} tiene un stock de {}, ¿Desea comprar dicho stock? SI/NO: ".format(articulo.nombre,
                                                                                                      cantidadStock))
                            res = res.lower()
                            while res != "si" and res != "no":
                                res = input(
                                    "{} tiene un stock de {}, ¿Desea comprar dicho stock? SI/NO: ".format(
                                        articulo.nombre,
                                        cantidadStock))
                                res = res.lower()
                            if res == "si":
                                articulo.restarStock(cantidadStock)
                                boletaGenerada = Boleta(numBoleta, articulo, cantidadStock)
                                listaBoleta.append(boletaGenerada)
                                print(boletaGenerada.mostrarBoleta())
                            else:
                                break

                if productoEncontrado == False:
                    print("No se ha encontrado el producto con ID '{}'".format(idBuscar))

            if buscar == 2:
                productoEncontrado = False
                mostrarProductos(listaProductos)
                nombreBuscar = input("Ingrese nombre: ")
                nombreBuscar = nombreBuscar.lower()
                for articulo in listaProductos:
                    if articulo.nombre == nombreBuscar:
                        productoEncontrado = True
                        if articulo.stock < 1 or articulo.stock == 0:
                            print("No hay stock de {}".format(articulo.nombre))
                            continue

                        print("Producto seleccionado", articulo)
                        cantidad = validarNumero("Ingrese cantidad: ")

                        while cantidad < 1:
                            cantidad = validarNumero("Ingrese cantidad mayor a 0: ")
                        cantidadStock = articulo.validarStock(cantidad)
                        if cantidadStock == True:
                            articulo.restarStock(cantidad)
                            boletaGenerada = Boleta(numBoleta, articulo, cantidad)
                            listaBoleta.append(boletaGenerada)
                            print(boletaGenerada.mostrarBoleta())
                        elif type(cantidadStock) == int:
                            res = input(
                                "{} tiene un stock de {}, ¿Desea comprar dicho stock? SI/NO: ".format(articulo.nombre,
                                                                                                      cantidadStock))
                            res = res.lower()
                            while res != "si" and res != "no":
                                res = input(
                                    "{} tiene un stock de {}, ¿Desea comprar dicho stock? SI/NO: ".format(
                                        articulo.nombre,
                                        cantidadStock))
                                res = res.lower()
                            if res == "si":
                                articulo.restarStock(cantidadStock)
                                boletaGenerada = Boleta(numBoleta, articulo, cantidadStock)
                                listaBoleta.append(boletaGenerada)
                                print(boletaGenerada.mostrarBoleta())
                            else:
                                break

                if productoEncontrado == False:
                    print("No se ha encontrado el producto  '{}'".format(nombreBuscar))


            respuesta = input("¿Desea comprar un nuevo producto? SI/NO")
            respuesta.lower()
            if respuesta == "si":
                respuesta = True
            elif respuesta == "no":
                print(generarBoletaVenta(numBoleta))
                numBoleta += 1
                respuesta = False

    elif opcion == 4:
        if len(listaBoleta) == 0:
            print("No se han generado boletas")
            continue
        idBuscar = validarNumero("Ingrese ID boleta:")
        while idBuscar > len(listaBoleta) or idBuscar < 1:
            idBuscar = validarNumero("Ingrese ID boleta entre {} y {}:".format(1, len(listaBoleta)))
        print(generarBoletaVenta(idBuscar))

    elif opcion == 5:
        mostrarProductos(listaProductos)

    elif opcion == 7:
        print("\nMantenedor de precios")
        print("1. Consultar precio de producto por ID")
        print("2. Actualizar precio de producto por ID (Precio - Precio ganancia")
        seleccionPrecio = validarNumero("Ingrese opción (1-2): ")
        while seleccionPrecio > 2 or seleccionPrecio < 1:
            seleccionPrecio = validarNumero("Ingrese opción (1-2): ")

        if seleccionPrecio == 1:
            idBuscar = validarNumero("Ingrese ID de producto:")
            while idBuscar > len(listaProductos):
                idBuscar = validarNumero("Ingrese un ID entre {} y {}:".format(1, len(listaProductos)))
            for articulo in listaProductos:
                if articulo.idproducto == idBuscar:

                    print("Artículo consultado: ",articulo,"\nPrecio consultado: {:.0f} ".format(articulo.precio))

        if seleccionPrecio == 2:
            idBuscar = validarNumero("Ingrese ID de producto:")
            while idBuscar > len(listaProductos):
                idBuscar = validarNumero("Ingrese un ID entre {} y {}:".format(1, len(listaProductos)))
            for articulo in listaProductos:
                if articulo.idproducto == idBuscar:

                    print("Precio a modificar: ", articulo)
                    nuevoPrecio = validarNumero("Ingrese nuevo precio: ")
                    nuevaGanancia = validarNumero("Ingrese un nuevo porcentaje de ganancia en número: ")
                    articulo.actualizarPrecio(nuevoPrecio, nuevaGanancia)
                    print("Precio modificado: ", articulo)



    else:
        print("\nProceso finalizado....")
        break


