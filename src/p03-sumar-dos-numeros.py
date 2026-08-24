# v1.0.0
# input() devuelve un str por lo tanto no podemos
# usar el valor para suma
"""
numero1 = input("Ingrese el primer número entero:")
numero2 = input("Ingrese el segundo número entero:")

suma = numero1 + numero2

print( f"La suma de los números es: {suma}")
"""

# v1.0.1
# Convertir el valor de input() a int()
# Pasamos el valor de input() como argumento de la función int()
"""
numero1 = int( input("Ingrese el primer número entero:") )
numero2 = int( input("Ingrese el segundo número entero:") )

suma = numero1 + numero2

print( f"La suma de los números es: {suma}")
"""

# v1.0.2
# Fix - El usuario ingresa un valor no numérico
# Caso de uso: Debemos validar que los valores ingresados
# son números enteros antes de realizar la suma
# Reproducción:
#    numero1 = 10
#    numero2 = .
numero1 = input("Ingrese el primer número entero:")
numero2 = input("Ingrese el segundo número entero:")

if numero1.isdigit() and numero2.isdigit():
    numero_1 = int( numero1 )
    numero_2 = int( numero2 )

    suma = numero_1 + numero_2

    print( f"La suma de los números es: {suma}")
else:
    print( "Error!!!!" )
    print( "Los valores ingresados deben ser números enteros" )
    print( f"Primer número es: {numero1} y segundo número es: {numero2}" )
