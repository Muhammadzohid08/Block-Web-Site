from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate


def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
            emailField = request.POST.get('email', None)
            firstNameField = request.POST.get('username', None)
            lastNameField = request.POST.get('lastName', None)
            passwordField = request.POST.get('password', None)

            user = User(
                email=emailField,
                firstName=firstNameField,
                lastName=lastNameField,
            )

            user.set_password(passwordField)
            user.save()
            return redirect('/')


    return render(request, 'register.html')

def home_view(request):
    return render(request, 'home.html')