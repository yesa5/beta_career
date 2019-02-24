from typing import Dict

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices


class User(AbstractUser):
    ROLES = Choices(
        (0, "student", _("Student")),
        (1, "advisor", _("Advisor")),
        (2, "approver", _("Approver")),
        (3, "mentor", _("Mentor")),
    )
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    role = models.IntegerField(choices=ROLES, default=ROLES.student)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def get_user_name(self, abc: Dict) -> str:
        return self.name
