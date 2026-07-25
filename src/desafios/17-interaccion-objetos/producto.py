
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.stock = stock

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        self._stock = valor if valor >= 0 else 0

    def __eq__(self, otro):
        return self.__nombre == otro.__nombre

    def __add__(self, otro):
        return Producto(self.__nombre, self.__precio, self._stock + otro._stock)

    def __sub__(self, cantidad):
        nuevo_stock =  self._stock - cantidad.stock
        return Producto(self.__nombre, self.__precio, nuevo_stock)
