import telebot
import pyowm

owm = pyowm.OWM('8abe2497f6167e77e46f4d329a58e800', language = "ru")
bot = telebot.TeleBot('930440634:AAEbV5dV3vzRHWlotbe4vKGC4M6zOIFvnzI')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('kushnarenkovo', 'ufa')


@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text == 'kushnarenkovo':
        observation = owm.weather_at_place('kushnarenkovo,RU')
        w = observation.get_weather()
        bot.send_message(message.chat.id, w.get_temperature('celsius')["temp"])
    
    elif message.text == 'ufa':
        observation = owm.weather_at_place('ufa,RU')
        w = observation.get_weather()
        bot.send_message(message.chat.id, w.get_temperature('celsius')["temp"])

bot.polling()