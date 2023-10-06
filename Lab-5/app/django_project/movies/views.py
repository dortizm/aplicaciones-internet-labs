from django.shortcuts import render
from .services import generate_request

def index(request):
    return render(request, 'index.html',{'generos':generate_request()}) #envia los generos como parametro al index.html