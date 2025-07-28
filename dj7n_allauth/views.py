from django.shortcuts import render, redirect
from django.http import JsonResponse

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

def google_login(request):
    if request.user.is_authenticated:
        return redirect("/dj7n-allauth/me")
    return render(request, 'dj7n_allauth/google_login.html')

def get_me(request):
    user = request.user
    if not user.is_authenticated:
        return render(request, 'dj7n_allauth/not_authenticated.html')
    
    refresh = RefreshToken.for_user(user)
    refresh_token = str(refresh),
    access_token = str(refresh.access_token),
    ctx = {
        'user': user,
        'refresh_token': refresh_token,
        'access_token': access_token,
    }
    
    if not user.has_usable_password():
        return render(request, 'dj7n_allauth/update_password.html', ctx)
   
    return render(request, 'dj7n_allauth/me.html', ctx)

def update_password(request):
    user = request.user
    if not user.is_authenticated:
        return render(request, 'dj7n_allauth/not_authenticated.html')
    return render(request, 'dj7n_allauth/update_password.html')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_get_me(request):
    return JsonResponse({
        "username": request.user.username
    })
