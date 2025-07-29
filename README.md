## Cài đặt
```
pip install -e git+https://github.com/baybk/dj7n_allauth.git@dj7n_allauth#egg=dj7n_allauth
```

## Một số chú ý

- CHÚ Ý 1: Dj7n Allauth app cần bạn đảm bảo khai báo trong root urls: `path('accounts/', include('allauth.urls'))`,
    và xóa bỏ (nếu có) urls mặc định của Django `(path('accounts/', include('django.contrib.auth.urls'))`.

- CHÚ Ý 2: Dj7n Allauth app cần bạn đảm bảo khai báo trong root urls: `path('dj7n-allauth/', include('dj7n_allauth.urls'))`,
    Sau đó bạn có thể truy cập vào đường dẫn `/dj7n-allauth/google-login` hoặc `/dj7n-allauth/google-login-js` để đăng nhập bằng Google.

- CHÚ Ý 3: Dj7n Allauth app cần bạn đảm bảo khai báo settings:
```
    ACCOUNT_ADAPTER = 'dj7n_allauth.adapters.MyAccountAdapter'
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        )
    }
    from datetime import timedelta
    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
        'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
        'AUTH_HEADER_TYPES': ('Bearer',),
    }
```

- Chú ý 5: Nếu Frontend dùng JS Framework, thì dòng 34 của file `google_login_js.html` bạn cần xử lý thêm
cần làm gì sau khi nhận đc access_token
