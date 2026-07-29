class DimensionError(Exception):

    def __init__(self, mensaje, dimension = None, maximo = None):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            return f"El mesaje es {self.mensaje} La dimensión es {self.dimension} El máximo es {self.maximo}"
