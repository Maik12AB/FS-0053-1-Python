import uuid
from django.shortcuts import render, redirect
from django.contrib import messages

from cursos.models import Cursos

# Create your views here.
from django.http import HttpResponse, JsonResponse

cursos = [
        {"id": 1, "nombre": "Python", "uuid": "488b0a66-20f7-45ee-87ef-941675592dff"},
        {"id": 2, "nombre": "SQL", "uuid": "1a8cf5f4-20e1-4b38-b586-9d324f45c4a5"},
        {"id": 3, "nombre": "Django 6.1", "uuid": "821eaf30-f6c6-486d-b120-32bdae88ab40"},
    ]

def get_cursos():
    return Cursos.objects.all()

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

def detalles_cursos(request, parametro_uuid):
    cursos = Cursos.objects.get( uuid=parametro_uuid )

    context = {
        'detalle': cursos,
    }

    return render(
        request,
        'cursos/detalle.html',
        context
    )

def crear_cursos(request):
    print( 'Crear cursos' )

    if request.method == 'POST':
        nombre_curso = request.POST.get('nombre_curso', None)

        Cursos.objects.create(
            nombre = nombre_curso,
        )

        messages.success(request, "Curso creado.")

        return redirect('/cursos/')

    return render(
        request,
        'cursos/crear.html'
    )


"""
Ciclo de vida de la petición Http
---------------------------------
GET /cursos/ (Navegador)
app/urls.py --> cursos/
cursos/views.py --> listado_cursos()
HttpResponse
Navegador
"""

