from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"index.html")

def base(request):
    return render(request,"base.html")

def reservacion(request):
    return render(request,"reservacion.html")

def promociones(request):
    return render(request,"promociones.html")

def recordatorios(request):
    return render(request,"recordatorios.html")

def inicio(request):
    return render(request,"inicio.html")
