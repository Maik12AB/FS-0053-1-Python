print()
print("Agregar elementos a un diccionario (dict)")
print("-----------------------------------------")

# Cuando hacemos referencia a la clave de un dict
# que no existe, la agrega

diccionario = {"llave 1": 5}

print(diccionario)

diccionario["llave 2"] = 9

print(diccionario)

print()
print("Cambiar valor de una clave de un diccionario (dict)")
print("---------------------------------------------------")

diccionario["llave 2"] = 18

print(diccionario)

print()
print("Eliminar elementos")
print("------------------")

diccionario = {
    "celular": 140000,
    "notebook": 489990,
    "tablet": 120000,
    "cargador": 12400,
}
print("Diccionario original", diccionario)

# Método pop()
# Elimina un elemento de un dict usando la clave `key`
# y devuelve el valor de dicho elemento
valor_eliminado = diccionario.pop("celular")
print(" - Eliminado 'celular", diccionario)
print(f"Valor de 'celular' = {valor_eliminado}")

print()
print("Actualizar diccionarios")
print("-----------------------")

diccionario_a = {"nombre": "Alejandra", "apellido": "López", "edad": 33, "altura": 1.55}
diccionario_b = {"mascota": "miti", "ejercicio": "bicicleta"}

diccionario_a.update(diccionario_b)

print("Diccionario actualizado", diccionario_a)

diccionario_c = {"edad": 40}
diccionario_a.update(diccionario_c)

print("Diccionario actualizado", diccionario_a)

print()
print("Método `keys()`")
print("---------------")

# Devuelve las clave de un diccionario
# El objeto devuelto se puede:
#  - Iterar
#  - Validar contenido
#  - Enlazado dinámicamente

llaves = diccionario.keys()
print(llaves)

# Se puede iterar
for aux in llaves:
    print(aux)

# Validar si existe una llave
if "celular" not in llaves:
    print("No existe la llave de [celular]")
    print("Actualizando dict... Agregando nuevo elemento...")
    diccionario["celular"] = 140_000

print("Nuevo diccionario", diccionario)
print("La variable llaves se actualiza dinámicamente", llaves)

print()
print("Método `value()`")
print("----------------")

# Comportamiento similar a keys()

valores = diccionario.values()
print(valores)

print()
print("Método `items()`")
print("----------------")

# Tiene un comportamiento similar a keys() y values()
# Regresa una tupla

lista = diccionario.items()
print(lista)

for clave, valor in diccionario.items():
    print(f"- {clave}: {valor}")

for i, item in enumerate(diccionario.items()):
    print(f"- {i} {item[0]}: {item[1]}")
