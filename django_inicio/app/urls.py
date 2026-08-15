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
from django.urls import path
from django.http import HttpResponse

from cursos.views import listado_cursos, detalles_cursos

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

# Entendiendo request
def info_http(request):
    print( '-' * 20)
    print(request)
    print(request.method)
    print(request.path)
    print( '-' * 20)

    return HttpResponse("Hello, Info Http!")

# [TODO] crear grupos de path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),
    path('inicio/', inicio_html),
    path('cursos/', listado_cursos),
    path('cursos/<uuid:uuid>/', detalles_cursos),
    path('info-http/', info_http),
]
