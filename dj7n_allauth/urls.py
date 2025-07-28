from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import google_login, get_me, api_get_me, update_password


urlpatterns = [
    # Define your URL patterns here
    path('google-login', google_login),
    path('me', get_me),
    path('update-password', update_password),

    # Define APIs
    # API login lấy access & refresh token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # API để refresh token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API get me
    path('api/get-me/', api_get_me),
]