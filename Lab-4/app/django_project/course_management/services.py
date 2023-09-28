import requests

def generate_request():
    url = "https://moviesdatabase.p.rapidapi.com/titles/random"
    querystring = {"list":"most_pop_movies"}
    headers = {
	"X-RapidAPI-Key": "9937e1efffmsh697d9382ff77e08p16a91bjsn5a45b3d0ddf1",
	"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
        }
    
    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()