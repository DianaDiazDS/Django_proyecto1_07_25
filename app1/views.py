from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
# agregamos este immport para poder usar HttpResponse
from datetime import datetime


def pagina_home(request): 
    return HttpResponse("pagina home") 


def display_date(request): 
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    return HttpResponse(f"Fecha y hora actual: {current_date}")


def menu(request):
    text = """<h1 style="color: #F4CE14;"> this is the little menu</h1>"""
    return HttpResponse(text)

# from django.views import View 
# class MyView(View): 
#     def get(self, request): 
#         # logic to process GET request
#         return HttpResponse('response to GET request') 
 
#     def post(self, request): 
#         # <logic to process POST request> 
#         return HttpResponse('response to POST request') 