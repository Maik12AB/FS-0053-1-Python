import sys

precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

def filtrar_productos(umbral: int, modo: str = "mayor") -> list[str]:
    """
    Filtra los productos según el umbral.
    Por defecto muestra los mayores, pero se puede indicar menor.
    """
    resultado = []

    for producto, valor in precios.items():
        if modo == "mayor" and valor > umbral:
            resultado.append(producto)
        elif modo == "menor" and valor < umbral:
            resultado.append(producto)

    return resultado


if len(sys.argv) < 2:
    print("Ingrese el umbral a superar")
    sys.exit()

try:
    umbral = int(sys.argv[1])
    if len(sys.argv) > 2:
        modo = sys.argv[2].lower()
    else:
        modo = "mayor"

    if modo not in ("mayor", "menor"):
        print("Lo sentimos, no es una operación válida")
        sys.exit()

    filtrados = filtrar_productos(umbral, modo)

    if modo == "mayor":
        print("Los productos mayores al umbral son:", ", ".join(filtrados))
    else:
        print("Los productos menores al umbral son:", ", ".join(filtrados))

except ValueError:
    print("Ingresa un número entero")
