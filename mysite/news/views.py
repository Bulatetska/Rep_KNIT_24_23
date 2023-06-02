from django.shortcuts import render
from .models import Articles
# Create your views here.
def news(request):
   news = Articles.objects.all()
   return render(request, 'news/index.html', {'news': news})