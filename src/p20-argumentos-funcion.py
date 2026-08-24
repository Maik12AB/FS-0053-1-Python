def extremo_multiplicado(lista, factor):
    print(type(lista))
    print(type(factor))
    print(variable_global)

    # minimo = min(lista)
    # maximo = max(lista)
    # return factor*minimo, factor*maximo

variable_global = 100

# Llamada correcta
# Argumentos por posición
print(
    extremo_multiplicado([1,2,3,4], 4)
)

# Llamada incorrecta
# Argumentos por posición
print(
    extremo_multiplicado(4, [1,2,3,4])
)

# Llamada correcta
# Argumentos por nombre
print(
    extremo_multiplicado(factor=4, lista=[1,2,3,4])
)
