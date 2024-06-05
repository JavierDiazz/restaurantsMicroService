from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class tipoComida_serializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = TipoComida
		fields = '__all__'
		
class tipoEstablecimiento_serializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = TipoEstablecimiento
		fields = '__all__'
		
class comida_serializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = Comida
		fields = '__all__'
		
class precio_serializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = Precio
		fields = '__all__'
		
class restaurante_serializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = Restaurante
		fields = '__all__'