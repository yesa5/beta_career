from django.db import models
from sdu_beta_career.users.models import Profile


class Resume(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    profession = models.CharField(blank=True, null=True, max_length=255)
