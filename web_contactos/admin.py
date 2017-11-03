from django.contrib import admin

from .models import ClienteContacto


class ClienteContactoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido', 'pais', 'empresa', 'cargo', 'correo', 'nro_contacto']


admin.site.register(ClienteContacto, ClienteContactoAdmin)
