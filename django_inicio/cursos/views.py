from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

def get_cursos():
    return [
        {"id": 1, "nombre": "Python", "uuid": "488b0a66-20f7-45ee-87ef-941675592dff"},
        {"id": 2, "nombre": "SQL", "uuid": "1a8cf5f4-20e1-4b38-b586-9d324f45c4a5"},
        {"id": 3, "nombre": "Django", "uuid": "821eaf30-f6c6-486d-b120-32bdae88ab40"},
    ]

def listado_cursos(request):
    cursos = get_cursos()

    context = {
        'cursos': cursos,
        'prueba': "Hola"
    }

    return render(
        request,
        'cursos/index.html',
        context
    )

def detalles_cursos(request, uuid):
    print(uuid)
    cursos = get_cursos()
    r = 'Curso no encontrado'

    for curso in cursos:
        if str(curso['uuid']) == str(uuid):
            r = f"{curso['uuid']} - {curso['nombre']}"
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

