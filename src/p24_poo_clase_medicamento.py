class Medicamento():

    def __init__(self, nombre: str = '', stock: int = 0):
        self.IVA = 0.18
        self.precio = 0
        self.descuento = 0.0
        self.nombre = nombre
        self.stock = stock
        self.precio_bruto = 0
        self.precio_neto = 0

    @staticmethod
    def validar_mayor_a_cero(numero: int) -> bool:
        return (numero > 0)

    @staticmethod
    def cal_descuento(precio: int) -> float:
        if precio >= 10_000 and precio < 20_000:
            descuento = 0.1
        elif precio >= 20_000:
            descuento = 0.2
        else:
            descuento = 0.0

        return descuento

    def asignar_precio(self, precio_entregado: int) -> bool:

        if self.validar_mayor_a_cero(precio_entregado):
            self.precio = precio_entregado

            # Definir descuento
            self.descuento = self.cal_descuento(precio_entregado)

            # Calcular el neto
            self.precio_neto = int(self.precio - (self.precio * self.descuento))

            iva = int(self.precio_neto * self.IVA)

            self.precio_bruto = int(self.precio_neto + iva)

            return True
        else:
            # Nuevo tratamiento del error
            # Se valida en el objeto en momento de ejecución si el método
            # devuelve False
            # print( f"El precio: {precio_entregado} no es un precio valido" )

            return False
