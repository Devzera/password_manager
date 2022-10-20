from django.urls import path

from .views import create_password, password_detail, save_password, change_password

app_name = 'generator'

urlpatterns = [
    path('create_password/', create_password, name='create_password'),
    path('save_password/', save_password, name='save_password'),
    path('change_password/<slug:key>', change_password, name='change_password'),
    path('password/<slug:key>/', password_detail, name='password_detail'),
]
