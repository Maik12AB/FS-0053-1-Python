
def factorial(valor):
    producto = 1
    for i in range(1, valor+1):
        producto *= i

    return producto

def productoria(valor):
    a = 1
    for i in valor:
        a *= i

    return a


# Función controladora
def calcular(**kwargs):
    for clave, valor in kwargs.items():
        if "fact" in clave:
            m = "El factorial de"
            r = factorial(valor)
        elif "prod" in clave:
            m = "La productoria de"
            r = productoria(valor)
        else:
            m = ""
            r = 0

        print( f"{m} {valor} es {r}" )


# Invocar función controladora
calcular(fact_1 = 5, prod_1 = [4, 6, 7, 4, 3], fact_2 = 6)
