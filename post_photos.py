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
    default_delay = 60 * 60 * 24
    telegram_api_key = os.getenv("TELEGRAM_API_KEY")
    posting_delay = os.getenv("POSTING_DELAY", default_delay)
    dir_path = Path.cwd()

    bot = telegram.Bot(telegram_api_key)
    photos = os.listdir(Path(dir_path, 'images'))

    while True:
        for photo in photos:
            path = Path(dir_path, 'images', photo)
            bot.send_photo(chat_id='-1001733936497', photo=open(path, 'rb'))
            time.sleep(int(posting_delay))


if __name__ == "__main__":
    main()
