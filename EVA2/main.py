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
        print("Agregando producto")
    elif opcion==2:
        print("Actualizando precio")
    elif opcion==3:
        print("Generando boleta")

    else:
        print("\nProceso finalizado....")
        break

