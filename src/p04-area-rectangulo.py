# v0.0.0
# Historia de usuario:
"""
El usuario necesita el cálculo del área de un rectángulo.
A partir de ingresar la base y la altura
"""

# Mejorar la ux
print()
print( "Calcular el área de un rectángulo" )
print( "--------------------------------- \n" )

base = input( "Ingrese la base del rectángulo: ")
altura = input( "Ingrese la altura del rectángulo: ")

# Manejo de errores
# Manejar errores con esta estructura
# tiene un costo
try:
    area = int( base ) * int( altura )
    print( f"\nEl área del rectángulo es: {area}" )
except ValueError:
    print( "ERROR" )
    print( "Los valores ingresados deben ser número enteros" )
    print( f"Valores ingresados Base: {base} - Altura: {altura}" )
