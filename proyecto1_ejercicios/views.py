from django.http import HttpResponse, HttpResponseNotAllowed
from django.views import View
from django.shortcuts import render



# def handler404(request, exception):
#     content = "<h3>NO SE ENCONTRO LA PAGINA</h3>"
#     content += " <br> <b>Not Found (404)</b>"
#     content += " <button onclick=\"location.href='/'\">Volver al inicio</button>"
#     return HttpResponse(content, status=404)
def handler500(request):
    content = "<h3>ERROR INTERNO DEL SERVIDOR</h3>"
    content += " <br> <b>Internal Server Error (500)</b>"
    content += " <button onclick=\"location.href='/'\">Volver al inicio</button>"
    return HttpResponse(content, status=500)
def handler403(request, exception):
    return HttpResponse("<h3>PROHIBIDO</h3> <br> Forbidden (403)", status=403)
def handler400(request, exception):
    return HttpResponse("<h3>BAD REQUEST</h3> <br> Bad Request (400)", status=400)


# Crear vista personalizada para el error 404 con herencia
class Custom404View(View):
    def dispatch(self, request, *args, **kwargs):
        if request.method != "GET":
            return HttpResponseNotAllowed(["GET"])
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, exception=None):
        content = """
            <div>
                <h1>Custom Error View for 404:</h1>
                <h2>Page not found</h2>
                <br>
                <button onclick="window.location.href='/app1'">Ir Inicio</button>
            </div>
            """
        return HttpResponse(content, status=404)


def handler404(request, exception):
    view = Custom404View.as_view()
    return view(request, exception=exception)



