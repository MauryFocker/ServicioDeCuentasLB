from django.shortcuts import render

# Create your views here.
def clientes_views(request):
    return render(request, 'clientes.html')