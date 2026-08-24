from utils import tiempo

def pizza(titulo, tipo_masa, tipo_salsa, tipo_ingre):
    print("-------------------------------------------------------")
    print("Su pedido es:\n")
    print(f"Su {titulo} de {tipo_masa} con {tipo_salsa} tiene: ")
    for i in tipo_ingre:
        print(i)
    print()
    print(f"Sera despachada en: {tiempo(tipo_ingre)} min")
    print("-------------------------------------------------------")

    op = input("Desea confirmar el pedido [S/N] ")

    return op
