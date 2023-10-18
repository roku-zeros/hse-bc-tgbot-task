import telebot
from pony.orm import *
from datetime import datetime
from db import User

bot = telebot.TeleBot('TOKEN')  # Свой токен не дам :)


@bot.message_handler(commands=['start'])
def start_handler(message):
    with db_session:
        user = User.get(id=message.chat.id)
        if not user:
            user = User(id=message.chat.id)
            commit()
        bot.reply_to(message, 'Привет! И я веду подсчет пользователей в боте.\n'
                              'Чтобы получить количество пользователей введи /admin')


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    with db_session:
        user = User.get(id=call.message.chat.id)
        if user:
            user.last_action_date = datetime.now()
            commit()


@bot.message_handler(commands=['admin'])
def admin_handler(message):
    with db_session:
        users_count = count(u for u in User)
        bot.reply_to(message, f'Количество пользователей в боте: {users_count}')

# Запуск бота
bot.polling()