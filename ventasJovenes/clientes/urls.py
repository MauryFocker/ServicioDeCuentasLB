from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.clientes_views, name='clientes'),

]