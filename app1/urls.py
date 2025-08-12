from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_home, name='pagina_home'),
    path('fecha/', views.display_date, name='display_date'),
    path('menu/', views.menu, name='menu'),
    path('index/', views.index, name='index'),

    path('getuser/<str:name>/<int:id>/', views.pathview, name='pathview'),
    path('getuser2/', views.qryview, name='qryview') ,

    path("showform/", views.showform, name="showform"), 
    path("getform/", views.getform, name="getform"),
    
    path("menuitems/<str:dish>/", views.menuitrems, name="menuitrems"),
]
