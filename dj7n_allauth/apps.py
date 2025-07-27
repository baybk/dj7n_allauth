from django.apps import AppConfig
from django.conf import settings


class Dj7nAllauthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dj7n_allauth'

    def ready(self):

        ### INSTALLED APPS
        required_apps = [
            "django.contrib.sites",
            "allauth",
            "allauth.account",
            "allauth.socialaccount",
            "allauth.socialaccount.providers.google",
        ]
        if not all(app in settings.INSTALLED_APPS for app in required_apps):
            raise ImportError(
                "The 'dj7n_allauth' app requires the following apps to be installed: "
                + ", ".join(required_apps)
            )
        
        ### MIDLEWARE
        required_middleware = [
            "allauth.account.middleware.AccountMiddleware"
        ]
        if not all(middleware in settings.MIDDLEWARE for middleware in required_middleware):
            raise ImportError(
                "The 'dj7n_allauth' app requires the following middleware to be included: "
                + ", ".join(required_middleware)
            )
        
        ### SITE_ID
        if not hasattr(settings, 'SITE_ID'):
            raise ImportError(
                "The 'dj7n_allauth' app requires the 'SITE_ID' setting to be defined in settings.py."
            )
        from django.contrib.sites.models import Site
        if not Site.objects.filter(id=settings.SITE_ID).exists():
            raise ImportError(
                f"The 'dj7n_allauth' app requires a Site with id {settings.SITE_ID} to exist in the database."
            )
        
        required_auth_backends = [
            'django.contrib.auth.backends.ModelBackend',
            'allauth.account.auth_backends.AuthenticationBackend'
        ]
        if not all(backend in settings.AUTHENTICATION_BACKENDS for backend in required_auth_backends):
            raise ImportError(
                "The 'dj7n_allauth' app requires the following authentication backends to be included: "
                + ", ".join(required_auth_backends)
            )
        
        from allauth.socialaccount.models import SocialApp
        try:
            SocialApp.objects.exists()  # Trigger query
        except Exception as e:
            raise ImportError(
                "The 'dj7n_allauth' app requires the DB migration"
            )
        
        if not SocialApp.objects.filter(provider='google').exists():
            raise ImportError(
                "The 'dj7n_allauth' requires a SocialApp for the 'google' provider to be created in the database.\n"+
                "You can create it via the Django admin interface or using the command line.\n"+
                "Google client id and secret are required for the SocialApp.\n" +
                "Access link to get Google client id and secret : https://console.cloud.google.com/apis/credentials"
            )
        
        print(
            "CHÚ Ý 1: Dj7n Allauth app cần bạn đảm bảo khai báo trong root urls: path('accounts/', include('allauth.urls')),\n" + 
            "và xóa bỏ (nếu có) urls mặc định của Django (path('accounts/', include('django.contrib.auth.urls')))")
        
        print(
            "CHÚ Ý 2: Dj7n Allauth app cần bạn đảm bảo khai báo trong root urls: path('dj7n-allauth/', include('dj7n_allauth.urls')) ,\n" +
            "Sau đó bạn có thể truy cập vào đường dẫn /dj7n-allauth/google-login để đăng nhập bằng Google.")
        
        print(
            "CHÚ Ý 3: Dj7n Allauth app cần bạn đảm bảo khai báo settings: LOGIN_REDIRECT_URL = '/dj7n-allauth/me' ")
        
        return super().ready()
