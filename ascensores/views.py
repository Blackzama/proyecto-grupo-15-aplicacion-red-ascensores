from django.shortcuts import render
from .models import Ascensor
from geopy.distance import geodesic

def lista_ascensores(request):
    ascensores = Ascensor.objects.all()

    # Capturar la ubicacion que manda el navegador por la URL
    lat_usuario = request.GET.get('lat')
    lon_usuario = request.GET.get('lon')

    # Lista formateada para enviar como JSON limpio a JavaScript
    ascensores_js = []
    for a in ascensores:
        distancia = None

        if lat_usuario and lon_usuario and a.latitud is not None and a.longitud is not None:
            try:
                punto_usuario = (float(lat_usuario), float(lon_usuario))
                punto_ascensor = (float(a.latitud), float(a.longitud))

                distancia = round(geodesic(punto_usuario, punto_ascensor).kilometers, 2)
            except (ValueError, TypeError):
                distancia = None

        if a.latitud is not None and a.longitud is not None:
            ascensores_js.append({
                'nombre': a.nombre,
                'estado': str(a.estado).strip().lower(),
                'estado_texto': a.get_estado_display(),
                'lat': float(a.latitud),
                'lng': float(a.longitud),
                'horario': f"{a.horario_apertura.strftime('%H:%M')} a {a.horario_cierre.strftime('%H:%M')}" if a.horario_apertura and a.horario_cierre else None,
                'distancia': distancia
            })

    # -------------------------------------------------------------
    # ORDENAR: Operativo (1) -> En Mantención (2) -> Cerrado (3) -> Institucional (4)
    # -------------------------------------------------------------
    prioridad_estado = {
        'operativo': 1,
        'mantencion': 2,
        'en_mantencion': 2,
        'en mantencion': 2,
        'en mantención': 2,
        'cerrado': 3,
        'fuera_de_servicio': 3,
        'fuera de servicio': 3,
        'institucional': 4,
    }

    ascensores_js.sort(key=lambda item: prioridad_estado.get(item['estado'], 99))

    return render(request, 'ascensores/lista.html', {
        'ascensores': ascensores,
        'ascensores_js': ascensores_js
    })

def vista_mapa(request):
    ascensores = Ascensor.objects.all()
    return render(request, 'ascensores/mapa.html', {'ascensores': ascensores})