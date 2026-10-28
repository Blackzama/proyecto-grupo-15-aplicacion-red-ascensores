from django.shortcuts import render
from .models import Ascensor

def lista_ascensores(request):
    ascensores = Ascensor.objects.all()
    
    # Lista formateada para enviar como JSON limpio a JavaScript
    ascensores_js = []
    for a in ascensores:
        if a.latitud is not None and a.longitud is not None:
            ascensores_js.append({
                'nombre': a.nombre,
                'estado': str(a.estado).strip().lower(),
                'estado_texto': a.get_estado_display(),
                'lat': float(a.latitud),
                'lng': float(a.longitud),
                'horario': f"{a.horario_apertura.strftime('%H:%M')} a {a.horario_cierre.strftime('%H:%M')}" if a.horario_apertura and a.horario_cierre else ""
            })

    return render(request, 'ascensores/lista.html', {
        'ascensores': ascensores,
        'ascensores_js': ascensores_js
    })

def vista_mapa(request):
    ascensores = Ascensor.objects.all()
    return render(request, 'ascensores/mapa.html', {'ascensores': ascensores})