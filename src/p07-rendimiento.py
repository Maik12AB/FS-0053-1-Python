print()
print("Rendimiento de un estudiante")
print("---------------------------- \n")

# Regla de negocio
# - Las notas y promedios se trabajan en rango de 10 a 70
# - Las notas y promedio deben ser de tipo int
#
# Promedio   Clasificación
# --------   -------------
# 60 a 70    Excelente
# 50 a 59    Bueno
# 40 a 49    Suficiente
# < 40       Insuficiente
# ---        Error en nota
#

nota = input("Ingrese el promedio del estudiante (10 a 70): ")

# Aunque se especifica que el valor se ingresa como entero
# el usuario por costumbre puede ingresar valores
# decimales
# Caso de uso:
# Usuario   Necesito
#  5.5        55
#  5,5        55
nota = nota.replace( ",", "" )
nota = nota.replace( ".", "" )

if nota.isdigit():
    nota = int(nota)

    if nota >= 60 and nota <= 70:
        print("El estudiante tiene un rendimiento EXCELENTE")
    elif nota >= 50 and nota <= 59:
        print("El estudiante tiene un rendimiento BUENO")
    elif nota >= 40 and nota <= 49:
        print("El estudiante tiene un rendimiento SUFICIENTE")
    elif nota >= 10 and nota <= 39:
        print("El estudiante tiene un rendimiento INSUFICIENTE")
    else:
        print( "Debe ingresar un promedio valid 10 - 70")
else:
    print( "Debe ingresar un promedio valid 10 - 70")

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
