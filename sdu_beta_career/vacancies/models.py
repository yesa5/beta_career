from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from sdu_beta_career.companies.models import Company


class Vacancy(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    experience = Choices(
        (1, 'no experience', _('no experience')),
        (2, 'less than 1 year', _('less than 1 year')),
        (3, '1-3 years', _('between 1 and 3 years')),
        (4, '3-6 years', _('between 3 and 6 years')),
        (5, 'more than 6 years', _('more than 6 years')),
    )
    busyness = Choices(
        (1, 'full time', _('full time')),
        (2, 'part time', _('part time')),
        (3, 'project work', _('project work')),
    )
    responsibility = models.CharField(max_length=200)
    requirements = models.CharField(max_length=200)
    conditions = models.CharField(max_length=200)
    skills = models.CharField(max_length=201)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'
