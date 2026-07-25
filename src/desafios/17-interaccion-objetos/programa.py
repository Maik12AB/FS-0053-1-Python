from tienda import Restaurante, Supermercado,  Farmacia 

def menu_principal():
    print("¿Que desa hacer?")
    print("1.Ingresar producto")
    print("2.Continuar")
    return int(input(".> "))

def menu_ventas():
    print("Listar y Vender")
    print("¿Que desa hacer?")
    print("1.Listar productos")
    print("2.Vender productos")
    print("3.Salir")
    return int(input(".> "))

print("Su tienda es un/a: ")
print("1.Restaurante")
print("2.Supermercado")
print("3.Farmacia")
tienda_nueva = int(input(".> "))
if tienda_nueva == 1:
    nombre = input("Ingrese el nombre de la tienda: ")
    delivery = input("Ingrese el costo del delivery: ")
    restaurante = Restaurante(nombre, delivery)
    print("Ingrese un producto")
    restaurante.ingresar_producto()

    opcion = menu_principal()
    while True:
        if opcion == 1:
            restaurante.ingresar_producto()
            opcion = menu_principal()
        elif opcion == 2:
            break

    opcion = menu_ventas()
    while True:
        if opcion == 1:
            print(restaurante.listar_productos())
            opcion = menu_ventas()
        elif opcion == 2:
            restaurante.realizar_venta()
            opcion = menu_ventas()
        elif opcion == 3:
            break    
elif tienda_nueva == 2:
    nombre = input("Ingrese el nombre de la tienda: ")
    delivery = input("Ingrese el costo del delivery: ")
    supermercado = Supermercado(nombre, delivery)
    print("Ingrese un producto")
    supermercado.ingresar_producto()


    opcion = menu_principal()
    while True:
        if opcion == 1:
            supermercado.ingresar_producto()

            opcion = menu_principal()
        elif opcion == 2:
            break
    opcion = menu_ventas()
    while True:
        if opcion == 1:
            print(supermercado.listar_productos())
            opcion = menu_ventas()
        elif opcion == 2:
            supermercado.realizar_venta()
            opcion = menu_ventas()
        elif opcion == 3:
            break    
elif tienda_nueva == 3:
    nombre = input("Ingrese el nombre de la tienda: ")
    delivery = input("Ingrese el costo del delivery: ")
    farmacia = Farmacia(nombre, delivery)
    print("Ingrese un producto")
    farmacia.ingresar_producto()

    opcion = menu_principal()
    while True:
        if opcion == 1:
            farmacia.ingresar_producto()
            opcion = menu_principal()
        elif opcion == 2:
            break

    opcion = menu_ventas()
    while True:
        if opcion == 1:
            print(farmacia.listar_productos())
            opcion = menu_ventas()
        elif opcion == 2:
            farmacia.realizar_venta()
            opcion = menu_ventas()
        elif opcion == 3:
            break   


