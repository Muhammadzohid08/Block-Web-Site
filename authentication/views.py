from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout


def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        email = request.GET.get('emal')
        firstName = request.GET.get('username')
        lastName = request.GET.get('lastName')
        password = request.GET.get('password')
        user = User(email=email, firstName=firstName, lastName=lastName)
        user.set_password(password)
        user.save()
        return redirect('/')
    return render(request, 'register.html')

def home_view(request):
    return render(request, 'home.html')