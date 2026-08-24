from te import Te

SABORES = {
    '1': "Té negro",
    '2': "Té verde",
    '3': "Agua de hierbas"
}
FORMATOS = {
    '1': '300gr',
    '2': '500gr'
}
TG = 40

def menu_pedido(opciones: dict) -> None:
    for c, v in opciones.items():
        print( f"   {c}. {v}")

def main():
    print("Bienvenidos al Té y hojas artesansal ACME")
    print("-----------------------------------------", "\n")

    print("Ingrese el sabor del té")
    menu_pedido(SABORES)
    sabor = input('> ')

    print("Ingrese el formato deseado")
    menu_pedido(FORMATOS)
    formato = input('> ')

    # Instanciamos la clase
    # Obtenemos los valores
    insta = Te()
    tiempo, reco = insta.obtener_tiempo_y_recomendacion( int(sabor) )
    precio = insta.obtener_precio( int(formato) )

    print('-' * TG)
    print('Su pedido es')
    print('-' * TG)
    print( f"Sabor del tipo de té {SABORES.get(sabor, "NA")}")
    print( f"Formato {FORMATOS.get(formato, "NA")}")
    print( f"Precio {precio}")
    print( f"Tiempo {tiempo} minutos")
    print( f"Recomendación {reco}")
    print('-' * TG)
    print('MUCHAS GRACIAS POR SU COMPRA')
    print('-' * TG)


if __name__ == '__main__':
    main()