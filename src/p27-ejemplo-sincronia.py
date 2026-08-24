
# 31%

def sumar_numeros(numeros):

    suma = 0
    for numero in range(numeros):
        suma += numero

    return suma


# Ejemplo de uso
print("Paso 1")
resultado = sumar_numeros(80_000_000)
print("Paso 2")

print( f"La suma es: {resultado:,}")
