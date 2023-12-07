
import requests
from django.shortcuts import render

def get_now_playing_movies(api_key):
    url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}&language=es-US&page=1'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def index(request):
    api_key = '93a44cbb9c891dfed032b92768cf1f56'  
    movies_data = get_now_playing_movies(api_key)
    if movies_data:
        return render(request, 'index.html', {'movies': movies_data['results']})
    else:
        return render(request, 'index.html', {'movies': []})
