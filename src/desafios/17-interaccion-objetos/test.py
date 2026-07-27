from producto import Producto
from tienda import Minimarket, Restaurante, Supermercado, Farmacia

mini = Minimarket("La Serena Market SpA", 1_000)

mini.ingresar_producto("Prod 1", 10, 15)

p1 = mini.lista_productos[0]
if p1.nombre == "Prod 1" and p1.precio == 10 and p1.stock == 15:
    print(".", end="")
else:
    print("E", end="")

mini.ingresar_producto("Prod 2", 100, 150)
p2 = mini.lista_productos[1]
if p2.nombre == "Prod 2" and p2.precio == 100 and p2.stock == 150:
    print(".", end="")
else:
    print("E", end="")

mini.ingresar_producto("Prod 1", 100, 15)
p3 = mini.lista_productos[0]
if p3.nombre == "Prod 1" and p3.precio == 10 and p3.stock == 30:
    print(".", end="")
else:
    print("E", end="")

mini.ingresar_producto("Prod 3", 100, -1)
p4 = mini.lista_productos[2]
if p4.nombre == "Prod 3" and p4.precio == 100 and p4.stock == 0:
    print(".", end="")
else:
    print("E", end="")

print()

rest = Restaurante("Restaurante SpA", 1_000)

rest.ingresar_producto("Prod 1", 10)
p1 = rest.lista_productos[0]
if p1.nombre == "Prod 1" and p1.precio == 10 and p1.stock == 0:
    print(".", end="")
else:
    print("E", end="")

rest.ingresar_producto("Prod 2", 10)
p2 = rest.lista_productos[1]
if p2.nombre == "Prod 2" and p2.precio == 10 and p2.stock == 0:
    print(".", end="")
else:
    print("E", end="")

r = rest.realizar_venta("Prod 2", 1_000)
if r == "Venta completada":
    print(".", end="")
else:
    print("E", end="")

r = rest.realizar_venta("Prod ABC", 1_000)
if r == "Producto no existe":
    print(".", end="")
else:
    print("E", end="")

print()

super = Supermercado("Supermercado SpA", 1_000)

super.ingresar_producto("Prod 1", 10, 10)
p1 = super.lista_productos[0]
if p1.nombre == "Prod 1" and p1.precio == 10 and p1.stock == 10:
    print(".", end="")
else:
    print("E", end="")

super.ingresar_producto("Prod 2", 10, -1)
p2 = super.lista_productos[1]
if p2.nombre == "Prod 2" and p2.precio == 10 and p2.stock == 0:
    print(".", end="")
else:
    print("E", end="")

super.ingresar_producto("Prod 3", 10, 5)
p3 = super.lista_productos[2]
if p3.nombre == "Prod 3" and p3.precio == 10 and p3.stock == 5:
    print(".", end="")
else:
    print("E", end="")

super.ingresar_producto("Prod 4", 10, 9)
p4 = super.lista_productos[3]
if p4.nombre == "Prod 4" and p4.precio == 10 and p4.stock == 9:
    print(".", end="")
else:
    print("E", end="")

super.ingresar_producto("Prod 5", 10, 11)
p5 = super.lista_productos[4]
if p5.nombre == "Prod 5" and p5.precio == 10 and p5.stock == 11:
    print(".", end="")
else:
    print("E", end="")

r = super.realizar_venta("Prod 1", 1)
if r == "Venta completada":
    print(".", end="")
else:
    print("E", end="")

r = super.realizar_venta("Prod 1", 9)
if r == "Venta completada":
    print(".", end="")
else:
    print("E", end="")

r = super.realizar_venta("Prod 1", 1)
if r == "No es posible vender 0 productos o productos negativos.":
    print(".", end="")
else:
    print("E", end="")

r = super.realizar_venta("Prod ABC", 1_000)
if r == "Producto no existe":
    print(".", end="")
else:
    print("E", end="")

r = super.realizar_venta("Prod 2", 1)
if r == "No es posible vender 0 productos o productos negativos.":
    print(".", end="")
else:
    print("E", end="")

r = super.realizar_venta("Prod 3", 10)
if r == "Venta completada. Solo se vendieron 5 unidades":
    print(".", end="")
else:
    print("E", end="")

r = super.realizar_venta("Prod 3", 10)
if r == "No es posible vender 0 productos o productos negativos.":
    print(".", end="")
else:
    print("E", end="")

print()

farma = Farmacia("Farmacia SpA", 1_000)

farma.ingresar_producto("Prod 1", 10, 10)
p1 = farma.lista_productos[0]
if p1.nombre == "Prod 1" and p1.precio == 10 and p1.stock == 10:
    print(".", end="")
else:
    print("E", end="")

farma.ingresar_producto("Prod 2", 10, -1)
p2 = farma.lista_productos[1]
if p2.nombre == "Prod 2" and p2.precio == 10 and p2.stock == 0:
    print(".", end="")
else:
    print("E", end="")

farma.ingresar_producto("Prod 3", 10, 5)
p3 = farma.lista_productos[2]
if p3.nombre == "Prod 3" and p3.precio == 10 and p3.stock == 5:
    print(".", end="")
else:
    print("E", end="")

farma.ingresar_producto("Prod 4", 15_001, 5)
p4 = farma.lista_productos[3]
if p4.nombre == "Prod 4" and p4.precio == 15_001 and p4.stock == 5:
    print(".", end="")
else:
    print("E", end="")

r = farma.realizar_venta("Prod 1", 3)
if r == "Venta completada":
    print(".", end="")
else:
    print("E", end="")

r = farma.realizar_venta("Prod 1", 4)
if r == "No se puede solicitar más de 3 unidades":
    print(".", end="")
else:
    print("E", end="")

print()

# Probando salida de listar_productos()
# Retorna un texto de salida

salida_rest = rest.listar_productos()

esperado_rest = """- Prod 1 | $10
- Prod 2 | $10"""

# Normalizamos ambas salidas para quitar espacios y saltos de línea
# Obtenemos una lista
salida_norm = [line.strip() for line in salida_rest.strip().splitlines()]
esperado_norm = [line.strip() for line in esperado_rest.strip().splitlines()]

if salida_norm == esperado_norm:
    print(".", end="")
else:
    print("E", end="")

# Supermercado
salida_super = super.listar_productos()

esperado_super = """- Prod 1 | $10 | Stock: 0 | Pocos productos disponibles
- Prod 2 | $10 | Stock: 0 | Pocos productos disponibles
- Prod 3 | $10 | Stock: 0 | Pocos productos disponibles
- Prod 4 | $10 | Stock: 9 | Pocos productos disponibles
- Prod 5 | $10 | Stock: 11"""

salida_norm = [line.strip() for line in salida_super.strip().splitlines()]
esperado_norm = [line.strip() for line in esperado_super.strip().splitlines()]

if salida_norm == esperado_norm:
    print(".", end="")
else:
    print("E", end="")

# Farmacia
salida_farma = farma.listar_productos()

esperado_farma = """- Prod 1 | $10
- Prod 2 | $10
- Prod 3 | $10
- Prod 4 | $15001 | Envío gratis al solicitar este producto"""

salida_norm = [line.strip() for line in salida_farma.strip().splitlines()]
esperado_norm = [line.strip() for line in esperado_farma.strip().splitlines()]

if salida_norm == esperado_norm:
    print(".", end="")
else:
    print("E", end="")




print()
