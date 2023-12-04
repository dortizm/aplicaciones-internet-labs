from django.shortcuts import render, redirect, get_object_or_404
from .models import Asignatura, Alumno
from .forms import AsignaturaForm, AlumnoForm

def index(request):
    asignaturas = Asignatura.objects.all()
    alumnos = Alumno.objects.all()
    return render(request, 'index.html', {'asignaturas': asignaturas, 'alumnos': alumnos})

def lista_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'lista_asignaturas.html', {'asignaturas': asignaturas})

def crear_asignatura(request):
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_asignaturas')
    else:
        form = AsignaturaForm()
    return render(request, 'crear_asignatura.html', {'form': form})

def editar_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, pk=asignatura_id)
    if request.method == 'POST':
        form = AsignaturaForm(request.POST, instance=asignatura)
        if form.is_valid():
            form.save()
            return redirect('lista_asignaturas')
    else:
        form = AsignaturaForm(instance=asignatura)
    return render(request, 'editar_asignatura.html', {'form': form, 'asignatura': asignatura})

def eliminar_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, pk=asignatura_id)
    if request.method == 'POST':
        asignatura.delete()
        return redirect('lista_asignaturas')
    return render(request, 'eliminar_asignatura.html', {'asignatura': asignatura})

def lista_alumnos_asignatura(request, asignatura_id):
    asignatura = Asignatura.objects.get(pk=asignatura_id)
    alumnos = asignatura.alumnos.all()
    return render(request, 'lista_alumnos_asignatura.html', {'asignatura': asignatura, 'alumnos': alumnos})

def inscribir_alumno(request, asignatura_id):
    asignatura =get_object_or_404(Asignatura, pk=asignatura_id)
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save()
            asignatura.alumnos.add(alumno)
            return redirect('lista_alumnos_asignatura', asignatuta_id=asignatura.id)
        else:
            form = AlumnoForm()
        return render(request, 'inscribir_alumno.html', {'form': form, 'asignatura': asignatura})
    