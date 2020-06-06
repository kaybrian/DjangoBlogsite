from django import forms 
from .models import *
from django.forms import ModelForm


class TrendForm(forms.ModelForm):
    class Meta:
        model = CommentsTrending
        fields = "__all__"

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'