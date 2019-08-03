import telebot
import pyowm

owm = pyowm.OWM('8abe2497f6167e77e46f4d329a58e800', language = "ru")
bot = telebot.TeleBot('930440634:AAEbV5dV3vzRHWlotbe4vKGC4M6zOIFvnzI')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('kushnarenkovo', 'ufa')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('bye')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('/start')

@bot.message_handler(commands=['start'])
def first_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text == 'kushnarenkovo':
        observation = owm.weather_at_place('kushnarenkovo,RU')
        w = observation.get_weather()
        bot.send_message(message.chat.id, w.get_temperature('celsius')["temp"], reply_markup=keyboard2)
    
    elif message.text == 'ufa':
        observation = owm.weather_at_place('ufa,RU')
        w = observation.get_weather()
        bot.send_message(message.chat.id, w.get_temperature('celsius')["temp"], reply_markup=keyboard2)

@bot.message_handler(content_types=['text'])
def end_message(message):
    if  message.text == 'bye':
        bot.send_message(message.chat.id, 'goodbye see you tomorrow', reply_markup=keyboard3)


bot.polling()