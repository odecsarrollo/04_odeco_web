from django.db.models.signals import pre_delete, post_init, post_save
from django.dispatch import receiver

from .models import Solucion, ItemSolucion, ItemSolucionImagen


# region Solucion

@receiver(pre_delete, sender=Solucion)
def header_imagen_solucion_pre_delete(sender, instance, **kwargs):
    instance.header_imagen.delete(False)
    instance.boton_soluciones.delete(False)


@receiver(post_init, sender=Solucion)
def backup_header_imagen_solucion_path(sender, instance, **kwargs):
    instance._current_imagen = instance.header_imagen
    instance._current_imagen_boton = instance.boton_soluciones


@receiver(post_save, sender=Solucion)
def delete_header_imagen_solucion(sender, instance, **kwargs):
    if hasattr(instance, '_current_imagen'):
        if instance._current_imagen != instance.header_imagen:
            instance._current_imagen.delete(save=False)
    if hasattr(instance, '_current_imagen_boton'):
        if instance._current_imagen_boton != instance.boton_soluciones:
            instance._current_imagen_boton.delete(save=False)


# endregion


# region ItemSolucion

@receiver(pre_delete, sender=ItemSolucion)
def imagen_principal_item_solucion_delete(sender, instance, **kwargs):
    instance.imagen_principal.delete(False)


@receiver(post_init, sender=ItemSolucion)
def backup_imagen_principal_item_solucion_path(sender, instance, **kwargs):
    instance._current_imagen = instance.imagen_principal


@receiver(post_save, sender=ItemSolucion)
def delete_imagen_principal_item_solucion(sender, instance, **kwargs):
    if hasattr(instance, '_current_imagen'):
        if instance._current_imagen != instance.imagen_principal:
            instance._current_imagen.delete(save=False)


# endregion



# region ItemSolucionImagen

@receiver(pre_delete, sender=ItemSolucionImagen)
def imagen_galeria_foto_empresa_imagen_delete(sender, instance, **kwargs):
    instance.imagen.delete(False)


@receiver(post_init, sender=ItemSolucionImagen)
def backup_imagen_galeria_foto_empresa_imagen_path(sender, instance, **kwargs):
    instance._current_imagen = instance.imagen


@receiver(post_save, sender=ItemSolucionImagen)
def delete_imagen_galeria_foto_empresa_imagen(sender, instance, **kwargs):
    if hasattr(instance, '_current_imagen'):
        if instance._current_imagen != instance.imagen:
            instance._current_imagen.delete(save=False)

# endregion
