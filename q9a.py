import requests # pip install requests
import os

def download_xkcd_comics():
    # Create a folder to store the downloaded comics
    os.makedirs('xkcd_comics', exist_ok=True)

    url = 'https://xkcd.com/{}/info.0.json'
    comic_number = 1

    while True:
        # Make a request to get the JSON data for the current comic
        response = requests.get(url.format(comic_number))
        if response.status_code != 200:
            break

        comic_data = response.json()
        image_url = comic_data['img']
        image_title = comic_data['title']

        # Download the comic image
        response = requests.get(image_url)
        if response.status_code == 200:
            image_path = os.path.join('xkcd_comics', f'{comic_number}_{image_title}.png')
            with open(image_path, 'wb') as file:
                file.write(response.content)
                print(f'Downloaded: {comic_number}_{image_title}.png')

        comic_number += 1

# Test the program
download_xkcd_comics()
