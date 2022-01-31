import datetime
import os
import urllib
from pathlib import Path

import requests
from dotenv import load_dotenv

from download import download_image


def fetch_nasa_epic_photos(nasa_api_key):
    params = {'api_key': nasa_api_key}
    url = 'https://api.nasa.gov/EPIC/api/natural'
    response = requests.get(url, params=params)
    response.raise_for_status()
    nasa_photos = response.json()

    for number, photo in enumerate(nasa_photos):
        photo_date = datetime.datetime.fromisoformat(photo['date'])
        photo_name = photo['image']
        formatted_date = photo_date.strftime("%Y/%m/%d")
        url = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{photo_name}.png'
        download_image(url, f'nasaepic{number}.png', params)


def fetch_nasa_apod_photos(nasa_api_key):
    params = {'api_key': nasa_api_key, 'count': 30}
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=params)
    response.raise_for_status()
    nasa_media = response.json()
    for number, media in enumerate(nasa_media):
        if media['media_type'] == 'image':
            file_name = f'nasa{number}{get_img_extension(media["url"])}'
            download_image(media['url'], file_name)


def get_img_extension(url):
    img_path = urllib.parse.urlsplit(url).path
    _, img_extension = os.path.splitext(img_path)
    return img_extension


def main():
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    Path("images").mkdir(parents=True, exist_ok=True)
    fetch_nasa_epic_photos(nasa_api_key)
    fetch_nasa_apod_photos(nasa_api_key)


if __name__ == "__main__":
    main()
