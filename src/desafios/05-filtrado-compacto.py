import sys

VENTAS = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

if len(sys.argv) < 2:
    print("Error debe ingresar un umbral. Ej: python mayor_a.py 40000")
else:
    try:
        umbral = int(sys.argv[1])
        resultado = {}
        for mes, monto in VENTAS.items():
            if monto > umbral:
                resultado[mes] = monto

        if resultado:
            print(resultado)
        else:
            print("No hay meses para este valor")

    except ValueError:
        print("Error el umbral debe ser un numero. Ej: python mayor_a.py 40000")
