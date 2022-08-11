from django.shortcuts import render, HttpResponse

# Create your views here.


def saludo_app(request):
    return HttpResponse('''
        <h1> Hola, este es mi primer despligue con django </h1>
        <h3> Soy Mario M </h3>
    ''')
