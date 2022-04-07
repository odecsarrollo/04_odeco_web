from django.db import models

from tinymce.models import HTMLField
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill, ResizeToFit

from web.utils import get_image_name
from web_clientes.models import Cliente

from model_utils.models import TimeStampedModel


class IndustriaCasoExito(models.Model):
    nombre = models.CharField(max_length=120)
    nombre_en = models.CharField(max_length=120, null=True, blank=True, verbose_name='Nombre en Ingles')
    icono = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Industria'
        verbose_name_plural = 'Industrias'


class CasoExito(TimeStampedModel):
    def imagen_principal_upload_to(instance, filename):
        new_filename = get_image_name('Caso Exito principal', filename)
        return "web/img/casexi/%s" % new_filename

    nombre = models.CharField(max_length=120, verbose_name='Nombre')
    nombre_en = models.CharField(max_length=120, verbose_name='Nombre en Ingles', null=True, blank=True)

    descripcion_corta = models.TextField(null=True, blank=True, verbose_name='Descripción Corta')
    descripcion_corta_en = models.TextField(null=True, blank=True, verbose_name='Descripción Corta Ingles')

    descripcion = HTMLField('Descripción', default='Descripción de este Caso de Éxito', null=True, blank=True)
    descripcion_en = HTMLField('Descripción Ingles', null=True, blank=True)

    orden = models.PositiveIntegerField(default=0)
    industria = models.ForeignKey(IndustriaCasoExito, related_name='mis_casos_exito', on_delete=models.PROTECT)
    fecha_entrega = models.DateField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    cliente = models.ForeignKey(Cliente, related_name='mis_casos_exito', null=True, blank=True,
                                on_delete=models.PROTECT)
    activo = models.BooleanField(default=False)
    imagen_principal = ProcessedImageField(
        processors=[ResizeToFit(width=400, height=200, upscale=False)],
        format='JPEG',
        options={'quality': 80},
        upload_to=imagen_principal_upload_to,
        verbose_name='Imagen Caso Éxito (400x200)',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Caso de Éxito'
        verbose_name_plural = 'Casos de Éxito'


class CasoExitoImagen(models.Model):
    CHOICES_MARCA_AGUA = (
        (0, 'Ninguna'),
        (1, 'Blanca'),
        (2, 'Naranja')
    )

    def imagen_upload_to(instance, filename):
        new_filename = get_image_name('Imagen Caso Exito', filename)
        return "web/img/casexi/%s" % new_filename

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        self.caso_exito.save()

    marca_agua = models.PositiveIntegerField(choices=CHOICES_MARCA_AGUA, default=2)
    caso_exito = models.ForeignKey(CasoExito, related_name='mis_imagenes', on_delete=models.PROTECT)
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


class CasoExitoVideo(models.Model):
    video = models.CharField(max_length=500)
    caso_exito = models.ForeignKey(CasoExito, related_name='mis_videos', on_delete=models.PROTECT)
    orden = models.PositiveIntegerField(default=0)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        self.caso_exito.save()


class CasoExitoTestimonio(models.Model):
    caso_exito = models.ForeignKey(CasoExito, related_name='mis_testimonios', on_delete=models.PROTECT)
    nombre_persona = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200, null=True, blank=True)
    testimonio = models.TextField()
    orden = models.PositiveIntegerField(default=0)
