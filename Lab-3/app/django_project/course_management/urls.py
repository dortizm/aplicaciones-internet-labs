from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('addAsignatura/', views.asig, name="addAsig"),
]