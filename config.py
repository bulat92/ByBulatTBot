import telebot #подключние телебота аипи    
import pyowm # погодоный информатор

owm = pyowm.OWM('8abe2497f6167e77e46f4d329a58e800', language = "ru") # токен для информатора и выбор языка  
bot = telebot.TeleBot('930440634:AAEbV5dV3vzRHWlotbe4vKGC4M6zOIFvnzI')# токен бота и 
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True) # клавыатуры
keyboard1.row('kushnarenkovo', 'ufa')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('bye')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('/start')

@bot.message_handler(commands=['start']) #фильтр обраблотчик
def first_message(message): # имя функций
    bot.send_message(message.chat.id, "Hello you wrote me /start \n What city temperature do you want to know?", reply_markup=keyboard1) # бот отправляет . чат иб ответ и вывыводит клаву
    

@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text == 'kushnarenkovo': # если кушнаренково
        observation = owm.weather_at_place('kushnarenkovo,RU') # достать погоду
        w = observation.get_weather() # достать погоду
        bot.send_message(message.chat.id, 'Air temperature in Kushnarenkovo ' . w.get_temperature('celsius')["temp"] . "°C", reply_markup=keyboard2) # поголдду градусы отправь
    
    elif message.text == 'ufa':
        observation = owm.weather_at_place('ufa,RU')
        w = observation.get_weather()
        bot.send_message(message.chat.id,'Air temperature in Ufa ' . w.get_temperature('celsius')["temp"] . "°C" , reply_markup=keyboard2)

    elif  message.text == 'bye':
        bot.send_message(message.chat.id, 'Goodbye see you tomorrow', reply_markup=keyboard3)


bot.polling() # крутись живи вечно