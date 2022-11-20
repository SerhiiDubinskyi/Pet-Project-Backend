from django.db import models
from abc_profile import ABCProfile


class UserProfile(ABCProfile):
    email = models.EmailField(max_length=254, blank=False, null=False)
    phone = models.CharField(max_length=30, blank=False, null=False) # TODO : need validation
