from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('weather', views.weather, name='weather'),
    path('news', views.weather, name='news'),
    path('admin/', admin.site.urls),
    path('get_weather/', views.get_weather, name='get_weather')
]