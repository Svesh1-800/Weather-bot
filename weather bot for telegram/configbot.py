import telebot
import pyowm
import  time

bot = telebot.TeleBot('1261929343:AAEtGbnxqCTJTYV-_CVoN-1z43jU-97qWtg')
owm = pyowm.OWM("4df08b04f52f2df5f91c063972301a40", language="RU")
@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id,
                         "Привет "+ message.from_user.username + ", погоду в каком городе ты бы хотел узнать? Мне не составит "
                                               "труда найти эту информацию для тебя. Введи команду /weather и через "
                                               "пробел название города.")

    elif message.text.lower() == "/help":
        bot.send_message(message.from_user.id, "Для того, чтобы узнать погоду, тебе нужно ввести команду /weather  "
                                               "и через пробел  название города на русском или английском. Регистр не имеет значения")

    elif message.text.split()[0] == '/weather':
        if len(message.text.split()) == 2:
            try:
                observation = owm.weather_at_place(message.text.split()[1])
                w = observation.get_weather()
                temperature = "Температура " +  str(w.get_temperature('celsius')['temp']) + " °С"
                humidity = "Влажность " + str(w.get_humidity()) + " %"
                status = w.get_detailed_status()
                pressure = "Давление " + str(w.get_pressure()["press"]) + "  миллиметров ртутного столба"
                wind = "Скорость ветра " + str(w.get_wind()["speed"]) + " m/c"

                bot.send_message(message.from_user.id, temperature)
                bot.send_message(message.from_user.id,  humidity)
                bot.send_message(message.from_user.id,  status)
                bot.send_message(message.from_user.id,pressure )
                bot.send_message(message.from_user.id,wind)
            except pyowm.exceptions.api_response_error.NotFoundError:
                         bot.send_message(message.from_user.id,"Вы неправильно ввели название города")
        else:
            bot.send_message(message.from_user.id, "Вы неправильно восопльзовались командой")
    elif message.text == 'cпасибо':
        bot.send_message(message.from_user.id, "Рад тебе помочь, мой друг")
    elif message.text == "как дела?":
        bot.send_message(message.from_user.id, "У меня все замечательно, надеюсь и у тебя")
    elif message.text=="я устал":
        bot.send_message(message.from_user.id, "Просто двигайся вперед и не обращай внимания на то, что думают другие. Делай то ,что должен, для себя.")
    else:
         bot.send_message(message.from_user.id,"Прости, но я тебя не понимаю. Введи команду /help")





bot.polling(none_stop=True, interval=0)