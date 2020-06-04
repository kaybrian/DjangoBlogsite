from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    editors = EditorsPick.objects.all()
    context = {'editors':editors}
    return render(request,'blog/index.html',context)