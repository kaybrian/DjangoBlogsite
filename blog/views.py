from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    editors = EditorsPick.objects.all().order_by('date_Created')[:3]
    trends = Trending.objects.all().order_by('date_Created')[:4]
    
    context = {
        'editors': editors,
        'trends': trends,
        'trendslarge':trendslarge
    }
    return render(request, 'blog/index.html', context)
