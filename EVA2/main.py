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

    txt += "El total de la compra es = ${}".format(total)
    return txt

listaProductos = []

martillo = Producto(1, "martillo", 3000, 50)
listaProductos.append(martillo)
taladro = Producto(2, "taladro", 30000, 50)
listaProductos.append(taladro)
cemento = Producto(3, "cemento", 10000, 50)
listaProductos.append(cemento)
clavos = Producto(4, "clavos", 3000, 50)
listaProductos.append(clavos)
tornillos = Producto(5, "tornillos", 2500, 50)
listaProductos.append(tornillos)
tuboPvc = Producto(6, "tubo pvc", 4000, 50)
listaProductos.append(tuboPvc)
pintura = Producto(7, "pintura", 6000, 50)
listaProductos.append(pintura)
pastaMuro = Producto(8, "pasta muro", 10000, 50)
listaProductos.append(pastaMuro)
desatornillador = Producto(9, "desatornillador", 4000, 50)
listaProductos.append(desatornillador)
diablo = Producto(10, "diablo", 8000, 50)
listaProductos.append(diablo)

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
    print("4. Registro de boleta emitida")
    print("5. Mostrar listado de productos")
    print("6. Salir/Finalizar")
    opcion = validarNumero("Ingrese una opción (1-6): ")

    while opcion < 1 or opcion > 6:
        opcion = validarNumero("Ingrese una opción (1-6): ")


    if opcion==1:
        print("\nAgregando producto...")
        nuevoProductoId = len(listaProductos)+1
        print("\nID nuevo producto: ", nuevoProductoId)
        nombre = input("\nIngrese nombre del producto: ")
        nombre = nombre.lower()
        precio = int(input("Ingrese precio: "))
        while precio < 1:
            precio = int(input("Ingrese precio: "))
        stock = int(input("Ingrese stock: "))
        while stock < 1:
            stock = int(input("Ingrese stock: "))
        nuevoProducto = Producto(nuevoProductoId, nombre, precio, stock)
        print("\nNuevo producto agregado: ", nuevoProducto)
        listaProductos.append(nuevoProducto)

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
                if articulo.id == idBuscar:

                    print("Precio a modificar: ", articulo)
                    nuevoPrecio = validarNumero("Ingrese nuevo precio: ")
                    articulo.actualizarPrecio(nuevoPrecio)
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
                    if articulo.id == idBuscar:
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
                            while res != "si" or res != "no":
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
                            while res != "si" or res != "no":
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




# FALTA: -PREGUNTAR AL USUARIO POR CIERRE DE LA VENTA (AGREGAR + PRODUCTOS O FINALIZAR)
    #    -GENERAR BOLETA DE VENTA (TRAER DATOS DE ESTA)
    #    -3.C. - 4.B. - 4.C.

    else:
        print("\nProceso finalizado....")
        break