from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_asignaturas, name='lista_asignaturas'),
    path('crear_asignatura/', views.crear_asignatura, name='crear_asignatura'),
    path('detalle_asignatura/', views.detalle_asignatura, name='detalle_asignatura'),
    path('crear_alumno/',views.crear_alumno, name='crear_alumno'),
    path('lista_alumno/',views.lista_alumno, name= 'lista_alumno')
    ]
