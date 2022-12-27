from django.db import models
from .abc_profile import ABCProfile


class UserProfile(ABCProfile):
    email = models.EmailField(max_length=254, blank=False, null=False)
    phone = models.CharField(max_length=30, blank=False, null=False)  # TODO : need validation
    telegram = models.CharField(max_length=30, null=False)  # TODO : need validation
    facebook = models.CharField(max_length=30, null=False)  # TODO : need validation
    instagram = models.CharField(max_length=30, null=False)  # TODO : need validation
    description = models.TextField(max_length=1000, blank=True, null=False)

    def __str__(self):
        return f'Id[{self.pk}] User "{self.name or self.email}"'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['created_at', 'name']
