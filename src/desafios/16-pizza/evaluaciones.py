from pizza import Pizza

def main():
    print("Pizza evaluación")
    print("----------------", "\n")

    print("Evaluación punto 5\n")
    print("Parte A")
    print("-------")
    print( f"Precio: {Pizza.precio:,}")
    print( f"Tamaño: {Pizza.tamano}")
    print( f"Ingrediente proteico: {Pizza.proteina}")
    print( f"Ingredientes vegetales: {Pizza.vegetal}")
    print( f"Tipo de masa: {Pizza.masa}")
    print( f"Pizza valida: {Pizza.pizza_valida}")

    print()
    print("Parte B")
    print("-------")
    if Pizza.validar_opcion("salsa de tomate", ["salsa de tomate", "salsa bbq"] ):
        print("La opción [salsa de tomate] se encuentra en la lista")
    else:
        print("La opción [salsa de tomate] NO se encuentra en la lista")

    print()
    print("Parte C")
    print("-------")
    mi_pizza = Pizza()
    mi_pizza.set_pedido()

    print()
    print("Parte D")
    print("-------")
    print( f"Precio: {mi_pizza.precio:,}")
    print( f"Tamaño: {mi_pizza.tamano}")
    print( f"Ingrediente proteico: {mi_pizza.proteina}")
    print( f"Ingredientes vegetales: {mi_pizza.vegetal}")
    print( f"Tipo de masa: {mi_pizza.masa}")

    print()
    print("Parte D")
    print("-------")
    if mi_pizza.pizza_valida:
        print( "[SUCCESS] La pizza solicitada es correcta")
    else:
        print( "[ERROR] Los ingredientes solicitados no son correctos")


if __name__ == '__main__':
    main()
