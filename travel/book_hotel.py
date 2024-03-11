"""
Name of File: travel/book_hotel.py
Brief description of the file: has function that creates a hotels.com url based on the location given by the user 
Inputs: Takes a region
Outputs: returns a url
"""

from urllib.parse import quote
from datetime import datetime, timedelta

# Function to generate hotels.com URL
def generate_hotel_url(destination_location):
    # Get the current date
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Get the date one week from now
    one_week_from_now = (datetime.now() + timedelta(weeks=1)).strftime('%Y-%m-%d')

    #Return the kayak address associated with source and destination airports
    return f"https://www.hotels.com/Hotel-Search?destination={quote(destination_location)}&endDate={one_week_from_now}&startDate={current_date}"