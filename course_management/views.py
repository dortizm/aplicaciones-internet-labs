from django.shortcuts import render
from .models import Alumno
from .models import Asignatura

def lista_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    
    return render(request, 'lista_asignaturas.html', {'asignaturas': asignaturas})

def crear_asignatura(request):
    return render(request, 'crear_asignatura.html')

def detalle_asignatura(request):
    return render(request, 'detalle_asignatura.html')

def crear_alumno(request):
    return render(request, 'crear_alumno.html')

def lista_alumno(request):
    alumnos = Alumno.objects.all()
    
    return render(request, 'lista_alumno.html', {'alumnos': alumnos})

    
