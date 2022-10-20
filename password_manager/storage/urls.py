from django.urls import path

from .views import profile, home


app_name = 'storage'

urlpatterns = [
    path('<slug:username>/', profile, name='storage'),
    path('', home, name='home'),
]