from django.http import HttpResponse
def handler404(request, exception):
    content = "<h3>NO SE ENCONTRO LA PAGINA</h3>"
    content += " <br> <b>Not Found (404)</b>"
    content += " <button onclick=\"location.href='/'\">Volver al inicio</button>"
    return HttpResponse(content, status=404)
def handler500(request):
    content = "<h3>ERROR INTERNO DEL SERVIDOR</h3>"
    content += " <br> <b>Internal Server Error (500)</b>"
    content += " <button onclick=\"location.href='/'\">Volver al inicio</button>"
    return HttpResponse(content, status=500)
def handler403(request, exception):
    return HttpResponse("<h3>PROHIBIDO</h3> <br> Forbidden (403)", status=403)
def handler400(request, exception):
    return HttpResponse("<h3>BAD REQUEST</h3> <br> Bad Request (400)", status=400)
