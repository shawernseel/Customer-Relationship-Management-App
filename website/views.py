from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def home(request): #everytime a page is visited request is sent to backend here which is passed to view
    return render(request, 'home.html', {}) #home page is returned from request



def login_user(request):
    pass

def logout_user(request):
    pass