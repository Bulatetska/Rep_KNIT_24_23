import requests
from django.http import JsonResponse
weather_translations = {
    "clear sky": "Ясно",
    "few clouds": "Малохмарно",
    "scattered clouds": "Розсіяні хмари",
    "broken clouds": "Розрізані хмари",
    "overcast clouds": "Похмуро з хмарами",
    "light rain": "Легкий дощ",
    "moderate rain": "Умірений дощ",
    "heavy rain": "Сильний дощ",
    "thunderstorm": "Гроза",
    "snow": "Сніг",
    "mist": "Туман",
    "fog": "Туман",
    "haze": "Легкий туман",
    "smoke": "Дим",
    "dust": "Пил",
    "sand": "Пісок",
    "ash": "Вулканічний попіл",
    "squalls": "Пориви вітру",
    "tornado": "Торнадо"
}

def get_weather(request):
    city = request.POST.get('city')
    api_key = "6de5c543d5bdf025d51c06da496cdb82"
    
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Для отримання погоди в метричній системі
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        weather_translation = weather_translations[weather]
        weather = weather_translation
        result = f"Погода в {city}: {weather}, Температура: {temperature}°C"
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'result': 'Не вдалося отримати дані'})


def weather(request):
    return render(request, 'myapp/weather.html')
