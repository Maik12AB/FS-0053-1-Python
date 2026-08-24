from ingredientes import PROTEINAS, VEGETALES, MASA

class Pizza():
    precio = 10_000
    tamano = "Familiar"
    proteina = ""
    vegetal = []
    masa = "Tradicional"
    pizza_valida = False

    def __init__(self):
        self.hola = "Hola"

    def set_pedido(self):
        print("Ingrese el ingrediente proteico. Opciones: ")
        print(PROTEINAS)
        proteina = input("> ")

        print("Ingrese el primer ingrediente vegetal. Opciones: ")
        print(VEGETALES)
        vegetal1 = input("> ")

        print("Ingrese el segundo ingrediente vegetal. Opciones: ")
        print(VEGETALES)
        vegetal2 = input("> ")

        print("Ingrese el tipo de masa. Opciones: ")
        print(MASA)
        masa = input("> ")

        # Asignar los atributos según el orden del punto 4
        self.proteina = proteina
        self.vegetal.append(vegetal1)
        self.vegetal.append(vegetal2)
        self.masa = masa

        # Validar si los ingredientes estan correctos según el orden del punto 4
        self.pizza_valida = self.validar_opcion(proteina, PROTEINAS) \
            and self.validar_opcion(vegetal1, VEGETALES) \
            and self.validar_opcion(vegetal2, VEGETALES) \
            and self.validar_opcion(masa, MASA)

    @classmethod
    def validar_opcion(cls, valor: str, opciones: list) -> bool:
        return (valor in opciones)
