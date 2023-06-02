import telebot
import requests
from datetime import datetime

# Ініціалізуємо токен вашого телеграм-бота
bot_token = '6019015707:AAGWfT8UdMd53adLR2XgnGP7g2Sly5SDO-4'

# Ініціалізуємо об'єкт бота
bot = telebot.TeleBot(bot_token)

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

# Функція для отримання рекомендацій щодо фільмів або серіалів
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
    bot.reply_to(message, 'Привіт! Вітаю у боті погоди. Введи назву міста, щоб отримати погоду.')

# Функція-обробник для повідомлень з текстом
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    city = message.text
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

# Запускаємо бота
bot.polling()
