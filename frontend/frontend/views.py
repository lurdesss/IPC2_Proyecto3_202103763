from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

def procesar_xml(request):
    if request.method == 'POST' and request.FILES['xml_file']:
        xml_file = request.FILES['xml_file']
        fs = FileSystemStorage()
        filename = fs.save(xml_file.name, xml_file)
        return redirect('pagina-de-exito')  # Redirige a una página de éxito
    return render(request, 'tu-template.html')


def visual_index(request):
    objeto_template = loader.get_template("index.html")
    html_index = objeto_template.render()
    return HttpResponse(html_index)