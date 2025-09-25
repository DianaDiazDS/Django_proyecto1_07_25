"""
URL configuration for proyecto1_ejercicios project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


# from django.urls import path 
# from . import views 

# urlpatterns = [ 
#     path('', views.index, name='index'), 
# ] 
from django.shortcuts import redirect

from django.contrib import admin 
from django.urls import include, path 
#importar include para poder incluir las urls de app1

from . import views

app_name='app4' 
urlpatterns = [   

    # path('', lambda request: redirect('/demo/')),
    path('', lambda request: redirect('app1:index')),  # Redirige a la vista index de app1
    path('app1/', include('app1.urls', namespace='app1')),
    path('app2/', include('app2.urls', namespace='app2')),
    path('app3/', include('app3.urls', namespace='app3')),
    path('app4/', include('app4.urls', namespace='app4')),
    path('app5/', include('app5.urls', namespace='app5')),
    path('restaurant/', include('restaurant.urls', namespace='restaurant')),


    path('admin/', admin.site.urls),    
] 

handler400= 'proyecto1_ejercicios.views.handler400'
handler403= 'proyecto1_ejercicios.views.handler403'
handler404= 'proyecto1_ejercicios.views.handler404'
handler500= 'proyecto1_ejercicios.views.handler500'
