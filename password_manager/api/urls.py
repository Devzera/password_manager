from django.urls import path

from .views import *

app_name = 'api'

urlpatterns = [
    path('<slug:username>/passwords/', PasswordsAPI.as_view(), name='api_passwords'),
    path('<slug:username>/passwords/<slug:key>/', PasswordDetailAPI.as_view(), name='api_passwords')
]
