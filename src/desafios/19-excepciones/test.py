from foto import Foto
from error import DimensionError

# Ancho, alto y ruta
foto1 = Foto(800, 600, "img/foto1.png")

# -- - ---------------------------
# Test correctos

# Cambiar el ancho
foto1.ancho = 2_499
if foto1.ancho == 2_499:
    print(".", end="")
else:
    print("E", end="")

foto1.alto = 900
if foto1.alto == 900:
    print(".", end="")
else:
    print("E", end="")

print()

# -- - ---------------------------
# Test incorrectos

try:
    foto1.ancho = 2_501
except DimensionError as e:
    if e.mensaje == "Ancho no permitido" \
        and e.dimension == 2_501 \
        and e.maximo == foto1.MAX:
        print(".", end="")
    else:
        print("E", end="")
else:
    print("E", end="")

try:
    foto1.alto = 2_501
except DimensionError as e:
    if e.mensaje == "Alto no permitido" \
        and e.dimension == 2_501 \
        and e.maximo == foto1.MAX:
        print(".", end="")
    else:
        print("E", end="")
else:
    print("E", end="")

try:
    foto1.ancho = 0
except DimensionError as e:
    if e.mensaje == "Ancho no permitido" \
        and e.dimension == 0:
        print(".", end="")
    else:
        print("E", end="")
else:
    print("E", end="")

try:
    foto1.alto = 0
except DimensionError as e:
    if e.mensaje == "Alto no permitido" \
        and e.dimension == 0:
        print(".", end="")
    else:
        print("E", end="")
else:
    print("E", end="")

try:
    foto1.ancho = 0
except DimensionError as e:
    # print(e)
    if str(e) == "El mesaje es Ancho no permitido La dimensión es 0 El máximo es 2500":
        print(".", end="")
    else:
        print("E", end="")
else:
    print("E", end="")

try:
    foto1.alto = 0
except DimensionError as e:
    # print(e)
    if str(e) == "El mesaje es Alto no permitido La dimensión es 0 El máximo es 2500":
        print(".", end="")
    else:
        print("E", end="")
else:
    print("E", end="")


# -- - ---------------------------
print()
