import telebot
import requests
from datetime import datetime, timedelta


bot_token = '6019015707:AAGWfT8UdMd53adLR2XgnGP7g2Sly5SDO-4'

# Ініціалізуємо об'єкт бота
bot = telebot.TeleBot(bot_token)

# Глобальна змінна для збереження останнього міста
last_city = None

# Функція для отримання перекладу погодних умов
def translate_weather(weather):
    translations = {
        'Thunderstorm': 'Гроза',
        'Drizzle': 'Мряка',
        'Rain': 'Дощ',
        'Snow': 'Сніг',
        'Mist': 'Туман',
        'Smoke': 'Дим',
        'Haze': 'Мгла',
        'Dust': 'Пил',
        'Fog': 'Туман',
        'Sand': 'Пісок',
        'Ash': 'Попіл',
        'Squall': 'Шквал',
        'Tornado': 'Торнадо',
        'Clear': 'Ясно',
        'Clouds': 'Хмари'
    }
    return translations.get(weather, 'Погода невідома')

def get_recommendation(weather, temperature):
    translated_weather = translate_weather(weather)
    if 'Дощ' in translated_weather and temperature < 15:
        return "На дворі йде дощ та холодно. Пропоную подивитись якийсь фільм або серіал!\n\n"
    elif temperature > 20:
        return "Погода гарна і тепло. Можна прогулятись на свіжому повітрі!\n\n"
    else:
        return "Хороша погода для того, щоб зайнятись чимось цікавим вдома чи на вулиці\n\n"

# Функція для визначення привітання залежно від часу
def get_greeting():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Гарного ранку!"
    elif 12 <= current_hour < 18:
        return "Гарного та продуктивного дня!"
    elif 18 <= current_hour < 23:
        return "Гарного вечора!"
    else:
        return "Доброї ночі! Сподіваюсь вона буде без повітряних тривог"

# Функція-обробник для команди /start

@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_weather = telebot.types.KeyboardButton(text='Перевірити погоду')
    button_forecast = telebot.types.KeyboardButton(text='Прогноз погоди на завтра')
    keyboard.add(button_weather, button_forecast)
    bot.reply_to(message, 'Привіт! Вітаю у боті погоди. Введи назву міста, щоб отримати погоду.', reply_markup=keyboard)

@bot.message_handler(commands=['menu'])
def handle_menu(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_weather = telebot.types.KeyboardButton(text='Перевірити погоду')
    button_forecast = telebot.types.KeyboardButton(text='Прогноз погоди на завтра')
    keyboard.add(button_weather, button_forecast)
    bot.reply_to(message, 'Меню:', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global last_city

    if message.text == 'Перевірити погоду':
        if last_city:
            get_weather(message, last_city)
        else:
            bot.reply_to(message, 'Введи назву міста, щоб отримати погоду.')
    elif message.text == 'Прогноз погоди на завтра':
        if last_city:
            get_weather_forecast(message, last_city)
        else:
            bot.reply_to(message, 'Введи назву міста, щоб отримати прогноз погоди на завтра.')
    else:
        last_city = message.text
        get_weather(message, last_city)

def get_weather(message, city):
    try:
        # Виконуємо HTTP GET запит до OpenWeatherMap API
        url = f'http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&appid=6de5c543d5bdf025d51c06da496cdb82'
        response = requests.get(url)
        data = response.json()

        # Отримуємо необхідну інформацію з відповіді API
        if response.status_code == 200:
            weather = data['weather'][0]['main']
            temperature = data['main']['temp']
            reply = f'Погода у місті {city}: {translate_weather(weather)}. Температура: {temperature:.2f}°C.\n\n'
            recommendation = get_recommendation(weather, temperature)
            reply += recommendation

            greeting = get_greeting()
            reply += f'\n{greeting}'
        else:
            reply = f'Не вдалося знайти погоду для міста {city}'
    except requests.exceptions.RequestException:
        reply = 'Помилка при отриманні погодових даних.'

    bot.reply_to(message, reply)

def get_weather_forecast(message, city):
    try:
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow_date = tomorrow.strftime('%Y-%m-%d')
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid=6de5c543d5bdf025d51c06da496cdb82'
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            forecast_list = data['list']
            forecast = None
            for item in forecast_list:
                dt_txt = item['dt_txt']
                if dt_txt.startswith(tomorrow_date) and '12:00:00' in dt_txt:
                    forecast = item
                    break

            if forecast:
                weather = forecast['weather'][0]['main']
                temperature_kelvin = forecast['main']['temp']
                temperature = temperature_kelvin - 273.15
                reply = f'Прогноз погоди на завтра у місті {city}: {translate_weather(weather)}. Температура вдень: {temperature:.2f}°C.\n\n'
                if 'Rain' in weather or 'Drizzle' in weather:
                    reply += 'Очікується дощ.\n\n'
            else:
                reply = f'Не вдалося отримати прогноз погоди на завтра для міста {city}'
        else:
            reply = f'Не вдалося знайти погоду для міста {city}'
    except requests.exceptions.RequestException:
        reply = 'Помилка при отриманні погодових даних.'

    bot.reply_to(message, reply)


bot.polling()
