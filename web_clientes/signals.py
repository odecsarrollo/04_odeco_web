from django.db.models.signals import pre_delete, post_init, post_save
from django.dispatch import receiver

from .models import Cliente


# region Cliente

@receiver(pre_delete, sender=Cliente)
def logo_cliente_pre_delete(sender, instance, **kwargs):
    instance.logo.delete(False)


@receiver(post_init, sender=Cliente)
def backup_logo_cliente_path(sender, instance, **kwargs):
    instance._current_imagen = instance.logo


@receiver(post_save, sender=Cliente)
def delete_logo_cliente(sender, instance, **kwargs):
    if hasattr(instance, '_current_imagen'):
        if instance._current_imagen != instance.logo:
            instance._current_imagen.delete(save=False)

# endregion
