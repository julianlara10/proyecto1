from django.urls import path, include
from rest_framework.routers import DefaultRouter

from usuarios.viewsets import UsuariosListaViewset, UsuariosCrearViewset, UsuariosUsuarioViewset, \
    UsuariosEliminarViewset, UsuariosGeoViewset

router = DefaultRouter()
router.register('lista', UsuariosListaViewset, basename='Lista')
router.register('crear', UsuariosCrearViewset, basename='Crear')
router.register('usuario', UsuariosUsuarioViewset, basename='Usuario')
router.register('eliminar', UsuariosEliminarViewset, basename='Eliminar')
router.register('geocodificar_base', UsuariosGeoViewset, basename='GeoCodificar Base')


urlpatterns = [
    path('', include(router.urls)),
]