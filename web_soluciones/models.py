from django.db import models
from django.urls import reverse
from django.utils import timezone
from tinymce import HTMLField
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import SmartResize, ResizeToFill, ResizeToFit
from django.utils.translation import gettext_lazy as _

from model_utils.models import TimeStampedModel

from web.utils import get_image_name
from web_configurations.models import CacheConfiguration


class CategoriaItemSolucion(models.Model):
    orden = models.PositiveIntegerField(default=0, unique=True)
    nombre = models.CharField(max_length=120, default=' ', null=True, blank=True, unique=True)
    nombre_en = models.CharField(max_length=120, default=' ', null=True, blank=True, unique=True)

    def __str__(self):
        if self.nombre:
            return self.nombre
        else:
            return ''

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        qs_soluciones = self.mis_items.select_related('solucion').distinct()
        for solucion in qs_soluciones.all():
            solucion.save()

    class Meta:
        verbose_name = 'Categoría Item Solucion'
        verbose_name_plural = 'Categorías Items Soluciones'


class Solucion(TimeStampedModel):
    def header_imagen_upload_to(instance, filename):
        new_filename = get_image_name(filename=filename)
        return "web/img/solu/%s" % new_filename

    def imagen_boton_upload_to(instance, filename):
        new_filename = get_image_name(filename=filename)
        return "web/img/solu/%s" % new_filename

    nombre = models.CharField(max_length=120, verbose_name=_('Nombre'))
    nombre_en = models.CharField(max_length=120, verbose_name='Nombre en ingles', default='Nombre en Ingles')
    icono_class = models.CharField(default='', max_length=100)
    texto = HTMLField('Texto Soluciones', default='Descripción de esta solución', null=True, blank=True)
    texto_en = HTMLField('Texto Soluciones Ingles', default='Descripción de esta solución en Ingles', null=True,
                         blank=True)
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

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        cache = CacheConfiguration.objects.get()
        cache.soluciones_update = timezone.now()
        cache.save()

    def delete(self, using=None, keep_parents=False):
        cache = CacheConfiguration.objects.get()
        cache.soluciones_update = timezone.now()
        cache.save()
        return super().delete(using, keep_parents)

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
        new_filename = get_image_name(clase='Solucion Imagen principal', filename=filename)
        return "web/img/solu/%s" % new_filename

    nombre = models.CharField(max_length=120)
    nombre_en = models.CharField(max_length=120, null=True, blank=True)

    solucion = models.ForeignKey(Solucion, related_name='mis_items', on_delete=models.PROTECT)

    descripcion_corta = models.TextField(null=True, blank=True)
    descripcion_corta_en = models.TextField(null=True, blank=True)

    mas = HTMLField('Texto Item Solución', default='Descripción de este Item', null=True, blank=True)
    mas_en = HTMLField('Texto Item Solución en Ingles', null=True,
                       blank=True)
    orden = models.PositiveIntegerField(default=0)
    categoria_item = models.ForeignKey(CategoriaItemSolucion, related_name='mis_items', null=True, blank=True)

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

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        self.solucion.save()

    def __str__(self):
        return '%s - %s' % (self.solucion.nombre, self.nombre)

    class Meta:
        verbose_name = 'Item Solución'
        verbose_name_plural = 'Items Soluciones'


class ItemSolucionImagen(TimeStampedModel):
    CHOICES_MARCA_AGUA = (
        (0, 'Ninguna'),
        (1, 'Blanca'),
        (2, 'Naranja')
    )

    def imagen_upload_to(instance, filename):
        new_filename = get_image_name(filename=filename)
        return "web/img/solu/%s" % new_filename

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        self.item_solucion.solucion.save()

    marca_agua = models.PositiveIntegerField(choices=CHOICES_MARCA_AGUA, default=2)
    item_solucion = models.ForeignKey(ItemSolucion, related_name='mis_imagenes')
    orden = models.PositiveIntegerField(default=0)
    alt_seo = models.CharField(max_length=125, default='', blank=True, null=True)
    alt_seo_en = models.CharField(max_length=125, default='', blank=True, null=True)
    descripcion = models.TextField(null=True, blank=True)
    descripcion_en = models.TextField(null=True, blank=True)
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
    imagen_thumbnail_webp = ImageSpecField(
        source='imagen',
        processors=[
            ResizeToFill(128, 76),
        ],
        format='WEBP'
    )


class ItemSolucionVideo(models.Model):
    video = models.CharField(max_length=500)
    item_solucion = models.ForeignKey(ItemSolucion, related_name='mis_videos')
    orden = models.PositiveIntegerField(default=0)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        self.item_solucion.solucion.save()


class Documento(models.Model):
    def documento_upload(instance, filename):
        return "web/img/solu/docu/%s" % filename

    documento = models.FileField(upload_to=documento_upload)
    nombre = models.CharField(max_length=120)
    orden = models.PositiveIntegerField(default=0)
    icono = models.CharField(max_length=120)
    item_solucion = models.ManyToManyField(ItemSolucion, related_name='mis_documentos')
    activo = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        for solucion in self.item_solucion.all():
            solucion.save()

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
