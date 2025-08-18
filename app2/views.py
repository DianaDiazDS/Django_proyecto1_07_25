from django.shortcuts import render

# Create your views here.
from django.http import HttpResponsePermanentRedirect 
from django.urls import reverse 

from django.http import HttpResponse 
def myview(request): 
   return render(request, "form2.html") 

def index(request): 
  return HttpResponsePermanentRedirect(reverse('app2:myview'))

def myview(request):
    return HttpResponsePermanentRedirect(reverse('app1:login'))
def login(request): 
    return render(request, "form3.html")



