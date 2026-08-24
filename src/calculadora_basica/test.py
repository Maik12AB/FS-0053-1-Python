from sumar import sumar
from restar import restar

# Sumar envio dos números enteros
resp = sumar(10, 20)
if resp == 30:
    print(".", end="")
else:
    print("E", end="")

# Sumar envio de un entero y una cadena
try:
    resp = sumar(10, "20")
    if resp == 30:
        print(".", end="")
    else:
        print("E", end="")
except:
    print("E", end="")

# Sumar envio de un cadena y un entero
try:
    resp = sumar("10", 20)
    if resp == 30:
        print(".", end="")
    else:
        print("E", end="")
except:
    print("E", end="")

# Sumar envio dos cadenas
try:
    resp = sumar("10", "20")
    if resp == 30:
        print(".", end="")
    else:
        print("E", end="")
except:
    print("E", end="")

# Restar envio dos números enteros
resp = restar(10, 20)
if resp == -10:
    print(".", end="")
else:
    print("E", end="")

# restar envio de un entero y una cadena
try:
    resp = restar(10, "20") # type: ignore
    print("E", end="")
except:
    print(".", end="")

print()

# x = 10
# print( isinstance(x, int) )     # true
# print( type(x) == int )         # true
# print( type(x) == "int" )       # false
# print( x == int )               # false

# if type(x) == int:
#     print( "es entero")

# r = type(x) == int
# print( r )
