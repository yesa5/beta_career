from django.db.models.signals import pre_save
from django.dispatch import receiver

from sdu_beta_career.access_control.config import DEFAULT_ACCESS_CONTROL
from sdu_beta_career.access_control.models import AccessControl
from .models import User


@receiver(pre_save, sender=User)
def profile_pre_save(sender, instance: User, *args, **kwargs):
    """
    Pre save actions on Prole.

    - Sets default access_control for profile if has not been provided.
    """
    if not instance.access_control:
        instance.access_control = AccessControl.objects.get(name=DEFAULT_ACCESS_CONTROL)
