from django.db import models
from .base import Base

class Case(Base):
    lost_date = models.DateTimeField() # TODO : dateformat as env variable
    lost_location = models.CharField(max_length=100, blank=False, null=False)
    status = models.TextChoices('status', 'Lost Found ')




