from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('get_movies_by_genre/', views.your_ajax_view, name="get_movies_by_genre"),
]
