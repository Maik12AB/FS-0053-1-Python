import sys

RUTA = "src/desafios/data/"

if len(sys.argv) < 2:
    print("Uso: python word_count.py <ruta_archivo>")
    sys.exit()

ruta_archivo = RUTA + sys.argv[1]

try:
    with open(ruta_archivo, "r") as file:
        texto = file.read()

    # Contar palabras distintas
    contador = {
        "caracteres" : len(set(texto)),
        "palabras" : len(set(texto.split(" ")))
    }

    # Contar caracteres distintos
    caracteres_distintos = set(texto)
    print("\nCantidad de caracteres distintos:", len(caracteres_distintos))

    palabras = texto.split(" ")
    palabras_distintas = set(palabras)
    print("Cantidad de palabras distintas:", len(palabras_distintas))


    # Ejercicio de limpieza para determinar realmente cuantas
    # palabras distintas son
    # NO ENVIAR A EVALUACIÓN
    #-- -
    normalizar = texto.lower().replace(".", "").replace(",", "")
    normalizar = normalizar.split()
    palabras_reales = set(normalizar)
    print("Cantidad de palabras reales:", len(palabras_reales))
    print(palabras_reales)
    #-- -

except FileNotFoundError:
    print(f"ERROR: No se encontró el archivo {ruta_archivo}")
