from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, AboutContent
from .models import AboutContent
from django.contrib.auth.decorators import login_required
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
    
def about(request):
    
    content1 = AboutContent()
    content1.title = "Blog"
    content1.id = 0
    content1.content = "lorem ipsum 1orem dis lorem ipdum lorem you lorem fillup lorem again lorem br ispum lego word dc is the worst comic ever"
    
    content2 = AboutContent()
    content2.title = "About"
    content2.id =1; 
    content2.content = "Testing software to be sure of functionality Status"
    
    content3 = AboutContent()
    content3.title = "About"
    content3.id =1; 
    content3.content = "Under Production"
      
    content = [content1, content2, content3]
    
    return render(request, 'core/about.html',{"contents": content})

@login_required
def aboutContent(request):
    if request.method == "POST":
        form = AboutContent(request.POST, request.FILES)

        if form.is_valid:
            content = form.save(commit=False)
            content.created_by = request.user
            content.save()
            
            return redirect('core/about_form.html')
    else:
        form = AboutContent()
        
    return render(request, 'core/about_form.html', {
        'form': form,
        'title': "Content"
    })
    