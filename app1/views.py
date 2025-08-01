from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
# agregamos este immport para poder usar HttpResponse



def pagina_home(request): 
    return HttpResponse("pagina home") 