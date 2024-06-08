from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from rest_framework import serializers
from rest_framework import viewsets
from django.core.serializers import serialize
from rest_framework.permissions import IsAuthenticated
from .serializers import *

"""
    Viewsets del modelo.

    Esta vista permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
    en los modelos.

    Permisos:
    - El usuario debe estar autenticado para acceder a esta vista.

    Serializer:
    - Se utiliza 'x_serializer' para serializar los datos del modelo.

    Atributos:
    - serializer_class: Clase del serializador utilizado.
    - permission_classes: Clases de permisos aplicadas a la vista.
    - queryset: Conjunto de objetos del modelo.

    Métodos HTTP admitidos:
    - GET: Obtiene una lista de usuarios.
    - POST: Crea un nuevo usuario.
    - PUT: Actualiza un usuario existente.
    - DELETE: Elimina un usuario existente.

    Gestión de solicutudes HTTP VIEWSETS:
    list: Maneja las solicitudes GET para obtener una lista de recursos.
    create: Maneja las solicitudes POST para crear un nuevo recurso.
    retrieve: Maneja las solicitudes GET para obtener un recurso específico por su clave primaria.
    update: Maneja las solicitudes PUT para actualizar un recurso específico por su clave primaria.
    partial_update: Maneja las solicitudes PATCH para realizar una actualización parcial de un recurso específico por su clave primaria.
    destroy: Maneja las solicitudes DELETE para eliminar un recurso específico por su clave primaria.
"""
# Create your views here.
class tipoComida_viewsets (viewsets.ModelViewSet):
    serializer_class = tipoComida_serializer
    #permission_classes = (IsAuthenticated,)
    queryset = tipoComida_serializer.Meta.model.objects.all()

class tipoEstablecimiento_viewsets (viewsets.ModelViewSet):
    serializer_class = tipoEstablecimiento_serializer
    #permission_classes = (IsAuthenticated,)
    queryset = tipoEstablecimiento_serializer.Meta.model.objects.all()

class comida_viewsets (viewsets.ModelViewSet):
    serializer_class = comida_serializer
    #permission_classes = (IsAuthenticated,)
    queryset = comida_serializer.Meta.model.objects.all()

class precio_viewsets (viewsets.ModelViewSet):
    serializer_class = precio_serializer
    #permission_classes = (IsAuthenticated,)
    queryset = precio_serializer.Meta.model.objects.all()

class restaurante_viewsets (viewsets.ModelViewSet):
    serializer_class = restaurante_serializer
    #permission_classes = (IsAuthenticated,)
    queryset = restaurante_serializer.Meta.model.objects.all()