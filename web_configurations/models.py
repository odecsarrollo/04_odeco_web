from django.db import models
from solo.models import SingletonModel
from tinymce import HTMLField
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFit, SmartResize

from web.utils import get_image_name


class IndexConfiguration(SingletonModel):
    def header_imagen_upload_to(instance, filename):
        new_filename = get_image_name('Header', filename)
        return "web/img/index/%s" % new_filename

    header_titulo = models.CharField(max_length=150, default='Aqui el titulo')
    header_text = models.TextField(max_length=150, default='Aqui la descripción', null=True, blank=True)
    header_imagen = ProcessedImageField(
        processors=[SmartResize(width=2560, height=1500, upscale=False)],
        format='JPEG',
        options={'quality': 50},
        upload_to=header_imagen_upload_to,
        verbose_name='Imagen Cabezote (2560 x 1500)',
        null=True,
        blank=True
    )

    def __unicode__(self):
        return "Index"

    class Meta:
        verbose_name = "Index"


class GeneralConfiguration(SingletonModel):
    direccion = models.CharField(max_length=200, default='Dirección aquí', verbose_name='Dirección')
    horarios_de_atencion = HTMLField('Horarios de Atención', default='Texto Horarios de Atención aquí')
    numeros_contacto = HTMLField('Numeros de Contacto', default='Numeros de contacto', null=True, blank=True)
    correos_contacto = HTMLField('Correos de Contacto', default='Correos de contacto', null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    youtube = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return "General"

    class Meta:
        verbose_name = "General"


class LaEmpresaConfiguration(SingletonModel):
    def imagen_principal_upload_to(instance, filename):
        new_filename = get_image_name('La Empresa Principal', filename)
        return "web/img/empr/%s" % new_filename

    titulo = models.CharField(max_length=150, default='Aqui el titulo')
    texto = HTMLField('Horarios de Atención', default='Aqui la descripción')
    imagen_principal = ProcessedImageField(
        processors=[SmartResize(width=570, height=362, upscale=False)],
        format='JPEG',
        options={'quality': 70},
        upload_to=imagen_principal_upload_to,
        verbose_name='Imagen Principal (570x362)',
        null=True,
        blank=True
    )

    def __unicode__(self):
        return "La Empresa"

    class Meta:
        verbose_name = "La Empresa"


class CacheConfiguration(SingletonModel):
    nombre_cache_empresa = models.CharField(max_length=40, verbose_name='Empresa Nombre Cache',
                                            help_text='Cambiar por cada cambio en Empresa, Aliados o Galeria Empresa',
                                            default='cache inicial empresa')
    tiempo_cache_empresa = models.PositiveIntegerField(verbose_name='Empresa Tiempo Cache', default=86400)
    nombre_cache_clientes = models.CharField(max_length=40, verbose_name='Clientes Nombre Cache',
                                             help_text='Cambiar por cada cambio en Clientes',
                                             default='cache inicial clientes'
                                             )
    tiempo_cache_clientes = models.PositiveIntegerField(verbose_name='Clientes Tiempo Cache', default=86400)
    nombre_cache_index_header = models.CharField(max_length=40, verbose_name='Index Header Nombre Cache',
                                                 help_text='Cambiar por cada cambio en Index Header',
                                                 default='Index Header'
                                                 )
    tiempo_cache_index_header = models.PositiveIntegerField(verbose_name='Index Header Tiempo Cache', default=86400)

    def __unicode__(self):
        return "Caches Index"

    class Meta:
        verbose_name = "Cache Index"
