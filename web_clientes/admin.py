from django.contrib import admin

from web_clientes.models import Cliente, ClienteIndustria


class ClienteIndustriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nombre_en', 'orden']
    list_editable = ['orden']

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('orden')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'orden', 'industria']
    list_editable = ['orden', 'industria']

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('orden')


admin.site.register(ClienteIndustria, ClienteIndustriaAdmin)
admin.site.register(Cliente, ClienteAdmin)
