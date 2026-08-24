# esta sintaxis de: int | float
# indica que puede recibir uno
# de estos tipos de datos
from curses.ascii import isdigit


def sumar(x: int | float | str, y: int | float | str):
    """
    fx que suma dos números
    """
    # hago validación de tipo de datos
    if isinstance(x, str):
        x = int(x)
    if isinstance(y, str):
        y = int(y)

    # Al sacar el print() de la función y retornar
    # el resultado de la suma, ahora la función
    # cumple con responsabilidad unica
    return x + y # type: ignore
