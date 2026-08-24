
def menu_masa():
    print("Tipo De Masa")
    print("1. Masa tradicional")
    print("2. Masa delgada")
    print("3. Masa con bordes de queso")
    print("---------")
    op1 = 0
    while op1 not in range(1,4):
        tipo = ''
        try:
            op1 = int(input("Ingrese opcion: "))
            if op1 == 1:
                tipo = "Masa tradicional"
            elif op1 == 2:
                tipo = "Masa delgada"
            elif op1 == 3:
                tipo = "Masa con bordes de queso"
            else:
                print("Opcion invalida")
                print("---------")
        except ValueError:
            print("Ingrese solo numeros")

    return tipo
