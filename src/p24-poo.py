from p24_poo_clase_medicamento import Medicamento

def main():
    medicamento_nuevo = Medicamento()
    print( f"Precio inicial {medicamento_nuevo.precio}" )

    precio = int( input("Ingrese precio del medicamento: ") )

    medicamento_nuevo.asignar_precio(precio)

    print( f"Precio nuevo {medicamento_nuevo.precio} y descuento {medicamento_nuevo.descuento}" )


if __name__ == '__main__':
    main()
