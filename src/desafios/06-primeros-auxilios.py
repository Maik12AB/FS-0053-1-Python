r_estimulos = input("¿Responde a estímulos?").lower()

if r_estimulos == "si":
    print("Valorar la necesidad de llevarlo al hospital más cercano")

elif r_estimulos == "no":
    print("Abrir la vía Aérea")
    respira = input("¿Respira?").lower()

    if respira == "si":
        print("Permitirle posición de suficiente ventilación")
    elif respira == "no":
        print("Administrar 5 Ventilaciones y llamar Ambulancia")

        while True:
            s_vida = input("¿Signos de vida?").lower()

            if s_vida == "si":
                print("Reevaluar a la espera de la Ambulancia")
            elif s_vida == "no":
                print("Administrar Compresiones Torácicas hasta que llegue ambulancia")

            ambulancia = input("¿Llegó la Ambulancia?").lower()
            if ambulancia == "si":
                break
            elif ambulancia != "no":
                print("Por favor responder las preguntas con si o no")
            else:
                print("Por favor responde solo con si o no")
    else:
        print("Por favor responde solo con si o no")
else:
    print("Por favor responde solo con si o no")
