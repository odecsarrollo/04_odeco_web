from django.db import models


class ClienteContacto(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    correo = models.EmailField(max_length=120)
    nro_contacto = models.CharField(max_length=120, null=True, blank=True)
    empresa = models.CharField(max_length=120)
    cargo = models.CharField(max_length=120, null=True, blank=True)
    pais = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = 'Contactos de Clientes'
        verbose_name = 'Contacto de Cliente'

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)
