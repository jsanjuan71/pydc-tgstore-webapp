from django.shortcuts import render

from django.http import HttpResponse

from .models import Product

# Create your views here.

def home(request):
    #return HttpResponse("Hola desde django en el home")
    return render(request, "index.html")

def products(request):
    productos__old = [
        {'nombre': "iPhone 12 rojo 128 GB", "precio": 15000, "ruta": "celular.webp"},
        {'nombre': "Tablet lenovo X", "precio": 1400, "ruta": "tablet.jpg"},
        {'nombre': "Bicileta Specialized Pro", "precio": 9500, "ruta": "bicicleta.webp"},
        {'nombre': "iPhone 12 rojo 128 GB", "precio": 15000, "ruta": "celular.webp"},
        {'nombre': "Tablet lenovo X", "precio": 1400, "ruta": "tablet.jpg"},
        {'nombre': "Bicileta Specialized Pro", "precio": 1000, "ruta": "bicicleta.webp"}
    ]
    products = Product.objects.all()
    print(products)


    nombre = "Juilo" #str
    datos = {"nombre": "julio"} #dict
    #datos.precio

    #productos[0].precio
    return render(request, "products.html", {'productos': products } )

def cart(request):
    return render(request, "cart.html")

def account(request):
    return render(request, "account.html")