import datetime
#import telebot
#import configparser
#
#config = configparser.ConfigParser()
#with open('mirddin.cfg') as fd:
#    config.read_file(fd)
#token = config['Mirddin']['token']
#print(token)

def get_moon_date():
    moon_number = 26
    date = datetime.date.today()
    day = date.strftime("%d")
    month = date.strftime("%m")
    age = moon_number + int(day) + int(month)
    while age > 30:
        age -= 30
    return age
