from django.urls import path

from .views import (ChangePasswordView, CreatePasswordView, HomeView,
                    PasswordDetailView, PasswordsView, SavePasswordView)

app_name = 'passwords'

urlpatterns = [
    path('create_password/', CreatePasswordView.as_view(), name='create_password'),
    path('save_password/', SavePasswordView.as_view(), name='save_password'),
    path('change_password/<slug:key>/', ChangePasswordView.as_view(), name='change_password'),
    path('passwords/<slug:key>/', PasswordDetailView.as_view(), name='password_detail'),
    path('passwords/', PasswordsView.as_view(), name='passwords'),
    path('', HomeView.as_view(), name='home')
]
