# Random
# Es una librería de Python (Biblioteca estándar)
# que permite generar números aleatorios

import random

print( "Tres formas base de utilizar random" )
print( "----------------------------------- \n" )

# Número aleatorio
# Número unico en un rango 0 a 1 y es tipo float
print( f"1. Número aleatorio (float) {random.random()}" )

# Número enter
print( f"2. Número aleatorio (int) {random.randint(1, 10)}" )

# Selección aleatorio de un valor
# en una lista
lista = ( "rojo", "verde", "azul", "blanco" )
print( f"3. Aleatorio de una lista (str) {random.choice(lista)}" )

# Semillas
print( f"Sin semilla {random.randint(1, 10)}" )
random.seed(42)
print( f"Con semilla (42) {random.randint(1, 10)}" )
random.seed(21)
print( f"Con semilla (21) {random.randint(1, 10)}" )

