from django.urls import path

from .views import passwords, home


app_name = 'passwords'

urlpatterns = [
    path('<slug:username>/passwords/', passwords, name='passwords'),
    path('', home, name='home'),
]