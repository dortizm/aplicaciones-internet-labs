import json
import urllib.request
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    api_key = "c4ab6bd505b68822b549cd53ec9fe2bc"
    url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}&language=en-US&page=1"

    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())

        movie_list = data["results"]
        '''for movie in data.get('results', []):
            movie_info = {
                'title': movie.get('title', 'No Title'),
                'overview': movie.get('overview', 'No Overview Available'),
                'poster_path': movie.get('poster_path', ''),
            }
            movie_list.append(movie_info)'''

        return render(request, 'index.html', {'movie_list': movie_list})
    except urllib.error.URLError as e:
        return HttpResponse(f"Error en la solicitud a la API: {str(e)}")
