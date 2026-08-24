# Esto es un comentario de línea

# print() es una función que tiene salida por la consola
# "Hola mundo" es un literal
print("Hola mundo")

"""
Esto es un comentario
de varias líneas
"""

"""
Trabajando con variables
- Nombre (Iniciar con una letra o el guion bajo _)
- Valor
- Tipo de dato
"""
nombre = "Carlos"
print(nombre)

print("Tipo de dato de la variable nombre: ", type(nombre))

"""
# Ejemplos con print()
print("Carlos", "Soto")  # Varios argumentos
print("Carlos" + " " + "Soto")  # Concatenación
"""

# Métodos en variables
print(nombre.upper())

# Asignar tipo de dato a la variable
apellido: str = "Soto"
print(apellido, type(apellido))

# Cambiar valor (otro tipo de dato) de una variable
# Originalmente tenemos la variable apellido declarada como str
# Cambiar su valor y tipo de datos no es un problema para Python
# El error que recibimos es de vscode
apellido = 10
print(apellido, type(apellido))

# Posición de memoria de una variable
# id() función que permite conocer la posición de memoria
# donde esta almacenada la variable
print(id(apellido))

# Tipo de dato numéricos
edad = 25
print("Edad:", edad, type(edad))

# Operadores matemáticos
#         +  Suma
#         -  Resta
#         *  Multiplicación
#        /  División
#        //  División entera (retorna int)
#         %  Modulo/Resto de la división
#        **  Potencia

# Comportamiento de números enteros
numero_entero_1 = 10
numero_entero_2 = 20
print("Sumando números enteros: ", numero_entero_1 + numero_entero_2)
print("Resta números enteros: ", numero_entero_1 - numero_entero_2)
print("Multiplicación números enteros: ", numero_entero_1 * numero_entero_2)

# La división retorna un float
print("División", 7 / 2, type(7 / 2))
print("División", 2 / 2, type(2 / 2))

# La doble división retorna un int
print("División (int)", 7 // 2, type(7 // 2))
print("División (int)", 2 // 2, type(2 // 2))

# La Módulo o resto de la división (Retorna int)
print("División (Módulo)", 7 % 2, type(7 % 2))
print("División (Módulo)", 2 % 2, type(2 % 2))

# Caso de uso
# Número de páginas para paginación
elementos = 33
por_pagina = 10
print("Tenemos", elementos // por_pagina, "páginas")

# Saber si un número es par
if (10 % 2) == 0:
    print("El número 10 es par")
else:
    print("El número es impar")


# Comportamiento de cadenas de texto
ciudad = "La Serena"
av = "10"

print(ciudad + av)  # Usamos el operador + para concatenar variables str

# Conversión de tipo de datos
av_numero = 10

print(ciudad + str(av_numero))  # str() hace una conversión de int a str

# Otro ejemplo
n1 = "10"
n2 = "20"

print("Concatenando n1+n2", n1 + n2)

# Trabajando con input()
print()
print("Sumar dos números")
print("-----------------")
primer_numero = input("Ingrese el primer número:")
segundo_numero = input("Ingrese el segundo número:")

# Aquí concatenar porque input() devuelve un str
print("La suma de los dos números es:", primer_numero + segundo_numero)

# Conversión de tipo de dato
print("La suma de los dos números es:", int(primer_numero) + int(segundo_numero))

# Usando f-string
suma_str = f"La suma de {primer_numero} con {segundo_numero} es: {int(primer_numero) + int(segundo_numero)}"
suma_otro = ("La suma de " + primer_numero + " con " + segundo_numero + " es: " + str(int(primer_numero) + int(segundo_numero)) )
print(suma_str)
print(suma_otro)
