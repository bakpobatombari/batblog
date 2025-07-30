from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect("login")  # Make sure you have a 'login' url name
    else:
        form = RegisterForm()
    return render(request, "core/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("index")  # Change 'index' to your homepage url name
    else:
        form = AuthenticationForm()
    return render(request, "core/login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("index")