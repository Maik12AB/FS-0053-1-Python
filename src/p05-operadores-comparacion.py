# Declaración de variables
nombre = "Carlos"
edad = 35
edad_minima = 18

# ¿La edad de la persona es igual a la edad mínima?
print( f"¿La edad es igual a la edad mínima? {edad == edad_minima} " )

# Saber si la persona es mayor de edad
print( f"¿La persona es mayor de edad? {edad >= edad_minima} " )

#-- - ---------------------------------------------
#-- - Nuevo contexto
#-- - Las variables anteriores las ignoramos
#-- - ---------------------------------------------
print("\n")
print("Perfil del estudiante")
print("---------------------\n")

# Suponemos que esta información llega desde BBDD (PostgreSQL)
id = 1500
nombre = "Camila"
edad = 20
promedio = 5.8
asistencia = 82

# Reglas de negocio
# -----------------
# Es buena práctica no tener los valores que representan condiciones
# establecidas por la organización, como valores fijos en el código
# de nuestro programa.
# Ideal tener estos valores en la BBDD
# Simulamos petición
# Simular trabajar con constantes (En Python no existen)
EDAD_MAYOR = 18
PROMEDIO_CLASES = 5.5
ASISTENCIA_APRUEBA = 80

es_mayor_edad = (edad >= EDAD_MAYOR)                # Por buena práctica utilizamos paréntesis
tiene_buen_promedio = promedio >= PROMEDIO_CLASES   # Pero no son requeridos
cumple_asistencia = ( asistencia >= ASISTENCIA_APRUEBA )

print( f"El estudiante: {nombre}" )
print( f"¿Es mayor de edad? {es_mayor_edad}" )
print( f"¿Tiene buen promedio? {tiene_buen_promedio}" )
print( f"¿Cumple con la asistencia: {cumple_asistencia}" )

