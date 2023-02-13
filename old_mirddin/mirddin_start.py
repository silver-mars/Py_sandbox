import telebot
import configparser
from datetime import datetime

config = configparser.ConfigParser()
with open('mirddin.cfg') as fd:
    config.read_file(fd)
token = config['Mirddin']['token']
bot = telebot.TeleBot(token)

def time_get():
    if 5 <= datetime.now().hour <= 6:
        time = 'раннего утра'
    elif 7 <= datetime.now().hour <= 11:
        time = 'доброго утра'
    elif 12 <= datetime.now().hour <= 16:
        time = 'доброго дня'
    elif 17 <= datetime.now().hour <= 22:
        time = 'доброго вечера'
    else:
        time = 'доброй ночи'
    return time

@bot.message_handler(commands=['start'])
def start(message):
    time = time_get()
    bot.send_message(message.chat.id, text=f'Здравствуйте.\nВернее {time}.')
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = telebot.types.KeyboardButton("Узнать какой сейчас лунный день.")
    markup.add(button)
    bot.send_message(message.chat.id, text='Меня зовут Мерлин.\nЯ - магический помощник своего Мастера, но могу помочь и Вам.\n', reply_markup=markup)
    id_user = message.chat.id
    with open('mirddin_memory', 'a') as fd:
        fd.write(str(id_user))
    bot.send_message(message.chat.id, text=f'Ваш id = {id_user}')

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Узнать какой сейчас лунный день."):
        import moon_phases_calc as moon
        day = moon.get_moon_date()
        bot.send_message(message.chat.id, text=f'Сейчас примерно {day} лунный день.')

bot.polling(none_stop=True)
