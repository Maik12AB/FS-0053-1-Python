
# ¿Quiero que mi método de sumar() reciba
# los argumentos directamente o quiero
# que los lea desde los atributos de
# la clase?

# Métodos no static
from ast import Try


class CalculadoraNoStatic():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sumar(self):
        return self.a + self.b

# Métodos static
class CalculadoraStatic():

    @staticmethod
    def sumar(a, b):
        return a + b

# Métodos no static con argumentos directos
# sin pasar por el constructor
class CalculadoraNoStaticWithArg():

    def sumar(self, a, b):
        return a + b

# Métodos Mixtos
class CalculadoraMix():
    def __init__(self, a, b):
        self.a = self._validar_int(a)
        self.b = self._validar_int(b)

    def sumar(self):
        return self.a + self.b # type: ignore

    # este  método no puede ser static, porque necesito
    # invocar al método sumar()
    def imprimir_resultado_suma(self):
        print( self.sumar() )

    # Puede ser static porque no depende de
    # los métodos/atributos de la clase
    @staticmethod
    def _validar_int(valor):
        if type(valor) == int:
            return valor
        elif type(valor) == str:
            try:
                return int(valor)
            except:
                print(f"Valor no se puede convertir {valor} de tipo {type(valor)}")

        return None





#-- - -----------------------------------------
calc = CalculadoraNoStatic(10, 20)
print( calc.sumar() )

calc_static = CalculadoraStatic()
print( calc_static.sumar(10, 20) )

calc_no_static_with_arg = CalculadoraNoStaticWithArg()
print( calc_no_static_with_arg.sumar(10, 20) )

calc_mix = CalculadoraMix('10', 20)
print(calc_mix.sumar())