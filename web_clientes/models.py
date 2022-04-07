from django.utils import timezone

from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFit
from web.utils import get_image_name

from web_configurations.models import CacheConfiguration


class ClienteIndustria(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    nombre_en = models.CharField(max_length=200)
    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        cache = CacheConfiguration.objects.get()
        cache.clientes_update = timezone.now()
        cache.save()

    def delete(self, using=None, keep_parents=False):
        cache = CacheConfiguration.objects.get()
        cache.clientes_update = timezone.now()
        cache.save()
        return super().delete(using, keep_parents)


class Cliente(models.Model):
    def imagen_upload_to(instance, filename):
        clase = ('%s %s') % ('Cliente', instance.nombre)
        new_filename = get_image_name(clase=clase, filename=filename)
        return "web/img/clien/%s" % new_filename

    nombre = models.CharField(max_length=60)
    industria = models.ForeignKey(ClienteIndustria, null=True, blank=True, related_name='clientes',
                                  on_delete=models.PROTECT)
    logo = ProcessedImageField(
        processors=[ResizeToFit(width=190, height=150, upscale=False)],
        format='PNG',
        options={'quality': 70},
        upload_to=imagen_upload_to,
        verbose_name='Logo Cliente',
        null=True,
        blank=True
    )
    logo_webp = ImageSpecField(
        source='logo',
        format='WEBP',
    )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        cache = CacheConfiguration.objects.get()
        cache.clientes_update = timezone.now()
        cache.save()

    def delete(self, using=None, keep_parents=False):
        cache = CacheConfiguration.objects.get()
        cache.clientes_update = timezone.now()
        cache.save()
        return super().delete(using, keep_parents)

    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre
