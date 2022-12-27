from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'v1/auth/', include('knox.urls')),
    path('v1/register/', views.RegisterAPIView.as_view()),
    path('v1/login/', views.LoginAPIView.as_view()),
    path('user/', views.UserAPIView.as_view()),
]
