from django.contrib import admin
from imagekit.admin import AdminThumbnail

from web_empresa.models import Aliado, GaleriaFotoEmpresa, GaleriaFotoEmpresaImagen

admin.site.register(Aliado)


class GaleriaFotoEmpresaImagenInline(admin.TabularInline):
    model = GaleriaFotoEmpresaImagen

    fields = ['admin_imagen_thumbnail', 'descripcion', 'orden', 'imagen']
    admin_imagen_thumbnail = AdminThumbnail(image_field='imagen_thumbnail')
    readonly_fields = ['admin_imagen_thumbnail']

    extra = 1


class GaleriaFotoEmpresaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'orden']
    list_editable = ['orden', ]

    inlines = [GaleriaFotoEmpresaImagenInline, ]


admin.site.register(GaleriaFotoEmpresa, GaleriaFotoEmpresaAdmin)
