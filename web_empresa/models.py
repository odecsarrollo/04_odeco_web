from django.db import models
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFit
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
