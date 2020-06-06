from django import forms 
from .models import *
from django.forms import ModelForm


class TrendComment(forms.ModelForm):
    class Meta:
        model = CommentsTrending
        fields = ("name","comment",)
