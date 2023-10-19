# hse-bc-tgbot-task

## How to launch

Для запуска понадобится Python3 и библиотеки

Нужно скачать все нужные библиотеки и зависимости:
linux/macos: pip3 install -r requirements.txt
windows: pip install -r requirements.txt

Для создания базы(уже есть в репе, но можно пересоздать):
linux/macos: python3 db.py
windows: python db.py

## How to start

Чтобы запустить проект нужно вставить токен сюда ([**как получить токен**](https://helpdesk.bitrix24.ru/open/17538378/#:~:text=Получить%20токен%20для%20существующего%20бота,а%20вместо%20него%20создан%20новый.)):
bot = telebot.TeleBot('TOKEN')

Запуск
linux/macos: python3 main.py
windows: python main.py
