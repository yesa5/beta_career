from django.db.models.signals import pre_save
from django.dispatch import receiver

from sdu_beta_career.access_control.models import AccessControl
from sdu_beta_career.access_control.config import DEFAULT_ACCESS_CONTROL

from .models import Profile


@receiver(pre_save, sender=Profile)
def profile_pre_save(sender, instance: Profile, *args, **kwargs):
    """
    Pre save actions on Prole.

    - Sets default access_control for profile if has not been provided.
    """
    if not instance.access_control:
        instance.access_control = AccessControl.objects.get(name=DEFAULT_ACCESS_CONTROL)
