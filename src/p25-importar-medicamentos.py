import csv
from p24_poo_clase_medicamento import Medicamento

def main():
    # Imprimir encabezado
    print("------------------------------------")
    print("Importando medicamentos desde el csv")
    print("------------------------------------", "\n")

    # Importar archivo csv
    items = []
    with open("src/data/medicamentos.csv", "r") as f:
        contenido = csv.reader(f)
        # Procesar archivo csv
        for item in contenido:
            items.append(item)

    # Imprimir cada medicamento con las reglas de la clase Medicamento
    C1 = 15
    C2 = 7
    C3 = 10
    C4 = 10
    C5 = 10
    C6 = 10
    for i, v in enumerate(items):
        if i == 0:
            t = f"{v[0]:<{C1}} {v[1]:>{C2}} {v[2]:>{C3}} {'Descuento':>{C4}} {'Neto':>{C5}} {'Bruto':>{C6}} "
            print( t )
            print( '-' * len(t) )
        else:
            stock = v[1]
            if stock == 'null':
                stock = 0
            else:
                stock = int(stock)

            precio = int(v[2])

            o = Medicamento(v[0], stock)
            o.asignar_precio(precio)
            print( f"{o.nombre:<{C1}} {o.stock:>{C2}} {o.precio:>{C3},} {o.descuento*100:>{C4}.0f}% {o.precio_neto:>{C5},} {o.precio_bruto:>{C6},}")


if __name__ == '__main__':
    main()
