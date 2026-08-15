from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

def get_cursos():
    return [
        {"id": 1, "nombre": "Python"},
        {"id": 2, "nombre": "SQL"},
        {"id": 3, "nombre": "Django"},
    ]

def listado_cursos(request):
    cursos = get_cursos()
    print(cursos)

    algo = '<h1>Listado de cursos (App Cursos)</h1>'
    algo += '<ul>'

    for curso in cursos:
        algo += f'<li>{curso["id"]} - {curso["nombre"]}</li>'
        print()

    algo += '</ul>'

    # Retornando un texto
    # return HttpResponse("Listado de cursos")

    # Retornar un json
    #return JsonResponse(cursos, safe=False)

    # Retornando HTML
    return HttpResponse(algo)

def detalles_cursos(request, id):
    cursos = get_cursos()
    r = 'Curso no encontrado'

    for curso in cursos:
        if curso['id'] == id:
            r = f"{curso['id']} - {curso['nombre']}"
            break

    return HttpResponse(r)

"""
Ciclo de vida de la petición Http
---------------------------------
GET /cursos/ (Navegador)
app/urls.py --> cursos/
cursos/views.py --> listado_cursos()
HttpResponse
Navegador
"""

