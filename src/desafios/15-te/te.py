class Te:
    # Atributo de clase
    duracion = 365  # días

    @staticmethod
    def obtener_tiempo_y_recomendacion(sabor: int):
        """
        Sabor
        1 = Té negro. Tiempo 3 min
        2 = Té verde. Tiempo 5 min
        3 = Agua de hierbas. Tiempo 6 min
        """
        if sabor == 1:
            return 3, "Se recomienda consumir al desayuno"
        elif sabor == 2:
            return 5, "Se recomienda consumir al medio día"
        elif sabor == 3:
            return 6, "Se recomienda consumir al atardecer"
        else:
            return None, "Sabor inválido"

    @staticmethod
    def obtener_precio(formato: int):
        """
        Formato
        1 = 300gr -> $3.000
        2 = 500gr -> $5.000
        """
        if formato == 1:
            return 3_000
        elif formato == 2:
            return 5_000
        else:
            return None

# Otra manera de trabajar los sabores y los formatos
# más parecida a cuando recibamos desde la bbdd
"""
    @staticmethod
    def obtener_sabores() -> dict:
        return {
            '1': {
                    'nombre:': "Té negro",
                    'tiempo': '3',
                    'tipo_tiempo': 'min',
                    'nota': "Se recomienda consumir al desayuno"
                },
            '2': {
                    'nombre:': "Té verde",
                    'tiempo': '5',
                    'tipo_tiempo': 'min',
                    'nota': "Se recomienda consumir al medio día"
                },
            '3': {
                    'nombre:': "Agua de hierbas",
                    'tiempo': '6',
                    'tipo_tiempo': 'min',
                    'nota': "Se recomienda consumir al atardecer"
                }
        }

    @staticmethod
    def obtener_formato() -> dict:
        return {
                '1': '300gr',
                '2': '500gr'
            }
"""
