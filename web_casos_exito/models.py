from django.db import models

from tinymce import HTMLField
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import SmartResize, ResizeToFill, ResizeToFit

from web.utils import get_image_name


class CasoExito(models.Model):
    def imagen_principal_upload_to(instance, filename):
        new_filename = get_image_name('Solucion Imagen principal', filename)
        return "web/img/casexi/%s" % new_filename

    nombre = models.CharField(max_length=120)
    descripcion_corta = models.TextField(null=True, blank=True)
    descripcion = HTMLField('Descripción', default='Descripción de este Caso de Éxito', null=True, blank=True)
    orden = models.PositiveIntegerField(default=0)
    categoria = models.CharField(max_length=120, default='', blank=True)
    categoria_dos = models.CharField(max_length=120, default='', blank=True)
    activo = models.BooleanField(default=False)
    imagen_principal = ProcessedImageField(
        processors=[ResizeToFit(width=400, height=200, upscale=False)],
        format='JPEG',
        options={'quality': 80},
        upload_to=imagen_principal_upload_to,
        verbose_name='Imagen Item Solución (400x200)',
        null=True,
        blank=True
    )

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     super().save(force_insert, force_update, using, update_fields)
    #     self.solucion.save()
    #
    # def __str__(self):
    #     return '%s - %s' % (self.solucion.nombre, self.nombre)

    class Meta:
        verbose_name = 'Item Solución'
        verbose_name_plural = 'Items Soluciones'


class ItemSolucionImagen(models.Model):
    CHOICES_MARCA_AGUA = (
        (0, 'Ninguna'),
        (1, 'Blanca'),
        (2, 'Naranja')
    )

    def imagen_upload_to(instance, filename):
        new_filename = get_image_name('Imagen Solucion', filename)
        return "web/img/casexi/%s" % new_filename

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     super().save(force_insert, force_update, using, update_fields)
    #     self.item_solucion.solucion.save()

    marca_agua = models.PositiveIntegerField(choices=CHOICES_MARCA_AGUA, default=2)
    caso_exito = models.ForeignKey(CasoExito, related_name='mis_imagenes')
    orden = models.PositiveIntegerField(default=0)
    alt_seo = models.CharField(max_length=125, default='', blank=True, null=True)
    descripcion = models.TextField(null=True, blank=True)
    imagen = ProcessedImageField(
        processors=[ResizeToFit(width=1024, height=768, upscale=False)],
        format='JPEG',
        options={'quality': 70},
        upload_to=imagen_upload_to,
        verbose_name='Imagen Caso de Exito',
        null=True,
        blank=True
    )
    imagen_thumbnail = ImageSpecField(
        source='imagen',
        processors=[
            ResizeToFill(128, 76),
        ],
        format='JPEG'
    )


class ItemSolucionVideo(models.Model):
    video = models.CharField(max_length=500)
    caso_exito = models.ForeignKey(CasoExito, related_name='mis_videos')
    orden = models.PositiveIntegerField(default=0)

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     super().save(force_insert, force_update, using, update_fields)
    #     self.item_solucion.solucion.save()
