from django.urls import path

from .views import CreatePasswordView, password_detail, SavePasswordView, change_password, PasswordsView, HomeView

app_name = 'passwords'

urlpatterns = [
    path('create_password/', CreatePasswordView.as_view(), name='create_password'),
    path('save_password/', SavePasswordView.as_view(), name='save_password'),
    path('change_password/<slug:key>/', change_password, name='change_password'),
    path('passwords/<slug:key>/', password_detail, name='password_detail'),
    path('passwords/', PasswordsView.as_view(), name='passwords'),
    path('', HomeView.as_view(), name='home')
]
