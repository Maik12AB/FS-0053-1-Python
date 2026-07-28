from abc import ABC, abstractmethod
from producto import Producto

# Una clase abstracta es una clase que no puede ser instanciada
# Es la plantilla para otras clases
class Tienda(ABC):
    def __init__(self, nombre, delivery):
        self.__nombre = nombre
        self.__delivery = delivery
        self.lista_productos = []

    @property
    def nombre(self):
        return self.__nombre

    def ingresar_producto(self, nombre, precio, stock = 0):

        producto_nuevo = Producto(nombre, precio, stock)

        i = self.buscar_producto(producto_nuevo)
        if i is None:
            self.lista_productos.append(producto_nuevo)
        else:
            self.lista_productos[i] = self.lista_productos[i] + producto_nuevo


    def buscar_producto(self, buscar: Producto) -> int | None:

        try:
            pos = self.lista_productos.index(buscar)
        except Exception:
            pos = None

        return pos

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self):
        pass


class Restaurante(Tienda):
    def listar_productos(self):
        salida = ""
        for producto in self.lista_productos:
            salida += f"- {producto.nombre} | ${producto.precio}\n"
        return salida

    def realizar_venta(self, nombre: str, cantidad: int):

        venta = Producto(nombre, 0, cantidad)
        i = self.buscar_producto(venta)

        if i is None:
            return "Producto no existe"

        return "Venta completada"


class Supermercado(Tienda):
    def listar_productos(self):
        salida = ""
        for producto in self.lista_productos:
            linea = f"- {producto.nombre} | ${producto.precio} | Stock: {producto.stock}"
            if producto.stock < 10:
                linea += " | Pocos productos disponibles"
            salida += linea + "\n"
        return salida

    def realizar_venta(self, nombre: str, cantidad: int):

        venta = Producto(nombre, 0, cantidad)
        i = self.buscar_producto(venta)

        if i is None:
            return "Producto no existe"
        elif self.lista_productos[i].stock == 0:
            return "No es posible vender 0 productos o productos negativos."
        elif self.lista_productos[i].stock < cantidad:
            aux = self.lista_productos[i].stock
            self.lista_productos[i].stock = 0
            return f"Venta completada. Solo se vendieron {aux} unidades"

        self.lista_productos[i] = self.lista_productos[i] - venta
        return "Venta completada"


class Farmacia(Tienda):

    def listar_productos(self):
        salida = ""
        for producto in self.lista_productos:
            linea = f"- {producto.nombre} | ${producto.precio}"
            if producto.precio > 15_000:
                linea += " | Envío gratis al solicitar este producto"
            salida += linea + "\n"
        return salida

    def realizar_venta(self, nombre: str, cantidad: int):

        if cantidad > 3:
            return "No se puede solicitar más de 3 unidades"

        venta = Producto(nombre, 0, cantidad)
        i = self.buscar_producto(venta)

        if i is None:
            return "Producto no existe"
        elif self.lista_productos[i].stock == 0:
            return "No es posible vender 0 productos o productos negativos."
        elif self.lista_productos[i].stock < cantidad:
            aux = self.lista_productos[i].stock
            self.lista_productos[i].stock = 0
            return f"Venta completada. Solo se vendieron {aux} unidades"

        self.lista_productos[i] = self.lista_productos[i] - venta
        return "Venta completada"

