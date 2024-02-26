import requests
from .map import search_location
from datetime import datetime, timedelta
from urllib.request import urlopen
from json import load


#function to get the coordinates of a user based on an ip address
def getCoordFromIp(addr=''):
    #if the ip address is none
    if addr == '':
        #return none
        return None
    #otherwise
    else:
        #if the current ip address is the localhost
        if addr == "127.0.0.1":
            #use university of Kansas's IP address for testing purposes
            addr = "129.237.91.0"
        #get the url for the ip address using this website as the api
        url = 'https://ipinfo.io/' + addr + '/json'
    #get the result json
    res = urlopen(url)
    #response from url(if res==None then check connection)
    data = load(res)
    #will load the json response into data
    return data["loc"]
        
# Function to get the IATA code from latitude and longitude
def get_iata_code(lat, lon):
    #get the url website that gives IATA codes from lat and lon
    url = f"https://iatageo.com/getCode/{lat}/{lon}"
    #get the response from it
    response = requests.get(url)
    #get the data from the response
    data = response.json()
    #return the code part which is the IATA from the url
    return data.get('code', None)

# Function to generate Kayak URL
def generate_kayak_url(google_api_key, user_ip_address, destination_location):
    #get the source locatino from the user ip address
    source_location = getCoordFromIp(user_ip_address)

    #get the source lat and source lon for the closest airport to the user
    _, _, source_lat, source_lon = search_location(google_api_key, f"international airports near {source_location}")
    #get the source lat and source lon for the closest airport to the destination
    _, _, dest_lat, dest_lon = search_location(google_api_key, f"international airports near {destination_location}")

    # Get the IATA codes for the nearest international airports
    source_iata = get_iata_code(source_lat, source_lon)
    dest_iata = get_iata_code(dest_lat, dest_lon)

    # Get the current date
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Get the date one week from now
    one_week_from_now = (datetime.now() + timedelta(weeks=1)).strftime('%Y-%m-%d')

    #Return the kayak address associated with source and destination airports
    return f"https://www.kayak.com/flights/{source_iata}-{dest_iata}/{current_date}/{one_week_from_now}?sort=bestflight_a"