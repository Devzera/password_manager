from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls', namespace='users')),
    path('generator', include('generator.urls', namespace='generator')),
    path('', include('storage.urls', namespace='storage')),
]
