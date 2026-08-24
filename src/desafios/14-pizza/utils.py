def tiempo(tipo_ingre: set) -> int:
    """
    Calcula el tiempo de coción de una pizza \n
    20 minutos de base \n
    +2 por cada ingrediente \n
    No se incluye tiempo por tipo de masa o tipo de salsa \n
    """

    t = 20 + (2 * len(tipo_ingre))
    return t
