import requests

def generate_request():
    url = "http://api.filmon.com/api/vod/search?genre=action"
    
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['response']