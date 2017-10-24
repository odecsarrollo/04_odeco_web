from django.contrib import admin
from imagekit.admin import AdminThumbnail

from web_soluciones.models import Solucion, ItemSolucion, ItemSolucionImagen


class SolucionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'orden']
    list_editable = ['orden', ]

    prepopulated_fields = {"slug": ("nombre",)}

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('orden')


admin.site.register(Solucion, SolucionAdmin)


class ItemSolucionImagenInline(admin.TabularInline):
    model = ItemSolucionImagen

    fields = ['admin_imagen_thumbnail', 'descripcion', 'orden', 'imagen', 'marca_agua']
    admin_imagen_thumbnail = AdminThumbnail(image_field='imagen_thumbnail')
    readonly_fields = ['admin_imagen_thumbnail']

    extra = 1

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('orden')


class ItemSolucionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'solucion', 'orden', 'categoria', 'categoria_dos']
    list_editable = ['nombre', 'orden', 'categoria', 'categoria_dos']

    inlines = [ItemSolucionImagenInline, ]

    list_filter = ['solucion', 'categoria', 'categoria_dos']


admin.site.register(ItemSolucion, ItemSolucionAdmin)
