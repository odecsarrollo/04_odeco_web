from django.db.models.signals import pre_delete, post_init, post_save
from django.dispatch import receiver

from .models import IndexConfiguration, LaEmpresaConfiguration


# region IndexConfiguration

@receiver(pre_delete, sender=IndexConfiguration)
def header_imagen_index_cofiguration_pre_delete(sender, instance, **kwargs):
    instance.header_imagen.delete(False)
    instance.overlay_publicidad.delete(False)


@receiver(post_init, sender=IndexConfiguration)
def backup_header_imagen_index_cofiguration_path(sender, instance, **kwargs):
    instance._current_imagen = instance.header_imagen
    instance._current_imagen_overlay_publicidad = instance.overlay_publicidad


@receiver(post_save, sender=IndexConfiguration)
def delete_header_imagen_index_cofiguration(sender, instance, **kwargs):
    if hasattr(instance, '_current_imagen'):
        if instance._current_imagen != instance.header_imagen:
            instance._current_imagen.delete(save=False)
    if hasattr(instance, '_current_imagen_overlay_publicidad'):
        if instance._current_imagen_overlay_publicidad != instance.overlay_publicidad:
            instance._current_imagen_overlay_publicidad.delete(save=False)


# endregion



# region LaEmpresaConfiguration

@receiver(pre_delete, sender=LaEmpresaConfiguration)
def imagen_principal_la_empresa_pre_delete(sender, instance, **kwargs):
    instance.imagen_principal.delete(False)


@receiver(post_init, sender=LaEmpresaConfiguration)
def backup_imagen_principal_la_empresa_path(sender, instance, **kwargs):
    instance._current_imagen = instance.imagen_principal


@receiver(post_save, sender=LaEmpresaConfiguration)
def delete_imagen_principal_la_empresa(sender, instance, **kwargs):
    if hasattr(instance, '_current_imagen'):
        if instance._current_imagen != instance.imagen_principal:
            instance._current_imagen.delete(save=False)

# endregion
