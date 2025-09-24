from django.shortcuts import render

# Create your views here.
def home(request): 
    return render(request, "app5/home.html", {}) 

def register(request): 
    return render(request, "app5/register.html", {}) 

def login(request): 
    return render(request, "app5/login.html", {}) 