from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_home, name='pagina_home'),
    path('fecha/', views.display_date, name='display_date'),
    path('menu/', views.menu, name='menu'),
]
