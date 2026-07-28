from tienda import Restaurante, Supermercado,  Farmacia

def menu_inicial():
    print("Su tienda es un/a: ")
    print("1. Restaurante")
    print("2. Supermercado")
    print("3. Farmacia")
    print("9. Salir")
    return input(".> ")

def menu_ventas():
    print("¿Que desa hacer?")
    print("1. Listar productos")
    print("2. Vender productos")
    print("9. Salir")
    return input(".> ")

def main():

    # Definir el tipo de tienda
    while True:
        tipo_tienda = menu_inicial()

        # validamos que la opción sea correcta
        if tipo_tienda not in ['1', '2', '3', '9']:
            print("Tipo de tienda no configurada")
            print("Debe seleccionar una opción valida")
            continue

        break

    if tipo_tienda == '9':
        print("Hasta la próxima")
        return None

    # -- --------------------------------------------------------------
    # Solicitamos nombre de la tienda y el costo del delivery
    # TODO: Validar con try
    nombre = input("Ingrese el nombre de la tienda: ")
    delivery = int(input("Ingrese el costo del delivery: "))

    # Validar el tipo de tienda
    if tipo_tienda == '1':
        tienda = Restaurante(nombre, delivery)
    elif tipo_tienda == '2':
        tienda = Supermercado(nombre, delivery)
    # ¿Pregunta de diseño?
    # Debo validar que tipo_tienda es 3 o simplemente uso un else
    else:
        tienda = Farmacia(nombre, delivery)

    # Ingresar productos
    print("Ingresar productos")
    print("------------------")
    i = 0
    while True:
        stock = 0
        i += 1
        print( f"Ingresar producto {i}")
        nombre = input("Ingrese el nombre: ")
        precio = int(input("Ingrese el precio: "))
        if tipo_tienda not in ('1'):
            stock = int(input("Ingrese el stock: "))

        tienda.ingresar_producto(nombre, precio, stock)

        s = input("¿Desea agregar más productos? [s/n]")
        if s.lower() == "n":
            break

    # Menú operaciones
    while True:
        print()
        print( tienda.nombre )
        print( '-' * len(tienda.nombre), "\n" )

        opcion = menu_ventas()

        if opcion == '1':
            print( tienda.listar_productos() )
        elif opcion == '2':
            # Vender
            # r = super.realizar_venta("Prod 1", 1)
            ...
        elif opcion == '9':
            break



if __name__ == "__main__":
    main()


