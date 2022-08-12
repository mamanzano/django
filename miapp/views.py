from turtle import ht
from django.shortcuts import render, HttpResponse

# Create your views here.

layout = """
    <h1>Sitio Web con Django | Mario M </h1>
    </br>
    <ul>
        <li> <a href=/inicio> Inicio </a> </li>
        <li> <a href=/saludo-app> Saludo </a> </li>
        <li> <a href=/contacto> Contacto </a> </li>
    </ul>
    </br>
"""

def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request,'blog.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request,'projects.html')