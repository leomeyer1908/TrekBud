"""
Name of File: travel/places.py
Brief description of the file: gets a place name, a place type (restaurant or attraction), and location, and returns the current logistical informations from that place
Inputs: place name, place type, location
Outputs: logistical information about the place
"""
import requests

#Function that gets place name, place type (restaurant or attraction), and location and returns logistical information about the place
def get_place_details(place_name, place_type, location, api_key):
    # Stage 1: Nearby Search

    # Define the Google Places (New) API endpoint for Place Search
    endpoint = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'

    # Define parameters for the API request
    params = {
        'input': f'{place_name} in {location}',
        'inputtype': 'textquery',
        'types': place_type,  # 'restaurant' or 'tourist_attraction'
        'key': api_key
    }

    # Make a request to the Places API
    response = requests.get(endpoint, params=params)
    data = response.json()

    # Check for successful response and results
    if data['status'] == 'OK' and data['candidates']:
        # Extract the place_id of the first result
        place_id = data['candidates'][0]['place_id']

        # Define the Places API endpoint for Place Details
        details_endpoint = 'https://maps.googleapis.com/maps/api/place/details/json'

        # Define parameters for the details request
        details_params = {
            'place_id': place_id,
            'key': api_key
        }

        # Make a request to the Place Details endpoint
        details_response = requests.get(details_endpoint, params=details_params)
        details_data = details_response.json()

        # Check for successful details response
        if details_data['status'] == 'OK':
            place = details_data['result']
            # Extract desired place details from the response
            place_details = {
                'name': place['name'],
                'address': place['formatted_address'],
                'rating': place.get('rating', 'N/A'),
                'total_ratings': place.get('user_ratings_total', 'N/A'),
                'business_status': place.get('business_status', 'N/A'),
                'website': place.get('website', 'N/A')
            }

            if 'opening_hours' in place:
                # Extract opening hours information
                opening_hours = place['opening_hours']
                if 'open_now' in opening_hours:
                    place_details['open_now'] = opening_hours['open_now']
                else:
                    place_details['open_now'] = 'N/A'

                if 'weekday_text' in opening_hours:
                    place_details['opening_hours'] = opening_hours['weekday_text']
                else:
                    place_details['opening_hours'] = 'N/A'
            else:
                place_details['open_now'] = 'N/A'
                place_details['opening_hours'] = 'N/A'


            return place_details
    else:
        return None
