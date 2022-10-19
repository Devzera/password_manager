from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('generator.urls', namespace='generator')),
    path('', include('users.urls', namespace='users')),
    path('profile/', include('storage.urls', namespace='storage')),
    path('admin/', admin.site.urls),
]
