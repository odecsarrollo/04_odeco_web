from django.contrib import admin

from web_clientes.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'orden']
    list_editable = ['orden']

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('orden')


admin.site.register(Cliente, ClienteAdmin)
