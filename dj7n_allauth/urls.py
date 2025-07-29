from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    google_login, get_me, api_get_me,
    update_password, login_success_popup,
    google_login_js
)


urlpatterns = [
    # Login Google dùng cho SSR 
    path('google-login', google_login),
    path('me', get_me),
    path('update-password', update_password),
    
    # Login Google thuần JS => Phục vụ cho JS framework như Vuejs..
    path('google-login-js', google_login_js),
    path('login-success-popup', login_success_popup),

    # Define APIs
    # API login lấy access & refresh token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # API để refresh token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API get me
    path('api/get-me/', api_get_me),
]