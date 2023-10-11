# api key 0e0b06d4b52348fe93b152402230510 
import requests

def weather(city: str):
    url = 'https://api.weatherapi.com/v1/current.json?key=0e0b06d4b52348fe93b152402230510 &q='+ city +'&aqi=no'

    x = requests.get(url)

    if x.status_code == 200:
        # Access the JSON data using .json()
        weather_data = x.json()
        print(weather_data) 
    else:
        print('Failed to retrieve data. Status code:', x.status_code)

def temperature(city):
    url = 'https://api.weatherapi.com/v1/current.json?key=0e0b06d4b52348fe93b152402230510 &q='+ city[0] +'&aqi=no'

    x = requests.get(url)

    if x.status_code == 200:
        # Access the JSON data using .json()
        weather_data = x.json()
        return [f"{weather_data['current']['temp_f']}° Fahrenheit"]
    else:
        return ["Not a valid place"]
    
def updated(city):
    url = 'https://api.weatherapi.com/v1/current.json?key=0e0b06d4b52348fe93b152402230510 &q='+ city[0] +'&aqi=no'

    x = requests.get(url)

    if x.status_code == 200:
        # Access the JSON data using .json()
        weather_data = x.json()
        return [f"Weather in {city[0]} last updated on: {weather_data['current']['last_updated']} (local time zone)"]
    else:
        return ["Not a valid place"]
    
def cond(city):
    url = 'https://api.weatherapi.com/v1/current.json?key=0e0b06d4b52348fe93b152402230510 &q='+ city[0] +'&aqi=no'

    x = requests.get(url)

    if x.status_code == 200:
        # Access the JSON data using .json()
        weather_data = x.json()
        return [f"The current condition in {city[0]} is: {weather_data['current']['condition']['text']}"]
    else:
        return ["Not a valid place"]
    
def wind_speed(city):
    url = 'https://api.weatherapi.com/v1/current.json?key=0e0b06d4b52348fe93b152402230510 &q='+ city[0] +'&aqi=no'

    x = requests.get(url)

    if x.status_code == 200:
        # Access the JSON data using .json()
        weather_data = x.json()
        return [f"The current wind speed in {city[0].capitalize()} is: {weather_data['current']['wind_mph']}mph"]
    else:
        return ["Not a valid place"]
    
def wind_deg(city):
    url = 'https://api.weatherapi.com/v1/current.json?key=0e0b06d4b52348fe93b152402230510 &q='+ city[0] +'&aqi=no'

    x = requests.get(url)

    if x.status_code == 200:
        # Access the JSON data using .json()
        weather_data = x.json()
        return [f"The current wind degree in {city[0].capitalize()} is: {weather_data['current']['wind_degree']}°"]
    else:
        return ["Not a valid place"]
    
def wind_dir(city):
    url = 'https://api.weatherapi.com/v1/current.json?key=0e0b06d4b52348fe93b152402230510 &q='+ city[0] +'&aqi=no'

    x = requests.get(url)

    if x.status_code == 200:
        # Access the JSON data using .json()
        weather_data = x.json()
        return [f"The current wind direction in {city[0].capitalize()} is: {weather_data['current']['wind_dir']}"]
    else:
        return ["Not a valid place"]
    
def precip(city):
    url = 'https://api.weatherapi.com/v1/current.json?key=0e0b06d4b52348fe93b152402230510 &q='+ city[0] +'&aqi=no'

    x = requests.get(url)

    if x.status_code == 200:
        # Access the JSON data using .json()
        weather_data = x.json()
        return [f"The current precipitation in {city[0].capitalize()} is: {weather_data['current']['precip_in']} inches"]
    else:
        return ["Not a valid place"]
    
def feels(city):
    url = 'https://api.weatherapi.com/v1/current.json?key=0e0b06d4b52348fe93b152402230510 &q='+ city[0] +'&aqi=no'

    x = requests.get(url)

    if x.status_code == 200:
        # Access the JSON data using .json()
        weather_data = x.json()
        return [f"The current feels like in {city[0].capitalize()} is: {weather_data['current']['feelslike_f']}° Fahrenheit"]
    else:
        return ["Not a valid place"]
    
def vis(city):
    url = 'https://api.weatherapi.com/v1/current.json?key=0e0b06d4b52348fe93b152402230510 &q='+ city[0] +'&aqi=no'

    x = requests.get(url)

    if x.status_code == 200:
        # Access the JSON data using .json()
        weather_data = x.json()
        return [f"The current visibility in {city[0].capitalize()} is: {weather_data['current']['vis_miles']} miles"]
    else:
        return ["Not a valid place"]
    
def uv(city):
    url = 'https://api.weatherapi.com/v1/current.json?key=0e0b06d4b52348fe93b152402230510 &q='+ city[0] +'&aqi=no'

    x = requests.get(url)

    if x.status_code == 200:
        # Access the JSON data using .json()
        weather_data = x.json()
        return [f"The current uv in {city[0].capitalize()} is: {weather_data['current']['uv']}"]
    else:
        return ["Not a valid place"]
    
def gust(city):
    url = 'https://api.weatherapi.com/v1/current.json?key=0e0b06d4b52348fe93b152402230510 &q='+ city[0] +'&aqi=no'

    x = requests.get(url)

    if x.status_code == 200:
        # Access the JSON data using .json()
        weather_data = x.json()
        return [f"The current gust in {city[0].capitalize()} is: {weather_data['current']['gust_mph']}mph"]
    else:
        return ["Not a valid place"]
    
def aqi(city):
    url = 'https://api.weatherapi.com/v1/current.json?key=0e0b06d4b52348fe93b152402230510 &q='+ city[0] +'&aqi=yes'

    x = requests.get(url)

    if x.status_code == 200:
        # Access the JSON data using .json()
        weather_data = x.json()
        return [f"The current air quality index in {city[0].capitalize()} is: {weather_data['current']['air_quality']['us-epa-index']} (Measured by the EPA)"]
    else:
        return ["Not a valid place"]

def all(city):
    return [updated(city)[0], temperature(city)[0], cond(city)[0], wind_speed(city)[0], wind_deg(city)[0], wind_dir(city)[0], precip(city)[0], feels(city)[0], vis(city)[0], uv(city)[0], gust(city)[0], aqi(city)[0]]