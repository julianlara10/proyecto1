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
        null=True,
        blank=True
    )
    tipo = models.CharField(
        max_length=25,
        choices=TIPO,
        default='vendedor',
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
        verbose_name='Cargo',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
