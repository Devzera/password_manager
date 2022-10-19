from django.urls import path

from .views import profile


app_name = 'storage'

urlpatterns = [
    path('<slug:username>/', profile, name='profile')
]