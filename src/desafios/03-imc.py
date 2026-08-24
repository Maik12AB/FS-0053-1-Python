# Calculo del IMC
# -- - ----------
# W : corresponde al peso de la persona en Kg.
# H: corresponde a la altura en metros.
# IMC: EL valor del IMC, en [Kg/m2]

# | IMC          | Clasificación OMS   |
# |--------------|---------------------|
# |< 18.5        | Bajo Peso
# |[ 18.5, 25 [  | Adecuado
# |[ 25, 30 [    | Sobrepeso
# |[ 30, 35[     | Obesidad Grado I
# |[ 35, 40 [    | Obesidad Grado II
# |> 40          | Obesidad Grado III

import sys

print()
print( "-----------------------------------")
print( "Calculo del índice de masa corporal")
print( "-----------------------------------\n")

if sys.argv[1].lower() == "--help" or sys.argv[1].lower() == "--h" or sys.argv[1].lower() == "/?":
    print( "El peso debe estar en kg")
    print( "La altura debe estar en cm")
    print( "Uso:")
    print( "python imc.py peso_kg altura_cm")
    sys.exit()
elif len( sys.argv ) < 3:
    print( "Error" )
    print( "Debe especificar todos los argumentos")
    sys.exit()

w = float( sys.argv[1] )
h = int( sys.argv[2] )

imc = round( w / ( (h / 100) ** 2 ), 2)

if imc < 18.5:
    clasificacion = "Bajo peso"
elif imc < 25:
    clasificacion = "Adecuado"
elif imc < 30:
    clasificacion = "Sobrepeso"
elif imc < 35:
    clasificacion = "Obesidad Grado I"
elif imc < 40:
    clasificacion = "Obesidad Grado II"
else:
    clasificacion = "Obesidad Grado III"

print( f"Su IMC es {imc}")
print( f"La clasificación OMS es {clasificacion}")
