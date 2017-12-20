from django.db.models.signals import pre_delete, post_init, post_save
from django.dispatch import receiver

from .models import CasoExito, CasoExitoImagen


# region CasoExito

@receiver(pre_delete, sender=CasoExito)
def imagen_principal_caso_exito_delete(sender, instance, **kwargs):
    instance.imagen_principal.delete(False)


@receiver(post_init, sender=CasoExito)
def backup_imagen_principal_caso_exito_path(sender, instance, **kwargs):
    instance._current_imagen = instance.imagen_principal


@receiver(post_save, sender=CasoExito)
def delete_imagen_principal_caso_exito(sender, instance, **kwargs):
    if hasattr(instance, '_current_imagen'):
        if instance._current_imagen != instance.imagen_principal:
            instance._current_imagen.delete(save=False)


# endregion


# region CasoExitoImagen

@receiver(pre_delete, sender=CasoExitoImagen)
def imagen_galeria_foto_caso_exito_imagen_delete(sender, instance, **kwargs):
    instance.imagen.delete(False)


@receiver(post_init, sender=CasoExitoImagen)
def backup_imagen_galeria_foto_caso_exito_imagen_path(sender, instance, **kwargs):
    instance._current_imagen = instance.imagen


@receiver(post_save, sender=CasoExitoImagen)
def delete_imagen_galeria_foto_caso_exito_imagen(sender, instance, **kwargs):
    if hasattr(instance, '_current_imagen'):
        if instance._current_imagen != instance.imagen:
            instance._current_imagen.delete(save=False)

# endregion
