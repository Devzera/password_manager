from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('profile/', include('users.urls', namespace='users')),
    path('generator/', include('generator.urls', namespace='generator')),
    path('admin/', admin.site.urls),
    path('', include('storage.urls', namespace='storage')),
]
