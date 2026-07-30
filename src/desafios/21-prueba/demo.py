from campaña import Campaña
from error import Error


datos_anuncios = (
    {
        "tipo": "Video",
        "url_archivo": "publicidad.mp4",
        "url_clic": "https://www.ejemplo.cl",
        "sub_tipo": "instream",
        "duracion": 30,
    },
)

campaña = Campaña(
    nombre="Campaña inicial",
    fecha_inicio="2026-08-01",
    fecha_termino="2026-08-31",
    anuncios=datos_anuncios,
)

print("Campaña antes de las modificaciones")
print(campaña)
print()

try:
    nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")
    nuevo_sub_tipo = input("Ingrese el nuevo subtipo del video: ")

    campaña.nombre = nuevo_nombre
    campaña.anuncios[0].sub_tipo = nuevo_sub_tipo

    campaña.anuncios[0].mostrar_formatos()

except Error as error:
    with open(
        "src/desafios/21-prueba/error.log",
        mode="a",
        encoding="utf-8",
    ) as archivo:
        archivo.write(f"{error}\n")

    print("Se produjo un error. Revise el archivo error.log.")

else:
    print()
    print("La campaña fue modificada correctamente.")
    print(campaña)
