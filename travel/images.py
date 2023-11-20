"""
Name of File: travel/images.py
Brief description of the file: get image query to be searched, and then return the url of those images by using the Google Search API
Inputs: image query
Outputs: print image url
"""

from google_images_search import GoogleImagesSearch

def get_location_images(query, num_images=3):
    # Set up Google Images Search API with the proper keys
    gis = GoogleImagesSearch('', '')

    # Define the search query paremeters
    _search_params = {
        'q': query,
        'num': num_images,
        'safe': 'high',
        'fileType': 'jpg',
    }

    # Search for images
    gis.search(search_params=_search_params)

    # loop through each image from the results
    for image in gis.results():
        #Right now we are only printing the image URL, but in the next sprint we will display it
        print("Image URL:", image.url)

#the following is used for debugging purposes
if __name__ == "__main__":
    location_query = input("Enter the location to search for: ")
    get_location_images(location_query)
