from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField, ImageSpecField
from tinymce import HTMLField
from pilkit.processors import SmartResize, ResizeToFill, ResizeToFit

from web.utils import get_image_name


class Solucion(models.Model):
    def header_imagen_upload_to(instance, filename):
        new_filename = get_image_name('Header', filename)
        return "web/img/solu/%s" % new_filename

    def imagen_boton_upload_to(instance, filename):
        new_filename = get_image_name('Boton Solucion', filename)
        return "web/img/solu/%s" % new_filename

    nombre = models.CharField(max_length=120)
    texto = HTMLField('Texto Soluciones', default='Descripción de esta solución', null=True, blank=True)
    descripcion_corta = models.TextField(null=True, blank=True)
    boton_soluciones = ProcessedImageField(
        processors=[SmartResize(width=85, height=85, upscale=False)],
        format='PNG',
        options={'quality': 70},
        upload_to=imagen_boton_upload_to,
        verbose_name='Imagen Boton',
        null=True,
        blank=True
    )
    orden = models.PositiveIntegerField(default=0)
    slug = models.SlugField(null=True, blank=True)

    header_imagen = ProcessedImageField(
        processors=[SmartResize(width=2560, height=588, upscale=False)],
        format='JPEG',
        options={'quality': 70},
        upload_to=header_imagen_upload_to,
        verbose_name='Imagen Cabezote',
        null=True,
        blank=True
    )

    def get_absolute_url(self):
        if self.slug:
            return reverse('web_soluciones:solucion_detail_slug', kwargs={"slug": self.slug})
        return reverse('web_soluciones:solucion_detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Solución'
        verbose_name_plural = 'Soluciones'


class ItemSolucion(models.Model):
    def imagen_principal_upload_to(instance, filename):
        new_filename = get_image_name('Solucion Imagen principal', filename)
        return "web/img/solu/%s" % new_filename

    nombre = models.CharField(max_length=120)
    solucion = models.ForeignKey(Solucion, related_name='mis_items', on_delete=models.PROTECT)
    descripcion_corta = models.TextField(null=True, blank=True)
    mas = HTMLField('Texto Soluciones', default='Descripción de este Item', null=True, blank=True)
    orden = models.PositiveIntegerField(default=0)
    categoria = models.CharField(max_length=120, default='', blank=True)
    categoria_dos = models.CharField(max_length=120, default='', blank=True)
    imagen_principal = ProcessedImageField(
        processors=[ResizeToFit(width=400, height=200, upscale=False)],
        format='JPEG',
        options={'quality': 80},
        upload_to=imagen_principal_upload_to,
        verbose_name='Imagen Item Solución (400x200)',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Item Solución'
        verbose_name_plural = 'Items Soluciones'


class ItemSolucionImagen(models.Model):
    def imagen_upload_to(instance, filename):
        new_filename = get_image_name('Imagen Solucion', filename)
        return "web/img/solu/%s" % new_filename

    item_solucion = models.ForeignKey(ItemSolucion, related_name='mis_imagenes', on_delete=models.PROTECT)
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
            ResizeToFill(128, 76),
        ],
        format='JPEG'
    )
