from django.db.models import Q
from rest_framework import viewsets, serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from usuarios.models import Usuarios
from usuarios.serializers import UsuariosSerializer

import googlemaps


class UsuariosListaViewset(viewsets.ModelViewSet):

    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = (
        AllowAny,
    )
    http_method_names = ('get',)
    ordering = ('pk',)
    ordering_fields = ('pk',)


class UsuariosCrearViewset(viewsets.ModelViewSet):

    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = (
        AllowAny,
    )
    http_method_names = ('post',)
    ordering = ('pk',)
    ordering_fields = ('pk',)

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        datos_validos = serializer.validated_data
        if datos_validos['tipo'] == 'vendedor':
            if 'cargo' not in serializer.validated_data:
                raise serializers.ValidationError("cargo es requerido")
        elif datos_validos['tipo'] == 'comprador':
            datos_validos['cargo'] = None
            if 'direccion' not in serializer.validated_data:
                raise serializers.ValidationError("direccion es requerido")
        serializer.save()


class UsuariosUsuarioViewset(viewsets.ModelViewSet):

    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = (
        AllowAny,
    )
    http_method_names = ('get',)
    ordering = ('pk',)
    ordering_fields = ('pk',)

    def list(self, request, *args, **kwargs):
        return Response('No disponible')


class UsuariosEliminarViewset(viewsets.ModelViewSet):

    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = (
        AllowAny,
    )
    http_method_names = ('delete',)
    ordering = ('pk',)
    ordering_fields = ('pk',)


class UsuariosGeoViewset(viewsets.ModelViewSet):

    queryset = Usuarios.objects.exclude(Q(latitud__isnull=False) & Q(longitud__isnull=False))
    serializer_class = UsuariosSerializer
    permission_classes = (
        AllowAny,
    )
    http_method_names = ('get',)
    ordering = ('pk',)
    ordering_fields = ('pk',)

    # gmaps = googlemaps.Client(key='AIzaSyD0txU5n7xlPZ3zkEsEjW09yVHmmEVjU4o')

