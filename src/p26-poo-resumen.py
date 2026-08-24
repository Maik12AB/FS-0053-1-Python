# En la POO tenemos 2 tipos de elementos
# Atributos -> Datos/Estados
# Métodos -> Acciones

"""
Automóvil

Datos:
- Marca
- Modelo
- Color
- Encendido
- Velocidad

Acciones/comportamiento:
- Encender
- Apagar el auto
- Acelerar
- Frenar
- Mostrar info
"""

from abc import ABC, abstractmethod


# Clase - Receta/Plantilla
class Automovil:

    cantidad_autos = 0  # Atributo de clase

    # Constructor
    # self == this
    def __init__(self, marca: str = "NA", modelo: str = "NA", color: str = "NA"):
        # Atributos de identidad
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.__patente = "NA"
        # atributos de estado
        self.__encendido = False
        self.__velocidad = 0

        # Invocando al atyributo de clase
        # utiizando el nombre de la clase
        Automovil.cantidad_autos += 1

    @classmethod
    def mostrar_cantidad_autos(cls):
        print(f"Se han creado {cls.cantidad_autos} autos")

    def __str__(self):
        return f"Automóvil: {self.marca} {self.modelo} {self.color}"

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Encendido: {self.__encendido}")
        print(f"Velocidad: {self.__velocidad} km/h")

    def encender(self):
        self.__encendido = True
        print("El auto está encendido")

    def apagar(self):
        self.__encendido = False
        print("El auto está apagado")

    def acelerar(self, velocidad: int = 10):
        if velocidad < 0:
            print("La velocidad no puede ser negativa")
        elif self.__encendido:
            self.__velocidad += velocidad
            print(f"El auto aceleró a {self.__velocidad} km/h")
        else:
            print("El auto está apagado, no puede acelerar")

    def frenar(self, velocidad: int = 10):
        if velocidad < 0:
            print("La velocidad no puede ser negativa")
        elif self.__encendido:
            if self.__velocidad - velocidad < 0:
                self.__velocidad = 0
            else:
                self.__velocidad -= velocidad
            print(f"El auto frenó a {self.__velocidad} km/h")
        else:
            print("El auto está apagado, no puede frenar")

    # Getter
    @property
    def velocidad(self):
        return self.__velocidad

    # Setter
    @velocidad.setter
    def velocidad(self, velocidad: int):
        if velocidad < 0:
            print("La velocidad no puede ser negativa")
        elif self.__encendido:
            self.__velocidad = velocidad
            print(f"El auto aceleró a {self.__velocidad} km/h")
        else:
            print("El auto está apagado, no puede acelerar")

    # Método estatico
    @staticmethod
    def mostrar_mensaje():
        print("Este es un método estático, no necesita una instancia de la clase para ser invocado")

    # Validación de patente
    # Ejemplo de Getters y Setters, y métodos estáticos
    @property
    def patente(self):
        return self.__patente

    @patente.setter
    def patente(self, patente: str):
        if self.validar_patente(patente):
            self.__patente = patente

    @staticmethod
    def validar_patente(patente: str):
        if len(patente) == 6:
            return True
        else:
            return False

    # Ejemplo de polimorfismo
    # el método mover() se comporta diferente según la clase que lo invoque
    # def mover(self):
    #     if self.__encendido and self.__velocidad > 0:
    #         print("El auto se está moviendo")
    #     else:
    #         print("El auto está apagado o esta detenido")

    # Abstracción
    @abstractmethod
    def mover(self):
        ...

class AutoElectrico(Automovil):
    def __init__(self, marca: str = "NA", modelo: str = "NA", color: str = "NA", autonomia: int = 0):
        # super() nos permite invocar al constructor de la clase padre
        # Entonces se ejecuta primero el constructor padre y luego el constructor de la clase hija
        super().__init__(marca, modelo, color)
        self.autonomia = autonomia

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Autonomía: {self.autonomia} km")

    # Sobre escritura de métodos
    def mover(self):
        print("hola")


# -- - ---------------------------------------------------------
# Objeto / Instancia
# auto_1 = Automovil("Toyota", "Corolla", "Rojo")
# auto_2 = Automovil()      # Los argumentos del constructor son opcionales y tienen valores por defecto
# auto_3 = Automovil(modelo="Civic", marca="Honda", color="Azul")

# print( type(1) )
# print( type(auto_1) )
# print( isinstance(auto_1, Automovil) )

# Cuando utilizamos el constructor, no es necesario asignar los
# valores de los atributos uno por uno
# auto_1.marca = "Toyota"
# auto_1.modelo = "Corolla"
# auto_1.color = "Rojo"

# print(auto_1.marca)
# print(auto_1.modelo)
# print(auto_1.color)
# print(auto_2.marca)
# print(auto_2.modelo)
# print(auto_2.color)
# print(auto_3.marca)
# print(auto_3.modelo)
# print(auto_3.color)

# print()
# print(auto_1)
# print(auto_1.__str__())



# auto_1.__velocidad = 10
# auto_1._Automovil__velocidad = 2000 # type: ignore

# auto_1.mostrar_info()

# print(auto_1.__velocidad)
# print(auto_1._Automovil__velocidad) # type: ignore

# print(auto_1.__dict__)  # Muestra los atributos del objeto


# auto_1.mostrar_info()
# print()
# auto_1.encender()
# print()
# auto_1.mostrar_info()
# print()
# auto_1.apagar()
# print()
# auto_1.mostrar_info()


# auto_1.mostrar_info()
# auto_1.acelerar(-10)
# auto_1.acelerar(5)
# auto_1.encender()
# auto_1.acelerar(5)
# auto_1.acelerar(10)
# auto_1.acelerar(15)
# auto_1.frenar(15)
# auto_1.frenar(45)

# auto_1.encender()
# auto_1.acelerar(5)
# auto_1.acelerar(10)
# print( auto_1.velocidad )   # getter

# auto_1.velocidad = 20       # setter
# print( auto_1.velocidad )

# Métodos de clase
# Queremos contar el número de autos creados
# 33%

# i = 1
# a1 = Automovil("Toyota", "Corolla", "Rojo")

# i += 1
# a2 = Automovil("Honda", "Civic", "Azul")

# i += 1
# a3 = Automovil("Ford", "Focus", "Blanco")

# print(f"Se han creado {i} autos")

# print(f"Se han creado {Automovil.cantidad_autos} autos (Métodos de clase)")

# print()
# Automovil.mostrar_mensaje()

# # Métodos estáticos
# # Validar patente
# print()
# print( f"Patente actual: {a1.patente}" )
# a1.patente = "ABC123"    ## Asignamos la nueva patente
# print( f"Nueva patente: {a1.patente}" )

# print( f"Patente actual: {a2.patente}" )
# a2.patente = "DE6"    ## Asignamos la nueva patente
# print( f"Nueva patente: {a2.patente}" )


# -- - ---------------------------------------------------------
# -- - Herencia

tesla_s = AutoElectrico("Tesla", "Model S", "Negro", 500)
tesla_s.encender()
tesla_s.acelerar(10)
tesla_s.mover()
