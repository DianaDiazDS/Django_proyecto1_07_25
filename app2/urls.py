#app2/urls.py 
from django.urls import path 
from . import views 
app_name='app2' 
urlpatterns = [ 
    path('', views.index, name='index'), 
    path('myview/', views.myview, name='myview'),
    path('login/', views.login, name='login') ,
    

] 