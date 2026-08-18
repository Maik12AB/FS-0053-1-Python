from django.urls import path

from cursos.views import listado_cursos, detalles_cursos

# [TODO] crear grupos de path
urlpatterns = [
    path('', listado_cursos),
    path('<uuid:uuid>/', detalles_cursos),
]
