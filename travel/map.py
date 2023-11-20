"""
Name of File: travel/map.py
Brief description of the file: gets a location and searches for it with the Google API to retrieve a latitude and longitude for it
Inputs: location name
Outputs: latidude and logintude for a location
"""

import googlemaps

def search_location(api_key, location_query):
    # Initialize the Google Maps client
    gmaps = googlemaps.Client(key=api_key)

    # Perform a Places API text search
    places_result = gmaps.places(location_query)

    # Extract information about the first result
    if places_result['status'] == 'OK' and len(places_result['results']) > 0:
        place = places_result['results'][0]
        name = place['name']
        address = place.get('formatted_address', 'Address not available')
        location = place['geometry']['location']

        return name, address, location['lat'], location['lng']
    else:
        return None

if __name__ == "__main__":
    api_key = 'GOOGLE_MAPS_API_KEY'
    location_query = input("Enter the location to search for: ")
    print(search_location(api_key, location_query))
