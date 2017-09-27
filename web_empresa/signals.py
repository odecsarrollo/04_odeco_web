from django.db.models.signals import pre_delete, post_init, post_save
from django.dispatch import receiver

from .models import Aliado, GaleriaFotoEmpresa, GaleriaFotoEmpresaImagen


# region Aliado

@receiver(pre_delete, sender=Aliado)
def logo_aliado_pre_delete(sender, instance, **kwargs):
    instance.logo.delete(False)


@receiver(post_init, sender=Aliado)
def backup_logo_aliado_path(sender, instance, **kwargs):
    instance._current_imagen = instance.logo


@receiver(post_save, sender=Aliado)
def delete_aliado_cliente(sender, instance, **kwargs):
    if hasattr(instance, '_current_imagen'):
        if instance._current_imagen != instance.logo:
            instance._current_imagen.delete(save=False)


# endregion

# region GaleriaFotoEmpresa

@receiver(pre_delete, sender=GaleriaFotoEmpresa)
def imagen_galeria_foto_empresa_delete(sender, instance, **kwargs):
    instance.imagen.delete(False)


@receiver(post_init, sender=GaleriaFotoEmpresa)
def backup_imagen_galeria_foto_empresa_path(sender, instance, **kwargs):
    instance._current_imagen = instance.imagen


@receiver(post_save, sender=GaleriaFotoEmpresa)
def delete_imagen_galeria_foto_empresa(sender, instance, **kwargs):
    if hasattr(instance, '_current_imagen'):
        if instance._current_imagen != instance.imagen:
            instance._current_imagen.delete(save=False)


# endregion

# region GaleriaFotoEmpresaImagen

@receiver(pre_delete, sender=GaleriaFotoEmpresaImagen)
def imagen_galeria_foto_empresa_imagen_delete(sender, instance, **kwargs):
    instance.imagen.delete(False)


@receiver(post_init, sender=GaleriaFotoEmpresaImagen)
def backup_imagen_galeria_foto_empresa_imagen_path(sender, instance, **kwargs):
    instance._current_imagen = instance.imagen


@receiver(post_save, sender=GaleriaFotoEmpresaImagen)
def delete_imagen_galeria_foto_empresa_imagen(sender, instance, **kwargs):
    if hasattr(instance, '_current_imagen'):
        if instance._current_imagen != instance.imagen:
            instance._current_imagen.delete(save=False)

# endregion
