from menu_masa import menu_masa
from menu_salsas import menu_salsa
from menu_ingredientes import menu_ingredientes, menu_eliminar_ingredientes
from utils import tiempo
from cierre import pizza

TITULO = "Pizza JAT"
COLUMNAS = 30

def menu_opciones(tipo_masa, tipo_salsa, tipo_ingre):

    if tipo_masa != '' or tipo_salsa != '' :
        print("Ingredientes seleccionados")
        print(f"Tipo de masa: {tipo_masa}" )
        print(f"Tipo de salsa: {tipo_salsa}" )
        print(f"Ingredientes: {tipo_ingre}" )
        print(f"Tiempo estimado : {tiempo(tipo_ingre)} min" )
        print()

    print("Seleccione una opción")
    print("1. Tipo de masa")
    print("2. Tipo de salsa")
    print("3. Agregar ingredientes")
    print("4. Eliminar ingredientes")
    print("5. Cerrar pedido")
    print("0. Salir")

    opcion = input("> ")

    return opcion

def inicializar():
    return '', '', set()

def menu_principal():

    opcion = ''
    tipo_masa, tipo_salsa, tipo_ingre = inicializar()
    while opcion != '0':
        print( f"{'Bienvenidos/as':^{COLUMNAS}}" )
        print(f"{TITULO:^{COLUMNAS}}")
        print("=" * COLUMNAS, "\n")

        opcion = menu_opciones(tipo_masa, tipo_salsa, tipo_ingre)

        if opcion == '1':
            tipo_masa = menu_masa()
        elif opcion == '2':
            tipo_salsa = menu_salsa()
        elif opcion == '3':
            tipo_ingre = menu_ingredientes(tipo_ingre)
        elif opcion == '4':
            tipo_ingre = menu_eliminar_ingredientes(tipo_ingre)
        elif opcion == '5':
            op = pizza(TITULO, tipo_masa, tipo_salsa, tipo_ingre)

            # Se imprime la comanda
            # Se limpian las variables
            if op.lower() == "s":
                tipo_masa, tipo_salsa, tipo_ingre = inicializar()

def main():
    menu_principal()

if __name__ == '__main__':
    main()
