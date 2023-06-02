from django.shortcuts import render
from django.http import HttpResponse
from .forms import CityForm
from .weather import get_weather
from django.views.decorators.csrf import csrf_protect



def index(request):
    return render(request, 'myapp/index.html')


def about(request):
    return render(request, 'myapp/about.html')

@csrf_protect
def weather(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            api_key = "6de5c543d5bdf025d51c06da496cdb82"
            city = form.cleaned_data['city']
            result = get_weather(city, api_key)
            context = {'weather_info': result}
            return render(request, 'myapp/weather.html', context)
    else:
        form = CityForm()

    context = {'form': form}
    return render(request, 'myapp/weather.html', context)