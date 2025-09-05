
from django.urls import path 
from . import views 
app_name='app3' 
urlpatterns = [  
    path('formulario1/', views.myview, name='myview'),
    path('tiposDatosForm/', views.render_demo_form, name='render_demo_form'),
    path('logform/', views.form_view, name='form_view')
    ]