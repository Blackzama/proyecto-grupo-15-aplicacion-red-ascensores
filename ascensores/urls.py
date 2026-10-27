from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ascensores, name='lista_ascensores'),
    path('mapa/', views.vista_mapa, name='mapa_ascensores'),
]