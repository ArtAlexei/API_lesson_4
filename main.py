import datetime
import os
import time
import urllib
from pathlib import Path

import requests
import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    Path("images").mkdir(parents=True, exist_ok=True)
    default_delay = 60 * 60 * 24
    nasa_api_key = os.getenv("NASA_API_KEY", default_delay)
    telegram_api_key = os.getenv("TELEGRAM_API_KEY")
    posting_delay = os.getenv("POSTING_DELAY")
    dir_path = Path.cwd()

    fetch_spacex_last_launch()
    fetch_nasa_photos(nasa_api_key)
    fetch_nasa_epic_photos(nasa_api_key)

    bot = telegram.Bot(telegram_api_key)

    photos = os.listdir(Path(dir_path, 'images'))

    while True:
        for photo in photos:
            path = Path(dir_path, 'images', photo)
            bot.send_photo(chat_id='-1001733936497', photo=open(path, 'rb'))
            time.sleep(int(posting_delay))


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


def fetch_nasa_photos(nasa_api_key):
    params = {'api_key': nasa_api_key, 'count': 30}
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=params)
    response.raise_for_status()
    nasa_media = response.json()
    for number, media in enumerate(nasa_media):
        if media['media_type'] == 'image':
            file_name = f'nasa{number}{get_img_extension(media["url"])}'
            download_image(media['url'], file_name)


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v3/launches"
    response = requests.get(url)
    response.raise_for_status()
    images = response.json()[35]['links']['flickr_images']
    for number, image in enumerate(images):
        download_image(image, f'spacex{number}.jpg')


def get_img_extension(url):
    img_path = urllib.parse.urlsplit(url).path
    _, img_extension = os.path.splitext(img_path)
    return img_extension


def download_image(url, file_name, params={}):
    file_path = f'images/{file_name}'

    response = requests.get(url, params)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)


if __name__ == "__main__":
    main()
