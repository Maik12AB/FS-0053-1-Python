from string import ascii_lowercase
import getpass

password = getpass.getpass("Ingrese la contraseña: ").lower()

intentos = 0
resultado = ""

if not password.isalpha():
    print("Error: la contraseña debe contener solo letras")
    exit()

clave = ""
for letra in password:
    for posible in ascii_lowercase:
        intentos += 1
        if posible == letra:
            clave += posible
            resultado += posible
            break

print(f"La contraseña [{clave}] fue forzada en {intentos} intentos")
