from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.ventas_views, name='ventas'),
    path('clientes/', views.clientes_views, name='clientes'),
    path('inventario/', views.inventario_views, name='inventario'),

]