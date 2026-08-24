
class Clase1:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def hola(self):
        print( "Hola desde clase1" )

    def mostrar(self):
        ...

class Clase2:

    def __init__(self, nombre, apellido, correo = None):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def __str__(self):
        aux = self.nombre + " " + self.apellido

        if self.correo:
            aux = aux + " " + self.correo

        return aux

    def hola(self):
        print( "Hola desde clase2" )

    def grabar(self):
        ...

class Curso(Clase1, Clase2):

    def __init__(self, nombre, apellido, correo = None):
        # Constructor de la Clase1
        super().__init__(nombre, apellido)
        self.correo = correo

    def prueba(self):
        print("Hola")


print("Inicio")
obj = Curso("Carlos", "Soto", "algo@algo.com")
obj.prueba()
obj.hola()
print( obj )

# for item in obj.__dir__():
#     print( item )

print("Fin")


