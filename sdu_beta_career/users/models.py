from typing import Dict

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from djchoices import ChoiceItem, DjangoChoices


class User(AbstractUser):
    class RoleType(DjangoChoices):
        student = ChoiceItem(1)
        advisor = ChoiceItem(2)
        approver = ChoiceItem(3)
        mentor = ChoiceItem(4)
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    role = models.IntegerField(choices=RoleType.choices, default=RoleType.student)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def get_user_name(self, abc: Dict) -> str:
        return self.name
