from django.shortcuts import render
from .models import asingatura #se deben importar desde el models los modelos que usaremos
from .models import almuno	# tienen sus propias funciones como si usaramos una base de datos
from django.db.models import Count # este es un ejemplo de ello

def index(request):
	#con annotate sirve como el AS en sql (preguntar para confirmar)
	#el count sirve para contar en este caso contamos con los alumnos que tengan una asignatura (raro que no sea al reves)
	cant_alumnos = asingatura.objects.annotate(total_alumnos=Count('almuno'))
	return render(request, 'index.html',{'cantidad':cant_alumnos})

def asig(request):
	#if request.method == 'POST':
		#form = AsignaturaForm(request.POST)
		#if form.is_valid():
			#form.save()
			#return redirect('index')
		#else:
			#form = AsignaturaForm()
	return render(request, 'addAsig.html')
