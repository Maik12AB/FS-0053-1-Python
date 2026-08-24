# Leer con input()
# r = radio
# g = gravedad
# 
# Mensajes
# "Ingrese el radio en Kilómetros:"
# "Ingrese la constante g:"
# "La velocidad de Escape es 11174.6 [m/s]"
# -- -
# Test
# g = 9.8 [m/s2]
# r = 6371 [Km]
# Se obtiene como resultado: Velocidad de Escape = 11174.6 [m/s]

# `math` librería de la biblioteca estándar de Python
# Para realizar calculos matemáticos
import math

g = input( "Ingrese la constante g [m/s2]: " )
r = input( "Ingrese el radio en Kilómetros [Km]: " )

# Convertir tipo de datos
g = g.replace( ",", "." )

try:
    g = float(g)

except ValueError:
    print( "Debe ingresar un valor valido para la Gravedad")

try:
    r = int(r)

except ValueError:
    print( "Debe ingresar un valor valido para los kilómetros")

# Convertir km a metros
r = r * 1000

# sqrt = Raíz cuadrada
Ve = round(math.sqrt(2 * g * r), 1) # type: ignore

print( f"Velocidad de Escape = {Ve} [m/s]" )
