from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_home, name='pagina_home'),
]
