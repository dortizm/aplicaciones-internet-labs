from django.shortcuts import render
from django.http import JsonResponse
import requests

def index(request):
    try:
        # Obtener la lista de géneros desde la API
        genres_url = 'http://api.filmon.com/api/vod/genres'
        response = requests.get(genres_url)
        response.raise_for_status()  # Levanta una excepción en caso de error en la respuesta HTTP
        genres = response.json()

        return render(request, 'index.html', {'genres': genres})
    except requests.exceptions.RequestException as e:
        # Manejar errores de solicitud, por ejemplo, problemas de red
        return render(request, 'index.html', {'error_message': f'Error al obtener géneros: {e}'})

def get_movies_by_genre(request, genre_id):
    try:
        # Utilizar la ID del género para hacer la llamada a la API
        api_url = f'http://api.filmon.com/api/vod/search?genre={genre_id}'
        response = requests.get(api_url)
        response.raise_for_status()  # Levanta una excepción en caso de error en la respuesta HTTP
        movies = response.json()

        return JsonResponse({'movies': movies})
    except requests.exceptions.RequestException as e:
        # Manejar errores de solicitud, por ejemplo, problemas de red
        return JsonResponse({'error_message': f'Error al obtener películas: {e}'}, status=500)
    except ValueError as e:
        # Manejar errores al decodificar JSON, por ejemplo, si la respuesta no es un JSON válido
        return JsonResponse({'error_message': f'Error al procesar la respuesta JSON: {e}'}, status=500)
