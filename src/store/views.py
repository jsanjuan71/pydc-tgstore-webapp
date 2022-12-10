from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hola desde django en el home")


def users(request):
    return HttpResponse("Hola esta es la pagina de usuarios")