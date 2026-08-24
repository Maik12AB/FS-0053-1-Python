import sys
import random

opciones = ('piedra', 'papel', 'tijera')

if len( sys.argv ) < 2:
    print(f"Debe enviar una opción {opciones}" )
    sys.exit()

usuario = sys.argv[1].lower()
compu = random.choice( opciones )

# Validar argumento ingresado por el usuario
if usuario not in opciones:
    print( "Argumento inválido: Debe ser piedra, papel o tijera." )
    sys.exit()

if usuario == "piedra" and compu == "tijera":
    resultado = "Ganaste!!"
elif usuario == "tijera" and compu == "papel":
    resultado = "Ganaste!!"
elif usuario == "papel" and compu == "piedra":
    resultado = "Ganaste!!"
elif compu == "piedra" and usuario == "tijera":
    resultado = "Perdiste!!"
elif compu == "tijera" and usuario == "papel":
    resultado = "Perdiste!!"
elif compu == "papel" and usuario == "piedra":
    resultado = "Perdiste!!"
else:
    resultado = "Empate!!"

print( f"Tu jugaste {usuario.capitalize()}" )
print( f"Computador jugó {compu.capitalize()}" )
print(resultado)
