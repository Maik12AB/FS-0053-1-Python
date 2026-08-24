
# -- -----------------------------------
# Tres tipos de errores en proigramación
# -- -----------------------------------

# Errores de sintaxis
# -- ----------------
# Estos errores impiden la ejecución del programa
# cuando son detectados

# edad = 20

# if edad >= 18:
# print("Eres mayor de edad")


# Errores en tiempo de ejecución
# -- ---------------------------
# Ocurren durante la ejecución del programa
# cuando queremos realizar una operación
# no valida

# n1 = 10
# n2 = 0

# r = n1 / n2


# Errores de lógica
# -- ---------------
# El programa se ejecuta sin detenerse, pero el resultado
# es incorrecto o no esperado.

# precio = 10_000
# descuento = 20

# precio_venta = precio - descuento

# print(f"El precio de venta es: {precio_venta:,}")

# -- -----------------------------------
# -- Excepciones
# -- -----------------------------------
# Una excepción es un evento de error que ocurre durante
# la ejecución de un programa y que interrumpe el flujo
# normal del código

# Al usuario le damos la mínima posibilidad de que
# rompa el programa
# -- -
# Caso de uso 1:
# El usuario tiene la posibilidad de ingresar uno
# Eso rompe el sistema

# numero = int( input("Ingrese un número: ") )
# print( f"El número ingresado es: {numero}" )

# Evitamos que si el usuario ingresa un valor no válido,
# el programa se rompa
# try:
#     numero = int(input("Ingrese un número: "))
#     print(f"El número ingresado es: {numero}")
# except ValueError:
#     # registrar log
#     print("Error: Debe ingresar un número entero válido.")

# -- -----------------------------------
# -- Excepciones | Captura múltiple
# -- -----------------------------------

# try:
#     edad = int(input("Ingrese su edad:"))
#     divisor = int(input("Ingrese número para dividir su edad:"))

#     print(edad / divisor)
# except ValueError:
#     print("Error: E1518-45-20")
# except ZeroDivisionError:
#     print("Error [E1518-45-21]: No se puede dividir por cero.")
# except Exception as e:
#     print(f"Error: {e}")

# -- -------------------------------------
# -- Excepciones | Uso de else / Finally
# -- -------------------------------------

# try:
#     edad = int(input("Ingrese su edad:"))
#     divisor = int(input("Ingrese número para dividir su edad:"))

#     print(edad / divisor)
# except ValueError:
#     print("Error: E1518-45-20")
# except ZeroDivisionError:
#     print("Error [E1518-45-21]: No se puede dividir por cero.")
# except Exception as e:
#     print(f"Error: {e}")
# else:
#     # Se ejecuta unicamente si no ocurre ninguna excepción
#     print("La operación se realizó correctamente.")
# finally:
#     # Se ejecuta siempre, haya ocurrido o no una excepción
#     print("Fin del programa.")

# -- -------------------------------------
# -- Excepciones | Uso de else / Finally
# -- -------------------------------------

# while True:
#     try:
#         edad = int(input("Ingrese su edad: "))
#         if edad < 0:
#             raise Exception("Edad debe ser un N° positivo (Excepcion).")
#             # print("Edad debe ser un N° positivo.")

#         while True:
#             try:
#                 divisor = int(input("Ingrese número para dividir su edad: "))

#                 div = edad / divisor
#             except ValueError:
#                 print("Debe ingresar un número")
#             except ZeroDivisionError:
#                 print("El N° por el cual desea dividir no puede ser cero")
#             else:
#                 break
#     except ValueError:
#         print("Debe ingresar un número")
#     except Exception as e:
#         print(f"ERROR: {e}")
#     else:
#         print(div)
#         break


# -- ----------------------------
# -- Excepciones | Personalizada
# -- ----------------------------

class SaldoInsuficienteError(Exception):
    ...

def retirar_dinero(saldo, retirar):
    if retirar > saldo:
        raise SaldoInsuficienteError(f"Su saldo es {saldo:,} y desea retirar {retirar:,}.")
    else:
        saldo -= retirar
        return saldo

#-- ----------------------------
saldo = 8_000
retirar = 10_000

try:
    saldo = retirar_dinero(saldo, retirar)
except SaldoInsuficienteError as e:
    print(f"ERROR de Saldo Insuficiente: {e}")

print(f"Saldo actual: {saldo:,}")


