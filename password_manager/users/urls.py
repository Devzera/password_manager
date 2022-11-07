from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import ProfileChangeInfoView, ProfileView, SignUp

app_name = 'accounts'

urlpatterns = [
    path(
        'signup/',
        SignUp.as_view(),
        name='signup'
    ),
    path(
        'logout/',
        LogoutView.as_view(
            template_name='users/logout.html',
        ),
        name='logout'
    ),
    path(
        'login/',
        LoginView.as_view(
            template_name='users/login.html',
        ),
        name='login'
    ),
    path('<slug:username>/edit', ProfileChangeInfoView.as_view(), name='profile_edit'),
    path('<slug:username>/', ProfileView.as_view(), name='profile'),
]
