# Mostrar menú por consola
def imprimir_menu(x: str = "Valor predeterminado") -> None:
    """
    Muestra menú de opciones en la consola\n
    x = Pregunta a ser realizada
    """
    print(x)
    print('Opciones: ')
    print('1). De acuerdo')
    print('2). En desacuerdo')
    print('3). No me interesa')

    # Python siempre regresa un valor desde una función
    # En el caso de no ser especificado, Pyhton retorna
    # None
    # return 1

preguntas = [
    "Enunciado Pregunta 1",
    "Enunciado Pregunta 2",
    "Enunciado Pregunta 3",
    "¿Esto es otra pregunta?"
]

respuestas = []

for p in preguntas:
    prueba = imprimir_menu(p)
    respuestas.append(input('> '))

print()
print("Las respuestas son:")
print("-------------------")
for i, r in enumerate(respuestas):
    print( f"- {preguntas[i]} es: {r}" )

print( "Muchas gracias por responder la encuesta")
