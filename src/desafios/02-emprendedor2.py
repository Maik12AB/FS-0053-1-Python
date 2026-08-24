# Leer
# P: Precio de Suscripción
# u_normal: Número de Usuarios normal
# u_premium: Número de Usuarios premium
# GT: Gastos Totales
# 𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇

p = float(input("Ingrese el precio de la suscripción: "))
u_normal = int(input("Ingrese el número de usuarios normal: "))
u_premium = int(input("Ingrese el número de usuarios premium: "))
gt = float(input("Ingrese los gastos totales: "))

ingreso_normal = (p * u_normal)
ingreso_premium = (p * u_premium) * 1.5

utilidades = (ingreso_normal + ingreso_premium) - gt

print( f"Las utilidades son: {utilidades}" )
