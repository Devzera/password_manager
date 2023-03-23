from django.urls import path

from .views import (ChangePasswordInfoView, ChangePasswordView,
                    CreatePassword2View, CreatePasswordView,
                    DeletePasswordView, HomeView, PasswordDetailView,
                    PasswordsView)

app_name = 'passwords'

urlpatterns = [
    path('create_password/', CreatePasswordView.as_view(), name='create_password'),
    # path('create_password_2/', CreatePassword2View.as_view(), name='create_password'),
    path('change_password/<slug:key>/', ChangePasswordView.as_view(), name='change_password'),
    path('change_password_info/<slug:key>/', ChangePasswordInfoView.as_view(), name='change_password_info'),
    path('delete_password/<slug:key>/', DeletePasswordView.as_view(), name='delete_password'),
    path('passwords/<slug:key>/', PasswordDetailView.as_view(), name='password_detail'),
    path('passwords/', PasswordsView.as_view(), name='passwords'),
    path('', HomeView.as_view(), name='home')
]
