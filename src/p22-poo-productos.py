
class Producto():

    # Cuando se requiere enviar valores a la clase
    # la definición debe estar en el constructor
    # en Python el constructor es un método
    # __init__(self)
    def __init__(self, nombre: str, precio: int, stock: int) -> None:
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.error = ''

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio

    def get_stock(self):
        return self.stock

    def vender(self, u: int):
        if self.stock < u:
            self.error = "No tenemos unidades suficientes"
            return False

        self.stock -= u
        return True


#datos = archivo_txt o base_de_datos
# for item in datos:
#     pelota = Producto(item[1], item[2], item[3])

pelota = Producto("Pelota de futbol", 20, 5)

print('-' * 30)
print( f"Nombre del producto: {pelota.get_nombre()}" )
print( f"Precio: {pelota.get_precio()}" )
print( f"Stock disponible: {pelota.get_stock()}" )
print('-' * 30)
unidades = int(input("Unidades a ser vendidas: "))

if pelota.vender(unidades):
    print("Venta realizada correctamente")
else:
    print( f"No se puede realizar la venta por -> {pelota.error}")

print('-' * 30)
print( f"Nombre del producto: {pelota.get_nombre()}" )
print( f"Precio: {pelota.get_precio()}" )
print( f"Stock disponible: {pelota.get_stock()}" )
print('-' * 30)

