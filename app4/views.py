from django.shortcuts import render

# una forma
from django.core.exceptions import PermissionDenied  
def myview(request): 
    if request.user.is_anonymous(): 
        raise PermissionDenied()     

from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required 

# aegunda forma
@login_required 
def myview2(request): 
    return HttpResponse("Hello World") 

# tercera forma
def testpermission(user): 
   
    if user.is_authenticated and user.has_perm("app4.change_category"):

        return True 
    else: 
        return False    

from django.contrib.auth.decorators import login_required 
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(testpermission, login_url="/app4/sinPermiso/")
def change_ctg(request):
    return HttpResponse("Cambio de categoría autorizado")

# usuario sin permiso
def myview3(request): 
   return HttpResponse("Acceso denegado: no tienes permiso para cambiar categorías.")


# lista de reservas
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView
from .models import Reservation

class ReservationListView(PermissionRequiredMixin, ListView):
    model = Reservation
    template_name = "app4/reservation_list.html"   # tu template
    context_object_name = "reservations"

    # Aquí defines el permiso que se debe tener
    permission_required = "app4.view_reservation"

    # Opcional: si quieres redirigir a otra página cuando no tiene permiso
    login_url = "/app4/sinPermiso/"




def menu(request):
    return render(request, "app4/menu.html")

def about(request):
    about_content = {
        "about": "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."
    }
    return render(request,"app4/about.html", {"content": about_content})