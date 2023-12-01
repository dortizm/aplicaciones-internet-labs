from django.shortcuts import render
import requests

def index(request):
    # Obtén el género seleccionado 
    selected_genre = request.GET.get('genres', '')

    # Lógica para consumir la API de Filmon 
    api_url = 'http://api.filmon.com/api/vod/search'
    params = {'genre': selected_genre}

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  
        movie_data = response.json()
    except requests.RequestException as e:
        
        return render(request, 'error.html', {'error_message': f'Error al obtener datos de la API: {str(e)}'})

  
    return render(request, 'index.html', {'movie_data': movie_data})
