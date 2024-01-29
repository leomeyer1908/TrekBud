"""
Name of File: travel/images.py
Brief description of the file: get image query to be searched, and then return the url of those images by using the Google Search API
Inputs: image query
Outputs: print image url
"""

from google_images_search import GoogleImagesSearch
from googleapiclient.errors import HttpError
import time
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

    #The following tries to search the images, but retries a certain number of times
    #because the Google API gives internal errors unrelated to this code sometimes.
    #Number of retries because API sometimes has internal error
    max_retries = 5
    #Delay in seconds between each retry
    retry_delay = 5
    #Retry loop
    for attempt in range(max_retries):
        try:
            #Attempt the search
            gis.search(search_params=_search_params)
            #If the search is successful, break out of the loop
            break
        except Exception as e:
            #Check if it's an HttpError and extract the internal error message
            if isinstance(e, HttpError):
                #Decode the response content to a string
                error_content = e.content.decode('utf-8')
                #Load the content as JSON
                error_details = json.loads(error_content)
                #Get the error message
                error_message = error_details['error']['message']
                #See if the error message was due to internal error
                if 'Internal error encountered.' in error_message:
                    #Print this to the console that we are going to try a new attempt
                    print(f"Attempt {attempt + 1} failed: {error_message}")
                    #If it's not the last attempt, wait before retrying
                    if attempt < max_retries - 1:
                        #wait the retry delay beefore retrying
                        time.sleep(retry_delay)
                    continue  # Retry the request
            #For other exceptions, raise the error
            raise

    else:
        #If all retries fail, raise an error
        raise Exception("All retry attempts failed")

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
