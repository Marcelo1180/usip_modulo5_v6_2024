from django.http import HttpResponse
from django.shortcuts import render
from .models import Categoria


def index(request):
    return HttpResponse("Hello World")

def contact(request, name):
    return HttpResponse(f"Hello {name}")

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, "categorias.html", {
        "categorias": categorias
    })