
# Iteramos una lista de valores
a = [1, 5, 8, 3, 4, "Javascript", "Python"]

for elemento in a:
    print( elemento )

# Profundizando en print()
print()
print("Imprimiendo horizontal (Quitando salto de línea)")
for elemento in a:
    print( elemento, end="" )

print()
print("Creando lista separada por coma")
print( a, sep=".", end="" )

print()

# 
texto = "hola mundo"
for caracter in texto:
    print(caracter)

# Usando enumerate
print("\n")

for indice, caracter in enumerate(texto):
    print( f"Iteración {indice} contiene {caracter}" )

print()
frutas = ["frutilla", "manzana", "platano"]

# 0, "frutilla"
# 1, "manzana"
# 2, "platano"


for i, item in enumerate(frutas):
    print( f"Iteración {i} contiene {item}" )

print()
i = 0
while i < len(frutas):
    print( f"Iteración {i} contiene {frutas[i]}" )
    i += 1

print("\n")

def prueba():
    return 1, 2

a, b = prueba()

print(a, b)


