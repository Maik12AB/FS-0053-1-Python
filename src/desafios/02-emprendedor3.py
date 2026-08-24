# Leer
# P: Precio de Suscripción
# u_normal: Número de Usuarios normal
# GT: Gastos Totales
# u_anterior: Utilidad del año anterior
# 𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇

p = float(input("Ingrese el precio de la suscripción: "))
u_normal = int(input("Ingrese el número de usuarios normal: "))
gt = float(input("Ingrese los gastos totales: "))
u_anterior = float(input("Ingrese la utilidad del año anterior: "))

u_actuales = (p * u_normal) - gt

razon = round( u_actuales / u_anterior, 2 )

print( f"Las utilidades actuales son: {u_actuales}" )
print( f"Razón (Utilidad actual vs utilidad del año anterior): {razon}" )
