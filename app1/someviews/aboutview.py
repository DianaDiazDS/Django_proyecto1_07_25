from django.views.generic import TemplateView
# Django tiene una vista genérica para esto TemplateView, 
# así que podemos subclasificarla y sobrescribir el nombre de la plantilla:
class AboutView(TemplateView):
    template_name = "form.html"