from django.contrib import admin
from imagekit.admin import AdminThumbnail

from web_empresa.models import Aliado, GaleriaFotoEmpresa, GaleriaFotoEmpresaImagen

admin.site.register(Aliado)


class GaleriaFotoEmpresaImagenInline(admin.TabularInline):
    model = GaleriaFotoEmpresaImagen

    fields = ['admin_imagen_thumbnail', 'descripcion', 'alt_seo', 'orden', 'imagen', 'marca_agua']
    admin_imagen_thumbnail = AdminThumbnail(image_field='imagen_thumbnail')
    readonly_fields = ['admin_imagen_thumbnail']

    extra = 1

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('orden')


class GaleriaFotoEmpresaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'orden', 'activo']
    list_editable = ['orden', 'activo']

    inlines = [GaleriaFotoEmpresaImagenInline, ]


admin.site.register(GaleriaFotoEmpresa, GaleriaFotoEmpresaAdmin)
