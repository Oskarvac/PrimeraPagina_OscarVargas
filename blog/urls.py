from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('producto/', views.agregar_producto, name='producto'),
    path('categoria/', views.agregar_categoria, name='categoria'),
    path('marca/', views.agregar_marca, name='marca'),
    path('buscar/', views.buscar_producto, name='buscar'),
]
