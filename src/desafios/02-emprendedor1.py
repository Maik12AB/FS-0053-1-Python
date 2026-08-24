# Leer
# P: Precio de Suscripción
# U: Número de Usuarios
# GT: Gastos Totales
# 𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇

p = float(input("Ingrese el precio de la suscripción: "))
u = int(input("Ingrese el número de usuarios: "))
gt = float(input("Ingrese los gastos totales: "))

utilidades = (p * u) - gt

print( f"Las utilidades son: {utilidades}" )
