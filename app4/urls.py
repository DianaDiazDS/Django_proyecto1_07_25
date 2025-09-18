from django.urls import path 
from . import views 
app_name='app4' 
urlpatterns = [  
    path('permisoUser/', views.myview, name='myview'),
    path('permisoUser2/', views.myview2, name='myview2'),
    path('sinPermiso/', views.myview3, name='myview3'),
    path("change-category/", views.change_ctg, name="change_category"),
    path("reservations/", views.ReservationListView.as_view(), name="reservation_list"),

    path("menu/", views.menu, name="menu"),
    path("about/", views.about, name="about"),

]