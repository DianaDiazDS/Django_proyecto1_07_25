from http.client import HTTPResponse
from django.shortcuts import render

from .forms import DemoForm
# Create your views here.
def myview(request): 
   return render(request, "form_ejemplo_tipos_campos.html") 

# def render_demo_form(request):
#     form = DemoForm()
#     return render(request, "form_ejemplo_tipos_campos.html", {"form_ejemplo_llamar": form})

def render_demo_form(request):
    if request.method == "POST":
        form = DemoForm(request.POST, request.FILES)  # Incluye request.FILES por si subes imágenes o archivos
        if form.is_valid():
            # Acceder a los datos limpios
            # name = form.cleaned_data['name']
            # age = form.cleaned_data['age']
            # date_reservation = form.cleaned_data['date_reservation']
            # email = form.cleaned_data['email']
            # agree = form.cleaned_data['agree_to_terms']
            # password = form.cleaned_data['password']
            # bio = form.cleaned_data['bio']
            # website = form.cleaned_data['website']
            # favorite_color = form.cleaned_data['favorite_color']
            # profile_picture = form.cleaned_data['profile_picture']
            # birth_month = form.cleaned_data['birth_month']
            # interests = form.cleaned_data['interests']
            # upload = form.cleaned_data['upload']

            # # Aquí decides qué hacer con los datos (guardar en BD, imprimir, etc.)
            # print("Nombre:", name)
            # print("Edad:", age)
            # print("Fecha reserva:", date_reservation)
            # print("Email:", email)
            # print("Acepta términos:", agree)
            # print("Password:", password)
            # print("Bio:", bio)
            # print("Website:", website)
            # print("Color favorito:", favorite_color)
            # print("Imagen:", profile_picture)
            # print("Mes de nacimiento:", birth_month)
            # print("Intereses:", interests)
            # print("Archivo:", upload)
            

            data = form.cleaned_data
            print(data)
            # Podrías redirigir o renderizar con mensaje de éxito
            return render(request, "form_ejemplo_tipos_campos.html", {
                "form_ejemplo_llamar": form,
                "mensaje": "Formulario enviado correctamente "
            })
    else:
        form = DemoForm()  # Si no es POST, muestra formulario vacío

    return render(request, "form_ejemplo_tipos_campos.html", {"form_ejemplo_llamar": form})


from .forms import logForm
def form_view(request):
    form = logForm()
    if request.method == "POST":
        form = logForm(request.POST)
        if form.is_valid():
            form.save()
    context={"form_para_BD": form}
    return render(request, "form_login.html", context)