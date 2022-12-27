from django.urls import path

import views

urlpatterns = [
    path('test/', views.PetFinderAPIVew.as_view()),
]
