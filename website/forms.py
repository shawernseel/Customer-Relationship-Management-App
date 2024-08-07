from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SingUpForm(UserCreationForm):
    email = forms.EmailField(label="", widgets=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'})) #attrs uses bootstap to style form
    first_name = forms.CharField(label="", max_length=100, widgets=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widgets=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
