from django.db import models

# Create your models here.
class Asignatura(models.Model):
    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    alumnos = models.ManyToManyField('Alumno', related_name='asignaturas')

    def __str__(self):
        return self.nombre
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
    