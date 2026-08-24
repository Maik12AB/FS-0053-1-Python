from p24_poo_clase_medicamento import Medicamento

resp = Medicamento()

print()

# Nueva regla de negocio, donde el valor de descuento se inicializa en cero
resp.asignar_precio(-1)
if resp.precio == 0 and resp.descuento == 0.0:
    print(".", end="")
else:
    print("E", end="")

resp.asignar_precio(5_000)
if resp.precio == 5_000 and resp.descuento == 0.0:
    print(".", end="")
else:
    print("E", end="")

resp.asignar_precio(11_000)
if resp.precio == 11_000 and resp.descuento == 0.1:
    print(".", end="")
else:
    print("E", end="")

resp.asignar_precio(25_000)
if resp.precio == 25_000 and resp.descuento == 0.2:
    print(".", end="")
else:
    print("E", end="")

# Nueva regla de negocio
# Invalida los descuentos del 30% para precios
# mayores de 30.000
# Nuevo descuento para estos vaslores es de 20%
resp.asignar_precio(35_000)
if resp.precio == 35_000 and resp.descuento == 0.2:
    print(".", end="")
else:
    print("E", end="")

# Regla modificada ver nota test anterior
if resp.cal_descuento(35_000) == 0.2:
    print(".", end="")
else:
    print("E", end="")

if resp.cal_descuento(19_999) == 0.1:
    print(".", end="")
else:
    print("E", end="")

# Según nueva regla de negocio
# Al instanciar la clase se debe asignar
# el nombre del medicamento y el stock
resp = Medicamento('Nombre medicamento', 10)
if resp.nombre == 'Nombre medicamento' and resp.stock == 10:
    print(".", end="")
else:
    print("E", end="")

# La nueva regla indica que si el stock no es suministrado
# se debe asignar 0
resp = Medicamento('Nombre medicamento')
if resp.nombre == 'Nombre medicamento' and resp.stock == 0:
    print(".", end="")
else:
    print("E", end="")

# Asigno el nuevo precio bruto
resp = Medicamento('Nombre medicamento')
if resp.asignar_precio(11_000):
    if resp.precio_bruto == 11_682 and resp.precio_neto == 9_900 and resp.descuento == 0.1:
        print(".", end="")
    else:
        print("E", end="")
else:
    print("E", end="")

resp = Medicamento('Nombre medicamento')
if resp.asignar_precio(25_000):
    if resp.precio_bruto == 23_600 and resp.precio_neto == 20_000 and resp.descuento == 0.2:
        print(".", end="")
    else:
        print("E", end="")
else:
    print("E", end="")

resp = Medicamento('Nombre medicamento')
if resp.asignar_precio(35_000):
    if resp.precio_bruto == 33_040 and resp.precio_neto == 28_000 and resp.descuento == 0.2:
        print(".", end="")
    else:
        print("E", end="")
else:
    print("E", end="")


"""
- Llega precio
- Calculo descuento
- Obtengo el precio a aplicar (Neto)
- Calculo el iva
- neto + iva = bruto
"""



"""
- [X] El precio bruto se debe asignar en una instancia ya creada.
- [X] Al ser asignado, en caso de que sea mayor a 0:
  - [X] precio bruto del medicamento
  - [X] descuento
  - [X] precio neto.
- [ ] El descuento se debe aplicar sobre el precio bruto más el IVA.
  - [ ] solo se aplicará en caso de que el valor del medicamento:
    - [ ] esté entre $10.000 y $19.999 (10% de descuento)
    - [ ] sea mayor o igual a $20.000 (20% de descuento)
"""



print()
