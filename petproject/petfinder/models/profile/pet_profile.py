from django.db import models
from .abc_profile import ABCProfile
from .user_profile import UserProfile


class PetProfile(ABCProfile):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # breed = models.CharField(max_length=30, blank=False, null=False) # TODO;#
    color = models.CharField(max_length=50, blank=False, null=False) # string split by plus
    size = models.PositiveSmallIntegerField()
    description = models.TextField(max_length=2000, blank=True, null=False)
    cases = models.ForeignKey(Case, on_delete=models.CASCADE, null=True)
    is_vaccinated = models.BooleanField(default=False)
    is_sterilized = models.BooleanField(default=False)
    is_microchipped = models.BooleanField(default=False)
    is_house_trained = models.BooleanField(default=False)
    is_good_with_other_animals = models.BooleanField(default=False)
    is_good_with_strangers = models.BooleanField(default=False)
