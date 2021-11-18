from EVA2.producto import Producto
from EVA2.boleta import Boleta


#Antes de agregarlo deberíamos hacer las comprobaciones correspondientes

def validarNumero (pregunta):
    while True:
        try:
            numero = int(input(pregunta))
        except ValueError:
            print("Debes escribir un número.")
            continue

        if numero < 0:
            print("Debes escribir un número positivo.")
            continue
        else:
            break
    return numero

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

for producto in listaProductos:
    print(producto.mostrarProducto())


while True:
    print("\nMenú de Opciones")
    print("1. Agregar producto (nuevo)")
    print("2. Actualizar precio producto")
    print("3. Generar boleta de venta")
    print("4. Salir/Finalizar")
    opcion = int(input("Ingrese una opción (1-4): "))

    if opcion==1:
        print("\nAgregando producto...")
        nuevoProductoId = len(listaProductos)+1
        print("\nID nuevo producto: ", nuevoProductoId)
        nombre = input("\nIngrese nombre del producto: ")
        nombre = nombre.lower()
        precio = int(input("Ingrese precio: "))
        stock = int(input("Ingrese stock: "))
        nuevoProducto = Producto(nuevoProductoId, nombre, precio, stock)
        print("\nNuevo producto agregado: ", nuevoProducto)
        listaProductos.append(nuevoProducto)

    elif opcion==2:
        print("\nActualizando precio...")
        print("1. Buscar por ID")
        print("2. Buscar por Nombre")
        buscar = int(input("Ingrese opción (1-2): "))

        if buscar == 1:
            idBuscar = validarNumero("Ingrese ID:")
            for articulo in listaProductos:
                if articulo.id == idBuscar:
                    print("Precio a modificar: ", articulo)
                    nuevoPrecio = int(input("Ingrese nuevo precio: "))
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
                    nuevoPrecio = int(input("Ingrese nuevo precio: "))
                    articulo.actualizarPrecio(nuevoPrecio)
                    print("Precio modificado: ", articulo)

    elif opcion==3:

        print("\nGenerando boleta...")
        print("1. Seleccionar producto por ID")
        print("2. Seleccionar producto por Nombre")
        buscar = int(input("Ingrese opción (1-2): "))
        numBoleta = len(listaBoleta) + 1

        if buscar == 1:
            idBuscar = validarNumero("Ingrese ID:")
            for articulo in listaProductos:
                if articulo.id == idBuscar:
                    print("Producto seleccionado", articulo)
                    cantidad = validarNumero("Ingrese cantidad: ")
                    articulo.restarStock(cantidad)
                    boletaGenerada = Boleta(numBoleta, articulo, cantidad)
                    print(boletaGenerada.mostrarBoleta())

        if buscar == 2:
            nombreBuscar = input("Ingrese nombre: ")
            nombreBuscar = nombreBuscar.lower()
            for articulo in listaProductos:
                if articulo.nombre == nombreBuscar:
                    print("Producto seleccionado", articulo)
                    cantidad = validarNumero("Ingrese cantidad: ")
                    articulo.restarStock(cantidad)
                    boletaGenerada = Boleta(numBoleta, articulo, cantidad)
                    print(boletaGenerada.mostrarBoleta())

    else:
        print("\nProceso finalizado....")
        break


