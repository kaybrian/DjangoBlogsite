from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

# this is the main index part that you can you see


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

# for the single Trending posts part


def PostDetail(request, pk):
    trend_post = Trending.objects.get(id=pk)
    comments = CommentsTrending.objects.filter(post=trend_post).order_by('-id')
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['email']
        comment = request.POST['comment']

        CommentsTrending.objects.create(
            post=trend_post, name=name, email=email, comment=comment)

    context = {
        'trend_post': trend_post,
        'comments': comments
    }
    return render(request, 'blog/blog-single.html', context)


# this is the part for the single posts blog part
def PostOnly(request, pk):
    Postsneeded = Posts.objects.get(id=pk)
    comments = CommentsPosts.objects.filter(post=Postsneeded).order_by('-id')
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['email']
        comment = request.POST['comment']

        CommentsPosts.objects.create(
            post=Postsneeded, name=name, email=email, comment=comment)

    context = {
        'trend_post': Postsneeded,
        'comments': comments
    }
    return render(request, 'blog/postSingle.html', context)


def inovate(request):
    innovation = Posts.objects.filter(
        tag='Innovation').order_by('-date_Created')[:9]
    context = {'innovation': innovation}
    return render(request, 'blog/innovations.html', context)


def programming(request):
    Programm = Posts.objects.filter(
        tag='programming').order_by('-date_Created')[:9]
    context = {'Programm': Programm}
    return render(request, 'blog/programming.html', context)

def inspirations(request):
    inspiration = Posts.objects.filter(
        tag='inspiration').order_by('-date_Created')[:9]
    context = {'inspiration': inspiration}
    return render(request, 'blog/inspiration.html', context)

def ContactMe(request):
    context = {}
    return render(request,'blog/contact.html',context)