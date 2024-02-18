from django.contrib import admin

from usuarios.models import Usuarios


# Register your models here.

@admin.register(Usuarios)
class usuariosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'apellido',
        'direccion',
        'tipo',
        'ciudad',
        'latitud',
        'longitud',
        'estado_geo',
        'cargo'
    )
    list_display_links = ('id',)