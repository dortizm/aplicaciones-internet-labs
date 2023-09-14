from django.shortcuts import render
from .models import asingatura
from .models import almuno
from django.db.models import Count

def index(request):
	cant_alumnos = asingatura.objects.annotate(total_alumnos=Count('almuno'))
	return render(request, 'index.html',{'cantidad':cant_alumnos})

def asig(request):
	return render(request, 'addAsig.html')
