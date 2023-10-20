from django import forms 
from .models import Alumno, Asignatura

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento']

class AsignaturaForm(forms.ModelForm):
    class Meta: 
        model = Asignatura
        fields = ['codigo', 'nombre']
        