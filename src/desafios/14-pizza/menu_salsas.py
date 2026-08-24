def menu_salsa():
    salsas = {
        "1": "Salsa de tomate",
        "2": "Salsa alfredo",
        "3": "Salsa barbecue",
        "4": "Salsa pesto",
    }

    print("Tipo De Salsa")
    for c, v in salsas.items():
        print( f"{c}. {v}")

    op2 = ""
    while op2 != '0':
        op2 = input("Ingrese opcion: ")
        salsa = salsas.get(op2, None)

        if salsa:
            break
        elif op2 == '0':
            break
        else:
            print("Opcion invalida debe seleccionar una opción del menú")
            print("---------")

    return salsa
