from typing import Any

# Any == str | int | float | bool | list | tuple ...

from anuncio import Anuncio, Display, Social, Video
from error import LargoExcedidoError


class Campaña:
    """Representa una campaña publicitaria compuesta por anuncios."""

    LARGO_MAXIMO_NOMBRE = 250

    def __init__(
        self,
        nombre: str,
        fecha_inicio: str,
        fecha_termino: str,
        anuncios: list[dict[str, Any]] | tuple[dict[str, Any], ...],
    ) -> None:
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino

        self.__anuncios: list[Anuncio] = []
        self.__crear_anuncios(anuncios)

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if len(nuevo_nombre) > self.LARGO_MAXIMO_NOMBRE:
            mensaje = (
                "El nombre de la campaña no puede superar los "
                f"{self.LARGO_MAXIMO_NOMBRE} caracteres."
            )

            raise LargoExcedidoError(mensaje)

        self.__nombre = nuevo_nombre

    @property
    def fecha_inicio(self) -> str:
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, nueva_fecha: str) -> None:
        self.__fecha_inicio = nueva_fecha

    @property
    def fecha_termino(self) -> str:
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, nueva_fecha: str) -> None:
        self.__fecha_termino = nueva_fecha

    @property
    def anuncios(self) -> list[Anuncio]:
        """
        Entrega una copia de la lista.

        Esto evita que la lista interna sea reemplazada o modificada
        directamente desde fuera de la clase.
        """

        return self.__anuncios.copy()

    def __crear_anuncios(
        self,
        datos_anuncios: list[dict[str, Any]]
        | tuple[dict[str, Any], ...],
    ) -> None:
        for datos in datos_anuncios:
            anuncio = self.__crear_anuncio(datos)
            self.__anuncios.append(anuncio)

    def __crear_anuncio(self, datos: dict[str, Any]) -> Anuncio:
        tipo = datos["tipo"].strip().lower()

        if tipo == "video":
            return Video(
                url_archivo=datos["url_archivo"],
                url_clic=datos["url_clic"],
                sub_tipo=datos["sub_tipo"],
                duracion=datos["duracion"],
            )

        if tipo == "display":
            return Display(
                ancho=datos["ancho"],
                alto=datos["alto"],
                url_archivo=datos["url_archivo"],
                url_clic=datos["url_clic"],
                sub_tipo=datos["sub_tipo"],
            )

        if tipo == "social":
            return Social(
                ancho=datos["ancho"],
                alto=datos["alto"],
                url_archivo=datos["url_archivo"],
                url_clic=datos["url_clic"],
                sub_tipo=datos["sub_tipo"],
            )

        raise ValueError(
            f"El tipo de anuncio '{datos['tipo']}' no está permitido."
        )

    def __str__(self) -> str:
        cantidad_video = 0
        cantidad_display = 0
        cantidad_social = 0

        for anuncio in self.__anuncios:
            if isinstance(anuncio, Video):
                cantidad_video += 1
            elif isinstance(anuncio, Display):
                cantidad_display += 1
            elif isinstance(anuncio, Social):
                cantidad_social += 1

        return (
            f"Nombre de la campaña: {self.nombre}\n"
            f"Anuncios: {cantidad_video} Video, "
            f"{cantidad_display} Display, "
            f"{cantidad_social} Social"
        )
