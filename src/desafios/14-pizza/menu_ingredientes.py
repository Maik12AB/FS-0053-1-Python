def menu_ingredientes(tipo_ingre: set):
    lista_ingre = {
        '1': 'Tomate',
        '2': 'Champiñones',
        '3': 'Aceitunas',
        '4': 'Cebolla',
        '5': 'Pollo',
        '6': 'Jamón',
        '7': 'Carne',
        '8': 'Tocino',
        '9': 'Queso'
    }

    op3 = ''
    while op3 != '0':
        print("Tipo de ingredientes")
        for c, v in lista_ingre.items():
            print( f"{c}. {v}")
        print( "0. Salir")

        op3 = input("Ingrese opcion: ")
        ing = lista_ingre.get(op3, None)

        if ing:
            tipo_ingre.add(ing)
            continue
        elif op3 == '0':
            break
        else:
            print("Opcion invalida debe seleccionar una opción del menú")
            print("---------")

    return tipo_ingre

def menu_eliminar_ingredientes(tipo_ingre: set):
    op = ''
    lista = list(tipo_ingre)
    while op != '0':
        print("Seleccione el ingrediente a eliminar")
        for i, v in enumerate(lista):
            print( f"{i+1}. {v}")
        print( "0. Salir")

        op = input("Ingrese opcion: ")

        if op == '0':
            break

        try:
            # UX para facilitar la selección no utilizamos
            # el cero para eliminar el elemento.
            # Mantenemos el cero para salir del menú
            opcion = int(op) - 1
            ing = lista.pop(opcion)
        except ValueError:
            print("Opción invalida debe seleccionar una opción del menú")
            print("---------")

    return set(lista)
