from django.urls import path

from .views import generate_password, check_password

app_name = 'generator'

urlpatterns = [
    path('generate_password/', generate_password, name='generate_password'),
    path('check_password/', check_password, name='check_password'),
]
