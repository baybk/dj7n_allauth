from django.urls import path
from .views import google_login, get_me

urlpatterns = [
    # Define your URL patterns here
    path('google-login', google_login),
    path('me', get_me),
]