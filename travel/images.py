"""
Name of File: travel/images.py
Brief description of the file: get image query to be searched, and then return the url of those images by using the Google Search API
Inputs: image query
Outputs: print image url
"""

from google_images_search import GoogleImagesSearch
import json

def get_location_images(query, num_images=3):
    #load up credentials file that has api keys
    with open("credentials.json") as f:
        #get credentials from json
        credentials = json.load(f)

    # Set up Google Images Search API with the proper keys
    gis = GoogleImagesSearch(credentials["google_images_api"], credentials["google_images_cx"])

    # Define the search query paremeters
    _search_params = {
        'q': query,
        'num': num_images,
        'safe': 'high',
        'fileType': 'jpg',
    }

    # Search for images
    gis.search(search_params=_search_params)

    #List that stores image urls
    image_urls = []
    #Loop through each image result
    for i, image in enumerate(gis.results()):
        #If i >= num_images, it means we have grabbed all image urls we want
        if i >= num_images:
            #Stop iterating through the results
            break
        #Add the current image url to the image_urls list 
        image_urls.append(image.url)

    #Return the image_urls list
    return image_urls

#the following is used for debugging purposes
if __name__ == "__main__":
    location_query = input("Enter the location to search for: ")
    get_location_images(location_query)
