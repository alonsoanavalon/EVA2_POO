from EVA2.producto import Producto
from EVA2.boleta import Boleta


#Antes de agregarlo deberíamos hacer las comprobaciones correspondientes
#boletita = Boleta(1, productito, 2, productito.precio)
#print(boletita.mostrarBoleta())

listaProductos = []

martillo = Producto(1, "Martillo", 3000, 50)
listaProductos.append(martillo)
taladro = Producto(2, "taladro", 30000, 50)
listaProductos.append(taladro)
cemento = Producto(3, "cemento", 10000, 50)
listaProductos.append(cemento)
clavos = Producto(4, "clavos", 3000, 50)
listaProductos.append(clavos)
tornillos = Producto(5, "tornillos", 2500, 50)
listaProductos.append(tornillos)
tuboPvc = Producto(6, "tuboPvc", 4000, 50)
listaProductos.append(tuboPvc)
pintura = Producto(7, "pintura", 6000, 50)
listaProductos.append(pintura)
pastaMuro = Producto(8, "pastaMuro", 10000, 50)
listaProductos.append(pastaMuro)
desatornillador = Producto(9, "desatornillador", 4000, 50)
listaProductos.append(desatornillador)
diablo = Producto(10, "Diablo", 8000, 50)
listaProductos.append(diablo)

boletita2 = Boleta(1, pintura, 3)
print(boletita2.mostrarBoleta())


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
        nombre = input("Ingrese nombre del producto: ")
        precio = int(input("Ingrese precio: "))
        stock = int(input("Ingrese stock: "))
        nuevoProducto = Producto(nuevoProductoId, nombre, precio, stock)
        print("\nNuevo producto agregado: ", nuevoProducto)
        listaProductos.append(nuevoProducto)
    elif opcion==2:
        print("Actualizando precio")
        print("1. Buscar por ID")
        print("2. Buscar por Nombre")
        buscar = int(input("Ingrese opción (1-2): "))
        if buscar==1:
            idBuscar = int(input("Ingrese ID: "))
            for producto in listaProductos:
                print(producto)
    elif opcion==3:
        print("Generando boleta")

    else:
        print("\nProceso finalizado....")
        break

