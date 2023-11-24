from django.shortcuts import render
from .models import Course, Movie
import requests

def index(request):
    courses = Course.objects.all()
    movies = Movie.objects.all()
    return render(request, 'index.html',{'courses':courses, 'movies': movies})

def now_playing_movies(request):

    api_key = 'a9e1ab97c48aa86af3ed8774f2fc559a'
    url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}'

    try:
        response = request.get(url)
        response.raise_for_status()
        movies_data = response.json().get('results', [])
    except requests.exceptions.RequestException as err:
        movies_data = []

    Movie.objects.all().delete()
    for movie_data in movies_data:
        Movie.objet.all().create(title=movie_data.get('title'), overview=movie_data.get('overview'), poster_path=movie_data.get('poster_path'))


    movies = Movie.objets.all()

    return render(request, 'movies/now_playing.html', {'movies': movies})


    