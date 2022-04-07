from django.db import models
from django.utils import timezone
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFit, ResizeToFill
from web.utils import get_image_name

from model_utils.models import TimeStampedModel

from web_configurations.models import CacheConfiguration


class MixingCacheConfiguration(object):
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        cache = CacheConfiguration.objects.get()
        cache.empresa_update = timezone.now()
        cache.save()

    def delete(self, using=None, keep_parents=False):
        cache = CacheConfiguration.objects.get()
        cache.empresa_update = timezone.now()
        cache.save()
        return super().delete(using, keep_parents)


class Aliado(MixingCacheConfiguration, models.Model):
    def imagen_upload_to(instance, filename):
        clase = ('%s %s') % ('Aliado', instance.nombre)
        new_filename = get_image_name(clase=clase, filename=filename)
        return "web/img/empr/%s" % new_filename

    nombre = models.CharField(max_length=60)
    url = models.URLField(null=True, blank=True)
    logo = ProcessedImageField(
        processors=[ResizeToFit(width=190, height=101, upscale=False)],
        format='PNG',
        options={'quality': 60},
        upload_to=imagen_upload_to,
        verbose_name='Logo Aliado',
        null=True,
        blank=True
    )
    logo_webp = ImageSpecField(
        processors=[ResizeToFit(width=190, height=101, upscale=False)],
        source='logo',
        format='WEBP',
    )

    def __str__(self):
        return self.nombre


class GaleriaFotoEmpresa(MixingCacheConfiguration, TimeStampedModel):
    CHOICES_MARCA_AGUA = (
        (0, 'Ninguna'),
        (1, 'Blanca'),
        (2, 'Naranja')
    )

    def imagen_upload_to(instance, filename):
        clase = ('%s %s') % ('Galeria', instance.nombre)
        new_filename = get_image_name(clase=clase, filename=filename)
        return "web/img/empr/%s" % new_filename

    marca_agua = models.PositiveIntegerField(choices=CHOICES_MARCA_AGUA, default=2)
    nombre = models.CharField(max_length=20)
    icono = models.CharField(max_length=40, help_text='Encontrar en http://fontawesome.io/')
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=False)
    imagen = ProcessedImageField(
        processors=[ResizeToFit(width=1920, height=1080, upscale=False)],
        format='JPEG',
        options={'quality': 71},
        upload_to=imagen_upload_to,
        verbose_name='Imagen principal galería',
        null=True,
        blank=True
    )

    imagen_webp = ImageSpecField(
        source='imagen',
        format='WEBP'
    )

    imagen_thumbnail = ImageSpecField(
        source='imagen',
        processors=[
            ResizeToFill(430, 246),
        ],
        format='JPEG'
    )

    imagen_thumbnail_webp = ImageSpecField(
        source='imagen',
        processors=[
            ResizeToFill(430, 246),
        ],
        format='WEBP'
    )

    imagen_thumbnail_galeria = ImageSpecField(
        source='imagen',
        processors=[
            ResizeToFill(162, 108),
        ],
        format='JPEG'
    )
    imagen_thumbnail_galeria_webp = ImageSpecField(
        source='imagen',
        processors=[
            ResizeToFill(162, 108),
        ],
        format='WEBP',
    )

    class Meta:
        verbose_name_plural = 'Galerías de Fotos Emperesa'
        verbose_name = 'Galería de Fotos Empresa'


class GaleriaFotoEmpresaImagen(models.Model):
    CHOICES_MARCA_AGUA = (
        (0, 'Ninguna'),
        (1, 'Blanca'),
        (2, 'Naranja')
    )

    def imagen_upload_to(instance, filename):
        clase = ('%s %s') % ('Imagen Galeria', instance.galeria.nombre)
        new_filename = get_image_name(clase=clase, filename=filename)
        return "web/img/empr/%s" % new_filename

    galeria = models.ForeignKey(GaleriaFotoEmpresa, related_name='mis_imagenes')
    orden = models.PositiveIntegerField(default=0)
    descripcion = models.TextField(null=True, blank=True)
    marca_agua = models.PositiveIntegerField(choices=CHOICES_MARCA_AGUA, default=2)
    alt_seo = models.CharField(max_length=125, default='', blank=True, null=True)
    imagen = ProcessedImageField(
        processors=[ResizeToFit(width=1920, height=1080, upscale=False)],
        format='JPEG',
        options={'quality': 71},
        upload_to=imagen_upload_to,
        verbose_name='Imagen Item Solución',
        null=True,
        blank=True
    )
    imagen_thumbnail = ImageSpecField(
        source='imagen',
        processors=[
            ResizeToFill(162, 108),
        ],
        format='JPEG'
    )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        self.galeria.save()

    def delete(self, using=None, keep_parents=False):
        self.galeria.save()
        return super().delete(using, keep_parents)
