from django.urls import path

from cursos.views import (
    listado_cursos,
    detalles_cursos,
    crear_cursos,
    editar_cursos
)

# [TODO] crear grupos de path
urlpatterns = [
    path('', listado_cursos),
    path('crear/', crear_cursos),
    path('<uuid:parametro_uuid>/', detalles_cursos),
    path('<uuid:parametro_uuid>/editar/', editar_cursos),
]
