from django.shortcuts import render

def google_login(request):
    return render(request, 'dj7n_allauth/google_login.html')

def get_me(request):
    return render(request, 'dj7n_allauth/me.html', {'user': request.user})