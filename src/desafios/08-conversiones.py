import sys

if len(sys.argv) < 5:
    print("ingrese tasa de conversión a sol peruano, peso argentino y dolar americano, también incluya finalmente cuanto pesos chilenos vamos a convertir a esas monedas")
    sys.exit()

tasa = {
    "s_peruano": sys.argv[1].replace(",", "."),
    "p_argentino": sys.argv[2].replace(",", "."),
    "d_americano": sys.argv[3].replace(",", ".")
}

valor_convertir = sys.argv[4]       # Pesos chilenos

try:
    p_chileno = int(valor_convertir)

    m_peruano = float(tasa["s_peruano"])*p_chileno
    m_argentino = float(tasa["p_argentino"])*p_chileno
    m_americano = float(tasa["d_americano"])*p_chileno

    print(f"Los {p_chileno:,} pesos equivalen a:")
    print(f"{m_peruano} Soles")
    print(f"{m_argentino} Pesos Argentinos")
    print(f"{m_americano} Dolares")

except ValueError:
    print("ERROR")
    print("Los valores ingresados deben ser números enteros")
    print(f"Valores ingresados: {tasa["s_peruano"]} - {tasa["p_argentino"]} - {tasa["d_americano"]} - {p_chileno}")
