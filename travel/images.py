from google_images_search import GoogleImagesSearch

def search_images(query, num_images=3):
    # Set up Google Images Search API
    gis = GoogleImagesSearch('', '')

    # Define the search query
    _search_params = {
        'q': query,
        'num': num_images,
        'safe': 'high',
        'fileType': 'jpg',  # You can change this based on your preference
    }

    # Search for images
    gis.search(search_params=_search_params)

    # Download or print image URLs
    for image in gis.results():
        print("Image URL:", image.url)
        # If you want to download the image, you can use a library like requests or urllib
        # For example, using requests:
        # response = requests.get(image.url)
        # with open(f'{query}_image_{image.index}.jpg', 'wb') as f:
        #     f.write(response.content)

if __name__ == "__main__":
    location_query = input("Enter the location to search for: ")
    search_images(location_query)
