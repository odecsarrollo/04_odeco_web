from django.db import models
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFit
from web.utils import get_image_name


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

    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre
