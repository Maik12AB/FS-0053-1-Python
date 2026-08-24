from te import Te

# Crear dos instancias
te1 = Te()
te2 = Te()

# Guardar tipo de dato
tipo1 = type(te1)
tipo2 = type(te2)

# Mostrar tipos
print("Tipo de té 1:", tipo1)
print("Tipo de té 2:", tipo2)

# Comparar
if tipo1 == tipo2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")
