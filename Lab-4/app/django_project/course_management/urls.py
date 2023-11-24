from django.urls import path 
from .views import now_playing_movies, index

app_name = "movies"

urlpatterns = [
    path ('', index, name ='index'),

    path('now_playing_movies/', now_playing_movies, name='now_playing_movies')
]