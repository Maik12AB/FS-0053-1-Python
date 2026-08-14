"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db.migrations import serializer
from django.urls import path
from django.http import HttpResponse, JsonResponse

def get_cursos():
    return [
        {"id": 1, "nombre": "Python"},
        {"id": 2, "nombre": "SQL"},
        {"id": 3, "nombre": "Django"},
    ]

def hello(request):
    # Podemos escribir directamente en la terminal
    # del servidor
    print('Hola mundo desde la terminal')
    return HttpResponse("Hello, world!")

def inicio_html(request):

    algo = '<h1>Hola, estamos en la url inicio/</h1>'
    algo += '<ul>'
    algo += '<li>Hola</li>'
    algo += '<li>Que tal!</li>'
    algo += '</ul>'

    return HttpResponse(algo)

def listado_cursos(request):
    cursos = get_cursos()
    print(cursos)

    algo = '<h1>Listado de cursos</h1>'
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


# [TODO] crear grupos de path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),
    path('inicio/', inicio_html),
    path('cursos/', listado_cursos),
]
