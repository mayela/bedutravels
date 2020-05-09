from rest_framework import viewsets

from django.shortcuts import render
from django.contrib.auth.models import User

from .serializers import UserSerializer, ZonaSerializer, TourSerializer
from .models import Tour, Zona

def index(request):
    """ Vista para atender la petición de la url / """
    return render(request, "tours/index.html")


class UserViewSet(viewsets.ModelViewSet):
   """
   API que permite realizar operaciones en la tabla User
   """
   # Se define el conjunto de datos sobre el que va a operar la vista,
   # en este caso sobre todos los users disponibles.
   queryset = User.objects.all().order_by('id')
   # Se define el Serializador encargado de transformar la peticiones
   # en formato JSON a objetos de Django y de Django a JSON.
   serializer_class = UserSerializer

class TourViewSet(viewsets.ModelViewSet):
   """
   API que permite realizar operaciones en la tabla Tour
   """
   # Se define el conjunto de datos sobre el que va a operar la vista,
   # en este caso sobre todos los tours disponibles.
   queryset = Tour.objects.all().order_by('id')
   # Se define el Serializador encargado de transformar la peticiones
   # en formato JSON a objetos de Django y de Django a JSON.
   serializer_class = TourSerializer


class ZonaViewSet(viewsets.ModelViewSet):
    queryset = Zona.objects.all().order_by('id')
    serializer_class = ZonaSerializer