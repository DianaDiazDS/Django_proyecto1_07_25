from django.urls import path


from . import views

from django.views.generic import TemplateView
from .someviews.aboutview import AboutView
from .someviews.BookListView import BookListView


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

    # Uso en su URLconf 
    path('about/', TemplateView.as_view(template_name="form.html")), 
    # Subclasificación de vistas genéricas  
    path('about2/', AboutView.as_view()),
    # otros métodos HTTP
    path('books/', BookListView.as_view()),
]
