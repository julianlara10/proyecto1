from django.db.models import Q
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import viewsets, serializers, status, permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from usuarios.models import Usuarios
from usuarios.serializers import UsuariosSerializer

import googlemaps


class UsuariosListaViewset(viewsets.ModelViewSet):

    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    http_method_names = ('get',)
    ordering = ('pk',)
    ordering_fields = ('pk',)


class UsuariosCrearViewset(viewsets.ModelViewSet):

    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
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
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    http_method_names = ('get',)
    ordering = ('pk',)
    ordering_fields = ('pk',)

    def list(self, request, *args, **kwargs):
        return Response('No disponible')


class UsuariosEliminarViewset(viewsets.ModelViewSet):

    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    http_method_names = ('delete',)
    ordering = ('pk',)
    ordering_fields = ('pk',)


class UsuariosGeoViewset(viewsets.ModelViewSet):

    queryset = Usuarios.objects.filter(tipo='comprador').exclude(Q(latitud__isnull=False) & Q(longitud__isnull=False))
    serializer_class = UsuariosSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    http_method_names = ('get',)
    ordering = ('pk',)
    ordering_fields = ('pk',)
    gmaps = googlemaps.Client(key='AIzaSyD0txU5n7xlPZ3zkEsEjW09yVHmmEVjU4o')

    def list(self, request, *args, **kwargs):

        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
            for item in data:
                dir_total = f'{item["direccion"]}, {item["ciudad"]}'
                geocode_result = self.gmaps.geocode(dir_total)
                latitud = geocode_result[0]['geometry']['location']['lat']
                longitud = geocode_result[0]['geometry']['location']['lng']
                item['latitud'] = latitud
                item['longitud'] = longitud
                item['estado_geo'] = True
                instancia = queryset.filter(pk=item['id']).first()
                instancia.longitud = longitud
                instancia.latitud = latitud
                instancia.estado_geo = True
                instancia.save()
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


