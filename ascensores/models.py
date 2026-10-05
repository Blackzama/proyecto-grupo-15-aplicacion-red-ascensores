from django.db import models

class Ascensor(models.Model):

    OPCIONES_ESTADO = [
        ('operativo', 'Operativo'),
        ('mantencion', 'En Mantención'),
        ('cerrado', 'Cerrado'),
    ]

    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Ascensor")
    estado = models.CharField(max_length=20, choices=OPCIONES_ESTADO, default='operativo', verbose_name="Estado Actual")
    

    horario_apertura = models.TimeField(null=True, blank=True, verbose_name="Horario de Apertura")
    horario_cierre = models.TimeField(null=True, blank=True, verbose_name="Horario de Cierre")


    def __str__(self):
        return self.nombre