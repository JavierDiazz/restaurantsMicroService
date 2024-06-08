from django.contrib import admin
from Explora.models import *

# Register your models here.
class tipoComida_admin(admin.ModelAdmin):
    list_display = ('id', 'nombreComida')
    list_filter = ('id', 'nombreComida')
    search_fields = ('id', 'nombreComida')

class tipoEstablecimiento_admin(admin.ModelAdmin):
    list_display = ('id', 'nombreEstablecimiento')
    list_filter = ('id', 'nombreEstablecimiento')
    search_fields = ('id', 'nombreEstablecimiento')

class comida_admin(admin.ModelAdmin):
    list_display = ('id', 'estiloComida')
    list_filter = ('id', 'estiloComida')
    search_fields = ('id', 'estiloComida')

class precio_admin(admin.ModelAdmin):
    list_display = ('id', 'precio')
    list_filter = ('id', 'precio')
    search_fields = ('id', 'precio')

class restaurante_admin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'pais', 'ciudad', 'direccion', 'nombreComida', 'nombreEstablecimiento', 'estiloComida', 'precio')
    list_filter = ('id', 'nombre', 'pais', 'ciudad', 'direccion', 'nombreComida', 'nombreEstablecimiento', 'estiloComida', 'precio')
    search_fields = ('id', 'nombre', 'pais', 'ciudad', 'direccion', 'nombreComida', 'nombreEstablecimiento', 'estiloComida', 'precio')


admin.site.register(TipoComida,tipoComida_admin)
admin.site.register(TipoEstablecimiento,tipoEstablecimiento_admin)
admin.site.register(Comida,comida_admin)
admin.site.register(Precio,precio_admin)
admin.site.register(Restaurante,restaurante_admin)