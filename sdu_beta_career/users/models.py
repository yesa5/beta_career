from typing import Dict

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    STUDENT = 1
    ADVISOR = 2
    APPROVER = 3
    MENTOR = 4
    USER_ROLES = (
        (STUDENT, "student"),
        (ADVISOR, "advisor"),
        (APPROVER, "approver"),
        (MENTOR, "mentor")
    )
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    role = models.IntegerField(choices=USER_ROLES, default=1)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def get_user_name(self, abc: Dict) -> str:
        return self.name
