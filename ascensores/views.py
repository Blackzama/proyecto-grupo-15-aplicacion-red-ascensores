from django.shortcuts import render
from .models import Ascensor

def lista_ascensores(request):

    ascensores = Ascensor.objects.all()
    

    return render(request, 'ascensores/lista.html', {'ascensores': ascensores})

def vista_mapa(request):
    ascensores = Ascensor.objects.all()
    return render(request, 'ascensores/mapa.html', {'ascensores': ascensores})