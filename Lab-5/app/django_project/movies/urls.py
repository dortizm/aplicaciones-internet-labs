from django.urls import path
from .views import index, get_movies_by_genre

urlpatterns = [
    path('', index, name="index"),
    path('get_movies/<int:genre_id>/', get_movies_by_genre, name='get_movies_by_genre'),
]
