#!/usr/bin/python3

import telebot
import configparser

config = configparser.ConfigParser()
with open('/home/silver/sscriptss/py/mirddin.cfg') as fd:
    config.read_file(fd)
token = config['Mirddin']['token']

if chat_id:
    name = config['Users'][chat_id]

mird = telebot.TeleBot(token) # Create mirddin object

# Upon calling this function, TeleBot starts polling the Telegram servers for new messages.
# - interval: int (default 0) - The interval between polling requests
# - timeout: integer (default 20) - Timeout in seconds for long polling.
# - allowed_updates: List of Strings (default None) - List of update types to request 
#mird.infinity_polling(interval=0, timeout=20)

back_exercises = f"Время оздоровления спины, {name}"
text = back_exercises

# sendMessage
mird.send_message(chat_id, text)
