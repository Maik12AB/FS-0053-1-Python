
# Definición
class Pelota():
    forma = 'redondeada'    # Atributo/propiedad
    error = ''

    # Método
    def get_forma(self):
        return self.forma

    def set_forma(self, texto):
        if texto in ('redondeada', 'cuadrada', 'circular'):
            self.forma = texto
            return True

        self.error = f"El valor no se puede asignar: {texto}"
        return False

# Esto instanciando la clase
pelota_futbol = Pelota()

# pelota_futbol => Objeto

print( type(pelota_futbol) )    # <class '__main__.Pelota'>
print( pelota_futbol.forma )    # redondeada

# Cambiar el valor de una propiedad/atributo de clase
pelota_futbol.forma = 'Cuadrada'

# Llamando al atributo directamente
print( "Desde un atributo:", pelota_futbol.forma )

# Usando un método para obtener el valor
print( "Desde un método: ", pelota_futbol.get_forma() )

# Creamos un validador para asignar un valor a la
# propiedad format
if pelota_futbol.set_forma('redondeada'):
    print( "Todo bien", pelota_futbol.get_forma() )
else:
    print( 'ERROR', pelota_futbol.error)

if pelota_futbol.set_forma('triangular'):
    print( "Todo bien", pelota_futbol.get_forma() )
else:
    print( 'ERROR', pelota_futbol.error)
