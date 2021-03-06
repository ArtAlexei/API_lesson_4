from pathlib import Path

import requests
from dotenv import load_dotenv

from download import download_image


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v3/launches"
    response = requests.get(url)
    response.raise_for_status()
    images = response.json()[35]['links']['flickr_images']
    Path("images").mkdir(parents=True, exist_ok=True)
    for number, image in enumerate(images):
        download_image(image, f'spacex{number}.jpg')


if __name__ == "__main__":
    fetch_spacex_last_launch()
