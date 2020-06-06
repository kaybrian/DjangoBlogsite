from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.


def index(request):
    editors = EditorsPick.objects.all().order_by('date_Created')[:3]
    trends = Trending.objects.all().order_by('-date_Created')[:6]
    trendshead = Trending.objects.all().order_by('date_Created')[:1]
    Programm = Posts.objects.filter(
        tag='programming').order_by('-date_Created')[:3]
    innovation = Posts.objects.filter(
        tag='Innovation').order_by('-date_Created')[:3]
    if request.method == "POST":
        email = request.POST['NewsletterEmail']
        newslet = Newsletter(email=email)
        newslet.save()
    context = {
        'editors': editors,
        'trends': trends,
        'trendshead': trendshead,
        'Programm': Programm,
        'innovation': innovation

    }
    return render(request, 'blog/index.html', context)


def PostDetail(request, pk):
    trend_post = Trending.objects.get(id=pk)
    comments = CommentsTrending.objects.all().order_by('-id')
    context = {
        'trend_post': trend_post,
        'comments':comments
        
    }
    return render(request, 'blog/blog-single.html', context)
