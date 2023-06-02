from django.urls import path, include 
from myapp import views

urlpatterns = [
    path('', include('myapp.urls')),
    path('news/', include ('news.urls'))
]