from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('asignaturas/', views.lista_asignaturas, name='lista_asignaturas'),
    path('asignaturas/crear/', views.crear_asignatura, name='crear_asignatura'),
    path('asignaturas/editar/<int:asignatura_id>/', views.editar_asignatura, name='editar_asignatura'),
    path('asignaturas/eliminar/<int:asignatura_id>/', views.eliminar_asignatura, name='eliminar_asignatura'),
    path('asignaturas/alumnos/<int:asignatura_id>/', views.lista_alumnos_asignatura, name='lista_alumnos_asignatura'),
    path('asignaturas/inscribir-alumno/<int:asignatura_id>/', views.inscribir_alumno, name='inscribir_alumno'),
]

