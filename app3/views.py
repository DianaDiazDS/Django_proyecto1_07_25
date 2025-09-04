from django.shortcuts import render

from .forms import DemoForm
# Create your views here.
def myview(request): 
   return render(request, "form_ejemplo.html") 

def render_demo_form(request):
    form = DemoForm()
    return render(request, "form_ejemplo.html", {"form_ejemplo_llamar": form})