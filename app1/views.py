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


# modulo 2 vistas

def index(request): 
    path = request.path 
    scheme = request.scheme
    method = request.method 
    address = request.META.get('REMOTE_ADDR', 'Unknown')
    user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')
    path_info = request.path_info
    edad = '30'  # Valor fijo para mostrar en la respuesta

    content = f''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : {path}</p> 
<p>Request Method : {method}</p></center> 
<p>Request Scheme : {scheme}</p>
<p>Request Address : {address}</p>
<p>Request User-Agent : {user_agent}</p>
<p>Request Path Info : {path_info}</p>
<P> Response Headers : Age={edad} </P>
'''
    response = HttpResponse(content, content_type='text/html; charset=utf-8')
    response['Age'] = edad  # Agrega el header 'Age' a la respuesta
#     Agrega un header personalizado
# Añade un encabezado HTTP llamado Age con el valor '30' a la respuesta.

# Devuelve la respuesta
# El navegador verá la página HTML con los datos y el header extra.
    return response

#se usa esta ruta http://127.0.0.1:8000/getuser/diana/3/
def pathview(request, name, id): 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

# para esta ruta http://127.0.0.1:8000/getuser2/?name=John&id=13
def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

# usa un formulario de la carpeta templates
def showform(request): 
    return render(request, "form.html") 
def getform(request): 
    if request.method == "POST": 
        id=request.POST['id'] 
        name=request.POST['name'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 


def menuitrems(request, dish):
    items ={
        'arroz dulce':'hecho con arroz y leche',
        'panqueques':'hechos con harina, huevos y leche',
        'huevo perico':'hecho con huevos, cebolla y tomate'
    }
    description=items[dish]
    return HttpResponse(f"El plato {dish} es {description}")





# from django.views import View 
# class MyView(View): 
#     def get(self, request): 
#         # logic to process GET request
#         return HttpResponse('response to GET request') 
 
#     def post(self, request): 
#         # <logic to process POST request> 
#         return HttpResponse('response to POST request') 

