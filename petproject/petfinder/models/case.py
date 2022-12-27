from django.db import models
from .base import Base
from .profile.user_profile import UserProfile as User
from .profile.pet_profile import PetProfile as Pet


class Case(Base):
    lost_pet = models.ForeignKey(Pet, on_delete=models.SET_NULL, null=True)
    lost_date = models.DateTimeField()  # TODO : dateformat as env variable
    lost_location = models.CharField(max_length=100, blank=False, null=False)
    status = models.TextChoices('status', 'Lost Found Boarding')
    found_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    found_date = models.DateField(null=True)
    description = models.TextField(max_length=500, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'Case id[{self.pk}] pet "{self.lost_pet.name}" from user "{self.lost_pet.owner}"'
