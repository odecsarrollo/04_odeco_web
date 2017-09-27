from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFit, ResizeToFill
from web.utils import get_image_name


class Aliado(models.Model):
    def imagen_upload_to(instance, filename):
        clase = ('%s %s') % ('Aliado', instance.nombre)
        new_filename = get_image_name(clase, filename)
        return "web/img/empr/%s" % new_filename

    nombre = models.CharField(max_length=60)
    logo = ProcessedImageField(
        processors=[ResizeToFit(width=190, height=101, upscale=False)],
        format='PNG',
        options={'quality': 70},
        upload_to=imagen_upload_to,
        verbose_name='Logo Aliado',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nombre


class GaleriaFotoEmpresa(models.Model):
    def imagen_upload_to(instance, filename):
        clase = ('%s %s') % ('Galeria', instance.nombre)
        new_filename = get_image_name(clase, filename)
        return "web/img/empr/%s" % new_filename

    nombre = models.CharField(max_length=20)
    icono = models.CharField(max_length=40, help_text='Encontrar en http://fontawesome.io/')
    orden = models.PositiveIntegerField(default=0)
    imagen = ProcessedImageField(
        processors=[ResizeToFit(width=1024, height=768, upscale=False)],
        format='JPEG',
        options={'quality': 70},
        upload_to=imagen_upload_to,
        verbose_name='Imagen principal galería',
        null=True,
        blank=True
    )

    imagen_thumbnail = ImageSpecField(
        source='imagen',
        processors=[
            ResizeToFill(430, 246),
        ],
        format='JPEG'
    )

    imagen_thumbnail_galeria = ImageSpecField(
        source='imagen',
        processors=[
            ResizeToFill(123, 82),
        ],
        format='JPEG'
    )

    class Meta:
        verbose_name_plural = 'Galerías de Fotos Emperesa'
        verbose_name = 'Galería de Fotos Empresa'


class GaleriaFotoEmpresaImagen(models.Model):
    def imagen_upload_to(instance, filename):
        clase = ('%s %s') % ('Imagen Galeria', instance.galeria.nombre)
        new_filename = get_image_name(clase, filename)
        return "web/img/empr/%s" % new_filename

    galeria = models.ForeignKey(GaleriaFotoEmpresa, related_name='mis_imagenes')
    orden = models.PositiveIntegerField(default=0)
    descripcion = models.TextField(null=True, blank=True)
    imagen = ProcessedImageField(
        processors=[ResizeToFit(width=1024, height=768, upscale=False)],
        format='JPEG',
        options={'quality': 70},
        upload_to=imagen_upload_to,
        verbose_name='Imagen Item Solución',
        null=True,
        blank=True
    )
    imagen_thumbnail = ImageSpecField(
        source='imagen',
        processors=[
            ResizeToFill(123, 82),
        ],
        format='JPEG'
    )
