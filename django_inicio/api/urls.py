from django.urls import path
from django.urls import include

from api.views import hello_v1, info_v1

urlpatterns = [
    path('v1/hola/', hello_v1),
    path('v1/info/', info_v1),
]
