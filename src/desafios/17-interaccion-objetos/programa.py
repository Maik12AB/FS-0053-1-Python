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


# if tienda_nueva == 1:
#     nombre = input("Ingrese el nombre de la tienda: ")
#     delivery = input("Ingrese el costo del delivery: ")
#     restaurante = Restaurante(nombre, delivery)
#     print("Ingrese un producto")
#     restaurante.ingresar_producto()

#     opcion = menu_principal()
#     while True:
#         if opcion == 1:
#             restaurante.ingresar_producto()
#             opcion = menu_principal()
#         elif opcion == 2:
#             break

#     opcion = menu_ventas()
#     while True:
#         if opcion == 1:
#             print(restaurante.listar_productos())
#             opcion = menu_ventas()
#         elif opcion == 2:
#             restaurante.realizar_venta()
#             opcion = menu_ventas()
#         elif opcion == 3:
#             break    
# elif tienda_nueva == 2:
#     nombre = input("Ingrese el nombre de la tienda: ")
#     delivery = input("Ingrese el costo del delivery: ")
#     supermercado = Supermercado(nombre, delivery)
#     print("Ingrese un producto")
#     supermercado.ingresar_producto()


#     opcion = menu_principal()
#     while True:
#         if opcion == 1:
#             supermercado.ingresar_producto()

#             opcion = menu_principal()
#         elif opcion == 2:
#             break
#     opcion = menu_ventas()
#     while True:
#         if opcion == 1:
#             print(supermercado.listar_productos())
#             opcion = menu_ventas()
#         elif opcion == 2:
#             supermercado.realizar_venta()
#             opcion = menu_ventas()
#         elif opcion == 3:
#             break    
# elif tienda_nueva == 3:
#     nombre = input("Ingrese el nombre de la tienda: ")
#     delivery = input("Ingrese el costo del delivery: ")
#     farmacia = Farmacia(nombre, delivery)
#     print("Ingrese un producto")
#     farmacia.ingresar_producto()

#     opcion = menu_principal()
#     while True:
#         if opcion == 1:
#             farmacia.ingresar_producto()
#             opcion = menu_principal()
#         elif opcion == 2:
#             break

#     opcion = menu_ventas()
#     while True:
#         if opcion == 1:
#             print(farmacia.listar_productos())
#             opcion = menu_ventas()
#         elif opcion == 2:
#             farmacia.realizar_venta()
#             opcion = menu_ventas()
#         elif opcion == 3:
#             break   

def menu_inicial():
    print("Su tienda es un/a: ")
    print("1. Restaurante")
    print("2. Supermercado")
    print("3. Farmacia")
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


if __name__ == "__main__":
    main()


