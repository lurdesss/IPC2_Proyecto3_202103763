from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import xml.etree.ElementTree as ET

def procesar_xml(request):
    if request.method == 'POST' and request.FILES['xml_file']:
        xml_file = request.FILES['xml_file']
        fs = FileSystemStorage()
        filename = fs.save(xml_file.name, xml_file)

        tree = ET.parse(fs.url(filename))
        root = tree.getroot()
        contenido_xml = ET.tostring(root, encoding='utf8').decode('utf8')

        return render(request, 'mostrarcarga.html', {'contenido_xml': contenido_xml})
    return render(request, 'nocarga.html')


def visual_index(request):
    objeto_template = loader.get_template("index.html")
    html_index = objeto_template.render()
    return HttpResponse(html_index)

def visual_opciones(request):
    objeto_template = loader.get_template("opciones.html")
    html_opciones = objeto_template.render()
    return HttpResponse(html_opciones)

def visual_carga(request):
    objeto_template = loader.get_template("mostrarcarga.html")
    html_carga = objeto_template.render()
    return HttpResponse(html_carga)