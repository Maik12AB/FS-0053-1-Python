from abc import ABC, abstractmethod

from error import SubTipoInvalidoError

class Anuncio(ABC):

    FORMATO: str = ""
    SUB_TIPOS: tuple[str, ...] = ()

    def __init__(
        self,
        ancho: int,
        alto: int,
        url_archivo: str,
        url_clic: str,
        sub_tipo: str,
    ) -> None:
        self.ancho = ancho
        self.alto = alto
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.sub_tipo = sub_tipo

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, nuevo_ancho: int) -> None:
        if nuevo_ancho > 0:
            self.__ancho = nuevo_ancho
        else:
            self.__ancho = 1

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, nuevo_alto: int) -> None:
        if nuevo_alto > 0:
            self.__alto = nuevo_alto
        else:
            self.__alto = 1

    @property
    def url_archivo(self) -> str:
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, nueva_url: str) -> None:
        self.__url_archivo = nueva_url

    @property
    def url_clic(self) -> str:
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, nueva_url: str) -> None:
        self.__url_clic = nueva_url

    @property
    def sub_tipo(self) -> str:
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, nuevo_sub_tipo: str) -> None:
        if nuevo_sub_tipo not in self.SUB_TIPOS:
            mensaje = (
                f"El subtipo '{nuevo_sub_tipo}' no es válido para anuncios "
                f"de tipo {self.FORMATO}. "
                f"Subtipos permitidos: {', '.join(self.SUB_TIPOS)}."
            )

            raise SubTipoInvalidoError(mensaje)

        self.__sub_tipo = nuevo_sub_tipo

    @abstractmethod
    def comprimir_anuncio(self) -> None:
        """Comprime el archivo asociado al anuncio."""

    @abstractmethod
    def redimensionar_anuncio(self) -> None:
        """Modifica las dimensiones del anuncio."""

    # Es un método abstracto porqie no depende del objeto
    # El imprime los formatos de los e tipos de anuncio
    # con sus subtipos
    @staticmethod
    def mostrar_formatos() -> None:
        """Muestra los formatos y subtipos disponibles."""

        # Objetos de cada tipo de anuncio
        clases_anuncio = (Video, Display, Social)

        for clase_anuncio in clases_anuncio:
            titulo = clase_anuncio.FORMATO.upper()

            print(f"{titulo}:")
            print("=" * (len(titulo) + 1))

            for sub_tipo in clase_anuncio.SUB_TIPOS:
                print(f"- {sub_tipo}")

            print()


class Video(Anuncio):
    """Anuncio de tipo video."""

    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(
        self,
        url_archivo: str,
        url_clic: str,
        sub_tipo: str,
        duracion: int,
    ) -> None:
        super().__init__(
            ancho=1,
            alto=1,
            url_archivo=url_archivo,
            url_clic=url_clic,
            sub_tipo=sub_tipo,
        )

        self.duracion = duracion

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, _: int) -> None:
        """
        Los anuncios de video siempre tienen ancho igual a 1.

        El valor recibido se ignora.
        """

        self.__ancho = 1

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, _: int) -> None:
        """
        Los anuncios de video siempre tienen alto igual a 1.

        El valor recibido se ignora.
        """

        self.__alto = 1

    @property
    def duracion(self) -> int:
        return self.__duracion

    @duracion.setter
    def duracion(self, nueva_duracion: int) -> None:
        if nueva_duracion > 0:
            self.__duracion = nueva_duracion
        else:
            self.__duracion = 5

    def comprimir_anuncio(self) -> None:
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self) -> None:
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


class Display(Anuncio):

    FORMATO = "Display"
    SUB_TIPOS = ("traditional", "native")

    def comprimir_anuncio(self) -> None:
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self) -> None:
        print(
            "REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY "
            "NO IMPLEMENTADO AÚN"
        )


class Social(Anuncio):
    """Anuncio para redes sociales."""

    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncio(self) -> None:
        print(
            "COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN"
        )

    def redimensionar_anuncio(self) -> None:
        print(
            "REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN"
        )
