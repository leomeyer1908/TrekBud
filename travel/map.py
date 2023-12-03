"""
Name of File: travel/map.py
Brief description of the file: gets a location and searches for it with the Google API to retrieve a latitude and longitude for it
Inputs: location name
Outputs: latidude and logintude for a location
"""

import googlemaps

def search_location(api_key, location_query):
    #Initialize the Google Maps client
    gmaps = googlemaps.Client(key=api_key)

    #Perform a Places API text search
    places_result = gmaps.places(location_query)

    #If the the status of the request was OK and there were at least 1 result
    if places_result['status'] == 'OK' and len(places_result['results']) > 0:
        #get the first result and save it to place
        place = places_result['results'][0]
        #get the name of the result
        name = place['name'] 
        #get the address if avaialble
        address = place.get('formatted_address', 'Address not available')
        #get the location which includes both the latitude and longitude
        location = place['geometry']['location']

        #return the name, address, and the latitude, and longitude
        return name, address, location['lat'], location['lng']
    #if a region is not found, then return None
    else:
        return None

#the following is used for debugging purposes
if __name__ == "__main__":
    api_key = 'GOOGLE_MAPS_API_KEY'
    location_query = input("Enter the location to search for: ")
    print(search_location(api_key, location_query))
