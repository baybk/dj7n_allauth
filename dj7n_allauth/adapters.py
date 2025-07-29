from allauth.account.adapter import DefaultAccountAdapter
from django.shortcuts import resolve_url
    
class MyAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        user = request.user

        # Chỉ xử lý khi user đã xác thực
        if user.is_authenticated:
            # Kiểm tra xem user có SocialAccount với provider là Google không
            if user.socialaccount_set.filter(provider="google").exists():
                return resolve_url('/dj7n-allauth/login-success-popup')

        # Các trường hợp còn lại (login thường) → redirect mặc định
        return super().get_login_redirect_url(request)
