# sys
# Es una librería de Python (Biblioteca estándar)
# permite interactuar con el sistema operativo
# y acceder a argumentos de la línea de comandos

import sys

# Los argumentos enviados desde consola se
# guardan en una lista (list) y el tamaño
# de la lista indica el número de
# argumentos.
# Los argumentos incluyen el nombre del archivo
# con su ubicación. La ubicación se considera
# a partir de la carpeta donde ejecutamos
# el comando `python`

print()
print( "Argumentos enviados desde la consola" )
print( "------------------------------------ \n" )
print( "Tipo de dato", type(sys.argv) )
print( f"Tamaño de la lista o número de argumentos: {len( sys.argv )} ")
print( sys.argv, "\n" )

print( f"Nombre del archivo: {sys.argv[0]} " )

if len( sys.argv ) >= 2:
    print( f"Primer argumento: {sys.argv[1]}")

if len( sys.argv ) >= 3:
    print( f"Segundo argumento: {sys.argv[2]}")

# Introducción al for en Python
for i in sys.argv:
    print( i )
