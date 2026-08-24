print()
print("Saber si un estudiante aprueba el curso")
print("--------------------------------------- \n")

# Regla de negocio
# Nota minima debe ser 4.0
# La nota a comparar debe ser decimal (float)
NOTA_MINIMA = 4.0

nota = input("Ingrese la nota del estudiante: ")

# Sabemos que input() regresa un texto con el valor ingresado por
# el usuario. Debemos hacer la conversión al tipo `float` como
# lo establecen las reglas de negocio.

# Primera validación: El punto marca la posición decimal
# Caso de uso:
#  Usuario     Necesito
#    5.5         5.5
#    5,5         5.5
# Utilizamos replace() reemplaza la coma `,` por `.`
nota = nota.replace( ",", "." )

try:
    nota = float(nota)

    if nota >= 1.0 and nota <= 7.0: # type: ignore
        if nota >= NOTA_MINIMA: # type: ignore
            print( "El estudiante Aprueba" )
        else:
            print( "El estudiante Reprueba" )
    else:
        print( "Debe ingresar una nota valida 1.0 - 7.0")

except ValueError:
    print( "Debe ingresar una nota valida 1.0 - 7.0")

# Casos de uso:
# Entrada        Resultado
#   5.5          Aprueba
#   4.0          Aprueba
#   7.0          Aprueba
#   5,5          Aprueba
#   4,0          Aprueba
#   7,0          Aprueba
#   8.0          Error en rango
#   ...          Error en rango
