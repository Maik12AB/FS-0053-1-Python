# dunder methods
lista = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print( lista.__dir__() )

# # Tamaño del objeto
# print( len(lista) )
# print( lista.__len__() )

# Mustra una pequeña ayuda del método
# help( lista.pop )

print( "Método append()" )
print( "---------------" )

# Inicialización de variable
colores = []

# Agregamos valores a la lista.
# Normalmente esto queda
# dentro de un for
colores.append('rojo')
colores.append('rosa')
colores.append('azul')

print( colores )

print()
print( "Método insert()" )
print( "---------------" )

lista_puntos = [ ".", ".", ".", ".", "." ]
print( lista_puntos )

#   0    1    2    3    4      índice
# ['.', '.', '.', '.', '.']

lista_puntos.insert(2, "-")
print( lista_puntos )

#   0    1    2    3    4    5    índice
# ['.', '.', '-', '.', '.', '.']

lista_puntos.insert(-1, "*")
print( lista_puntos )

print()
print( "Método pop()" )
print( "------------" )

# Elimina un elemento de una lista
# retorna el valor del elemento eliminado

print( colores )

color_eliminado = colores.pop(2)

print( 'Lista', colores)
print( f"Color eliminado: {color_eliminado}" )

print()
print( "Método remove()" )
print( "---------------" )

# Recibe el valor a eliminar
# Elimina la primera ocurrencia
# retorna None
# Si el valor no existe devuelve error

numeros = [ 100, 400, 50, 200, 50, 300 ]

numeros.remove(50)

print( 'Lista', numeros)

print()
print( "Método reverse() y sort()" )
print( "-------------------------" )
# [WARNING] Modifican la lista

# Invierte el orden actual
numeros.reverse()
print( "Lista con orden cambiado", numeros )

# Ordena una lista de ascendente
numeros.sort()
print( "Lista ordenada [asc]", numeros )

# Ordena una lista descendente
numeros.sort( reverse = True )
print( "Lista ordenada [desc]", numeros )

print()
print( "Función sorted()" )
print( "----------------" )
# Crea una nueva lista ordenada
# Mantiene la lista original sin cambios

numeros_aux = [ 100, 400, 200, 50, 300 ]

lista_ordenada = sorted( numeros_aux, reverse = True )

print( "Lista original", numeros_aux )
print( "Lista ordenada ", lista_ordenada )


