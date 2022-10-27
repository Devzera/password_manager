from django.urls import path, include, re_path

from .views import *

app_name = 'api'

urlpatterns = [
    path('<slug:username>/passwords/', PasswordsAPI.as_view(), name='api_passwords'),
    path('<slug:username>/passwords/<slug:key>/', PasswordDetailAPI.as_view(), name='api_passwords'),
    path('v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
