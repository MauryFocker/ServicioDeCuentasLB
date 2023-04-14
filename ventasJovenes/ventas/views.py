from django.shortcuts import render
from .models import Cliente, Producto


# Create your views here.
def ventas_views(request):
    return render(request, 'ventas.html')

def clientes_views(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes
    }
    return render(request, 'clientes.html')

def inventario_views(request):
    return render(request, 'inventario.html')