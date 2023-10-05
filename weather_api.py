# api key 0e0b06d4b52348fe93b152402230510 
import requests

def weather(city: str):
    url = 'https://api.weatherapi.com/v1/current.json?key=0e0b06d4b52348fe93b152402230510 &q='+ city +'&aqi=no'

    x = requests.get(url)

    if x.status_code == 200:
        # Access the JSON data using .json()
        weather_data = x.json()
        print(weather_data['location']['name'])
    else:
        print('Failed to retrieve data. Status code:', x.status_code)