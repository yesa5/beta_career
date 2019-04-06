from typing import Dict

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices

from sdu_beta_career.access_control.models import AccessControl


class User(AbstractUser):
    ROLES = Choices(
        (1, "student", _("Student")),
        (2, "advisor", _("Advisor")),
        (3, "approver", _("Approver")),
        (4, "mentor", _("Mentor")),
    )
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    role = models.IntegerField(choices=ROLES, default=ROLES.student)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def get_user_name(self, abc: Dict) -> str:
        return self.name


class Profile(models.Model):
    FACULTIES = Choices(
        (1, 'engineering', _('Faculty of Engineering')),
        (2, 'law', _('Faculty of Law')),
        (3, 'economy', _('Faculty of Economy')),
        (4, 'philosophy', _('Faculty of Philosophy')),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_control = models.ForeignKey(AccessControl, on_delete=models.CASCADE, null=True)
    course = models.PositiveSmallIntegerField(null=True, validators=[MinValueValidator(1)])
    gpa = models.DecimalField(
        null=True,
        validators=[MinValueValidator(0.0), MaxValueValidator(4.0)],
        max_digits=3,
        decimal_places=2
    )
    birth_date = models.DateField(null=True)
    avatar = models.ImageField(null=True)
    faculty = models.PositiveSmallIntegerField(choices=FACULTIES, null=True)
    linked_in = models.URLField(null=True)
    github = models.URLField(null=True)
    phone_number = models.CharField(blank=True, null=True, max_length=12)
