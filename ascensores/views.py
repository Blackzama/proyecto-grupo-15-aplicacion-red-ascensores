from django.shortcuts import render
from .models import Ascensor

def lista_ascensores(request):

    todos_los_ascensores = Ascensor.objects.all()
    

    return render(request, 'ascensores/lista.html', {'ascensores': todos_los_ascensores})