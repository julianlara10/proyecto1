from django.db import models

from usuarios.utils import TIPO, CARGO


# Create your models here.


class Usuarios(models.Model):
    nombre = models.CharField(
        max_length=254,
        verbose_name='Nombre',
    )
    apellido = models.CharField(
        max_length=254,
        verbose_name='Apellido',
    )
    direccion = models.CharField(
        max_length=254,
        verbose_name='Dirección',
    )
    tipo = models.CharField(
        max_length=25,
        choices=TIPO,
        default='vendedores',
        verbose_name='Tipo'
    )
    ciudad = models.CharField(
        max_length=150,
        verbose_name='Ciudad'
    )
    longitud = models.FloatField()
    latitud = models.FloatField()
    estado_geo = models.BooleanField(
        default=False,
    )
    cargo = models.CharField(
        max_length=25,
        choices=CARGO,
        default='asesor',
        verbose_name='Cargo'
    )

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
