# weatherapp/api.py
import requests

def get_weather(region, travel_duration):
    api_key = '21cd681675a5b34b9a8b33e7b847f14b'
    base_url = 'https://api.openweathermap.org/data/2.5/forecast'

    # Construct the API URL based on region (city) and travel duration (in hours)
    params = {
        'q': region,
        'appid': api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
