import os
import time
from pathlib import Path

import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    default_delay = 60 * 60 * 24
    telegram_api_key = os.getenv("TELEGRAM_API_KEY")
    posting_delay = os.getenv("POSTING_DELAY", default_delay)
    telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
    dir_path = Path.cwd()

    bot = telegram.Bot(telegram_api_key)
    photos = os.listdir(Path(dir_path, 'images'))

    while True:
        for photo in photos:
            path = Path(dir_path, 'images', photo)
            with open(path, 'rb') as file:
                bot.send_photo(chat_id=telegram_chat_id, photo=file)
            time.sleep(int(posting_delay))


if __name__ == "__main__":
    main()
