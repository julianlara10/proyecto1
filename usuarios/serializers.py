from rest_framework import serializers

from usuarios.models import Usuarios
from usuarios.utils import TIPO, CARGO


class UsuariosSerializer(serializers.ModelSerializer):
    tipo = serializers.CharField(required=True)

    class Meta:
        model = Usuarios
        fields = '__all__'

    def validate_tipo(self, value):

        choices_tipo = dict(TIPO)

        if value not in choices_tipo:
            raise serializers.ValidationError(f'El tipo debe ser uno de: {list(choices_tipo.keys())}')
        return value

    def validate_cargo(self, value):

        choices_cargo = dict(CARGO)

        if value not in choices_cargo:
            raise serializers.ValidationError(f'El cargo debe ser uno de: {list(choices_cargo.keys())}')
        return value
