from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
"""
    Endpoints
"""
router.register(r'tipoComida', tipoComida_viewsets,basename='tipoComida')
router.register(r'tipoEstablecimiento', tipoEstablecimiento_viewsets,basename='tipoEstablecimiento')
router.register(r'comida', comida_viewsets,basename='comida')
router.register(r'precio', precio_viewsets,basename='precio')
router.register(r'restaurante', restaurante_viewsets,basename='restaurante')

urlpatterns = router.urls