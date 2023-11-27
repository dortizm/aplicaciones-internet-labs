import json
import urllib.request
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import GenreForm

def index(request):
    api_key = "c4ab6bd505b68822b549cd53ec9fe2bc"
    url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}&language=en-US&page=1"

    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())
        movie_list = data["results"]

        # Obtener géneros de películas
        genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
        genre_response = urllib.request.urlopen(genre_url)
        genre_data = json.loads(genre_response.read().decode())
        genres = [(g['id'], g['name']) for g in genre_data['genres']]

        genre_form = GenreForm(genres=genres)
        return render(request, 'index.html', {'movie_list': movie_list, 'genre_form': genre_form})
    except urllib.error.URLError as e:
        return HttpResponse(f"Error en la solicitud a la API: {str(e)}")

def your_ajax_view(request):
    api_key = "c4ab6bd505b68822b549cd53ec9fe2bc"
    genre = request.GET.get('genre')
    genre_movies_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=en-US&with_genres={genre}"

    try:
        response = urllib.request.urlopen(genre_movies_url)
        data = json.loads(response.read().decode())
        movie_list = data["results"]
        return JsonResponse({'movies': movie_list})
    except urllib.error.URLError as e:
        return JsonResponse({'error': str(e)}, status=500)