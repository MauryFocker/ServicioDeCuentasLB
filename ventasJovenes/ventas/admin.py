from django.contrib import admin
from ventas.models import Cliente, Producto
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class ClienteSearchResource(resources.ModelResource):
    class Meta:
        model = Cliente

# Register your models here.

class ClienteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'apellido', 'clase', 'telefono')
    search_fields = ['nombre']
    readonly_fields = ['created', 'updated']
    #Resource Class meta
    resource_class = ClienteSearchResource
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'costo', 'cantidad')
    search_fields = ['codigo', 'descripcion']
    readonly_fields = ['created', 'updated']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

#Invocar clases al panel de admin de django    
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)