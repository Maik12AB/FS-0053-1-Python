from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def hello_v1(request):
    saludo = {
        'saludo': "Hola"
    }
    return JsonResponse(saludo)

def info_v1(request):
    info = {
        'method': request.method,
        'path': request.path
    }

    return JsonResponse(info)
