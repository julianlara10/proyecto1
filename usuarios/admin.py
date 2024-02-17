from django.contrib import admin

from usuarios.models import Usuarios


# Register your models here.

@admin.register(Usuarios)
class usuariosAdmin(admin.ModelAdmin):
    pass