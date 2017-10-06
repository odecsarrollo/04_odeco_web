from django.utils import timezone

from django.db import models
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFit
from web.utils import get_image_name

from web_configurations.models import CacheConfiguration


class Cliente(models.Model):
    def imagen_upload_to(instance, filename):
        clase = ('%s %s') % ('Cliente', instance.nombre)
        new_filename = get_image_name(clase, filename)
        return "web/img/clien/%s" % new_filename

    nombre = models.CharField(max_length=60)
    logo = ProcessedImageField(
        processors=[ResizeToFit(width=190, height=150, upscale=False)],
        format='PNG',
        options={'quality': 70},
        upload_to=imagen_upload_to,
        verbose_name='Logo Aliado',
        null=True,
        blank=True
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
