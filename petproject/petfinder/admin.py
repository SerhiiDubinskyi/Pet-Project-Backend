from django.contrib import admin

from .models import *

# class UserProfileAdmin(admin.ModelAdmin): #TODO: Create models classes here
#     list_display =
#     list_editable =
#     list_display_links =
#     search_fields =

# Register your models here.
admin.site.register(UserProfile) # (UserProfile, UserProfileAdmin)
admin.site.register(PetProfile)
admin.site.register(Case)
