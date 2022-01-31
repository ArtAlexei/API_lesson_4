# Space Telegram

Программа скачивает фотографии NASA и SpaceX, публикует их в телеграмм канал с заданным интервалом.

## Как установить
Для запуска программы у вас уже должен быть установлен Python 3.
- Скачайте код  
- Установите зависимости командой `pip install -r requirements.txt`  

## Запуск скриптов
- Скачать фотографии NASA `python3 fetch_nasa.py`  
- Скачать фотографии SpaceX `python3 fetch_spacex.py`  
- Начать постить фотографии `python3 post_photos.py`  

## Переменные окружения
Данные хранятся в файле `.env`  
`NASA_API_KEY`- ключ для доступа к api сайта [NASA](https://api.nasa.gov/)  
`TELEGRAM_API_KEY`- ключ для доступа к api [Telegram](https://telegram.org/) бота. . [Инструкция](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html)  
`POSTING_DELAY` - интервал загрузки фото в секундах  
`TELEGRAM_CHAT_ID` - ID канала в телеграмме  


## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/)