cursos = [
    {"id": 1, "nombre": "Python"},
    {"id": 2, "nombre": "SQL"},
    {"id": 3, "nombre": "Django"},
]

def main():
    for curso in cursos:
        print(curso["nombre"])

if __name__ == "__main__":
    main()



# Flujo de trabajo hasta hoy
# usuario -> terminal -> python -> procesa algo


# Flujo de aplicación web
# usuario -> navegador -> servidor web -> python -> respuesta -> navegador

# python -m venv nombre_del_entorno
