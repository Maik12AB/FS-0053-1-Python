efemerides = {
    "1 de enero": "Año Nuevo",
    "27 de febrero": "Terremoto en Chile",
    "8 de marzo": "Día de la Mujer",
    "21 de mayo": "Glorias Navales",
    "18 de septiembre": "Fiestas Patrias",
    "19 de septiembre": "Glorias del Ejercito",
    "25 de diciembre": "Navidad",
}
fecha = input("Ingrese un fecha: ")

fecha_buscar = fecha.lower()

efe = efemerides.get(fecha_buscar, "ND")

if efe == "ND":
    print("No hay efemérides para esta fecha")
    print(f"El usuario a ingresado: {fecha_buscar}")
else:
    print(efe)
