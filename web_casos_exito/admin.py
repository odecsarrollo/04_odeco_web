from django.contrib import admin
from imagekit.admin import AdminThumbnail

from .models import CasoExito, CasoExitoVideo, CasoExitoImagen, CasoExitoTestimonio, IndustriaCasoExito

admin.site.register(IndustriaCasoExito)


class CasoExitoImagenInline(admin.TabularInline):
    model = CasoExitoImagen

    fields = [
        'admin_imagen_thumbnail',
        'descripcion',
        'alt_seo',
        'orden',
        'imagen',
        'marca_agua'
    ]
    admin_imagen_thumbnail = AdminThumbnail(image_field='imagen_thumbnail')
    readonly_fields = ['admin_imagen_thumbnail']

    extra = 1

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('orden')


class CasoExitoVideoInline(admin.TabularInline):
    model = CasoExitoVideo
    fields = [
        'orden',
        'video'
    ]
    extra = 1

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('orden')


class CasoExitoTestimonioInline(admin.TabularInline):
    model = CasoExitoTestimonio
    fields = [
        'nombre_persona',
        'cargo',
        'testimonio',
        'orden'
    ]
    extra = 1

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('orden')


class CasoExitoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'activo', 'orden']
    list_editable = ['nombre', 'orden', 'activo']
    prepopulated_fields = {"slug": ("nombre",)}

    inlines = [
        CasoExitoImagenInline,
        CasoExitoVideoInline,
        CasoExitoTestimonioInline
    ]

    list_filter = ['activo']


admin.site.register(CasoExito, CasoExitoAdmin)
