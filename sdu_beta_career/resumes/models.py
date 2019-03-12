from django.db import models
from sdu_beta_career.users.models import Profile


class Resume(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    profession = models.CharField(blank=True, null=True, max_length=255)
    career_summary = models.TextField(blank=True, null=True)


class WorkExperience(models.Model):
    title = models.CharField(blank=False, null=False, max_length=255)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True,)
    company_name = models.CharField(blank=True, null=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
