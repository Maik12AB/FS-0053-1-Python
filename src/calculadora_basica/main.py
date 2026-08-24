#      nombre_modulo
import     sumar

# Util cuando modulo/libreria es muy grande
# para que ocupe menos memoria
#     modulo            Funcion
from  restar    import   restar

def tomar_datos():
    x = int(input("Ingrese el primer número: "))
    y = int(input("Ingrese el segundo número: "))
    return x, y

opcion = ""
while opcion != "0":
    print("Calculadora básica")
    print("------------------\n")
    print("¿Qué operación le gustaria realizar?")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("0. Salir")

    opcion = input("> ")

    if opcion == "0":
        print("Nos vemos a la próxima")
        break
    elif opcion not in ("1", "2"):
        print("No existe la opción solicitada")
        continue

    # Esto esta fuera del if
    x, y = tomar_datos()

    if opcion == "1":
        resp = sumar.sumar(x, y)
        print( f"El resultado de la suma es: {resp}")

    elif opcion == "2":
        resp = restar(x, y)
        print( f"El resultado de la resta es: {resp}")
