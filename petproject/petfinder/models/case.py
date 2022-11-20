from django.db import models
from .base import Base
from profile.user_profile import UserProfile


class Case(Base):
    lost_date = models.DateTimeField()  # TODO : dateformat as env variable
    lost_location = models.CharField(max_length=100, blank=False, null=False)
    status = models.TextChoices('status', 'Lost Found Boarding')
    found_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    found_date = models.DateField(null=True)
    description = models.TextField(max_length=500, null=True)
