from django.db import models

# Create your models here.

#Modelo de la tabla Tipo_Comida
class TipoComida(models.Model):
    nombreComida = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'TipoComida'

#Modelo de la tabla Tipo_Establecimiento
class TipoEstablecimiento(models.Model):
    nombreEstablecimiento = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'TipoEstablecimiento'

#Modelo de la tabla Comida
class Comida(models.Model):
    estiloComida = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'Comida'

#Modelo de la tabla Precio
class Precio(models.Model):
    precio = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'Precio'

#Modelo de la tabla Restaurante
class Restaurante(models.Model):
    nombre = models.CharField(max_length=50, default=None)
    pais = models.CharField(max_length=50, default=None)
    ciudad = models.CharField(max_length=50, default=None)
    direccion = models.CharField(max_length=80, default=None)
    nombreComida = models.ForeignKey(TipoComida,on_delete=models.CASCADE,default=0,related_name='nombreComida_TipoComida')
    nombreEstablecimiento = models.ForeignKey(TipoEstablecimiento,on_delete=models.CASCADE,default=0,related_name='nombreEstablecimiento_TipoEstablecimiento')
    estiloComida = models.ForeignKey(Comida,on_delete=models.CASCADE,default=0,related_name='estiloComida_Comida')
    precio = models.ForeignKey(Precio,on_delete=models.CASCADE,default=0,related_name='precio_Precio')

    class Meta:
        db_table = 'Restaurante'