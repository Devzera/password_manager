from django.urls import path

from .views import create_password, password_detail, save_password

app_name = 'generator'

urlpatterns = [
    path('create_password/', create_password, name='create_password'),
    path('save_password/', save_password, name='save_password'),
    path('password/<slug:key>/', password_detail, name='password_detail'),
]
