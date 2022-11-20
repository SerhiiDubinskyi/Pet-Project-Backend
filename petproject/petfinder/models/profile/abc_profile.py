from django.db import models
from django.core.validators import MaxValueValidator


class ABCProfile(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    age = models.PositiveSmallIntegerField(validators=[MaxValueValidator(250)])
    gender = models.TextChoices('gender', 'Male Female Neuter')
    photo = models.URLField(null=True)
