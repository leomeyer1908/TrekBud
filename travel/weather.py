"""
Name of File: travel/weather.py
Brief description of the file: gets information about the weather for a specified region 
Inputs: region the user wants to see weather for
Outputs: weather information for a region
"""
# Import the 'requests' library to make HTTP requests
import requests
import json

# Import the 'datetime' module to work with date and time data, and 'timedelta' for time intervals
from datetime import datetime, timedelta

# Define a function 'get_weather' that retrieves weather data for a specific region and date range
def get_weather(region, start_date, end_date, unit):
    #load up credentials file that has api keys
    with open("credentials.json") as f:
        #get credentials from json
        credentials = json.load(f)
    # OpenWeatherMap API key
    api_key = credentials["openweathermap_api"]
    
    # Define the base URL for the OpenWeatherMap API
    base_url = 'https://api.openweathermap.org/data/2.5/forecast'

    # Calculate the end_date by adding one day to the user-provided end_date
    end_date = end_date + timedelta(days=1)

    # Format the start_date and end_date in the required format (YYYY-MM-DD HH:00:00)
    start_date_str = start_date.strftime('%Y-%m-%d 00:00:00')
    end_date_str = end_date.strftime('%Y-%m-d 00:00:00')

    # Construct the API URL with the specified region, dates, API key, and temperature unit
    params = {
        'q': region,       # Location or city name
        'start_date': start_date_str,  # Start date and time
        'end_date': end_date_str,      # End date and time
        'appid': api_key,              # Your API key
        'units': unit                  # Temperature unit (e.g., 'metric' for Celsius or 'imperial' for Fahrenheit)
    }

    # Send an HTTP GET request to the OpenWeatherMap API
    response = requests.get(base_url, params=params)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # If the response is successful, convert it to a Python dictionary
        data = response.json()
        # Return the weather data
        return data
    else:
        # If the response status code is not 200, return None to indicate an unsuccessful request
        return None
