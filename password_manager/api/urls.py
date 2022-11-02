from django.urls import include, path, re_path

from .views import *

app_name = 'api'

urlpatterns = [
    path('passwords/<slug:key>/', PasswordDetailAPI.as_view(), name='api_passwords'),
    path('passwords/', PasswordsAPI.as_view(), name='api_passwords'),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
