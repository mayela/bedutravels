from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Zona, Tour


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class TourSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Tour """
    class Meta:
        # Se define sobre que modelo actúa
        model = Tour
        # Se definen los campos a incluir
        fields = ('id', 'nombre', 'slug', 'operador', 'tipoDeTour',
         'descripcion', 'img', 'pais', 'zonaSalida', 'zonaLlegada')


class ZonaSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Zona """

    # Se define la relación de una zona y sus tours realizados
    tours_salida = TourSerializer(many=True, read_only=True)
    tours_llegada = TourSerializer(many=True, read_only=True)

    class Meta:
        # Se define sobre que modelo actúa
        model = Zona
        # Se definen los campos a incluir
        fields = ('id', 'nombre', 'descripcion', 'latitud', 'longitud', 'tours_salida', 'tours_llegada')