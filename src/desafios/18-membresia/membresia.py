from abc import ABC, abstractmethod


class Membresia(ABC):

    def __init__(self, correo_suscriptor, numero_tarjeta):
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta

    @property
    def correo_suscriptor(self):
        return self.__correo_suscriptor

    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta

    @abstractmethod
    def cambiar_suscripcion(self, tipo_nuevo):
        pass

    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 1:
            return Basico(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)


class Gratis(Membresia):
    costo = 0
    max_dispositivos = 1

    def cambiar_suscripcion(self, tipo_nuevo):
        if tipo_nuevo in (1, 2, 3, 4):
            return self._crear_nueva_membresia(tipo_nuevo)
        return self


class Basico(Membresia):
    costo = 3000
    max_dispositivos = 2

    def cambiar_suscripcion(self, tipo_nuevo):
        if tipo_nuevo in (2, 3, 4):
            return self._crear_nueva_membresia(tipo_nuevo)
        return self

    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)


class Familiar(Basico):
    costo = 5000
    max_dispositivos = 5

    def __init__(self, correo_suscriptor, numero_tarjeta, dias_regalo = 7):
        Membresia.__init__(self, correo_suscriptor, numero_tarjeta)
        self.__dias_regalo = dias_regalo

    def cambiar_suscripcion(self, tipo_nuevo):
        if tipo_nuevo in (1, 3, 4):
            return self._crear_nueva_membresia(tipo_nuevo)
        return self

    def modificar_control_parental(self):
        pass


class SinConexion(Basico):
    costo = 3500
    max_dispositivos = 2

    def __init__(self, correo_suscriptor, numero_tarjeta, dias_regalo = 7):
        Membresia.__init__(self, correo_suscriptor, numero_tarjeta)
        self.__dias_regalo = dias_regalo

    def cambiar_suscripcion(self, tipo_nuevo):
        if tipo_nuevo in (1, 2, 4):
            return self._crear_nueva_membresia(tipo_nuevo)
        return self

    def incrementar_max_descargas(self):
        pass


class Pro(Familiar, SinConexion):
    costo = 7000
    max_dispositivos = 6

    def __init__(self, correo_suscriptor, numero_tarjeta, dias_regalo = 15):
        Membresia.__init__(self, correo_suscriptor, numero_tarjeta)
        self.__dias_regalo = dias_regalo

    def cambiar_suscripcion(self, tipo_nuevo):
        if tipo_nuevo in (1, 2, 3):
            return self._crear_nueva_membresia(tipo_nuevo)
        return self
