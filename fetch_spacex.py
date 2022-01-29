from pathlib import Path

import requests
from dotenv import load_dotenv


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v3/launches"
    response = requests.get(url)
    response.raise_for_status()
    images = response.json()[35]['links']['flickr_images']
    for number, image in enumerate(images):
        download_image(image, f'spacex{number}.jpg')


def download_image(url, file_name, params={}):
    Path("images").mkdir(parents=True, exist_ok=True)
    file_path = f'images/{file_name}'

    response = requests.get(url, params)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)


if __name__ == "__main__":
    fetch_spacex_last_launch()
