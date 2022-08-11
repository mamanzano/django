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

    lista = ['Futbol', 'Basquetball', 'volleyball']
    li = ''

    for element in lista:
        li = li + '<li>' + element + '</li>' + ' '
    
    return render(request, 'index.html')

def saludo_app(request):
    return HttpResponse(layout + '''
        <h1> Hola, este es mi primer despligue con django </h1>
        <h3> Soy Mario M </h3>
    ''')

def contacto(request, nombre=None, apellidos=None):

    html = ''

    if nombre and apellidos:
        html = f'<p> {nombre} {apellidos} </p>'

    return HttpResponse(layout + '''
    <p> Nombre del contacto: </p>
    ''' + html)