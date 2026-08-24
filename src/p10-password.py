# getpass es una librería de la biblioteca estandar de Python
import getpass
import hashlib
import hmac

PASS_BBDD = "hola mundo"     # Esto debe estar encriptado

# Contraseña encriptada
# Así se guarda y recupera de la BBDD
PASS_HASH = hashlib.sha256(PASS_BBDD.encode()).hexdigest()

print( PASS_HASH )


# Para trabajar con password es mala práctica utilizar
# input() debido a que podemos ver la clave que
# estamos ingresando
#password = input("Ingrese la clase secreta: ")
#password = getpass.getpass("Ingrese la clase secreta: ")
password = ""
i = 0

while True:
    password = getpass.getpass("Ingrese la clase secreta: ")

    if hmac.compare_digest(
        hashlib.sha256(password.encode()).hexdigest(),
        PASS_HASH
    ):
        break

    i += 1
    if i >= 3:
        break

if i >= 3:
    print("Intentos completados. No tiene acceso al sistema")
    # Rutina de bloquear usuario en BBDD
else:
    print( "Clave correcta. Puede utilizar el programa" )
