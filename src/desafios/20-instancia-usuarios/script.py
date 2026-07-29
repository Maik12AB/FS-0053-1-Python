import json
from usuario import Usuario

def main():

    usuario = []
    cuenta = 0

    with open("src/desafios/20-instancia-usuarios/data/usuarios.txt", "r", encoding="utf-8") as f:
        for linea in f:
            try:
                cuenta += 1
                dato = json.loads(linea)
                nuevo_usuario = Usuario(**dato)
                usuario.append(nuevo_usuario)
            except Exception as e:
                with open("src/desafios/20-instancia-usuarios/error.log", "a") as log:
                    log.write(f"Error: {e}\n")

    print( f"Filas importadas: {len(usuario):,} / {cuenta:,}")
    print("Detalles")
    for item in usuario:
        print( item )

if __name__ == '__main__':
    main()
